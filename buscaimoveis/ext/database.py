from pymongo import MongoClient


def configure(app):
    client = MongoClient(app.config.get('DATABASE_URL'))
    app.db = client[app.config.get('DATABASE_NAME')]
