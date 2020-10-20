# coding:utf-8
import unittest

class TestTaskServiceTwo(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        print("end!")

    def test_03(self):
        a = 1
        b = 2
        self.assertTrue(3, a+b)

    def test_04(self):
        a = 3
        b = 2
        self.assertTrue(6, a*b)

if __name__ == "__main__":
    unittest.main()
