from datetime import datetime as dt


def lastTweet(lastTweetDate, todayDate=""):
    date_format = "%m-%d-%Y"
    if todayDate == "":
        td = dt.now()
        todayDate = td.strftime(date_format)
    a = dt.strptime(lastTweetDate, date_format)
    b = dt.strptime(todayDate, date_format)
    delta = b - a
    return delta.days

print lastTweet("2-6-2017")
