# task:
# - change area_of_square should throw AreaError if following condition are not met
#      - value must be number
#      - number must be 0 or positive
# - if Exception AreaError is throw, re-ask user for numbers.


class AreaError(Exception):
    pass


def area_of_square(side):
    side = float(side)
    return side*side


if __name__ == '__main__':
    area_of_square(10)


