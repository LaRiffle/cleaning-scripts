
from scripts.custom import foo

def test_foo():

    output = foo("you")
    assert output == "you"

