import typer
from typing_extensions import Annotated

from .cwl2nx import cwl_to_str


def cwlviz(
    cwl: Annotated[str, typer.Argument(help="Path to the cwl file")],
    display_colors: Annotated[
        bool, typer.Argument(help="Whether to display colors")
    ] = False,
    verbose: Annotated[
        bool,
        typer.Argument(help="If verbose is true, display full names of cwl objects"),
    ] = False,
):
    print(cwl_to_str(cwl, display_colors=display_colors, verbose=verbose))


app = typer.Typer()
app.command()(cwlviz)


if __name__ == "__main__":
    app()
