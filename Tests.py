import unittest
import Main as mm


class testMainMethods(unittest.TestCase):
    def testDateFormat(self):
        self.assertEquals(mm.lastTweet("1-6-2017", "2-6-2017"), 31)

    def testDateFormat2(self):
        self.assertEquals(mm.lastTweet("2-6-2017", "2-7-2017"), 1)

if __name__ == '__main__':
    unittest.main()

