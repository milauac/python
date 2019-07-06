# name = "Jenifer"
#
# for letter in name:
#     print(letter)
#
# list = ["a", "k", "c", "12", "r"]
#
# for symbol in list:
#     print(symbol)
#
# user_input = input('Yes or No?')
#
# known = ["Anna", "Maria", "Bob"]
#
# person = input("Type the name")
#
# if person in known:
#     print("recognized {} ".format(person))
#
# else:
#     print("who is that? {}".format(person))


def who_do_you_know():
    names = input("Type a few names: ")
    list_of_names = names.strip()
    return list_of_names


def ask_user():
    answer = input("Type one name :")
    if answer in who_do_you_know():
        print("You know {}".format(answer))
    else:
        print("This person is out of list{}".format(answer))

ask_user()