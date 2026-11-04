import pytest

from calculadora import sumar, dividir


def test_sumar():
    assert sumar(2, 3) == 5


def test_suma_negativos():
    assert sumar(-2, -3) == -5


def test_division_correcta():
    assert dividir(10, 2) == 5


def test_division_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
