
import csv
import os
import platform
import re
import signal
import sys
from argparse_utils import ArgumentParser, ArgumentTypeError, RawDescriptionHelpFormatter
from time import monotonic

import pandas as pd
import requests
from colorama import init
from requests_futures.sessions import FuturesSession
from torrequest import TorRequest

from notify import QueryNotifyPrint
from result import QueryResult, QueryStatus
from sites import SitesInformation

from argparse_utils import parse_arguments
from request_utils import make_request, handle_response
from sites_utils import load_sites_data

__version__ = "0.14.3"
module_name = "Sherlock: Find Usernames Across Social Networks"


def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Load sites data
    sites_data = load_sites_data("data.json")

    # Process each username
    for username in args.usernames:
        results = []
        for site_name, site_info in sites_data.items():
            # Prepare request parameters
            url, headers, method = prepare_request_data(site_info, username)

            # Make the request
            response = make_request(url, method=method, headers=headers)

            # Process the response
            result = process_response(response, site_info)
            results.append(result)

        # Generate output based on command-line options
        generate_output(results, args)


if __name__ == "__main__":
    main()
