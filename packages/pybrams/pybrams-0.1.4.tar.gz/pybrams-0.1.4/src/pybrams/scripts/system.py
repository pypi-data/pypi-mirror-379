from rich.table import Table
from rich.console import Console
from pybrams.brams import system


def setup_args(subparsers):
    subparser_system = subparsers.add_parser("system")
    subparser_system_subparsers = subparser_system.add_subparsers(
        dest="system_cmd", required=True
    )

    subparser_system_subparsers.add_parser("list", help="list all BRAMS systems")


def run(args):
    if args.system_cmd == "list":
        systems = system.all()
        console = Console()
        table = Table(title="BRAMS systems")

        table.add_column("System code", justify="center", style="cyan", no_wrap=True)
        table.add_column("Display name", justify="center", style="magenta")

        for code, item in systems.items():
            table.add_row(
                code,
                item.name,
            )

        console.print(table)
