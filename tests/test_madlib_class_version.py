import pytest
from madlib_cli.madlib_class_version import read_template,parse_template,merge


def test_read_template_returns_stripped_string():
    actual = read_template ("files/template2.txt")
    expected ="A {adjective} and {adjective} {Noun} ."
    assert actual == expected

@pytest.mark.skip("pending")
def test_read_template_raise_expection_with_bad_path():
    with pytest.reises(FileNotFoundError):
        read_template("template2.txt") 

@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template("A {adjective} and {adjective} {Noun} .")   
    expected_stripped = "A {} and {} {} ."
    expected_parts =("adjective","adjective","Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

@pytest.mark.skip("pending")
def test_merge():
    actual = merge ("A {} and {} {} .", ("bright","blue", "day")) 
    expected = "A bright and blue day"
    assert actula == expected

