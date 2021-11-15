from src.hello import hello
from unittest import TestCase


class TestHello(TestCase):
    def test_hello(self):
        assert "hello" in hello(name="taimore")
