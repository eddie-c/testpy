import pytest

@pytest.mark.parametrize("param",[[1,2,3],[4,5,7]])
def test_add(param):
    assert param[0]+param[1] == param[2]
