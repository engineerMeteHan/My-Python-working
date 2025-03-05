import unittest

def is_true(value):
    return bool(value)

class TestBool(unittest.TestCase):
    def test_is_true_with_true(self):
        self.assertTrue(is_true(True))

    def test_is_true_with_false(self):
        self.assertFalse(is_true(False))

    def test_is_true_with_non_empty_string(self):
        self.assertTrue(is_true("non-empty"))

    def test_is_true_with_empty_string(self):
        self.assertFalse(is_true(""))

if __name__ == '__main__':
    unittest.main()