import pytest
from selenium import webdriver


@pytest.fixture(scope="class") # scope is at class level
#@pytest.fixture() # scope is at method level
def setup():
    print("I will be executed first as setup")
    yield
    print("I will be executed last")

@pytest.fixture() # fixture to load data into testcase
def dataLoad():
    print("Fixture to load User data")
    return["Rahul","Shetty","rahulshettyacademy.com"]

#fixture with parameters
@pytest.fixture(params =["chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param

#fixture with parameters having multiple arguments
@pytest.fixture(params =[("chrome","Rahul"),("Firefox","Shetty"),("IE","academy")])
def crossBrowser1(request):
    return request.param

# this is registering the options from terminal
def pytest_addoption(parser):
    parser.addoption("--browser_name",action = "store", default = "Chrome", help="browser_selection")
#browser_name is the option here, action is whether we are storing the value,
# default is the value used if no value is given in command line and help is the description of steps

@pytest.fixture()
#request is a special built-in fixture object that gives you access to information about the current test context.
def browserInstance(request):
    browser_name=request.config.getoption("--browser_name")
    if browser_name=="Chrome":
      driver = webdriver.Chrome()
      driver.implicitly_wait(5)
    elif browser_name=="Firefox":
      driver= webdriver.Firefox()
      driver.implicitly_wait(5)
    yield driver
    #driver.close()

