from flask_debugtoolbar import DebugToolbarExtension


def configure(app):
    if app.config.get('DEBUG_TB_ENABLED'):
        DebugToolbarExtension(app)
