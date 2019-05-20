# -*- coding: utf-8 -*-

"""Console script for training_logger."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for training_logger."""
    click.echo("Replace this message by putting your code into "
               "training_logger.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
