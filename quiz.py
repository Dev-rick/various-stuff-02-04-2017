

import random


countrydict = {"Slovenia": "Ljubljana",
               "Croatia": "Zagreb",
               "Austria": "Vienna",
               "Italy": "Rome",
               "Germany": "Berlin"}

def get_random_capital(countrydict):
    country = random.choice(countrydict.keys())
    return country


def check_result(capital, user_capital, countrydict):
    check = countrydict.get(capital, None)
    if check == user_capital:
        text = "You are right!!"
        return text
    else:
        text = "Sorry the capital of %s is %s! Try again!" % (capital, check)
        return text

