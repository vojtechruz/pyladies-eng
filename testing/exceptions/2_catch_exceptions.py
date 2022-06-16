def get_age_of_user():
    while True:
        age = input('Age: \n')

        # what is gonne happened when string is passed?
        age = int(age)

        if age < 0:
            print("Negative Age")
        else:
            print("All OK")
            return age

if __name__ == '__main__':
    print(get_age_of_user())
