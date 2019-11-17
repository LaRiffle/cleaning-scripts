
from scripts.custom import test_script

def test_test_script():

    output = test_script("aze")
    assert output == "azelol"

