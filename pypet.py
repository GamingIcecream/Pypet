import random
from time import sleep

py_cat = {
    'photo': '(=^●.●^=)__',
    'full': '(=^x.x^=)__',
    'sleep': '(=^+.+^=)__',
    'angry': '(=^>.<^=)__',
    'knowing': '(=^o.o^=)__',
    'zeroage': '[404 not found]',
    'name': 'Mochi',
    'age': 1,
    'weight': 5.7,
    'hungry': True,
    'phrases': ["Purrr", "*lick* *lick*", "Meow! Mew!", 'So you expected me to say "meow," huh?'],
    'petPhrase': ["Purrrrrr", "*Snuggle *Snuggle", "*lick meeew", "Mew! Mew!", "*mew meow", "Thank you."],
    'happy': 50
}
py_mouse = {
    'photo': '‹:3 )~~~~',
    'name': 'Speck',
    'age': 3,
    'weight': 0.98,
    'hungry': False,
    'phrases': ["SqueK!", "*nibble *nibble", "*Squeek SQUEEK", "Squeak."],
    'sleep': '‹|3 )~~~~',
    'happy': 100
}
py_duck = {
    'photo': '🦆',
    'name': 'Waddles',
    'age': 0.5,
    'weight': 12
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
    print("Use 'help' to show commands.")
    print(py_cat['photo'])


def pypet_stats():
    if py_cat['age'] <= 0:
        print(py_cat["zeroage"])
    elif py_cat['happy'] <= 0:
        print(py_cat['angry'])
    elif py_cat['happy'] <= 50:
        print(py_cat['photo'])
    elif py_cat['happy'] <= 99:
        print(py_cat['photo'])
    elif py_cat['happy'] >= 100:
        print(py_cat['sleep'])

    print(py_cat['name'] + " weighs " + str(py_cat['weight']) + " pounds ")
    print(py_cat['name'] + " is " + str(py_cat['age']) + " years old")
    print(py_cat['name'] + " has a happiness level of " + str(py_cat['happy']))

    if py_cat['hungry']:
        print("Your pypet is hungry!")
    else:
        print("Your pypet *BURPS* loudly")


startup_pypet()

speckUnlock = False
# pypet_stats()

terminate = False
sleepNum = 0
MsleepNum = 0
while not terminate:
    print("#####################################")

    user_input=input('> ').lower()

    if user_input == "quit":
        terminate = True
    elif user_input == "stats":
        pypet_stats()
    elif user_input == "feed":
        if py_cat['hungry']:
            print("Om Nom Nom")
            py_cat['weight'] = py_cat['weight'] + 1.5
            py_cat['hungry'] = False
            py_cat['happy'] = 100
        else:
            print(py_cat['full'])
            print("TOO full... *BURP* ...")
            py_cat['happy'] = py_cat['happy'] - 5
    elif user_input == "chat":
        print(random.choice(py_cat['phrases']))
    elif user_input == "name":
        print("What do you want to name your cat?")
        print(py_cat['photo'])
        py_cat['name'] = input('> ')
        print(py_cat['name'] + " learned its new name!")
    elif user_input == "help":
        print(
            "You can use the [stats, feed, chat, name, quit, help, sleep, play, view] commands to do things with your pypet!")
    elif user_input == "play":
        print(py_cat['photo'])
        print("Its time to play! Want to play [guess the number (gtm), quiz (q)]?")
        game = input('> ').lower()
        if game == "guess the number" or game == "gtm":
        # if game == "guess the number":
            tries = 1
            print("Lets play guess the number!")
            number = random.randrange(1, 10)
            print("I am thinking of a number 1-10. Guess what it is! You have 3 tries.")
            guessNum = input('> ').lower()
            if guessNum == number:
                print("You got it! Lets play again later.")
                py_cat['hungry'] = True
            while not guessNum == number:
                tries = tries + 1
                print("Nope, thats not it, try again.")
                guessNum = input('> ').lower()
                py_cat['happy'] = py_cat['happy'] - 10
                if guessNum == number:
                    print("You got it! Lets play again later.")
                    py_cat['hungry'] = True
                    py_cat['weight'] = py_cat['weight'] - 0.4
                if tries == 3:
                    print("Your tries are up! The correct answer was: " + str(number))
                    py_cat['hungry'] = True
                    guessNum = number
        elif game == "quiz" or game == "q":
        # if game == "quiz":
            print("All right! Lets get started. Choose your genre!")
            print("The genre options are: Adventure, Marvel, Star Wars, Harry Potter, (Not Case Sensitive)")
            genre = input('> ').lower()
            points = 0
            if genre == "adventure":
                print("Coming soon.")
                print("#Hopefully_something_cool.")
            elif genre == "marvel":
                print("Coming soon.")
                print("#Waiting_for_Shang-Shi_2!_Lol...")
            elif genre == "harry potter":
                print("Coming soon.")
                print("For experimental usage, type 'xp' below. If you want to go back, just hit [Enter]. ")
                if input('> ').lower() == "xp":
                    print("1st question! Who are Harry Potter's Friends?")
                    print("a.) Ron, Malfoy, Hermione")
                    print("b.) Ron, Hermione, Harry Potter")
                    print("c.) Ron, Hermione")
                    answerQ = input('> ').lower()
                    if answerQ == "c":
                        print("You got it!")
                        points += 1
                    elif answerQ == "b":
                        print("Being friends with yourself? How lonely... Btw that's wrong.")
                    elif not answerQ == "c":
                        print("Oops. That's wrong.")
                    print("2nd question! How does Harry get his Scar?")
                    print("a.) Because he just was born w/ it. ")
                    print("b.) Because Voldemort hit him")
                    print("c.) b/c He who must not be name cursed him")
                    answerQ = input('> ').lower()
                    if answerQ == "c":
                        print("Great! A point for you.")
                        points += 1
                    elif not answerQ == "c":
                        print("Oh well. Too bad. Wrong answer.")
                    print("3rd and final question. What house is Malfoy put in?")
                    print("a.) Ravenclaw")
                    print("b.) Hufflepuff")
                    print("c.) Slytherin")
                    answerQ = input('> ').lower()
                    if answerQ == "c":
                        print("Amazing! You got a point.")
                        points += 1
                    elif not answerQ == "c":
                        print("You gave it your best shot. Incorrect answer.")
                    print(f"You got {str(points)} points!")
                    if points == 3:
                        py_cat['happy'] += 30

            elif genre == "(not case sensitive)":
                print("Lol! That's not a genre, but you tried it. Just for that you get some more happiness. ")
                py_cat['happy'] += 5
            elif genre == "Star Wars":
                print(
                    "1st question! Who is the main character in the original star wars trilogy? (Choose a letter, ex: a, b, or c)")
                print("a.) Luke Skywalker")
                print("b.) Han Solo")
                print("c.) Rey (Palpatine?)")
                answerQ = input("Answer: ").lower()
                if answerQ == "a":
                    print("You got it!")
                    points = points + 1
                elif not answerQ == "a":
                    print("That's the wrong answer.")
                print("2nd question! What does the Mandalorian decide to do right after finding the Child.")
                print("a.) Shoot it")
                print("b.) Turn it in")
                print("c.) Take it away and go into hiding. ")
                answerQ = input("Answer: ").lower()
                if answerQ == "b":
                    print("Correct! A point for you.")
                    points = points + 1
                elif not answerQ == "b":
                    print("Oops, that's not right. Moving on.")
                print("3rd question! What color does Kilo Ren's saber become at the end of the last movie?")
                print("a.) Red")
                print("b.) Yellow")
                print("c.) Green")
                answerQ = input("Answer: ").lower()
                if answerQ == "b":
                    print("Nice job! Points points points.")
                    points = points + 1
                elif not answerQ == "b":
                    print("Oof. That's incorrect.")
                print("You got " + str(points) + " points!")
                py_cat['hungry'] = True
                if points == 3:
                    py_cat['happy'] = py_cat['happy'] + 30
            else:
                print("That isn't a genre.")
    elif user_input == "view":
        print(
            """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░
░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████▓▓▓▓██░░░░
░░░░██▒▒▒▒▒▒████████████░░░░░░░░░░████████████████▓▓▓▓██░░░░
░░░░██▒▒▒▒▒▒████▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓████████▓▓██░░░░
░░██▒▒▓▓▒▒▒▒████▓▓████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓████▓▓██░░░░
░░██▒▒▒▒▓▓██████▓▓████████▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓██████░░░░
██▓▓▒▒▒▒▒▒██░░████░░░░██████▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▓▓████░░░░
██▒▒▓▓▓▓██░░░░████░░░░░░██████▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒████░░░░
██▓▓▒▒▒▒██░░░░████░░░░░░░░████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████░░░░
██▒▒▓▓▓▓██░░░░░░████░░░░░░████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████░░░░
██▓▓▒▒▒▒██░░░░░░██████░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒██░░░░
██▓▓▓▓▓▓██░░░░░░░░████████▒▒▒▒▒▒▓▓████▒▒▒▒▒▒▒▒▒▒░░██░░██░░░░
██▓▓▒▒▒▒▒▒██░░░░░░████▓▓▓▓▒▒▒▒▓▓████████▒▒░░░░▒▒████░░██████
██▒▒▒▒▓▓▓▓▓▓████████▓▓▓▓▒▒▒▒▒▒██▒▒██████▒▒░░░░░░▓▓▓▓░░░░▓▓░░
░░██▓▓▓▓▓▓████▒▒▓▓██▒▒▒▒▒▒▒▒░░▒▒░░░░████▒▒░░░░░░░░░░▓▓██████
░░██▓▓▓▓██▓▓▓▓▓▓▒▒██▓▓▓▓▓▓▒▒░░░░░░██████░░░░▒▒▒▒░░░░░░▓▓░░░░
░░░░████▓▓▓▓▓▓▒▒▒▒██▓▓▒▒▒▒████▒▒░░▓▓▓▓░░░░░░████░░░░░░▓▓░░░░
░░░░██▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░
░░██▓▓▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓████▓▓░░░░░░░░░░░░░░░░▓▓░░░░░░░░
░░██▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░
░░██▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░░░░░░░░░░░░░
░░██▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒▒▒░░▒▒▓▓▓▓▒▒██░░░░░░░░░░░░
██▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░░░▓▓▒▒▒▒▒▒▓▓██░░░░░░░░░░
██▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓██░░▒▒██░░░░░░░░▓▓██░░░░░░░░
██▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒████████░░░░░░░░░░██░░░░░░░░
██░░▒▒▒▒▒▒▒▒░░░░▒▒██████░░▒▒░░▒▒░░██░░░░██░░░░▒▒░░██░░░░░░░░
██░░░░░░░░▒▒██████░░░░░░██░░░░░░░░▒▒██░░██▒▒▒▒░░░░██░░░░░░░░
██░░░░░░░░████████░░░░░░██▒▒░░░░░░░░██░░░░████████░░░░░░░░░░
██░░░░░░██░░░░░░░░░░░░░░░░██░░▒▒▒▒░░██░░░░░░░░░░░░░░░░░░░░░░
░░██████░░░░░░░░░░░░░░░░░░██▒▒▒▒░░██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    elif user_input == "view duck":
        print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░████░░██████████░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░████░░██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░██░░░░░░░░░░░░░░██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░██░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░██░░░░░░██░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░████████████░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        
        
        """)

    elif user_input == "sleep":
        print(py_cat['sleep'])
        print("Zzzzz...")
        sleep(1)
        print(py_cat['photo'])
        print("Yawn!!")
        py_cat['hungry'] = True
        sleepNum += 1
        print(sleepNum)
        py_cat['happy'] = py_cat['happy'] - 10
        if sleepNum == 10:
            py_cat['age'] = py_cat['age'] + 1
            sleepNum = 0
            print(py_cat['name'] + " grew up!")
    elif user_input == 'duck':
        print(py_duck['photo'])
        print("Your duck is " + str(py_duck['age']) + " years old.")
        print("Your duck's name is " + py_duck['name'])
    elif user_input == "pet":
        print(py_cat['photo'])
        print(random.choice(py_cat['petPhrase']))
    elif user_input == "sudo unfeed":
        print("You fed your cat poison. It's now barfing. ")
        print(py_cat['full'])
        print("*BARF *Cry *Barf MEOOOOOOOOW ooooowwwww")
        py_cat['happy'] = py_cat['happy'] - 100
        py_cat['hungry'] = True
    elif user_input == "sudo mouse":
        if speckUnlock == False:
            print("You unlocked " + py_mouse['name'] + " !")
            speckUnlock == True
        print(py_mouse['photo'])
        print(py_mouse['name'])
        print(py_mouse['age'])
        print(py_mouse['weight'])
    elif user_input == "meow":
        print(py_cat["knowing"])
        print("Hello, human being. Good to know that you can speak to me. MEOW.")
    elif user_input == "sudo mouse sleep":
        print(py_mouse['sleep'])
        print("Zzzzz...")
        sleep(3)
        print(py_mouse['photo'])
        print("Yawn!!")
        py_mouse['hungry'] = True
        MsleepNum += 1
        # print(sleepNum)
        py_mouse['happy'] = py_mouse['happy'] - 10
        if MsleepNum == 10:
            py_mouse['age'] = py_mouse['age'] + 1
            MsleepNum = 0
            print(f"{py_mouse['name']} grew up!")
    elif user_input == "sudo debug(happy)":
        print("//Welcome to the debug console. You are debugging happiness. Set the value of happiness below.")
        py_cat["happy"] = int(input('>>> '))
    elif user_input == "sudo debug(age)":
        print("//Welcome to the debug console. You are debugging age. Set the value of age below.")
        py_cat['age'] = int(input('>>> '))
    elif user_input == "sudo debug(weight)":
        print("//Welcome to the debug console. You are debugging weight. Set the value of weight below.")
        py_cat['weight'] = int(input('>>> '))
    elif user_input == "sudo debug()":
        print("//Welcome to the debug console. Choose a debugging option. [happy, age, weight]")
        debugOpt = input('>>> ')
        if debugOpt == "happy":
            print("//Welcome to the debug console. You are debugging happiness. Set the value of happiness below.")
            py_cat["happy"] = int(input('>>> '))
        elif debugOpt == "age":
            print("//Welcome to the debug console. You are debugging age. Set the value of age below.")
            py_cat['age'] = int(input('>>> '))
        elif debugOpt == "weight":
            print("//Welcome to the debug console. You are debugging weight. Set the value of weight below.")
            py_cat['weight'] = int(input('>>> '))
    elif py_cat['happy'] <= 0:
        print(py_cat['name'] + " is mad.")
        print("FEED ME! MEOW MEOW MEOW. FOOOOOD FOOOOOD FOOOOD, *cry, Foood........")
    elif user_input == "helpme":
        print(py_cat['name'] + " cannot help you. But the \"help\" command can!")
    elif user_input == "asdfghjklqwertyuiopzxcvbnm":
        print("You are bored.")
    else:
        print("Sorry, I don't understand \"" + user_input + "\", type \"help\" for help.")

print("Goodbye!")
