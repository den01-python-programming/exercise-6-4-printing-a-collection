import pytest
from src.simple_collection import SimpleCollection

def test_exercise():
    s = SimpleCollection("alphabet")

    assert str(s) == "The collection alphabet is empty."

    s.add("s")

    assert str(s) == "The collection alphabet has 1 element:\ns"
