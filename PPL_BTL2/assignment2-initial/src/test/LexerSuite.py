import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def testfinal(self):
        self.assertTrue(TestLexer.test(""" "test\\\\ abc" """,
                        """ """, 1))
