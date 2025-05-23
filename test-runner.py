import unittest
import importlib

class TestAssignmentFour(unittest.TestCase):
    def test_01_Pet(self):
        dog = asgmt.Pet('Dog', 'Bark')
        self.assertEqual(dog.species, 'Dog')
        self.assertEqual(dog.make_sound(), 'Bark')
        kitty = asgmt.Pet('Cat', 'Meow')
        self.assertEqual(kitty.species, 'Cat')
        self.assertEqual(kitty.make_sound(), 'Meow')
    def test_02_Hogwarts(self):
        hogwarts = asgmt.Hogwarts()
        self.assertEqual(hogwarts.location, 'Scotland')
        self.assertEqual(hogwarts.founders, ['Godric Gryffindor', 'Salazar Slytherin', 'Rowena Ravenclaw', 'Helga Hufflepuff'])
        self.assertEqual(hogwarts.houses, ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'])
    def test_03_StrCase(self):
        luke = asgmt.StrCase('Luke Skywalker')
        self.assertEqual(luke.upper_case(), 'LUKE SKYWALKER')
        self.assertEqual(luke.lower_case(), 'luke skywalker')
        self.assertEqual(luke.swap_case(), 'lUKE sKYWALKER')
        anakin = asgmt.StrCase('Anakin Skywalker')
        self.assertEqual(anakin.upper_case(), 'ANAKIN SKYWALKER')
        self.assertEqual(anakin.lower_case(), 'anakin skywalker')
        self.assertEqual(anakin.swap_case(), 'aNAKIN sKYWALKER')
    def test_04_MethodCalculator(self):
        method_calculator = asgmt.MethodCalculator(5, 6)
        self.assertEqual(method_calculator.add(), 11)
        self.assertEqual(method_calculator.subtract(), -1)
        self.assertEqual(method_calculator.multiply(), 30)
        self.assertGreaterEqual(method_calculator.divide(), 0.8)
        method_calculator = asgmt.MethodCalculator(10, 10)
        self.assertEqual(method_calculator.add(), 20)
        self.assertEqual(method_calculator.subtract(), 0)
        self.assertEqual(method_calculator.multiply(), 100)
        self.assertGreaterEqual(method_calculator.divide(), 1)
    def test_05_SymbolicCalculator(self):
        symbolic_calculator = asgmt.SymbolicCalculator(5, 6)
        self.assertGreaterEqual(symbolic_calculator.calculate('+'), 11)
        self.assertGreaterEqual(symbolic_calculator.calculate('-'), -1)
        self.assertGreaterEqual(symbolic_calculator.calculate('*'), 30)
        self.assertGreaterEqual(symbolic_calculator.calculate('/'), 0.8)
        symbolic_calculator = asgmt.SymbolicCalculator(10, 10)
        self.assertGreaterEqual(symbolic_calculator.calculate('+'), 20)
        self.assertGreaterEqual(symbolic_calculator.calculate('-'), 0)
        self.assertGreaterEqual(symbolic_calculator.calculate('*'), 100)
        self.assertGreaterEqual(symbolic_calculator.calculate('/'), 1)
    def test_06_FizzBuzz(self):
        fizz_buzz = asgmt.FizzBuzz()
        self.assertEqual(fizz_buzz.scalar_fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz.scalar_fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz.scalar_fizz_buzz(3), 'Fizz')
        self.assertEqual(fizz_buzz.scalar_fizz_buzz(4), 4)
        self.assertEqual(fizz_buzz.scalar_fizz_buzz(5), 'Buzz')
        self.assertEqual(fizz_buzz.scalar_fizz_buzz(15), 'Fizz Buzz')
        self.assertEqual(fizz_buzz.range_fizz_buzz(1, 6), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(fizz_buzz.range_fizz_buzz(11, 16), [11, 'Fizz', 13, 14, 'Fizz Buzz'])
        self.assertEqual(fizz_buzz.range_fizz_buzz(6, 11), ['Fizz', 7, 8, 'Fizz', 'Buzz'])
    def test_07_Summation(self):
        summation = asgmt.Summation(1, 2)
        self.assertEqual(summation.total(), 3)
        self.assertEqual(summation.cumulative(), [1, 3])
        summation = asgmt.Summation(1, 2, 3)
        self.assertEqual(summation.total(), 6)
        self.assertEqual(summation.cumulative(), [1, 3, 6])
        summation = asgmt.Summation(2, 3, 5)
        self.assertEqual(summation.total(), 10)
        self.assertEqual(summation.cumulative(), [2, 5, 10])
        summation = asgmt.Summation(2, 3, 5, 7, 11)
        self.assertEqual(summation.total(), 28)
        self.assertEqual(summation.cumulative(), [2, 5, 10, 17, 28])
    def test_08_DaysOfWeek(self):
        days_of_week = asgmt.DaysOfWeek(0)
        self.assertEqual(days_of_week.get_name(), 'Sunday')
        self.assertEqual(days_of_week.get_abbreviation(), 'Sun.')
        days_of_week = asgmt.DaysOfWeek(1)
        self.assertEqual(days_of_week.get_name(), 'Monday')
        self.assertEqual(days_of_week.get_abbreviation(), 'Mon.')
        days_of_week = asgmt.DaysOfWeek(2)
        self.assertEqual(days_of_week.get_name(), 'Tuesday')
        self.assertEqual(days_of_week.get_abbreviation(), 'Tue.')
        days_of_week = asgmt.DaysOfWeek(6)
        self.assertEqual(days_of_week.get_name(), 'Saturday')
        self.assertEqual(days_of_week.get_abbreviation(), 'Sat.')
    def test_09_Month(self):
        month = asgmt.Month(1)
        self.assertEqual(month.get_name(), 'January')
        self.assertEqual(month.get_abbreviation(), 'JAN')
        month = asgmt.Month(2)
        self.assertEqual(month.get_name(), 'February')
        self.assertEqual(month.get_abbreviation(), 'FEB')
        month = asgmt.Month(3)
        self.assertEqual(month.get_name(), 'March')
        self.assertEqual(month.get_abbreviation(), 'MAR')
        month = asgmt.Month(12)
        self.assertEqual(month.get_name(), 'December')
        self.assertEqual(month.get_abbreviation(), 'DEC')
    def test_10_Palindrome(self):
        palindrome = asgmt.Palindrome("yay")
        self.assertEqual(palindrome.get_reversed_text(), 'yay')
        self.assertTrue(palindrome.is_palindrome())
        palindrome = asgmt.Palindrome("eye")
        self.assertEqual(palindrome.get_reversed_text(), 'eye')
        self.assertTrue(palindrome.is_palindrome())
        palindrome = asgmt.Palindrome("day")
        self.assertEqual(palindrome.get_reversed_text(), 'yad')
        self.assertFalse(palindrome.is_palindrome())
        palindrome = asgmt.Palindrome("dye")
        self.assertEqual(palindrome.get_reversed_text(), 'eyd')
        self.assertFalse(palindrome.is_palindrome())
        palindrome = asgmt.Palindrome("kayak")
        self.assertTrue(palindrome.is_palindrome())
        palindrome = asgmt.Palindrome("maya")
        self.assertFalse(palindrome.is_palindrome())

asgmt = importlib.import_module("asgmt")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFour)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))