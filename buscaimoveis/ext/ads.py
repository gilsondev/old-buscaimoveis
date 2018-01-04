import pymongo

from flask import Blueprint, render_template, current_app
from flask_wtf import FlaskForm
from wtforms import fields


ads_blueprint = Blueprint('ads', __name__, template_folder='template')


LIMIT_SELLS = 30


@ads_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        sells = current_app.db.properties.find({
            "$or": [
                {"title": {"$regex": form.keywords.data}},
                {"description": {"$regex": form.keywords.data}},
                {"city": {"$regex": form.keywords.data}},
                {"district": {"$regex": form.keywords.data}}
            ]
        }).sort([
            ("created_at", pymongo.DESCENDING)
        ]).limit(LIMIT_SELLS)
    else:
        sells = current_app.db.properties.find().sort([
            ("created_at", pymongo.DESCENDING)
        ]).limit(LIMIT_SELLS)

    return render_template('index.html', sells=sells, form=form)


class SearchForm(FlaskForm):
    keywords = fields.StringField('Busque por local e descrição')


def configure(app):
    app.register_blueprint(ads_blueprint)
