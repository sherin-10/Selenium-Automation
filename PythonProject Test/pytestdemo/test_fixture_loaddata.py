
import pytest

@pytest.mark.usefixture("dataLoad")
class TestExample2():
    def test_editprofile(self,dataLoad):
        print(dataLoad)
        print(dataLoad[1])

# Usually when fixture is defined at class level, then the testcase doesn't take any other arguments other than self.