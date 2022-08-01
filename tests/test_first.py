import pytest
from src.calc import Caluculator

def test_first():
    assert (1, 2, 3) == (1, 2, 3)

def test_second():
    assert (1, 2, 3) == (1, 2, 3)

def test_sum():
    calculator = Caluculator()
    assert calculator.sum(1, 2) == 3

def test_sum_of_minus_value():
    calculator = Caluculator()
    with pytest.raises(ValueError):
        calculator.sum(-1, 2)

@pytest.mark.skip("skip this test")
def test_skip_case():
    calculator = Caluculator()
    assert calculator.sum(1, 2) == 3

@pytest.mark.parametrize('test_values',[
    (1,2,3),
    (10,20,30),
    (100,200,300)
])
def test_sum_of_multi_values(test_values):
    calculator = Caluculator()
    assert calculator.sum(test_values[0], test_values[1]) == test_values[2]

@pytest.mark.parametrize('left, right, excepted',[
    (1,2,3),
    (10,20,30),
    (100,200,300)
])
def test_sum_of_multi_values(left, right, excepted):
    calculator = Caluculator()
    assert calculator.sum(left, right) == excepted

def test_mock(mocker):
    mock = mocker.patch('src.calc.DbAccessor')
    calculator = Caluculator()
    calculator.save(1)
    mock.assert_called_once()
