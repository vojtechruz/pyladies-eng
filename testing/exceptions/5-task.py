#To Do - add condition to program, which ensure that user will input only number.
#Program should repeat asking till user input number.

def square():
    while True:
        side = float(input('Side size in cm: '))
        if side <= 0:
            print('side cannot be negative')
        else:
            break
    return side * side


if __name__ == '__main__':
    print(square())