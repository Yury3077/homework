from unittest import TestCase
from unittest.mock import patch

import requests

from homework4.task_2_mock_input import count_dots_on_i


class FetchTests(TestCase):
    """Checking that function return true value of i in a text"""

    def test_returns_true_if_url_text_contain_4_i(self):
        with patch("requests.get") as mock_request:
            url = "http://google.com"
            mock_request.return_value.text = "iiii"
            self.assertTrue(count_dots_on_i(url) == 4)

    def test_returns_true_if_url_co_found(self):
        """Checking that function return false value of i in a text"""
        with patch("requests.get") as mock_request:
            url = "http://google.com"
            mock_request.return_value.text = "some_html_code with two letter i"
            self.assertFalse(count_dots_on_i(url) == 3)
