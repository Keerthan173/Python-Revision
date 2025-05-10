def test_numbers():
    assert 1 in [1,2,3]     # Should pass
def test_comparison():
    a,b=5,10
    assert a<b              # Should pass
def test_string():
    assert 'fizz' in 'fizzbuzz'  # Should pass
def test_failure():
    assert 1 in [2, 3, 4]   # Should fail