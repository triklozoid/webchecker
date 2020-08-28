import argparse
import logging

from webchecker.consumer import run_consumer
from webchecker.producer import run_producer


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    setup_logging()
    actions_map = {
        'producer': run_producer,
        'consumer': run_consumer,
        'list': '',
    }

    parser = argparse.ArgumentParser(
        prog="webchecker", description="websites checking tool"
    )
    parser.add_argument("action", choices=actions_map.keys())

    args = parser.parse_args()

    action_function = actions_map[args.action]
    action_function()

