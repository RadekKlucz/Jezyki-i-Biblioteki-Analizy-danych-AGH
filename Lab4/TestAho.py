import unittest
from AhoCorasick import SearchStrings

class TestAhoModule(unittest.TestCase):

    def test_trie(self):
        test_object = SearchStrings(["abc", "aab", "cba"])
        self.assertTrue(test_object.trie)

    def test_show_trie(self):
        test_object = SearchStrings(["abc", "aab", "cba"])
        self.assertIsNone(test_object.show_trie())

    def test_methods(self):
        test_object = SearchStrings(["abc", "aab", "cba"])
        text = "aaaaaabc"
        # If is the true, the function correct prints the results 
        self.assertIsNone(test_object.check_inside(text))
        self.assertIsNone(test_object.search_patterns(text))

    def test_error_occure(self):
        test_object = SearchStrings(["abc", "aab", "cba"])
        text = "aaaaaabc"
        self.assertIsNone(test_object.show_trie())
        self.assertEqual(test_object.search_patterns(text), KeyError)


if __name__ == "__main__":
    unittest.main()