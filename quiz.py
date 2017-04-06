

import random


countrydict = {"Slovenia": "Ljubljana",
               "Croatia": "Zagreb",
               "Austria": "Vienna",
               "Italy": "Rome",
               "Germany": "Berlin"}

def get_random_capital(countrydict):
    country = random.choice(countrydict.keys())
    return country

capitalpicturedict = {"Slovenia": "http://images.wisegeek.com/ljubljana-slovenia.jpg",
                  "Croatia": "http://3.bp.blogspot.com/-54vAIFuCaBk/T2c_2J31MsI/AAAAAAAABPE/-sCCNZvkdpY/s1600/croatia+tourism.jpg",
                  "Austria": "https://s-media-cache-ak0.pinimg.com/originals/03/1d/54/031d545871a9960382f3011692cc4a9d.jpg",
                  "Italy": "http://www.enjoyourholiday.com/wp-content/uploads/2012/03/Rome-the-romantic-capital-of-Italy-1.jpg",
                  "Germany": "http://www.english-online.at/current_affairs/german-reunification/brandenburg-gate-symbol-of-reunification.jpg"}

def get_capital_picture(country, capitalpicturedict):
    picture = capitalpicturedict.get(country, None)
    return picture


def check_result(capital, user_capital, countrydict):
    check = countrydict.get(capital, None)
    if check == user_capital:
        text = "You are right!!"
        return text
    else:
        text = "Sorry the capital of %s is %s! Try again!" % (capital, check)
        return text

