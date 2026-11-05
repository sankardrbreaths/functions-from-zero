import click
import wikipedia


@click.command()
@click.option("--name", default="Microsoft", prompt="Wikipedia page to scrap", help="Name of the topic to search on Wikipedia")
def scrape(name="Microsoft", length=1):
    try:
        summary = wikipedia.summary(name, sentences=length)
        click.echo(click.style(f"Summary of {name}:\n{summary}", bg="white", fg="black"))
    except wikipedia.exceptions.DisambiguationError as e:
        click.echo(click.style(f"Disambiguation error: {e.options}", fg="red"))
    except wikipedia.exceptions.PageError:
        click.echo(click.style("Page not found.", fg="red"))
    except Exception as e:
        click.echo(click.style(f"An error occurred: {str(e)}", fg="red"))

if __name__ == "__main__":
    scrape()