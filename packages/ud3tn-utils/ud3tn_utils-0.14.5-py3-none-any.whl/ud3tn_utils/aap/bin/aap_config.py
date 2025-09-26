#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause OR Apache-2.0
# encoding: utf-8

import argparse
import logging

from ud3tn_utils.aap import AAPTCPClient, AAPUnixClient
from ud3tn_utils.aap.bin.helpers import (
    add_socket_group_parser_arguments,
    add_verbosity_parser_argument,
    initialize_logger,
    get_config_eid,
)
from ud3tn_utils.config import (
    JSONConfigMessage as ConfigMessage,
    make_contact,
)


logger = logging.getLogger(__name__)


def main():
    import sys

    parser = argparse.ArgumentParser(
        description="create or update a node in uD3TN",
    )

    add_socket_group_parser_arguments(parser)
    add_verbosity_parser_argument(parser)

    parser.add_argument(
        "--dest_eid",
        default=None,
        help="the EID of the node to which the configuration belongs",
    )
    parser.add_argument(
        "eid",
        help="the EID of the node to which the contact exists",
    )
    parser.add_argument(
        "cla_address",
        help="the CLA address of the node",
    )
    parser.add_argument(
        "-s", "--schedule",
        nargs=3,
        type=int,
        metavar=("start_offset", "duration", "bitrate"),
        action="append",
        default=[],
        help="schedule a contact relative to the current time",
    )
    parser.add_argument(
        "-r", "--reaches",
        type=str,
        action="append",
        default=[],
        help="specify an EID reachable via the node",
    )

    args = parser.parse_args()
    global logger
    logger = initialize_logger(args.verbosity)

    logger.warning(
        "DEPRECATED: This tool does not support new security mechanisms "
        "provided by µD3TN and, thus, has been deprecated. Please use "
        "aap2-config to configure contacts with the compatibility BDM "
        "and provide the administrative secret to both µD3TN and the "
        "configuration tool in release builds."
    )

    if not args.schedule:
        logger.fatal("At least one -s/--schedule argument must be given!")
        sys.exit(1)

    msg = bytes(ConfigMessage(
        args.eid,
        args.cla_address,
        contacts=[
            make_contact(*contact)
            for contact in args.schedule
        ],
        reachable_eids=args.reaches,
    ))

    logger.info("> %s", msg)

    if args.tcp:
        with AAPTCPClient(address=args.tcp) as aap_client:
            aap_client.register()
            dest_eid = args.dest_eid or aap_client.node_eid
            aap_client.send_bundle(get_config_eid(dest_eid), msg)
    else:
        with AAPUnixClient(address=args.socket) as aap_client:
            aap_client.register()
            dest_eid = args.dest_eid or aap_client.node_eid
            aap_client.send_bundle(get_config_eid(dest_eid), msg)


if __name__ == "__main__":
    main()
