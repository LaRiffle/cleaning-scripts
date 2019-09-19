
from scripts.custom import foo

def test_foo():

    output = foo("one ")
    assert output == "one"

