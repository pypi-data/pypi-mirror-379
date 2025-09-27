import pytest

from tiny_python import tiny_exec
from tiny_python.executor import ExecutionError


def test_import_blocked():
    with pytest.raises(ValueError):
        tiny_exec("import os")

    with pytest.raises(ValueError):
        tiny_exec("from os import path")


def test_exec_blocked():
    with pytest.raises((ValueError, NameError)):
        tiny_exec("exec('print(1)')")


def test_eval_blocked():
    with pytest.raises((ValueError, NameError)):
        tiny_exec("eval('1+1')")


def test_open_blocked():
    with pytest.raises((ValueError, NameError)):
        tiny_exec("open('file.txt')")


def test_compile_blocked():
    with pytest.raises((ValueError, NameError)):
        tiny_exec("compile('1+1', 'string', 'eval')")


def test_dunder_access_blocked():
    with pytest.raises(ValueError):
        tiny_exec("__import__('os')")

    with pytest.raises(ValueError):
        tiny_exec("__builtins__")

    with pytest.raises(ValueError):
        tiny_exec("__file__")


def test_globals_locals_blocked():
    with pytest.raises((ValueError, NameError)):
        tiny_exec("globals()")

    with pytest.raises((ValueError, NameError)):
        tiny_exec("locals()")

    with pytest.raises((ValueError, NameError)):
        tiny_exec("vars()")


def test_attribute_access_blocked():
    with pytest.raises((ValueError, NameError)):
        tiny_exec("getattr(str, '__class__')")

    with pytest.raises((ValueError, NameError)):
        tiny_exec("setattr(str, 'test', 123)")

    with pytest.raises((ValueError, NameError)):
        tiny_exec("delattr(str, 'test')")


def test_max_iterations():
    with pytest.raises(ExecutionError, match="iterations"):
        tiny_exec(
            """
while True:
    pass
""",
            max_iterations=100,
        )

    with pytest.raises(ExecutionError, match="iterations"):
        tiny_exec(
            """
for i in range(1000000):
    x = i * 2
""",
            max_iterations=100,
        )


def test_iteration_limit_not_triggered():
    # This should work fine
    code = """
total = 0
for i in range(10):
    total += i
total
"""
    result = tiny_exec(code, max_iterations=100)
    assert result == 45


def test_function_definition_blocked():
    with pytest.raises(ValueError):
        tiny_exec("""
def my_func():
    return 42
""")

    with pytest.raises(ValueError):
        tiny_exec("""
lambda x: x * 2
""")
