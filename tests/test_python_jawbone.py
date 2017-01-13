#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_jawbone
----------------------------------

Tests for `python_jawbone` module.
"""

import unittest

from python_jawbone import JawboneClient

TEST_TOKEN = ''


class TestJawboneClient(unittest.TestCase):
    def setUp(self):
        self.test_client = JawboneClient(token=TEST_TOKEN)

    def tearDown(self):
        self.test_client = None

    def test_get_body_events(self):
        info = self.test_client.get_body_events()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_band_events(self):
        info = self.test_client.get_band_events()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_heart_rates(self):
        info = self.test_client.get_heart_rates()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_custom_events(self):
        info = self.test_client.get_custom_events()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_goals(self):
        info = self.test_client.get_goals()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_meals(self):
        info = self.test_client.get_meals()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_mood(self):
        info = self.test_client.get_mood()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_moves(self):
        info = self.test_client.get_mood()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_sleeps(self):
        info = self.test_client.get_sleeps()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_timezone(self):
        info = self.test_client.get_timezone()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_trends(self):
        info = self.test_client.get_trends()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_user(self):
        info = self.test_client.get_user()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_friends(self):
        info = self.test_client.get_friends()
        self.assertEqual(info['meta']['code'], 200)

    def test_get_workouts(self):
        info = self.test_client.get_workouts()
        self.assertEqual(info['meta']['code'], 200)
