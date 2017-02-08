from datetime import datetime as dt

def tweet_age(last_tweet_date, today_date=""):
    date_format = "%m-%d-%Y"
    if today_date == "":
        td = dt.now()
        today_date = td.strftime(date_format)
    a = dt.strptime(last_tweet_date, date_format)
    b = dt.strptime(today_date, date_format)
    delta = b - a
    return delta.days
