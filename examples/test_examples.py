"""
Test Examples - GitHub Copilot in PyCharm

This file demonstrates how Copilot can generate unit tests.
Use the /tests command in Copilot Chat to generate tests automatically.
"""

import unittest
from examples.basic_examples import (
    factorial,
    is_palindrome,
    get_even_numbers,
    square_numbers,
    BankAccount,
    merge_dictionaries,
    invert_dictionary,
    safe_divide,
    calculate_age,
    to_title_case,
    count_words,
    remove_duplicate_chars
)


class TestBasicFunctions(unittest.TestCase):
    """Test cases for basic utility functions."""
    
    def test_factorial_zero(self):
        """Test factorial of 0 should return 1."""
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_one(self):
        """Test factorial of 1 should return 1."""
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_positive(self):
        """Test factorial of positive numbers."""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
    
    def test_is_palindrome_true(self):
        """Test palindrome detection for valid palindromes."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
    
    def test_is_palindrome_false(self):
        """Test palindrome detection for non-palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
    
    def test_is_palindrome_empty(self):
        """Test palindrome detection for empty string."""
        self.assertTrue(is_palindrome(""))
    
    def test_get_even_numbers(self):
        """Test filtering even numbers from a list."""
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(get_even_numbers([1, 3, 5]), [])
        self.assertEqual(get_even_numbers([2, 4, 6]), [2, 4, 6])
    
    def test_square_numbers(self):
        """Test squaring numbers in a list."""
        self.assertEqual(square_numbers([1, 2, 3, 4]), [1, 4, 9, 16])
        self.assertEqual(square_numbers([]), [])
        self.assertEqual(square_numbers([5]), [25])


class TestBankAccount(unittest.TestCase):
    """Test cases for BankAccount class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.account = BankAccount("123456", 1000)
    
    def test_initial_balance(self):
        """Test initial balance is set correctly."""
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_deposit_positive_amount(self):
        """Test depositing positive amount."""
        self.assertTrue(self.account.deposit(500))
        self.assertEqual(self.account.get_balance(), 1500)
    
    def test_deposit_negative_amount(self):
        """Test depositing negative amount should fail."""
        self.assertFalse(self.account.deposit(-100))
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_deposit_zero(self):
        """Test depositing zero should fail."""
        self.assertFalse(self.account.deposit(0))
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_withdraw_valid_amount(self):
        """Test withdrawing valid amount."""
        self.assertTrue(self.account.withdraw(300))
        self.assertEqual(self.account.get_balance(), 700)
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than balance should fail."""
        self.assertFalse(self.account.withdraw(1500))
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_withdraw_negative_amount(self):
        """Test withdrawing negative amount should fail."""
        self.assertFalse(self.account.withdraw(-100))
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_transaction_history(self):
        """Test transaction history is recorded correctly."""
        self.account.deposit(500)
        self.account.withdraw(200)
        history = self.account.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertIn("Deposit: +$500", history[0])
        self.assertIn("Withdrawal: -$200", history[1])


class TestDictionaryOperations(unittest.TestCase):
    """Test cases for dictionary operations."""
    
    def test_merge_dictionaries(self):
        """Test merging two dictionaries."""
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})
    
    def test_merge_empty_dictionaries(self):
        """Test merging with empty dictionaries."""
        dict1 = {'a': 1}
        dict2 = {}
        result = merge_dictionaries(dict1, dict2)
        self.assertEqual(result, {'a': 1})
    
    def test_invert_dictionary(self):
        """Test inverting dictionary keys and values."""
        d = {'a': 1, 'b': 2, 'c': 3}
        result = invert_dictionary(d)
        self.assertEqual(result, {1: 'a', 2: 'b', 3: 'c'})
    
    def test_invert_empty_dictionary(self):
        """Test inverting empty dictionary."""
        result = invert_dictionary({})
        self.assertEqual(result, {})


class TestErrorHandling(unittest.TestCase):
    """Test cases for error handling functions."""
    
    def test_safe_divide_normal(self):
        """Test safe division with valid inputs."""
        self.assertEqual(safe_divide(10, 2), 5.0)
        self.assertEqual(safe_divide(7, 2), 3.5)
    
    def test_safe_divide_by_zero(self):
        """Test safe division by zero returns None."""
        self.assertIsNone(safe_divide(10, 0))
    
    def test_safe_divide_type_error(self):
        """Test safe division with invalid types returns None."""
        self.assertIsNone(safe_divide("10", 2))
        self.assertIsNone(safe_divide(10, "2"))


class TestStringManipulation(unittest.TestCase):
    """Test cases for string manipulation functions."""
    
    def test_to_title_case(self):
        """Test converting string to title case."""
        self.assertEqual(to_title_case("hello world"), "Hello World")
        self.assertEqual(to_title_case("python programming"), "Python Programming")
    
    def test_count_words(self):
        """Test counting words in a string."""
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words("one two three four"), 4)
        self.assertEqual(count_words("single"), 1)
    
    def test_count_words_empty(self):
        """Test counting words in empty string."""
        self.assertEqual(count_words(""), 0)
    
    def test_remove_duplicate_chars(self):
        """Test removing duplicate characters."""
        self.assertEqual(remove_duplicate_chars("hello"), "helo")
        self.assertEqual(remove_duplicate_chars("aabbcc"), "abc")
        self.assertEqual(remove_duplicate_chars("abcdef"), "abcdef")


class TestDateCalculations(unittest.TestCase):
    """Test cases for date calculation functions."""
    
    def test_calculate_age(self):
        """Test age calculation from birthdate."""
        # Note: These tests may need adjustment based on current date
        # Using a known birthdate for testing
        age = calculate_age("1990-01-01")
        self.assertGreater(age, 30)  # Should be at least 30 years old
        self.assertLess(age, 40)  # Should be less than 40 years old
    
    def test_calculate_age_recent(self):
        """Test age calculation for recent birthdate."""
        age = calculate_age("2020-01-01")
        self.assertGreater(age, 4)  # Should be at least 4 years old
        self.assertLess(age, 10)  # Should be less than 10 years old


# Test runner
if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
