# 1. Make sure you have virtual env - 'venv'
#     - instructions: http://naucse.python.cz/2017/pyladies-praha-podzim-cznic/beginners/install/windows/
#     - make: py -3 -m venv venv
#     - activate: \venv\Scripts\activate
#     - if active you will see (venv)
#
# 2. install pip pytest pytest
#     - python -m pip install pytest
#
#
# 3. run pytest
#    - python -m pytest -v [file_name.py]
#    - python -m pytest -v 1_instalace.py
#    -




def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3