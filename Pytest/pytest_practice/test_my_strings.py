from my_strings import to_uppercase
def test_string_positive():
    assert to_uppercase("jai hind")=="JAI HIND"
def test_string_negative():
    assert to_uppercase("jai hind")=="jai HIND"
def test_string_mixed():
    assert to_uppercase("jai hind")=="jai HIND"
    assert to_uppercase("jai hind")=="JAI HIND"