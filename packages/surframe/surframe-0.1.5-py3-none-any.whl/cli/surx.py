import sys
import typer
from surframe import is_pro_enabled

app = typer.Typer(add_completion=False, help="SURX CLI")

@app.callback(invoke_without_command=True)
def _root(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo("Uso: surx [write|read|plan|inspect|learn|reencode|zopt|tier] --help")
        raise typer.Exit(code=1)

@app.command()
def learn():
    if not is_pro_enabled("ucodec"):
        typer.echo("Comando PRO bloqueado: falta licencia con feature 'ucodec'.", err=True)
        raise typer.Exit(code=2)
    from surframe.ucodec.learn import learn_ucodec
    learn_ucodec()

@app.command()
def reencode():
    if not is_pro_enabled("ucodec"):
        typer.echo("Comando PRO bloqueado: falta licencia con feature 'ucodec'.", err=True)
        raise typer.Exit(code=2)
    from surframe.ucodec.reencode import reencode_ucodec
    reencode_ucodec()

@app.command()
def zopt():
    if not is_pro_enabled("zopt"):
        typer.echo("Comando PRO bloqueado: falta licencia con feature 'zopt'.", err=True)
        raise typer.Exit(code=2)
    from surframe.ucodec.layout import zorder_optimize
    zorder_optimize()

@app.command()
def tier():
    if not is_pro_enabled("tier"):
        typer.echo("Comando PRO bloqueado: falta licencia con feature 'tier'.", err=True)
        raise typer.Exit(code=2)
    from surframe.ucodec.tier import tier_plan
    tier_plan()

def main():
    app()

if __name__ == "__main__":
    main()
