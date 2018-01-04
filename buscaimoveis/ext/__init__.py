import import_string


def configure(app):
    """Extension Factory, load the extensions
    defined on the app.config.EXTENSIONS
    """
    for extension in app.config.get('EXTENSIONS', []):
        try:
            factory = import_string(extension)
            factory(app)
        except Exception as e:
            app.logger.error(f'Error to load the extension {extension}: {e}')
        else:
            app.logger.info(f'Extension {extension} loaded.')
