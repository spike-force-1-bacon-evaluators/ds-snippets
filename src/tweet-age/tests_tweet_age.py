import tweet_age as ta

def test_tweet_age():
    assert ta.tweet_age("1-6-2017", "2-6-2017") == 31
    assert ta.tweet_age("2-6-2017", "2-7-2017") == 1
