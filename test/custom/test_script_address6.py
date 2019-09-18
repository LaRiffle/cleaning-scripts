
from scripts.custom import foo

def test_foo():

    output = foo("rue")
    assert output == "formatedrue"

