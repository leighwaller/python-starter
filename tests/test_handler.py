import pytest
import moto

from handler import handle


def test_handler_prints():
    assert handle(None, None) is None

