"""
Basic Examples - GitHub Copilot Usage in PyCharm

This file demonstrates basic GitHub Copilot features and commands.
Try these examples to learn how Copilot can help expedite development.
"""


# Example 1: Function Generation with Comments
# =============================================
# Write a descriptive comment and let Copilot suggest the implementation

# Function to calculate the factorial of a number
def factorial(n):
    """Calculate factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Function to check if a string is a palindrome
def is_palindrome(text):
    """Check if the given text is a palindrome (case-insensitive)."""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


# Example 2: List Comprehensions and Data Processing
# ==================================================

# Function to filter even numbers from a list
def get_even_numbers(numbers):
    """Return only even numbers from the list."""
    return [n for n in numbers if n % 2 == 0]


# Function to square all numbers in a list
def square_numbers(numbers):
    """Return a list of squared numbers."""
    return [n ** 2 for n in numbers]


# Example 3: Class Generation
# ============================

# Class to represent a simple bank account
class BankAccount:
    """Simple bank account with deposit and withdrawal capabilities."""
    
    def __init__(self, account_number, balance=0):
        """Initialize bank account with account number and optional initial balance."""
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_balance(self):
        """Return current account balance."""
        return self.balance
    
    def get_transaction_history(self):
        """Return list of all transactions."""
        return self.transaction_history


# Example 4: Dictionary Operations
# =================================

# Function to merge two dictionaries
def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries, with dict2 values taking precedence."""
    result = dict1.copy()
    result.update(dict2)
    return result


# Function to invert a dictionary (swap keys and values)
def invert_dictionary(d):
    """Return a new dictionary with keys and values swapped."""
    return {v: k for k, v in d.items()}


# Example 5: Error Handling
# ==========================

# Function to safely divide two numbers
def safe_divide(a, b):
    """Divide a by b with error handling for division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None


# Function to read a file safely
def read_file_safely(filename):
    """Read file content with proper error handling."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except PermissionError:
        return None


# Example 6: Working with Dates
# ==============================

from datetime import datetime, timedelta


# Function to get current date and time
def get_current_datetime():
    """Return current date and time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Function to calculate age from birthdate
def calculate_age(birthdate):
    """Calculate age in years from birthdate string (YYYY-MM-DD)."""
    birth = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birth.year
    if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
        age -= 1
    return age


# Example 7: String Manipulation
# ===============================

# Function to convert string to title case
def to_title_case(text):
    """Convert text to title case."""
    return ' '.join(word.capitalize() for word in text.split())


# Function to count words in a string
def count_words(text):
    """Count the number of words in text."""
    return len(text.split())


# Function to remove duplicates from a string while maintaining order
def remove_duplicate_chars(text):
    """Remove duplicate characters while maintaining order."""
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


# Example Usage
if __name__ == "__main__":
    # Test factorial
    print(f"Factorial of 5: {factorial(5)}")
    
    # Test palindrome
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    
    # Test bank account
    account = BankAccount("12345", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Account balance: ${account.get_balance()}")
    print(f"Transactions: {account.get_transaction_history()}")
    
    # Test age calculation
    print(f"Age for birthdate 1990-01-01: {calculate_age('1990-01-01')}")
