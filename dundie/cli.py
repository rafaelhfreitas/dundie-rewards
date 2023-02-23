import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dunder Mifflin Rewards System

    This cli application controls DM rewards.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database.

    ## Features

    - Validates data
    - Parses the file
    - Loads to database
    """
    table = Table(title="Dunder Mufflin Associates")
    headers = ["name", "dept", "role", "created", "email"]
    for header in headers:
        table.add_column(header, style="green")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()])
        # table.add_row(*[field.strip() for field in person.split(",")])
        # table.add_row(*person.split(","))
        # print("-" * 50)
        # for key, value in zip(header, person.split(",")):
        #     print(f"[red]{key}[/] -> [magenta]{value.strip()}[/]")

    console = Console()
    console.print(table)


@main.command()
@click.option("--dept", required=False)
@click.option("--email", required=False)
def show(**query):
    """Retrieve data from database using **query params"""
    result = core.read(**query)

    if not result:
        print("Nothing to show")

    table = Table(title="Dunder Mufflin Report")
    for key in result[0]:
        table.add_column(key.title(), style="magenta")

    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)
