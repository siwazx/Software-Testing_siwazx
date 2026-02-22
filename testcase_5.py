import unittest

def gridChallenge(grid):
    rows_item = []
    for item in grid:
        items = list(item)
        items.sort()
        rows_item.append(items)
    for i in range(len(rows_item[0])):
        for j in range(1, len(rows_item)):
            if rows_item[j][i] < rows_item[j-1][i]:
                return "NO"
    
    return "YES"

class TestGridChallengeFunction(unittest.TestCase):

    def test_grid_challenge(self):
        test_cases = [
            (["abc", "def", "ghi"], "YES"),  # Rows and columns are already in alphabetical order
            (["abc", "fde", "ghi"], "YES"),  # One row is not initially sorted, but becomes valid after sorting
            (["axb"], "YES"),  # Smallest case where a single row is not sorted initially
            (["aaa", "aaa", "aaa"], "YES"),  # All characters are identical
            (["abcd", "bcde", "cdef", "defg"], "YES"),  # 4x4 grid sorted correctly by rows and columns
            (["a", "b", "c"], "YES"),  # Single column in ascending alphabetical order
            (["c", "b", "a"], "NO"),  # Single column in descending order
            (["az", "by", "cx"], "NO"),  # Characters are scattered and columns are not sorted
            (["aa", "bb", "cc"], "YES"),  # Repeated characters grouped and sorted properly
            (["zy", "wx", "vu"], "NO"),  # Characters are in reverse alphabetical order
            (["mnop", "qrst", "uvwx", "yzab"], "NO"),  # Alphabet wraps from z back to a, breaking order
            (["abc"], "YES"),  # Only one row and already sorted
            (["aab", "abb", "bcc"], "YES"),  # Repeated characters valid across rows and columns
            (["abc", "ade", "efg"], "YES"),  # Rows and columns sorted (e.g., columns: a a e, b d f, c e g)
            (["zyx", "wvu", "tsr"], "NO")  # Rows cannot be sorted to satisfy column condition
        ]

        for grid, expected in test_cases:
            with self.subTest(grid=grid):
                self.assertEqual(gridChallenge(grid), expected)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGridChallengeFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
    
    total_tests = results.testsRun
    passed_tests = total_tests - len(results.failures) - len(results.errors)
    percentage_passed = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Test Passed: {passed_tests} from {total_tests} ({percentage_passed:.2f}%)")

if __name__ == '__main__':
    main()