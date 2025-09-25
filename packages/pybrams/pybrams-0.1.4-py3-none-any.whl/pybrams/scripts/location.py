from rich.table import Table
from rich.console import Console
from pybrams.brams import location


def setup_args(subparsers):
    subparser_location = subparsers.add_parser("location")
    subparser_location_subparsers = subparser_location.add_subparsers(
        dest="location_cmd", required=True
    )

    subparser_location_subparsers.add_parser("list", help="list all BRAMS locations")


def run(args):
    if args.location_cmd == "list":
        locations = location.all()
        console = Console()
        table = Table(title="BRAMS locations")

        table.add_column("Location code", justify="center", style="cyan", no_wrap=True)
        table.add_column("Display name", justify="center", style="magenta")

        for code, item in locations.items():
            table.add_row(
                code,
                item.name,
            )

        console.print(table)
