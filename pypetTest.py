import os
from time import sleep
print("Hii")

sleep(4)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()