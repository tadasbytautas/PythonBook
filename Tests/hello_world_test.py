import pytest
from applications import labs


# def test_hello_world():
#     assert labs.hello_world() == "Hello World!"
#
# def test_storeHello():
#     assert labs.storeHello() == "Hello World!"
#
# def test_newString():
#     assert labs.newString() == "new string"
#
# def test_sum():
#     assert labs.sumOfInts(15, 25) == 40
#     assert labs.sumOfInts(11, 2) == 13
#     assert labs.sumOfInts(12, 5) == 17

# def test_conditionals():
#     assert labs.conditionals(5, 12, True) == 17
#     assert labs.conditionals(5, 12, False) == 60
#     assert labs.conditionals(-1, 12, True) == 11
#     assert labs.conditionals(-1, 12, False) == -12

# def test_conditionals_two():
#     assert labs.conditionals(0, 12, True) == 12
#     assert labs.conditionals(5, 12, False) == 60
#     assert labs.conditionals(1, 0, True) == 1
#     assert labs.conditionals(-1, 12, False) == -12
#     assert labs.conditionals(0, 0, False) == 0

def test_recursion():
    assert labs.recursion(5, 12, False) == "60606060606060606060"
    assert labs.recursion(3, 12, False) == "36363636363636363636"
    assert labs.conditionals(0, 12, True) == 12
    assert labs.conditionals(1, 0, True) == 1
    assert labs.conditionals(-1, 12, False) == -12
    assert labs.conditionals(0, 0, False) == 0

def test_newList():
    assert labs.newList(1) == 1
    assert labs.newList(12) == 12
    assert labs.newList(-1) == -1
    assert labs.newList(0) == 0
