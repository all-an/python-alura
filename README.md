# python-alura
python-alura


# How to Create a Python Virtual Environment

## 1. Install `virtualenv` (optional step)

While Python has a built-in module called `venv`, you can also use the `virtualenv` package if you prefer more features. To install it, run:
```bash
pip install virtualenv
```

## 2. Create a virtual environment

- Using `venv` (Python 3.3+ comes with `venv` built-in):
  ```bash
  python -m venv myenv
  ```

- Using `virtualenv`:
  ```bash
  virtualenv myenv
  ```

Replace `myenv` with the name of your virtual environment.

## 3. Activate the virtual environment

- On **Windows**:
  ```bash
  myenv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source myenv/bin/activate
  or
  source /home/all-an/Public/code/python-alura/myenv/bin/activate
  ```

## 4. Deactivate the virtual environment

When you're done, deactivate it by running:
```bash
deactivate
```

## install pytest

```bash
pip3 install pytest
```

## run tests

```bash
pytest
or
pytest -v # verbose mode
```

## running one test by word in it's name:

```
# will run the first test
pytest -k idade
or
pytest -k idade -v
```

## running two tests by mark decorator:

```
pytest -v -m calcular_bonus
```

## see all marks possible to use:

```
pytest --markers

```
Example:
If you use mark @mark.skip and run pytest, you will skip the test with the mark


## code coverage requirements:

```
pip install pytest-cov==3.0.0
```

## coverage all files:

```
pytest --cov

```

## specify directory:

```
pytest --cov=bytebank
# will run coverage only on bytebank.py file
```

## specify part of code where tests are not covering

```
pytest --cov=bytebank --cov-report term-missing
```
The new Missing column on the report is the line of code not covered