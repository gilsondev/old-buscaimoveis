# -*- coding: utf-8 -*-

from mongomock import MongoClient

from flask_testing import TestCase, LiveServerTestCase

from selenium import webdriver

from buscaimoveis.app import create_app
from tests.fixtures import ads_fixture_data


def _prepare_test_app():
        app = create_app()
        app.db = MongoClient().db

        ads_fixture_data(app.db)

        return app


class TestBase(TestCase):
    def create_app(self):
        return _prepare_test_app()


class TestLiveBase(LiveServerTestCase):
    def create_app(self):
        return _prepare_test_app()

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()
