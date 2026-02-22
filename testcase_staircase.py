import unittest

def staircase(n, display):
    if n <= 0 or n > 30:
        return "n must be in the range of 1 to 30"
    
    result = []
    for i in range(1, n + 1):
        result.append(display * i)
    return '\n'.join(result)

class TestStaircaseFunction(unittest.TestCase):

    def test_valid_inputs(self):
        test_cases = [
            (1, "#", "#"),  
            (4, "#", "#\n##\n###\n####"),  
            (5, "*", "*\n**\n***\n****\n*****"),  
            (30, "+", "+\n++\n+++\n++++\n+++++\n" + "\n".join(["+" * i for i in range(6, 31)])),  
            (5, "A", "A\nAA\nAAA\nAAAA\nAAAAA"),  
            (2, "@", "@\n@@")  
        ]

        for n, display, expected_output in test_cases:
            with self.subTest(n=n, display=display):
                self.assertEqual(staircase(n, display), expected_output)

    def test_invalid_inputs(self):
        test_cases = [
            (0, "#", "n must be in the range of 1 to 30"),  
            (-1, "*", "n must be in the range of 1 to 30"),  
            (31, "+", "n must be in the range of 1 to 30"),  
            (100, "*", "n must be in the range of 1 to 30"),  
        ]

        for n, display, expected_output in test_cases:
            with self.subTest(n=n, display=display):
                self.assertEqual(staircase(n, display), expected_output)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStaircaseFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)

    total_tests = results.testsRun
    passed_tests = total_tests - len(results.failures) - len(results.errors)
    percentage_passed = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Test passed: {passed_tests} จาก {total_tests} ({percentage_passed:.2f}%)")

if __name__ == '__main__':
    main()