"""
example implementation of pytest

author: taimore khan
"""
from unittest import TestCase

from src.hello import hello


class TestHello(TestCase):
    """
    class structure helps divide test code into logical sections
    """

    def test_hello(self):
        """
        simple positive test case
        """
        self.assertTrue("hello" in hello(name="taimore"))
