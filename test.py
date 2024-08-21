import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("аеёиоуыэюя") == 10
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():
    assert count_vowels("бвгджзйклмнпрстфхцчшщ") == 0
    assert count_vowels("БВГДЖЗЙКЛМНПРСТФХЦЧШЩ") == 0

def test_mixed_string():
    assert count_vowels("Привет, мир!") == 3
    assert count_vowels("Тестирование функции") == 8
    assert count_vowels("12345!@#$%") == 0
    assert count_vowels("ПрОгРамМИрОвАние") == 7

def test_empty_string():
    assert count_vowels("") == 0