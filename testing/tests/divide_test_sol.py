
def sale_on_the_ticket(basic_price, age):

    if basic_price < 0:
        raise ValueError

    if age < 0:
        raise ValueError
    elif age <=10:
        return 0
    elif age <=18:
        return basic_price / 2
    elif age < 65:
        return basic_price
    elif age < 80:
        return basic_price / 3
    else:
        return 0
