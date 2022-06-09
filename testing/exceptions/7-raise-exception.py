LIST_SIZE = 20

def verify_number(number):
    if 0 <= number < LIST_SIZE:
        print('OK!')
    else:
        raise ValueError('The number {n} is not in the list!'.format(n=number))


if __name__ == '__main__':
    verify_number(10)
    verify_number(30)