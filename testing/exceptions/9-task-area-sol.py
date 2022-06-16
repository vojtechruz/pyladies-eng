class AreaError(Exception):
    pass

def area_of_square(side):
    try:
        side = float(side)

        if side < 0:
            raise AreaError("Side must be positive or 0!")

        return side*side
    except ValueError:
        raise AreaError("This is nto a number!")

while True:
    side = input("Side in CM:")
    try:
        area = area_of_square(side)
        break
    except AreaError as error:
        print(error)

if __name__ == '__main__':
    print("Area is: {}".format(area))


