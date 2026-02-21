import unittest

def alternatingCharacters(s):
    # Write your code here
    deletions = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            deletions += 1
    return deletions

class TestAlternatingCharactersFunction(unittest.TestCase):

    def test_alternating_characters(self):
        test_cases = [
            ("AAAA", 3, "ซ้ำกันทั้งหมด A"),
            ("BBBBB", 4, "ซ้ำกันทั้งหมด B"),
            ("ABABABAB", 0, "ไม่มีการลบ (AB สลับกัน)"),
            ("BABABA", 0, "ไม่มีการลบ (BA สลับกัน)"),
            ("AAABBB", 4, "แบ่งเป็นสองกลุ่มซ้ำกัน"),
            ("A", 0, "มีตัวอักษรเดียว"),
            ("AB", 0, "ไม่มีการลบ AB"),
            ("BA", 0, "ไม่มีการลบ BA"),
            ("AABBAB", 2, "ซ้ำกันบางจุด"),
            ("ABBAABB", 3, "ซ้ำกันและมีรูปแบบที่ต้องลบหลายจุด")
        ]

        for s, expected, desc in test_cases:
            with self.subTest(s=s, desc=desc):
                self.assertEqual(alternatingCharacters(s), expected)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlternatingCharactersFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)

    total_tests = results.testsRun
    passed_tests = total_tests - len(results.failures) - len(results.errors)
    percentage_passed = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Test Passed: {passed_tests} จาก {total_tests} ({percentage_passed:.2f}%)")

if __name__ == '__main__':
    main()