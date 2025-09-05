# COBOL x Copilot Project

## Modernizing a Cobol accounting system to a Python application using GitHub Copilot

### Table of contents

- [Context](#context)
- [Defining the steps](#defining-the-steps)
- [Establishing a set of automated tests](#establishing-automated-tests)
- [Organizing the tests](#organizing-the-tests)
- [Converting the COBOL code into Python](#converting-the-cobol-code-into-python)
- [Organizing the python code](#organizing-the-python-code)
- [Expanding the tests](#expanding-the-tests)

## Context

This project consists of converting legacy COBOL code to Python in order to obtain an identical project with the same features, in a way that users won't notice a difference.

We initially dispose of a git repository containing the deprecated COBOL code, a simple test plan and starting steps to use Github Copilot to our advantage to make it easier.

## Defining the steps

The first thing we needed to do was define how to convert this code in a way that keeps the program perfectly functional.

- In order to make the COBOL compilation slightly easier we started by making a simple bash compilation file.

- Convert [Test plan](TESTPLAN.md) to a list of automated end-to-end tests to have a list of what should already work, using an adequate technology.

- Organize the test directory and code into respective files and classes.

- Convert the COBOL code into Python to get to a perfect equivalent of the initial program, using the list of tests we gathered.

- Organize the Python code in an OOP way that respects SOLID principles.

- Expand the tests list to guarantee maximal coverage, introducing integration tests and unit tests compatible with python code.

## Establishing automated tests

With the help of a Copilot prompt :

```
@workspace we would like to create unit and integration tests cases from the test plan mentioned in #file:TESTPLAN.md file, to test the cobol files #file:data.cob #file:main.cob and #file:operations.cob. Use an adequate language and framework for this.
```

Using Python's Pytest module, we was able to get a list of the 7 initial use cases listed in the test plan, using Python and pytest. After a bit of refinement in the unsure code that Copilot gave me and getting more coverage with more end-to-end tests, 19 out of 23 test functions were already working all by executing a single command, ```pytest ./```.

## Organizing the tests

## Converting the COBOL code into Python

With the following prompt :
```
TODO
```

Copilot was able to reproduce the initial COBOL code in python. Since the code was simple and the conversion was pretty straightforward, all tests were passing on first try, but the python code only contained standalone functions and a code refactoring was necessary.

## Organizing the Python code



## Expanding the tests

Our set of end-to-end tests is not enough for comprehensive coverage. we needed to add tests of various types that go more in-depth in the possibilities of user input. By the same occasion we could organize the directory better by grouping the tests in separate files and classes and documenting the code.

With the help of Copilot we was able to get a list of many more tests that challenge float serialization handling as well as float overflow and positive/negative values. After we deemed that all possibilities we could think of were covered, we had a total of X tests across X files.
