import unittest
from algorithm import summary

class TestSummary(unittest.TestCase):
    def setUp(self):
        self.array = [10, 5, 20, 30, 1, 4]
    def test_successful(self):
        self.assertEqual(summary(self.array, 1, 2), 25)
    def test_emptyArray(self): 
        self.assertEqual(summary([], 0, 5), 0)
    def test_whenArrayIsNone(self):
        self.assertEqual(summary(None, 1, 2), 0)
    def test_FirstIndiceIsNone(self):
        self.assertEqual(summary(self.array, None, 2), 0)
    def test_SecondIndiceIsNone(self):
        self.assertEqual(summary(self.array, 2, None), 0)
    def test_OutOfIndex(self):
        self.assertEqual(summary(self.array, 3, 15), 0)

if __name__ == '__main__':
    unittest.main()
