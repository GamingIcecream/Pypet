import random
from time import sleep
py_cat = {
    'photo': '(=^●.●^=)__',
    'full': '(=^x.x^=)__',
    'sleep': '(=^+.+^=)__',
    'name': 'Mochi',
    'age': 1,
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
    print (py_cat['name'] + " is " + str(py_cat['age']) + " years old")

    if py_cat['hungry']:
        print ("Your pypet is hungry!")
    else:
      print ("Your pypet *BURPS* loudly")
    
startup_pypet()
# pypet_stats()

terminate = False
sleepNum = 0
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
            print(py_cat['full'])
            print("TOO full... *BURP* ...")
    elif user_input == "chat":
        print (random.choice(py_cat['phrases']))
    elif user_input == "name":
        print ("What do you want to name your cat?")
        print (py_cat['photo'])
        py_cat['name'] = input()
        print(py_cat['name'] + " learned its new name!")
    elif user_input == "help":
        print("You can use the [stats, feed, chat, name, quit, help, sleep, play, view] commands to do things with your pypet!")
    elif user_input == "play":
        print(py_cat['photo'])
        print("Its time to play! Want to play [guess the number, other]?")
        game = input('> ')
        if game == "guess the number":
            tries = 1
            print("Lets play guess the number!")
            number = ['1','2','3','4','5','6','7','8','9','10']
            print("I am thinking of a number 1-10. Guess what it is! You have 3 tries.")
            trueNum = random.choice(number)
            guessNum = input()
            if guessNum == trueNum:
                print("You got it! Lets play again later.")
                py_cat['hungry'] = True
            while not guessNum == trueNum:
                tries = tries + 1
                print("Nope, thats not it, try again.")
                guessNum = input()
                if guessNum == trueNum:
                    print("You got it! Lets play again later.")
                    py_cat['hungry'] = True
                    py_cat['weight'] = py_cat['weight'] - 0.4
                if tries == 3:
                    print("Your tries are up! The correct answer was: " + trueNum)
                    guessNum = trueNum
        elif game == "other":
            print("Coming soon. Lets play later")
    elif user_input == "view":
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓▓▓██░░░░░░")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████▓▓██░░░░░░")
        print("░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████▓▓▓▓██░░░░")
        print("░░░░██▒▒▒▒▒▒████████████░░░░░░░░░░████████████████▓▓▓▓██░░░░")
        print("░░░░██▒▒▒▒▒▒████▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓████████▓▓██░░░░")
        print("░░██▒▒▓▓▒▒▒▒████▓▓████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓████▓▓██░░░░")
        print("░░██▒▒▒▒▓▓██████▓▓████████▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓██████░░░░")
        print("██▓▓▒▒▒▒▒▒██░░████░░░░██████▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▓▓████░░░░")
        print("██▒▒▓▓▓▓██░░░░████░░░░░░██████▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒████░░░░")
        print("██▓▓▒▒▒▒██░░░░████░░░░░░░░████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████░░░░")
        print("██▒▒▓▓▓▓██░░░░░░████░░░░░░████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████░░░░")
        print("██▓▓▒▒▒▒██░░░░░░██████░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒██░░░░")
        print("██▓▓▓▓▓▓██░░░░░░░░████████▒▒▒▒▒▒▓▓████▒▒▒▒▒▒▒▒▒▒░░██░░██░░░░")
        print("██▓▓▒▒▒▒▒▒██░░░░░░████▓▓▓▓▒▒▒▒▓▓████████▒▒░░░░▒▒████░░██████")
        print("██▒▒▒▒▓▓▓▓▓▓████████▓▓▓▓▒▒▒▒▒▒██▒▒██████▒▒░░░░░░▓▓▓▓░░░░▓▓░░")
        print("░░██▓▓▓▓▓▓████▒▒▓▓██▒▒▒▒▒▒▒▒░░▒▒░░░░████▒▒░░░░░░░░░░▓▓██████")
        print("░░██▓▓▓▓██▓▓▓▓▓▓▒▒██▓▓▓▓▓▓▒▒░░░░░░██████░░░░▒▒▒▒░░░░░░▓▓░░░░")
        print("░░░░████▓▓▓▓▓▓▒▒▒▒██▓▓▒▒▒▒████▒▒░░▓▓▓▓░░░░░░████░░░░░░▓▓░░░░")
        print("░░░░██▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░")
        print("░░██▓▓▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓████▓▓░░░░░░░░░░░░░░░░▓▓░░░░░░░░")
        print("░░██▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░")
        print("░░██▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░░░░░░░░░░░░░")
        print("░░██▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒▒▒░░▒▒▓▓▓▓▒▒██░░░░░░░░░░░░")
        print("██▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░░░▓▓▒▒▒▒▒▒▓▓██░░░░░░░░░░")
        print("██▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓██░░▒▒██░░░░░░░░▓▓██░░░░░░░░")
        print("██▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒████████░░░░░░░░░░██░░░░░░░░")
        print("██░░▒▒▒▒▒▒▒▒░░░░▒▒██████░░▒▒░░▒▒░░██░░░░██░░░░▒▒░░██░░░░░░░░")
        print("██░░░░░░░░▒▒██████░░░░░░██░░░░░░░░▒▒██░░██▒▒▒▒░░░░██░░░░░░░░")
        print("██░░░░░░░░████████░░░░░░██▒▒░░░░░░░░██░░░░████████░░░░░░░░░░")
        print("██░░░░░░██░░░░░░░░░░░░░░░░██░░▒▒▒▒░░██░░░░░░░░░░░░░░░░░░░░░░")
        print("░░██████░░░░░░░░░░░░░░░░░░██▒▒▒▒░░██░░░░░░░░░░░░░░░░░░░░░░░░")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░")

    elif user_input == "sleep":
        print (py_cat['sleep'])
        print ("Zzzzz...")
        sleep(15)
        print (py_cat['photo'])
        print ("Yawn!!")
        py_cat['hungry'] = True
        sleepNum = sleepNum + 1
        if sleepNum == 10:
            py_cat['age'] = py_cat['age'] + 1
            sleepNum = 0
            print(py_cat['name'] + " grew up!")
    else:
        print ("Sorry, I don't understand")
    
        
print ("Goodbye!")