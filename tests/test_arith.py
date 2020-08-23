import pytest

from python_travis.arithmetic import Arithmetic

def test_arith_add():
    assert(Arithmetic(10, 20).add() == 30)

def test_arith_minus():
    assert(Arithmetic(10, 20).minus() == -10)

def test_arith_multiple():
    assert(Arithmetic(10, 20).multiple() == 200)
