from flask_analytics import Analytics


def configure(app):
    if app.config.get('ANALYTICS_ENABLED'):
        Analytics(app)
        app.config['ANALYTICS']['GOOGLE_CLASSIC_ANALYTICS']['ACCOUNT'] = app.config.get( # noqa
            'ANALYTICS_SITE_ID'
        )
