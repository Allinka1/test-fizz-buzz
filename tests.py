from fb import FizzBuzzDetector
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_min_length(self):
        string = 'abc'
        obj = FizzBuzzDetector(string)
        with self.assertRaises(ValueError):
            obj.getOverlappings()

    def test_max_length(self):
        string = 50 * 'abc'
        obj = FizzBuzzDetector(string)
        with self.assertRaises(ValueError):
            obj.getOverlappings()

    def test_uppercase(self):
        string = 10 * 'A'
        obj = FizzBuzzDetector(string)
        with self.assertRaises(ValueError):
            obj.getOverlappings()

    def test_numbers(self):
        string = 50 * '1'
        obj = FizzBuzzDetector(string)
        with self.assertRaises(ValueError):
            obj.getOverlappings()

    def test_correct_data(self):
        string = 'hello my name is alina nice to meet you'
        obj = FizzBuzzDetector(string)
        self.assertEqual(obj.getOverlappings(), {'F': 3, 'B': 2})

if __name__ == '__main__':
    unittest.main()
