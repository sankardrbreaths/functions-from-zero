import click
import wikipedia
from mylib.bot import get_summary


# CLI interface
@click.command()
@click.option("--name", default="Microsoft", prompt="Wikipedia page")
@click.option("--length", default=1, type=int)
def scrape(name, length):
    try:
        summary = get_summary(name, length)
        click.echo(f"Summary of {name}:\n{summary}")
    except wikipedia.exceptions.PageError:
        click.echo("Page not found.")


if __name__ == "__main__":
    scrape()
