import pytest
from applications import labs

def test_hello_world():
    assert labs.hello_world() == "Hello World!"

def test_storeHello():
    assert labs.storeHello() == "Hello World!"

def test_newString():
    assert labs.newString("asd") == "asd"

def test_sum():
    assert labs.sumOfInts(15, 25) == 40
    assert labs.sumOfInts(11, 2) == 13
    assert labs.sumOfInts(12, 5) == 17