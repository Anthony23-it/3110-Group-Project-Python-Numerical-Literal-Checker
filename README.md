# 3110 Group Project – Python Numerical Literal Checker

1. Henry Nguyen

Full Name: Henry Nguyen

Tasks Completed:

Designed & implemented decinteger NFA

Designed & implemented octinteger NFA

Designed & implemented hexinteger NFA

Created pt12nfa.jff

Tested integer NFAs in JFLAP and provided screenshots

Helped verify integer behavior with test cases

Hoai Nam Nguyen

Full Name: Hoai Nam Nguyen

Tasks Completed:

Implemented full floating-point NFA (floatnumber.jff + PNG)

Integrated FP logic into final program

Updated README, organized project files

Created extended test suite for FP literals

Helped implement combined integer/float recognizer

An external helper came to our help in checking our code organization. 
and to assist us in re-writing and to structure the README document. 
The group members made all the NFA designs, testing and final implementation decisions.
Once the project requirements have been learnt fully.

Project Description:

This project implements a recognizer for Python numerical literals following the Python 3 lexical specification:

    -decinteger

    -octinteger

    -hexinteger

    -floatnumber (extra credit)

All literal types use NFAs designed in JFLAP, with a Python implementation that simulates each NFA using transition tables.

Project Structure:

numeric_literal_checker.py       renamed from pt12.py
in_ans.txt                   test input + expected result
out.txt                      output produced by program
README.md                    documentation

nfa_integer:
pt12nfa.jff
pt12nfa.png

nfa_float:
floatnumber.jff
 floatnumber.png

Testing Instructions: run python numeric_literal_checker.py in_ans.txt out.txt

This produces:

Actual result

Expected result

Type (dec/octal/hex/float)

PASS/FAIL


NFA Files Included:
Integer NFA
    -pt12nfa.jff
    -pt12nfa.png

Covers:
    -decimal

    -octal

    -hexadecimal

Floating-Point NFA
    -floatnumber.jff
    -floatnumber.png

Covers:

    -digitpart "." [digitpart] [exponent]

    -"." digitpart [exponent]

    -digitpart exponent

    -Optional + / - in exponent








