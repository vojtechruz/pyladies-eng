def square():
    while True:
        try:
            side = float(input('Side size in cm: '))
        except ValueError:
            print("Not  a number.")
            continue
        if side <= 0:
            print('side cannot be negative')
        else:
            break
    return side * side


if __name__ == '__main__':
    print(square())
