# All files should begin with test_
# All code should be inside function
# Method names should always start with test_ and should be sensible
# Each method is treated as a test case
# No 2 test case can have same name. if 2 have same name then second one overwrites the first one
# -k is used to match regular expression, -v is used to get metadata, -s is used to print output
# py.test <filename> is used to run specific file
# py.test -v is used to run all files in the project after pointing to correct directory using cd(change directory)
# If 2 methods in same file has same name, the first method is replaced with the second method. only 2 runs
# Mark testcases by @pytest.mark.smoke and then run with -m
# Skip testcases by @pytest.mark.skip and then run py.test -v -s
# Run the tc but skip it in report with @pytest.mark.xfail
# Fixtures are used to setup and do close setup for a testcase, defined by @pytest.fixture()
# passing name of fixture method in testcase argument.
# All test cases with fixture argument will run fixture before executing tc.
# In order to generalise fixture, we can write it in a seperate file called conftest.py
# and put the fixture method in that file.
# All testcases with fixture argument in whichever file it is will run the fixture first
# we can put all testcases in a class and assign fixture to it.
# In that case all testcases will run fixture first and then only the actual test case.
# But if we specify scope = class for fixture, then it will only once for the whole class
# and not for each testcase
# We can parameterize fixtures to pass the testdata to test case
# Request is used as an object for the fixture and then return request
# Parameters for a fixture can have many values for a single argument. We put in braces and seperate by commas
# To generate report for testcases in HTML run pip install pytest-html
# To get report of testcases pytest --html=report.html, where report.html is the name of the file

import pytest

def test_firstprogram():
    print('Hello')

#not considered as it has same name as first method so changing name to get 2 test cases
#def test_firstprogram():
   # print("Good Morning")
@pytest.mark.xfail # run the tc but skip it in report
def test_greet():
    print("Good Morning")

@pytest.mark.smoke # mark the tc as smoke which is a label
def test_greetCreditCard():
    print("Good Morning CreditCard")