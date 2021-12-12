import random
from time import sleep
py_cat = {
    'photo': '(=^o.o^=)__',
    'name': 'Mochi',
    'age': 5,
    'weight': 5.7,
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
    print ("Welcome to Pypet")
    print ("Hello, it's " + py_cat['name'])
    print (py_cat['photo'])

def pypet_stats():

    print (py_cat['photo'])    

    print (py_cat['name'] + " weighs " + str(py_cat['weight']) + " pounds ")

    if py_cat['hungry']:
        print ("Your pypet is hungry!")
    else:
      print ("Your pypet *BURPS* loudly")
    
startup_pypet()
# pypet_stats()

terminate = False

while not terminate:
    print ("#####################################")

    user_input = input('> ')

    if user_input == "quit":
        terminate = True
    elif user_input == "stats":
        pypet_stats()
    elif user_input == "feed":
        if py_cat['hungry']:
          print ("Om Nom Nom")
          py_cat['weight'] = py_cat['weight'] + 1.5
          py_cat['hungry'] = False
        else:
            print("(=^x.x^=)__")
            print("TOO full... *BURP* ...")
    elif user_input == "chat":
        print (random.choice(py_cat['phrases']))
    elif user_input == "name":
        print ("What do you want to name your cat?")
        print ("(=^o.o^=)__")
        py_cat['name'] = input()
        print(py_cat['name'] + " learned its new name!")
    elif user_input == "help":
        print("You can use the [stats, feed, chat, name, quit, help, sleep] commands to do things with your pypet!")
    elif user_input == "sleep":
        print ("(=^+.+^=)__")
        print ("Zzzzz...")
        sleep(30)
        print ("(=^o.o^=)__")
        print ("Yawn!!")
        py_cat['hungry'] = True
    else:
        print ("Sorry, I don't understand")
    
        
print ("Goodbye!")