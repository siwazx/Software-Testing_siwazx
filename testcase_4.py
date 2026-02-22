import unittest

def alternate(s):
    lens = [0]   
    letters = list(set(s))
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            two = []
            for c in s:
                if c in (letters[i], letters[j]):
                    if two and two[-1] == c:
                        two = []
                        break
                    two.append(c)
            lens.append(len(two))
    return max(lens)

class TestAlternateFunction(unittest.TestCase):

    def test_alternate(self):
        test_cases = [
            ("beabeefeab", 5),     # Normal case
            ("aaaa", 0),           # Single character
            ("ababab", 6),         # Alternating sequence
            ("abcabcabc", 6),      # Multiple characters, choose best pair
            ("aabbcc", 0),         # No alternating pair
            ("abcde", 2),          # Choose best pair
            ("zazbzbz", 0),        # No alternating pair
            ("a", 0),              # Single character
            ("", 0),               # Empty string
            ("ababababababa", 13), # Longest alternating sequence
        ]

        for s, expected in test_cases:
            with self.subTest(s=s):
                self.assertEqual(alternate(s), expected)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlternateFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
    
    # Calculate percentage of passed tests
    total_tests = results.testsRun
    passed_tests = total_tests - len(results.failures) - len(results.errors)
    percentage_passed = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Passed tests: {passed_tests} out of {total_tests} ({percentage_passed:.2f}%)")

if __name__ == '__main__':
    main()