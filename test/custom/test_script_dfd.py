
from scripts.custom import foo

def test_foo():

    output = foo("aze")
    assert output == "azel"

