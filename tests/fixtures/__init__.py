# -*- coding: utf-8 -*-

import os
import json

from pathlib import Path

FIXTURES_PATH = os.path.dirname(__file__)

ADS_DATA = 'ads.json'


def ads_fixture_data(db):
    with open(Path(FIXTURES_PATH) / Path(ADS_DATA)) as ads_file:
        ads = json.loads(ads_file.read())
        db.properties.insert_many(ads)
