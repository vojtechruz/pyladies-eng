def area():
    try:
        a = float(input("please choose first side number  "))
        b = float(input("please choose second side number  "))
    except ValueError:
        print("Not a number.")

    if (a < 0 or b < 0):
        raise ValueError("The side cannot be negative first: {a} second: {b}".format(a = a, b = b))
    return a * b


if __name__ == '__main__':
    print(area())