prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for pair in enumerate(prime_numbers):
    print(pair)
    print('Prime number on position {} is {}'.format(pair[0], pair[1]))


for index, value in enumerate(prime_numbers):
    print('Prime number on position {} is {}'.format(index, value))
