import subprocess
import sys

import pytest

from toolkit.calculator import calculate
from toolkit.converter import convert
from toolkit.errors import error


def test1():
    assert calculate("2+3*4") == 14


def test2():
    assert calculate("10 / 4") == 2.5


def test3():
    assert calculate("-2 * -3") == 6


def test4():
    assert calculate("1+-2") == -1


def test5():
    assert calculate("1.5 + 2.25") == 3.75


def test6():
    assert calculate(" - 2 * - 3 ") == 6


def test7():
    with pytest.raises(error):
        calculate("")


def test8():
    with pytest.raises(error):
        calculate("2+a")


def test9():
    with pytest.raises(error):
        calculate("2*/3")


def test10():
    with pytest.raises(error):
        calculate("1+")


def test11():
    with pytest.raises(error):
        calculate("1/0")


def test12():
    assert convert(1000, "mm", "m") == 1.0


def test13():
    assert convert(1.5, "kg", "g") == 1500.0


def test14():
    assert abs(convert(0, "c", "f") - 32) < 1e-9


def test15():
    assert abs(convert(-273.15, "c", "k")) < 1e-9


def test16():
    assert convert(100, "CM", "M") == 1.0


def test17():
    with pytest.raises(error):
        convert(-274, "c", "k")


def test18():
    with pytest.raises(error):
        convert(1, "kg", "m")


def test19():
    with pytest.raises(error):
        convert(1, "unknown", "m")


def test20():
    p = subprocess.run(
        [sys.executable, "-m", "toolkit", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert p.returncode == 0
    assert "calc" in p.stdout


def test21():
    p = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2+3*4"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert p.returncode == 0
    assert float(p.stdout) == 14


def test22():
    p = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2*/3"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert p.returncode == 2
    assert "Ошибка" in p.stderr
