# test.py
from hello import hello, goodbye, add


def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_goodbye(capsys):
    goodbye()
    captured = capsys.readouterr()
    assert captured.out == "Goodbye, World!\n"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
