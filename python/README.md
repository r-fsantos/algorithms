# Python "Algos"

Algorithms and Data Structures implemented in Python, among with unit tests

## Activating the `virtual env`

This project is developed on a very simple manner, using `poetry` basics, for now. So to activate the virtual env, please run the following

## Running the unit tests

1. On the root of the python implementation folder (👀 _tech debt_ 👀), run

```python
poetry run python -m unittest tests/**/test*.py
```

or, you can alternatively:

2. Also on the root folder, use the following

```python
poetry run python -m tests.module_a.test_module_b
```
