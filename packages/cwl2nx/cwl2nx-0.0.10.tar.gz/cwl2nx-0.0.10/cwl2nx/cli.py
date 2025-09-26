import typer

from .cwl2nx import cwl_to_str


def cwlviz(dir: str):
    print(cwl_to_str(dir))


app = typer.Typer()
app.command()(cwlviz)


if __name__ == "__main__":
    app()
