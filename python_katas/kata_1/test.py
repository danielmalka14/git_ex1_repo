import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner

testers = ['dorondollev',
           'danielbar0101',
           'DustyMadDude',
           'Amitpoz',
           'netanalm',
           'AlexeyMihaylovDev',
           'xXxARLxXx']


class TestSumOfElements(unittest.TestCase):
    """
    1 Katas
    """

# def sum_of_element(self):
#     return sum(self)

    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)

    def test_integers_list(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(questions.sum_of_element(lst), 15)

    def test_negative_numbers(self):
        lst = [1, -6, 7, 0, 99]
        self.assertEqual(questions.sum_of_element(lst), 101)

    def test_all_zeros(self):
        lst = [0] * 50000
        self.assertEqual(questions.sum_of_element(lst), 0)


class TestVerbing(unittest.TestCase):
    """
    1 Katas
    """
    def test_sample(self):
        # your code here
        pass


class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """


class TestReverseWordsConcatenation(unittest.TestCase):

    """
    1 Katas
    """
    def reverse_empty_string(self):
        lst = []
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)

    def reverse_long_strings(self):
        lst = ["runasdfasdffwerfzvxzcvzxcvfassdafasfeqewr", "jvxcvzxcvzxvcxzcvxzvcxvcohnny", "hzxvczxvcxzcvzxvcxzcvome"]
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)

    def reverse_integer_string(self):
        lst = ['1', '3', '2', '0']
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)

    def reverse_mixed_elements(self):
        lst = ["1", 'foo', 'bar', 'baz', "2"]
        self.assertEqual(questions.reverse_words_concatenation(lst), 0)


class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestPalindromeNum(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestPairMatch(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestBadAverage(unittest.TestCase):
    """
    1 Katas
    """

    def BadAverage_int_elements(self):
        lst = [1, 2, 3]
        self.assertEqual(questions.bad_average(lst), 0)

    def BadAverage_big_negative_element(self):
        lst = [-500000000000000000000000000, 50000000000000000000000001, 1]
        self.assertEqual(questions.bad_average(lst), 0)

    def BadAverage_negative_elements(self):
        lst = [-1, -2, -3]
        self.assertEqual(questions.bad_average(lst), 0)

    def BadAverage_float_elements(self):
        lst = [1.1111111111111, 2.2, 3.5]
        self.assertEqual(questions.bad_average(lst), 0)


class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """

    def BestGrade_example_elements(self):
        dict1 = {
            "Ben": 78,
            "Hen": 88,
            "Natan": 99,
            "Efraim": 65,
            "Rachel": 95
        }
        self.assertEqual(questions.best_student(dict1), 0)


   def bestgrade_overgrade_elements(self):
        dict1 = {
            "Ben": 101,
            "Hen": 112,
            "Natan": 110,
            "Efraim": 103,
            "Rachel": 30
        }
        self.assertEqual(questions.best_student(dict1), 0)


    def bestgrade_samegrade_elements(self):
        dict1 = {
            "Ben": 88,
            "Hen": 88,
            "Natan": 88,
            "Efraim": 88,
            "Rachel": 88
        }
        self.assertEqual(questions.best_student(dict1), 0)


class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestSevenBoom(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestCaesarCipher(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


if __name__ == '__main__':
    import inspect
    import sys

    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
