import pytest
# @pytest.fixture() is used to define fixture. it is setup method here
# actual testcase takes fixture method as argument and fixture runs first as opening actions
# after fixture actual testcase is executed
# if yield is present in fixture , it is executed last after original testcase as closing actions
#@pytest.fixture()
#def setup(): ---> commented here for reference but it is put in the  conftest file
 #   print("I will be executed first as setup")
  #  yield
   # print("I will be executed last")
@pytest.mark.usefixtures("setup") # class is using setup fixture
class TestExample():
 def test_fixturedemo(self):
    print("I will be run after fixture is executed and then yield is executed")
 def test_fixturedemo1(self):
    print("I will be run after fixture is executed and then yield is executed")
 def test_fixturedemo2(self):
    print("I will be run after fixture is executed and then yield is executed")
 def test_fixturedemo3(self):
    print("I will be run after fixture is executed and then yield is executed")


 #def test_fixturedemo3(setup): # normal method with fixture outside class
   # print("I will be run after fixture is executed and then yield is executed")

