from pybrams.utils.interval import Interval
from pybrams.brams.file import get
from pybrams.processing.constants import SHORT_TO_FLOAT_FACTOR
from rich.table import Table
from rich.console import Console


def setup_args(subparsers):
    subparser_psd = subparsers.add_parser("psd")

    subparser_psd.add_argument(
        "--unscaled-output", action="store_true", help="Display the PSD without scaling"
    )
    subparser_psd.add_argument(
        "--recompute",
        action="store_true",
        help="Ignore data from the BRAMS API and recompute the PSD",
    )
    subparser_psd_subparsers = subparser_psd.add_subparsers(
        dest="psd_cmd", required=True
    )

    subparser_psd_calibrator = subparser_psd_subparsers.add_parser(
        "calibrator", help="Compute calibrator PSD"
    )
    subparser_psd_noise = subparser_psd_subparsers.add_parser(
        "noise", help="Compute noise PSD"
    )

    for subparser in [subparser_psd_calibrator, subparser_psd_noise]:
        subparser.add_argument(
            "interval", type=str, help="datetime interval in ISO 8601 format"
        )
        subparser.add_argument(
            "systems",
            type=str,
            nargs="*",
            default=[],
            help="one or multiple BRAMS systems",
        )


def run(args):
    interval_str = args.interval
    systems = args.systems if args.systems else None

    interval = Interval.from_string(interval_str)
    files = get(interval, systems)

    if files:
        console = Console()
        table = Table(title=f"{args.psd_cmd.title()} PSD")

        table.add_column("File", justify="center", style="cyan", no_wrap=True)
        table.add_column("PSD", justify="center", style="magenta")

        for _, filelist in files.items():
            for file in filelist:
                psd: float
                if file.calibrator_psd and file.noise_psd and not args.recompute:
                    psd = (
                        file.calibrator_psd
                        if args.psd_cmd == "calibrator"
                        else file.noise_calibrator
                    )
                else:
                    file.process()
                    freq_interval = tuple()
                    if args.psd_cmd == "calibrator":
                        calibrator_freq = file.signal.calibrator_frequency
                        freq_interval = (calibrator_freq - 3, calibrator_freq + 3)
                    elif args.psd_cmd == "noise":
                        freq_interval = (800, 900)
                    psd = file.signal.series.psd(*freq_interval)
                table.add_row(
                    file.wav_name,
                    str(
                        psd
                        if not args.unscaled_output
                        else psd * SHORT_TO_FLOAT_FACTOR**2
                    ),
                )

        console.print(table)
    else:
        print("No file found in this interval for this/these system(s)")
