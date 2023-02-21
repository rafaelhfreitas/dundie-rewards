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
import os
import uuid
import pytest  
from dundie.core import load
from .constants import PEOPLE_FILE

def setup_module():
    print()
    print("Running before this module s tests")

def teardown_module():
    print()
    print("Running after this module s tests")
      

@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso é sujeira...")
    yield
    file_.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function."""

    filepath = f"arquivo-indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))

    with open(filepath,"w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == "R"


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test load function."""

    with open(f"arquivo-indesejado-{uuid.uuid4()}.txt","w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == "R"