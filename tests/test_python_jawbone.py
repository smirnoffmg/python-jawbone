#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_jawbone
----------------------------------

Tests for `python_jawbone` module.
"""

import unittest

try:
    import mock
except ImportError:
    import unittest.mock as mock

from python_jawbone import JawboneClient

TEST_TOKEN = 'WEDONTHAVEIT'

GOOD_RESULT = {
    'meta': {
        'code': 200
    }
}


class TestJawboneClient(unittest.TestCase):
    def setUp(self):
        self.test_client = JawboneClient(token=TEST_TOKEN)

    def tearDown(self):
        self.test_client = None

    @mock.patch('python_jawbone.JawboneClient.get_body_events', return_value=GOOD_RESULT)
    def test_get_body_events(self, mock_get_body_event):
        info = mock_get_body_event()
        self.assertEqual(info['meta']['code'], 200)

    @mock.patch('python_jawbone.JawboneClient.get_band_events', return_value=GOOD_RESULT)
    def test_get_band_events(self, mock_band_events):
        info = mock_band_events()
        self.assertEqual(info['meta']['code'], 200)
