
from scripts.custom import format_address

def test_format_address():

    output = format_address("rue")
    assert output == "formatedrue"

