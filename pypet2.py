# abandoned; use pypet.py

import random
from time import sleep
from multiprocessing import Process

py_cat = {
    'photo': '(=^o.o^=)__',
    'name': 'Mochi',
    'age': 5,
    'weight': 5.78,
    'hungry': True,
    'phrases': ["Purrr", "*lick* *lick*", "Meow! Mew!"]
}
py_mouse = {
    'photo': '‹:3 )~~~~',
    'name': 'Speck',
    'age': 3,
    'weight': 0.98,
    'hungry': False,
    'phrases': ["SqueK!", "*nibble *nibble", "*Squeek SQUEEK"]
}


# photo = "(=^o.o^=)__"
# name = "Mochi"
# age = 5
# weight = 5.78
# hungry = True
# phrases = ["Purrr", "*lick* *lick*", "Meow! Mew!"]


def startup_pypet():
    print("Welcome to Pypet")
    print("Hello, it's " + py_cat['name'])
    print(py_cat['photo'])


def pypet_stats():
    print(py_cat['photo'])

    print(py_cat['name'] + " weighs " + str(py_cat['weight']) + " pounds ")

    if py_cat['hungry']:
        print("Your pypet is hungry!")
    else:
        print("Your pypet *BURPS* loudly")


startup_pypet()


# pypet_stats()

# terminate = False

def usrgui():
    # while not terminate:
    while True:
        print("#####################################")

        user_input = input('> ')

        if user_input == "quit":
            #   terminate = True
            print("do ctrl+c")
        elif user_input == "stats":
            pypet_stats()
        elif user_input == "feed":
            print("Om Nom Nom")
            py_cat['weight'] = py_cat['weight'] + 1.5
            py_cat['hungry'] = False
        elif user_input == "chat":
            print(random.choice(py_cat['phrases']))
        else:
            print("Sorry, I don't understand")


def hunger():
    # while not terminate:
    while True:
        while not py_cat['hungry']:
            if py_cat['hungry'] == False:
                print("not hungry")
                sleep(1)
                py_cat['hungry'] = True


if __name__ == '__main__':
    proc1 = Process(target=usrgui)
    proc1.start()

    proc2 = Process(target=hunger)
    proc2.start()

print("Goodbye!")
