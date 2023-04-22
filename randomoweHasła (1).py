#tryb podstawowy 4 zad 3
import random

LetterUpper = ['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LetterLower = ['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']

passwordList = []

def addRandom (password,mode):
    if (mode == 0):
        for x in range(len(LetterLower)):
            if x % 2 == 0 or x % 5 == 0:
                password += LetterLower[x]
    elif (mode == 1):
        for x in range(len(LetterUpper)):
            if x % 2 == 0 and x % 3 == 0:
                password += LetterUpper[x]
    elif (mode == 2):
        for x in range(len(Numbers)):
            if not x % 2 == 0:
                password += Numbers[x]
    return password

def generatepassowrd(difficulty,scramble):
    password = ""

    if difficulty == 'easy':
        randomchoice1 = random.randint(0,2)
        password = addRandom(password,randomchoice1)

    elif difficulty == 'medium':
        randomchoice1 = random.randint(0,2)
        randomchoice2 = random.randint(0,2)
        while randomchoice1 == randomchoice2:
            randomchoice2 = random.randint(0, 2)
        password = addRandom(password, randomchoice1)
        password = addRandom(password, randomchoice2)

    elif difficulty == 'hard':
        password = addRandom(password, 0)
        password = addRandom(password, 1)
        password = addRandom(password, 2)

    if scramble:
        password=''.join(random.sample(password,len(password)))

    passwordList.append(password)

#MAM NADZIEJE, ŻE TAKA MODUŁOWOŚĆ WYSTARCZY
if __name__ == '__main__':
    while True:
        password = generatepassowrd(input("jaka trudność: "),False)
        #password = generatepassowrd('easy',False)

        iterator = iter(passwordList)
        while True:
            try:
                element = next(iterator)
                print(element)
            except StopIteration:
                break



