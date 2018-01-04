from flask import Flask

from buscaimoveis import config, ext


def create_app(import_name='buscaimoveis'):
    app = Flask(import_name)

    # Configuration
    config.configure(app)

    # Extensions
    ext.configure(app)

    return app
