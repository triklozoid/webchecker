import argparse
import logging

from webchecker.consumer import run_consumer
from webchecker.manager import add_site
from webchecker.producer import run_producer


def setup_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def main():
    setup_logging()
    actions_map = {
        "producer": run_producer,
        "consumer": run_consumer,
        "add": add_site,
    }

    parser = argparse.ArgumentParser(
        prog="webchecker", description="websites checking tool"
    )
    parser.add_argument("action", choices=actions_map.keys())
    parser.add_argument(
        "--url",
        type=str,
        help="add site with url",
    )

    args = parser.parse_args()

    if args.action == "add" and not args.url:
        parser.error("You must specify site url via --url parameter")

    action_function = actions_map[args.action]
    action_function(args)
