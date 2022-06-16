def get_age_of_user():
    while True:
        age = input('Age: \n')

        try:
            age = int(age)
        except ValueError:
            print("{0} Age is not intege!!".format(age))
            continue

        if age < 0:
            print("Negative Age")
        else:
            print("All OK")
            return age


if __name__ == '__main__':
    print(get_age_of_user())
