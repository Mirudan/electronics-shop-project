import pytest
from src.item import Item


@pytest.fixture
def fix_item_class():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(fix_item_class):
    """Общая стоимость товара = кол-во * на стоимость"""
    assert fix_item_class.calculate_total_price() == 200000


def test_apply_discount(fix_item_class):
    """При применении скидки цена товара становится меньше"""
    fix_item_class.pay_rate = 0.7
    fix_item_class.apply_discount()
    assert fix_item_class.price == 7000.0


def test_all(fix_item_class):
    """аргумент self.all добавляет экземпляры класса в список при инициализации"""
    assert type(fix_item_class.all) is list
    assert bool(fix_item_class.all) is True

