#testcase with paramaeterised fixture for a single argument
def test_crossBrowser(crossBrowser):
    print(crossBrowser)

#test case for parameterised fixture with many arguments
def test_crossBrowser1(crossBrowser1):
    print(crossBrowser1[0])
    print(crossBrowser1[1])


