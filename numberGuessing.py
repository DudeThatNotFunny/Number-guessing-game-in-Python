import os,random

clear = lambda: os.system('cls')
clear()

countTries = 0
x = random.randint(1,100)
print(f"Number will be from 1 to 100.\nGuess the number:")

def isItInt(x):
    try:
        int(x)
    except:
        clear()
        return False

while True:
    inputData = input()
    if(isItInt(inputData)==False):
        print(f"Intiger what you inputed wasn't a intiger.\nIntiger will be from 1 to 100.\nGuess the intiger:")
        continue
    inputData = int(inputData)
    if(inputData == x):
        clear()
        print(f"Yes, you guessed the number right!\nWith {countTries} tries\nIf you want to continue you can start guessing the number.")
        x = random.randint(1,100)
        countTries = 0
        continue
    elif(inputData > x):
        clear()
        countTries += 1
        print("Your guess is too high!\nGuess the number: ")
    elif(inputData < x):
        clear()
        countTries += 1
        print("Your guess is too low!\nGuess the number: ")