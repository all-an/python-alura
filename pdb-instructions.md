
# Python Debugger (`pdb`) Usage Instructions

## Table of Contents
1. [Introduction to `pdb`](#introduction-to-pdb)
2. [Basic `pdb` Commands](#basic-pdb-commands)
3. [Using `pdb` in a Project](#using-pdb-in-a-project)
4. [Using `pdb` in a FastAPI Project](#using-pdb-in-a-fastapi-project)

---

## Introduction to `pdb`

The Python Debugger (`pdb`) is a built-in interactive debugger for Python programs. It provides a powerful way to step through your code, inspect variables, set breakpoints, and execute commands to better understand what is happening in your code at runtime.

### When to Use `pdb`

- You want to pause execution at a certain point and inspect what's going on.
- You want to debug a particular function or piece of logic.
- You need to check the value of variables and the flow of execution.

## Basic `pdb` Commands

Here are the most common `pdb` commands you'll use:

| Command | Description |
|---------|-------------|
| `b [lineno]` | Set a breakpoint at the specified line number. |
| `b [file:lineno]` | Set a breakpoint at a line number in another file. |
| `b` | List all breakpoints. |
| `cl` or `clear [bpnumber]` | Clear the breakpoint by its number or clear all breakpoints. |
| `n` or `next` | Execute the current line and move to the next line. |
| `s` or `step` | Step into a function. |
| `r` or `return` | Continue execution until the current function returns. |
| `l` or `list` | List the code around the current line (or a specific location). |
| `p [expression]` | Print the value of the given expression or variable. |
| `c` or `continue` | Continue execution until the next breakpoint. |
| `q` or `quit` | Quit the debugger and stop program execution. |
| `h` or `help [command]` | Get help for a specific command, or show all commands if none is specified. |
| `! [statement]` | Execute a Python statement. |

## Using `pdb` in a Project

### Project Structure Example

```bash
your_project/
│
├── main_folder/
│   └── main.py
│
└── bank_folder/
    └── bank.py
```

### Setting Breakpoints

You can add breakpoints in your code by using `pdb.set_trace()`.

**Example in `main.py`**:

```python
import pdb
from bank_folder.bank import some_function_in_bank

def main():
    pdb.set_trace()  # Breakpoint in main.py
    result = some_function_in_bank()
    print(result)

if __name__ == '__main__':
    main()
```

**Example in `bank.py`**:

```python
import pdb

def some_function_in_bank():
    pdb.set_trace()  # Breakpoint in bank.py
    return "This is from bank.py"
```

### Running the Debugger

To run `pdb`, execute your script with the `-m pdb` flag:

```bash
python -m pdb main_folder/main.py
```

The debugger will start, and execution will stop at the first breakpoint.

### Example Workflow

- `l`: List code to see where you are.
- `n`: Step to the next line of code.
- `p variable`: Print the value of a variable.
- `s`: Step into a function.
- `c`: Continue until the next breakpoint.

## debug test with pytest:

```
pytest --pdb
```