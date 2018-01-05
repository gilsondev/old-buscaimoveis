import code
import click

from buscaimoveis.app import create_app

app = create_app(__name__)


@click.group()
def main():
    """Busca Imóveis APP"""
    pass


@main.command()
def shell():
    """Open a shell with app in the context"""
    with app.app_context():
        try:
            from IPython import start_ipython
            start_ipython(argv=[], user_ns={'app': app})
        except:
            code.interact(banner='Busca Imóveis', local={'app': app})


@main.command()
@click.option('--debug/--no-debug', default=app.config.DEBUG)
@click.option('--reloader/--no-reloader', default=app.config.RELOADER)
@click.option('--host', default=app.config.HOST)
@click.option('--port', default=app.config.PORT)
def runserver(debug, reloader, host, port):
    """Run the server with dev/debug mode"""
    app.run(debug=debug, use_reloader=reloader, host=host, port=port)
