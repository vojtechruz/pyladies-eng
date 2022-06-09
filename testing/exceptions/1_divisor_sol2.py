# Simple example
def out_func():
    return in_func(0)


def in_func(divisor):
    try:
        return 1 / divisor
    except ZeroDivisionError:
        print("Dividing by 0 returning 0")
        return 0

if __name__ == '__main__':
    print(out_func())