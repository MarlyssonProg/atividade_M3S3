
import pytest

# aparti da "pasta app" do "arquivo desconto" importar a class Desconto
from app.desconto import Desconto


def test_desconto():
    assert test_desconto(1,1) == 3
    assert test_desconto(10, 10) == 95
    assert test_desconto(100, 10) == 900
    assert test_desconto(1000, 10) == 8500

    