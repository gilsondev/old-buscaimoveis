import code
import click

from buscaimoveis.app import create_app

app = create_app(__name__)


@click.group()
def main():
    """Main Group"""
    pass


@main.command()
def shell():
    """Open a shell with app in the context"""
    with app.app_context():
        code.interact(banner='Busca Imoveis APP', local={'app': app})


@main.command()
@click.option('--debug/--no-debug', default=app.config.DEBUG)
@click.option('--reloader/--no-reloader', default=app.config.RELOADER)
@click.option('--host', default=app.config.HOST)
@click.option('--port', default=app.config.PORT)
def runserver(debug, reloader, host, port):
    """Run the server with dev/debug mode"""
    app.run(debug=debug, use_reloader=reloader, host=host, port=port)


@main.command()
@click.option('--username', prompt=True, required=True)
@click.option('--password', prompt=True, required=True, hide_input=True,
              confirmation_prompt=True)
def adduser(username, password):
    """Create a new user"""
    with app.app_context():
        try:
            with app.app_context():
                app.db.create_user(username, password)
        except Exception as e:
            click.echo(f'Could not create a user {username}')
            raise
        else:
            click.echo(f"User {username} created successfully!")
