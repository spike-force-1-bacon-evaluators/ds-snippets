import unittest
import tweet_age as ta

class TestMainMethods(unittest.TestCase):
    def test_date_format(self):
        self.assertEquals(ta.tweet_age("1-6-2017", "2-6-2017"), 31)
        self.assertEquals(ta.tweet_age("2-6-2017", "2-7-2017"), 1)

if __name__ == '__main__':
    unittest.main()

