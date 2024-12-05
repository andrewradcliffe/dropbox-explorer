from main import main
import click

@click.group()
def cli():
    """Welcome to Python Dropbox Explorer"""
    pass

@cli.command()
def explore():
    """Explore your Dropbox files"""
    main()

if __name__ == "__main__":
    cli()
