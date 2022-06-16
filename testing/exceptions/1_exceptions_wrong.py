# Simple example
def out_func():
    return in_func(0)


def in_func(divisor):
    try:
        print("All great")
        return 1 / divisor
    except:
        return
if __name__ == '__main__':
    print(out_func())