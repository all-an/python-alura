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
  ```

## 4. Deactivate the virtual environment

When you're done, deactivate it by running:
```bash
deactivate
```