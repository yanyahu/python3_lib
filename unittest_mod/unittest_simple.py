import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)

"""
$ python3 -m unittest unittest_simple.py
.
----------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
