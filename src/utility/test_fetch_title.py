import unittest
from fetch_title import fetch_title

class TestFetchTitle(unittest.TestCase):
    def test_fetch_title(self):
        self.assertEqual(fetch_title("# Main Title"), "Main Title")
        