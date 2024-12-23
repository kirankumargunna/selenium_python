import unittest

class TestCaseDemo(unittest.TestCase):

    def test1(self):
        print("executing test case")

    def test2(self):
        print("executing test case2")
    def test3(self):
        print("executing test case3")

    def tearDown(self):
        print("teardown\n")

    def setUp(self):
        print("setup")
    @classmethod
    def setUpClass(cls):
        print("setupclass")

unittest.main()
