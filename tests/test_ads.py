# -*- coding: utf-8 -*-

import time

from flask import url_for

from tests import TestLiveBase


class HomepageTest(TestLiveBase):

    def test_should_return_status_code_200(self):
        with self.app.test_client() as client:
            response = client.get(url_for('ads.index'))
            self.assertEqual(response.status_code, 200)

    def test_should_render_template(self):
        title_page = self.driver.find_element_by_xpath(
            '//*/h1[@class="text-center"]'
        )
        title_page = self.driver.find_element_by_css_selector(
            'h1.text-center'
        )
        self.assertEqual('Busca Imóveis', title_page.text)

        input_search = self.driver.find_element_by_name('keywords')
        submit = self.driver.find_elements_by_css_selector(
            'button'
        )

        self.assertIsNotNone(input_search)
        self.assertIsNotNone(submit)

    def test_should_list_sells(self):
        card_box = self.driver.find_elements_by_css_selector('div.card')
        card_image = self.driver.find_elements_by_css_selector(
            'a.link-image > img'
        )
        card_title = self.driver.find_elements_by_css_selector(
            'div.card > div > h3'
        )
        card_description = self.driver.find_elements_by_css_selector(
            'div.card > div:nth-of-type(1) > p'
        )
        card_owner = self.driver.find_elements_by_css_selector(
            'div.card > div:nth-of-type(2) > p'
        )

        contents = [
            (card_box, 1),
            (card_image, 1),
            (card_title, 1),
            (card_description, 4),
            (card_owner, 2),
        ]

        for content, count in contents:
            with self.subTest():
                self.assertEqual(count, len(content))


class HomepageSearchTest(TestLiveBase):
    def test_should_search_a_sell(self):
        input_search = self.driver.find_element_by_name('keywords')
        input_search.send_keys("armários")

        submit = self.driver.find_element_by_css_selector('button')
        submit.click()
        time.sleep(3)

        result_search = self.driver.find_elements_by_css_selector('div.card')
        self.assertEqual(1, len(result_search))

    def test_should_show_message_not_found(self):

        input_search = self.driver.find_element_by_name('keywords')
        input_search.send_keys("!@(#*&)")

        submit = self.driver.find_element_by_css_selector('button')
        submit.click()
        time.sleep(3)

        result_search = self.driver.find_elements_by_css_selector('div.card')
        not_found_message = self.driver.find_element_by_css_selector(
            'div.message > h2'
        )

        self.assertEqual(0, len(result_search))
        self.assertEqual('Nenhum anúncio encontrado.', not_found_message.text)
