def area():
    try:
        a = float(input("please choose first side number  "))
        b = float(input("please choose second side number  "))
    except ValueError:
        print("Not a number.")
    return a * b


if __name__ == '__main__':
    print(area())