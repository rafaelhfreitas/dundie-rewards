"""
In [2]: def soma(a, b):
   ...:     return a + b

In [3]: soma(1, 2)
Out[3]: 3

In [4]: def dobra(f):
   ...:     def manipuladora(a, b):
   ...:         return f(a * 2, b * 2)

In [5]: def dobra(f):
   ...:     def manipuladora(a, b):
   ...:         return f(a * 2, b * 2)

In [6]: def dobra(f):
   ...:     def manipuladora(a, b):
   ...:         return f(a * 2, b * 2)
   ...:
   ...:     return manipuladora

In [7]: soma = dobra(soma)

In [8]: soma
Out[8]: <function __main__.dobra.<locals>.manipuladora(a, b)>

In [9]: soma(1, 2)
Out[9]: 6

In [10]: from functools import wraps

In [11]: def bold(f):
    ...:     @wraps(f)
    ...:     def wrapper(text):
    ...:         return f(f"<strong>{text}</strong>")
    ...:
    ...:     return wrapper

In [12]:

In [12]: def italic(f):
    ...:     @wraps(f)
    ...:     def wrapper(text):
    ...:         return f(f"<i>{text}</i>")
    ...:
    ...:     return wrapper

In [13]: @bold
    ...: @italic
    ...: def hello(text):
    ...:     return f"Hello {text}"

In [14]: hello("Rafael")
Out[14]: 'Hello <i><strong>Rafael</strong></i>'

In [16]: assert hello("Rafael") == "Hello <i><strong>Rafael</strong></i>"

"""
import pytest

from dundie.core import load

from .constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    """Test load function."""

    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_r(request):
    """Test load function."""

    assert load(PEOPLE_FILE)[0]["name"] == "Rafael Freitas"
