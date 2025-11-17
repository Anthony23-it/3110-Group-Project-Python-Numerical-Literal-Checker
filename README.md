# 3110 Group Project – Python Numerical Literal Checker

## Overview

This project is for **CS 3110** and implements a numerical literal checker based on the
Python 3 lexical specification. It recognizes:

- **Decimal integers** (`decinteger`, including multiple leading zeros)
- **Octal integers** (`0o` / `0O` prefix)
- **Hexadecimal integers** (`0x` / `0X` prefix)
- **Floating-point literals** (`floatnumber` – extra credit)

The checker is implemented using an NFA model in code (for integers) and a
separate float parser that follows the Python grammar for `floatnumber`.

---

## How to Run

You need **Python 3** installed.

### 1. Interactive mode

```bash
python pt12.py

This project includes an extra-credit extension that adds full support for recognizing Python floating-point literals according to the Python 3 lexical specification.
This portion of the project was implemented by Hoai Nam Nguyen.
