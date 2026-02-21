import unittest

def funnyString(s):
    n = len(s)
    for i in range(1, n):
        start_diff = abs(ord(s[i]) - ord(s[i - 1]))
        end_diff = abs(ord(s[n - i]) - ord(s[n - i - 1]))
        if start_diff != end_diff:
            return 'Not Funny'
    return 'Funny'

class TestFunnyStringFunction(unittest.TestCase):

    def test_funny_strings(self):
        test_cases = [
            ("", "Funny"),            # Empty string
            ("a", "Funny"),           # Single character
            ("aa", "Funny"),          # Two identical characters
            ("ab", "Funny"),          # Two different characters
            ("aaa", "Funny"),         # All same characters
            ("racecar", "Funny"),     # Palindrome (odd length)
            ("abba", "Funny"),        # Palindrome (even length)
            ("abcde", "Funny"),       # Non-palindrome (odd length)
            ("abcd", "Funny"),        # Non-palindrome (even length)
            ("abababab", "Funny"),    # Alternating characters
            ("azAZ", "Funny"),        # Large differences
        ]

        for s, expected in test_cases:
            with self.subTest(s=s):
                self.assertEqual(funnyString(s), expected)

    def test_not_funny_strings(self):
        test_cases = [
            ("bcxz", "Not Funny"),    # Non-funny string (odd length)
        ]

        for s, expected in test_cases:
            with self.subTest(s=s):
                self.assertEqual(funnyString(s), expected)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunnyStringFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
    
    total_tests = results.testsRun
    passed_tests = total_tests - len(results.failures) - len(results.errors)
    percentage_passed = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Test passed: {passed_tests} จาก {total_tests} ({percentage_passed:.2f}%)")

if __name__ == '__main__':
    main()
