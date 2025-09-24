from matrixutils import matrix_transpose
import pytest

def test_basic_transpose():
    m = [[1,2,3],[4,5,6]]
    assert matrix_transpose(m) == [[1,4],[2,5],[3,6]]

def test_empty():
    assert matrix_transpose([]) == []

def test_non_rectangular():
    m = [[1,2],[3]]
    with pytest.raises(ValueError):
        matrix_transpose(m)
