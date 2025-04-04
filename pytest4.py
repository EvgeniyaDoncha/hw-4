import math
import random
import pytest


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25

    output = f"{'Привет, ' + name + '! '}{'Тебе ' + str(age) + ' лет.'}"
    assert output == "Привет, Анна! Тебе 25 лет."

    output = f"Привет, {name}! Тебе {age} лет."
    assert output == "Привет, Анна! Тебе 25 лет."

    output = "Привет, {name}! Тебе {age} лет." .format(name=name, age=age)
    assert output == "Привет, Анна! Тебе 25 лет."

    output = "Привет, " + name + "! Тебе " + str(age) + " лет."
    assert output == "Привет, Анна! Тебе 25 лет."


    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    perimeter = 0

    perimeter = 2 * (a + b)
    assert perimeter == 60


    area = 0
    area = a * b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23

    area = 0
    area = math.pi * r ** 2
    assert area == 1661.9025137490005

    area = math.pi * math.pow(r, 2)
    assert area == 1661.9025137490005


    length = 0
    length = 2 * math.pi * r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и
    отсортируйте его по возрастанию.
    """
    l = [
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),

    ]
    l.sort()
    l = sorted(l)
    assert  len(l) ==10
    assert  l[0] < l[-1]




def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first,  second))
    print(d)


    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second