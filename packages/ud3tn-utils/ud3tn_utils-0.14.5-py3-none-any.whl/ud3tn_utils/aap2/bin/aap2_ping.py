#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause OR Apache-2.0
# encoding: utf-8

"""
A tool to send "ping bundles" (like the ICMP echos we all know and love)
to another DTN node, expect responses from there, and measure the time in
between.
"""

import argparse
import logging
import os
import signal
import sys
import time
import threading

from ud3tn_utils.aap2 import (
    AAP2UnixClient,
    AAP2TCPClient,
    AAP2CommunicationError,
    AAP2ServerDisconnected,
    BundleADU,
    ResponseStatus,
)
from ud3tn_utils.aap2.bin.helpers import (
    add_common_parser_arguments,
    add_keepalive_parser_argument,
    argparse_non_empty_str,
    get_secret_from_args,
    initialize_logger,
)
from pyd3tn.eid import validate_eid


logger = logging.getLogger(__name__)


class PingTerminated(Exception):
    """An Exception used to signal termination of the ping."""

    def __init__(self, exit_status=0):
        self.exit_status = exit_status


def _send_pings(
    aap2_client,
    destination,
    interval,
    count,
    stop_event,
    timeout,
):
    counter = 0
    while counter < count or not count:
        # Send a bundle containing the current count & timestamp as a string.
        # Why the timestamp? -> To easily calculate how long it took to come
        # back! Otherwise, we would need some tricks for making the other
        # thread know when we sent which bundle.
        # We do not use aap_client.send but the lower-level function as
        # AAPClient invokes receive() at the end and this would confuse
        # the other thread if run here (we would receive partial data
        # everywhere).
        payload = f"PING:{str(counter)}:{str(time.time())}".encode("utf-8")
        aap2_client.send_adu(
            BundleADU(
                dst_eid=destination,
                payload_length=len(payload),
            ),
            payload,
        )
        response = aap2_client.receive_response()
        if response.response_status != ResponseStatus.RESPONSE_STATUS_SUCCESS:
            logger.warning(
                "µD3TN responded with unexpected status: %s (%d)",
                aap2_client.response_status_name(response.response_status),
                response.response_status,
            )

        # We could use time.sleep() here, but this would not allow to properly
        # stop this thread. Thus, we rather wait until the stop Event occurs.
        # -> In normal operation this will not be the case and the function
        #    will run into the timeout in which case the condition is False.
        if stop_event.wait(timeout=interval):
            # We were requested to stop -> terminate by returning here
            return

        counter += 1

    # If we come here, termination has been requested after sending a
    # specified number of bundles and this was reached. We wait at maximum
    # for the interval to pass _again_ but do not send an additional bundle
    # during that period. Note that the receiver might trigger the stop event
    # if the last bundle has been received already.
    if timeout and stop_event.wait(timeout=timeout):
        # We were requested to stop -> no need to signal the main thread
        return

    # Terminate the main thread via KeyboardInterrupt
    os.kill(os.getpid(), signal.SIGINT)


def _run_send_pings(
    aap2_client,
    agent_id,
    secret,
    destination,
    interval,
    count,
    stop_event,
    timeout,
):
    with aap2_client:
        aap2_client.configure(
            agent_id,
            subscribe=False,
            secret=secret,
        )
        _send_pings(
            aap2_client,
            destination,
            interval,
            count,
            stop_event,
            timeout,
        )


def _try_receive_ping(aap2_client, logger):
    # Wait for the next AAP message to be received and catch possible
    # connection errors (e.g., if µD3TN disconnects).
    try:
        msg = aap2_client.receive_msg()
    except AAP2ServerDisconnected:
        logger.warning("µD3TN has closed the connection, quitting.")
        raise PingTerminated(1)
    except AAP2CommunicationError as e:
        logger.warning("AAP2 communication error, quitting: %s", str(e))
        raise PingTerminated(1)

    # Store the time we received the bundle as early as possible
    recv_time = time.time()

    msg_type = msg.WhichOneof("msg")
    if msg_type == "keepalive":
        logger.debug("Received keepalive message, acknowledging.")
        aap2_client.send_response_status(ResponseStatus.RESPONSE_STATUS_ACK)
        # Continue loop.
        return False, None
    elif msg_type != "adu":
        # Nothing we want, continue loop.
        return False, None

    adu_msg, bundle_data = aap2_client.receive_adu(msg.adu)
    aap2_client.send_response_status(
        ResponseStatus.RESPONSE_STATUS_SUCCESS
    )

    if bundle_data[0:4] != b"PING":
        # Just show we got something we do not want
        logger.warning((
            "Received bundle of length %d bytes from %s that does not seem "
            "to be a PING bundle!"
        ), len(bundle_data), msg.adu.src_eid)
        return False, None

    # Try to decode the payload of the message
    try:
        _, counter_str, time_str = bundle_data.decode("utf-8").split(":")
    except UnicodeError:  # if str.decode fails
        logger.warning("Could not decode PING bundle from %s", msg.adu.src_eid)
        return False, None

    # Try to get the numbers back
    try:
        counter_at_src = int(counter_str)
        time_at_src = float(time_str)
    except ValueError:  # int(...) or  float(...) failed
        logger.warning("Could not read values in PING bundle from %s",
                       msg.adu.src_eid)
        return False, None

    # Calculate the Round Trip Time (duration from sending to receiving)
    rtt = recv_time - time_at_src
    logger.info("Received PING from %s: seq=%d, rtt=%f",
                msg.adu.src_eid, counter_at_src, rtt)

    return True, counter_at_src


def run_aap_ping(
    rpc_client,
    sub_client,
    agent_id,
    secret,
    destination,
    interval,
    count,
    logger,
    timeout,
):
    start_time = time.time()  # remember to calculate how many bdl. we expected

    # Start a second thread for sending the bundles!
    # Note that normally it is not a great idea to use threads in Python
    # due to the "Global Interpreter Lock" but in this case the threads mostly
    # wait for I/O (send/recv on the socket) which happens outside of the GIL.
    # Also note that the AAP client is not thread safe (it would call receive
    # on the socket twice concurrently and, thus, receive only partial garbage
    # in both threads). Hence, we directly use the socket send function
    # to make it thread safe...
    stop_event = threading.Event()  # for clean termination
    send_worker = threading.Thread(
        target=_run_send_pings,
        args=(
            rpc_client,
            agent_id,
            secret,
            destination,
            interval,
            count,
            stop_event,
            timeout,
        ),
    )
    send_worker.start()

    receive_counter = 0
    try:
        while True:
            success, seqno = _try_receive_ping(sub_client, logger)
            if success:
                receive_counter += 1
                # If we got the last bundle, terminate immediately
                if count and seqno == count - 1:
                    raise PingTerminated
    # Exception handler: Either Ctrl+C was pressed or the sender signaled us a
    # SIGINT (raising a KeyboardInterrupt), or we are terminating normally.
    except (KeyboardInterrupt, PingTerminated) as e:
        # Calculate and print some statistics
        duration = time.time() - start_time
        expected_bundles = int(duration / interval) + 1
        if count:
            expected_bundles = min(expected_bundles, count)
        logger.info("Ping ran for %f seconds, received %d of %d sent",
                    duration, receive_counter, expected_bundles)
        if receive_counter < expected_bundles:
            # Indicate that we did not receive everything
            sys.exit(1)
        if isinstance(e, PingTerminated) and e.exit_status != 0:
            # Another exit status was requested
            sys.exit(e.exit_status)
    finally:  # Note that _try_receive_ping might raise SystemExit
        # Tell the sending thread to terminate
        stop_event.set()


def main():
    parser = argparse.ArgumentParser(
        description=(
            "send bundles to a given EID, wait for responses, "
            "and print them"
        ),
    )

    add_common_parser_arguments(parser)
    add_keepalive_parser_argument(parser)

    parser.add_argument(
        "destination",
        type=argparse_non_empty_str,
        help="the destination EID to ping",
    )
    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=1.0,
        help=(
            "interval, in seconds, to wait between sending bundles "
            "(default: 1 second)"
        ),
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=0,
        help=(
            "stop after sending the specified number of bundles "
            "(default: 0 = infinite)"
        ),
    )
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=0,
        help=(
            "add a waiting time after sending all ping bundles "
            "(default: 0 = program terminates after sending all bundles)"
        ),
    )

    args = parser.parse_args()
    global logger
    logger = initialize_logger(args.verbosity + 1)  # log INFO by default
    validate_eid(args.destination)

    if args.tcp:
        rpc_client = AAP2TCPClient(address=args.tcp)
        sub_client = AAP2TCPClient(address=args.tcp)
    else:
        rpc_client = AAP2UnixClient(address=args.socket)
        sub_client = AAP2UnixClient(address=args.socket)

    with sub_client:
        secret = sub_client.configure(
            args.agentid,
            subscribe=True,
            secret=get_secret_from_args(args),
            keepalive_seconds=args.keepalive_seconds,
        )
        run_aap_ping(
            rpc_client,
            sub_client,
            sub_client.agent_id,
            secret,
            args.destination,
            args.interval,
            args.count,
            logger,
            args.timeout,
        )


if __name__ == "__main__":
    main()
