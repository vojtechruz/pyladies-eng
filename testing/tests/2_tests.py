# 1. children  up to 10 years included for free
# 2. young till 18 included for half price
# 3. seniors from 65 years included for 1/3
# 4. Other for full price
# 5. negative age must be ValueError

def sale_on_the_ticket(basic_price,age ):
    if age < 0:
        raise ValueError
    elif age <=10:
        return 0
    elif age <=18:
        return basic_price / 2
    elif age < 65:
        return basic_price
    else:
        return basic_price / 3


def test_addult_full_price():
    assert sale_on_the_ticket(30.0, 35) == 30.0


def test_young_half_price():
    assert sale_on_the_ticket(30.0, 16) == 15.0


def test_senior_for_third():
    assert sale_on_the_ticket(30.0, 70) == 10.0

#task
#add test: children till 10 year are having free ride (za 0)
#add test: negative age throw ValueError
#add test: 18 is still young - half price then

#bonus tasks:
# add condition: basic price < 0 thorw ValueError and add test to check it
# add condition: from 80 years - included is ticket for free , with testing that


