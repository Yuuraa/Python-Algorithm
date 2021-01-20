def isValid(s:str) -> bool:
    matching_brackets = {'}': '{', ']': '[', ')': '('}
    stack = []
    for bracket in s:
        if bracket in matching_brackets:
            if not stack:
                return False
            if stack.pop() != matching_brackets[bracket]:
                return False
        else:
            stack.append(bracket)
    return len(stack) == 0


if __name__ == '__main__':
    import unittest
    from mock import patch
    from io import StringIO

    class TestIsValid(unittest.TestCase):
        def test_is_valid(self):
            self.assertEqual(True, isValid("()"))
            self.assertEqual(True, isValid("()[]{()}"))
            self.assertEqual(False, isValid("(]"))
            self.assertEqual(False, isValid("([)]"))
            self.assertEqual(True, isValid("{[]}"))

    unittest.main()
