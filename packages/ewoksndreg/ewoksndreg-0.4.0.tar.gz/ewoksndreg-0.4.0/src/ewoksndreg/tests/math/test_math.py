import pytest

from ...math.indices import get_positive_index


def test_get_positive_index():
    n = 5
    for i in [0, 1, 2, 3, 4]:
        assert get_positive_index(i, n) == i
    for i in [-5, -4, -3, -2, -1]:
        assert get_positive_index(i, n) == i + n

    assert get_positive_index(0.0, n) == 0
    assert get_positive_index(0.5, n) == 2
    assert get_positive_index(1.0, n) == 4

    error_msg = "Index must be between -5 and 4 or 0.0 and 1.0"

    for i in [-6, 5]:
        with pytest.raises(ValueError, match=error_msg):
            _ = get_positive_index(i, n)

    for i in [-0.1, 1.1]:
        with pytest.raises(ValueError, match=error_msg):
            _ = get_positive_index(i, n)
