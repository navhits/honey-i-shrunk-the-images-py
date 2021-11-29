import typer
import random

from awesomecli import __version__

app = typer.Typer(help="Awesome CLI can do awesome stuff in the CLI like saying 'Hi!'")

@app.command("version")
def version():
    """
    Displays the AwesomeCLI version and exits.
    """
    typer.echo(f"AwesomeCLI v{__version__}")
    raise typer.Exit(0)

@app.command("hello")
def hello():
    """
    Say hello to the world.
    """
    mylist = ["Hey..", "Hi!", "Hello!", "Howdy!", "Greetings!"]
    typer.echo(random.choices(mylist)[0])
    