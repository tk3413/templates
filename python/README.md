# python3 generic code template

## description

generic template repository to include the following:

- [x] unit test suite
- [x] end to end test suite
- [ ] logger
- [x] linter
- [ ] script to package module

## local setup

linux:
```
pip3 install virtualenv --user
python3 -m virtualenv venv
make install
```

## unit tests
```
make utest
```

```
pytest --cov-report term-missing --cov=src.hello test/
======================================================= test session starts ========================================================
platform darwin -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/taimorekhan/code/templates/python
plugins: cov-3.0.0
collected 1 item                                                                                                                   

test/test_hello.py .                                                                                                         [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
src/hello.py       2      0   100%
--------------------------------------------
TOTAL              2      0   100%


======================================================== 1 passed in 0.04s =========================================================
```

## end to end tests
```
make etest
```

```
behave e2e/features
Feature: working end to end tests # e2e/features/success.feature:1

  Scenario: establish a test suite          # e2e/features/success.feature:3
    Given we have some code                 # e2e/features/steps/steps_success.py:5
    Given we have some code                 # e2e/features/steps/steps_success.py:5 0.000s
    When it is called                       # e2e/features/steps/steps_success.py:11
    When it is called                       # e2e/features/steps/steps_success.py:11 0.000s
    Then we are able to validate the result # e2e/features/steps/steps_success.py:17
    Then we are able to validate the result # e2e/features/steps/steps_success.py:17 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```

## lint
```
make lint
```

```
sorting imports
Skipped 1 files
formatting code
All done! ✨ 🍰 ✨
2 files left unchanged.
All done! ✨ 🍰 ✨
1 file left unchanged.
reformatted test/test_hello.py
All done! ✨ 🍰 ✨
1 file reformatted, 1 file left unchanged.
applying linter

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.00/10, +2.00)
```
