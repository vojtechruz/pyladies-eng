def area():
    while True:
        try:
            a = float(input("please choose first side number  "))
            b = float(input("please choose second side number  "))
            if (a < 0 or b < 0):
                print("The side cannot be negative first: {a} second: {b}".format(a = a, b = b))
            else:
                break
        except ValueError:
            print("Not a number.")
    return a * b


if __name__ == '__main__':
    print(area())