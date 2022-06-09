# Zmen kod tak aby:
# - vypocitej_obsah_ctverce hazela ObsahError kdyz dostane spatnou hodnotu
#      - hodnota musi byt cislo
#      - cislo musi byt nezaporne
# - kdyz se ptas uzivatele na vstup zjisti, jestli nastal ObsahError a kdyz ano, ptej se znovu


# task:
# - varea_of_square should throw AreaError if following condition are not met
#      - value must be number
#      - number must be 0 or positive
# - if Exception AreaError is throwed, re-ask user for numbers.


class AreaError(Exception):
    pass


def area_of_square(side):
    side = float(side)
    return side*side


if __name__ == '__main__':
    area_of_square(10)


