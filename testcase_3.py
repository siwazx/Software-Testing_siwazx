import unittest

def caesarCipher(s, k):
    def transform(char):
        if char.islower():
            return chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        if char.isupper():
            return chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            return char
    
    characters = list(s)
    
    return "".join(map(transform, characters))

class TestCaesarCipherFunction(unittest.TestCase):

    def test_lowercase(self):
        test_cases = [
            ("abc", 2, "cde"),
            ("xyz", 2, "zab"),
            ("morning", 5, "rtwsnsl")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

    def test_uppercase(self):
        test_cases = [
            ("ABC", 3, "DEF"),
            ("XYZ", 3, "ABC"),
            ("MORNING", 7, "TVYUPUN")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

    def test_mixed_case(self):
        test_cases = [
            ("GoodMorning", 4, "KsshQsvrmrk")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

    def test_special_characters(self):
        test_cases = [
            ("Hello, World!", 3, "Khoor, Zruog!"),
            ("123-456!", 5, "123-456!")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

    def test_k_zero(self):
        test_cases = [
            ("NoChange", 0, "NoChange")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

    def test_k_greater_than_26(self):
        test_cases = [
            ("abc", 26, "abc"),
            ("xyz", 28, "zab"),
            ("ABC", 52, "ABC")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

    def test_k_negative(self):
        test_cases = [
            ("def", -2, "bcd"),
            ("XYZ", -3, "UVW"),
            ("aBc", -1, "zAb")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

    def test_empty_string(self):
        test_cases = [
            ("", 5, "")
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaesarCipherFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
    
    total_tests = results.testsRun
    passed_tests = total_tests - len(results.failures) - len(results.errors)
    percentage_passed = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Test Passed: {passed_tests} จาก {total_tests} ({percentage_passed:.2f}%)")

if __name__ == '__main__':
    main()