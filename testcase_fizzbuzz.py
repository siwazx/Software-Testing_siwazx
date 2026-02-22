import unittest

# FizzBuzz function
def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

# Test class
class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz(self):
        test_cases = [
            (3, "Fizz"),
            (6, "Fizz"),
            (9, "Fizz"),
            (12, "Fizz"),
            (5, "Buzz"),
            (10, "Buzz"),
            (20, "Buzz"),
            (25, "Buzz"),
            (15, "FizzBuzz"),
            (30, "FizzBuzz"),
            (45, "FizzBuzz"),
            (60, "FizzBuzz"),
            (1, "1"),
            (2, "2"),
            (4, "4"),
            (7, "7"),
            (8, "8"),
            (11, "11"),
        ]
        
        passed_tests = 0
        total_tests = len(test_cases)
        
        # Loop through each test case
        for x, expected in test_cases:
            with self.subTest(x=x):
                result = fizzbuzz(x)
                if result == expected:
                    passed_tests += 1
                self.assertEqual(result, expected)
        
        # Calculate percentage of passed tests
        passed_percentage = (passed_tests / total_tests) * 100
        print(f"Test Passed: {passed_tests}/{total_tests} ({passed_percentage:.2f}%)")

# Run the tests
if __name__ == "__main__":
    unittest.main()