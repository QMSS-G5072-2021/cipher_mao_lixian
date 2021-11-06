from cipher_lm3598 import cipher_lm3598
def test_cipher():
    expected = 'M'
    actual = cipher_lm3598.cipher('L',1)
    assert actual == expected