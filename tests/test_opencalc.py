from main import opencalc


def test_opencalc():
    assert opencalc() == ['1 × 2 - 3 + 1', '0']
