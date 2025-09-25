import argparse
import os
import sys
from importlib.metadata import version
import pybrams
import pybrams.scripts.get
import pybrams.scripts.cache
import pybrams.scripts.config
import pybrams.scripts.trajectory
import pybrams.scripts.wavinfo
import pybrams.scripts.spectrogram
import pybrams.scripts.cams
import pybrams.scripts.availability
import pybrams.scripts.location
import pybrams.scripts.system
import pybrams.scripts.psd
import logging


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="PyBRAMS executable",
        epilog=f"Usage : python {os.path.basename(__file__)} command [args...]",
    )

    parser.add_argument(
        "-v", "--verbose", action="count", help="increase verbosity level"
    )
    parser.add_argument(
        "--version", action="version", version=f"PyBRAMS {version('pybrams')}"
    )
    subparsers = parser.add_subparsers(dest="cmd")
    pybrams.scripts.get.setup_args(subparsers)
    pybrams.scripts.cache.setup_args(subparsers)
    pybrams.scripts.config.setup_args(subparsers)
    pybrams.scripts.trajectory.setup_args(subparsers)
    pybrams.scripts.wavinfo.setup_args(subparsers)
    pybrams.scripts.spectrogram.setup_args(subparsers)
    pybrams.scripts.cams.setup_args(subparsers)
    pybrams.scripts.availability.setup_args(subparsers)
    pybrams.scripts.location.setup_args(subparsers)
    pybrams.scripts.system.setup_args(subparsers)
    pybrams.scripts.psd.setup_args(subparsers)
    parsed_args = parser.parse_args(args)
    if not parsed_args.cmd:
        parser.print_help()
        sys.exit(1)
    return parsed_args


def main():
    parsed_args = parse_args()
    commands = {
        "get": pybrams.scripts.get.run,
        "cache": pybrams.scripts.cache.run,
        "config": pybrams.scripts.config.run,
        "trajectory": pybrams.scripts.trajectory.run,
        "wavinfo": pybrams.scripts.wavinfo.run,
        "spectrogram": pybrams.scripts.spectrogram.run,
        "cams": pybrams.scripts.cams.run,
        "availability": pybrams.scripts.availability.run,
        "location": pybrams.scripts.location.run,
        "system": pybrams.scripts.system.run,
        "psd": pybrams.scripts.psd.run,
    }

    if parsed_args.verbose:
        if parsed_args.verbose == 1:
            pybrams.enable_logging(level=logging.INFO)
        elif parsed_args.verbose >= 2:
            pybrams.enable_logging(level=logging.DEBUG)
        else:
            pybrams.enable_logging(level=logging.WARNING)

    if parsed_args.cmd:
        commands[parsed_args.cmd](parsed_args)


if __name__ == "__main__":
    main()
