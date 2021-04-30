import pytest

import math
import app

@pytest.mark.a
def testsquare():
    val = app.sum_values()
    assert val == [1,2]

@pytest.mark.b
def tesequality():
    num = 10
    assert num == 11

""" 
commands to be performed:
    pytest -m a test_square.py
    pytest -v [for verbose testings]
"""