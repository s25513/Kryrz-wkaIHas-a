import random

from modularKrzyrzówka.Question import Question
from modularKrzyrzówka.Utility import Utility


class Game:
    def __init__(self, playerSpace,questions):
        self.playerSpace=playerSpace
        self.questions=questions
        self.cathegory="none"
        self.playersTurn=-1
        self.mainPassword = ""

    def preparePlayers(self):#previously firstStep
        while True:
            howManyPlayers = input("how many players should play: \n")
            count = 0
            try:
                if ((int)(howManyPlayers) < 1):
                    print("to little players")
                    return False
                while (count < (int)(howManyPlayers)):
                    try:
                        gettingIn = (str)(input("for login write 1 for register write 2: \n"))

                        if (gettingIn == "2"):
                            print("registerning...")
                            nick = input("provide your nick:")
                            mail = input("provide your mail:")
                            password = input("provider you password:")

                            resultOfRegistery = self.playerSpace.register(nick, mail, password)

                            if (resultOfRegistery == 0):
                                print("succesfully registered")
                                print("logining in...")
                                if (self.playerSpace.login(nick, password)):
                                    print("succedfully logged in")
                                    count += 1
                                else:
                                    print("cant log in")
                            elif (resultOfRegistery == -1):
                                print("invalid formating")
                            else:
                                print("account already exist")
                        elif gettingIn == "1":
                            print("logining in...")
                            nick = input("provide your nick:")
                            password = input("provide your password:")

                            if not self.playerSpace.loggeDplayers.__contains__(nick):
                                if (self.playerSpace.login(nick, password)):
                                    print("succedfully logged in")
                                    count += 1
                                else:
                                    print("wrong login or password")
                            else:
                                print("already logged in")
                        else:
                            print("invalid response")
                    except Exception as e:
                        #problem?
                        print("problems with formating")
                        print(e)
                return True
            except Exception:
                print("invalid argument")
                return False



    #setUp
    def setCathegory(self,questionfile,cathegoryId):

        self.questions.clear()
        count = 0

        with open(questionfile, 'r') as file:
            for line in file:
                if line.__contains__("<") and line.__contains__(">"):
                    count = count + 1
                    if count == cathegoryId:
                        self.cathegory = line.strip()
                elif count == cathegoryId and line.__contains__("-"):
                    self.questions.append(Question(line.split("-", 1)[0], line.split("-", 1)[1].strip()))

    def setRandomCathegory(self, questionfile):
        with open(questionfile, 'r') as file:
            maxRan = (int)(file.readline().strip())

        cathegoryId = random.randint(0, maxRan)
        self.setCathegory(questionfile,cathegoryId)

    def setTurn(self, turn):
        self.playersTurn = turn

    def setRandomTurn(self):
        playersTurn = random.randint(0, len(self.playerSpace.loggeDplayers) - 1)
        self.setTurn(playersTurn)


    def play(self):
        print("The cathegory is: " + self.cathegory)

        mainGuessed = False
        cipher = []
        self.mainPassword = ""

        for x in self.questions:
            cipher.append(len(x.answer) * "*")
            self.mainPassword += ((str)(x.answer))[0]

        while Utility.anyContain(cipher, "*"):
            count = 1
            for x in cipher:
                print((str)(count) + ": " + x)
                count += 1

            print("turn of a player: " + self.playerSpace.loggeDplayers[self.playersTurn].nick + ", current points: " + (str)(self.playerSpace.loggeDplayers[self.playersTurn].points))

            finished = False
            while not finished:
                try:
                    chosenQuestion = (int)(input("choose question number: ")) - 1
                    if chosenQuestion <= len(self.questions):
                        if cipher[chosenQuestion].__contains__("*"):
                            finished = True
                        else:
                            print("this one is already guessed")
                    else:
                        print("out of bounds")
                except Exception:
                    print("try again")

            print(cipher[chosenQuestion] + " - " + self.questions[chosenQuestion].question)
            guess = (input("guess: \n"))

            if (Utility.betterEqual(guess,self.questions[chosenQuestion].answer)):
                cipher[chosenQuestion] = self.questions[chosenQuestion].answer
                print("correct")
                self.playerSpace.loggeDplayers[self.playersTurn].addPoints(len(cipher[chosenQuestion]))
                print((str)(len(cipher[chosenQuestion])) + " points added")

                if not mainGuessed:
                    guess = (input("guess main password: \n"))
                    if Utility.betterEqual(guess,self.mainPassword):
                        print("CORRECT!!!")
                        toAdd = 0
                        for x in self.questions:
                            if ((str)(x.answer)).__contains__("*"):
                                toAdd += 2
                        for x in range(len(self.questions)):
                            cipher[x] = str(self.questions[x].answer)[0] + cipher[x][1:]
                        self.playerSpace.loggeDplayers[self.playersTurn].addPoints(len(cipher[chosenQuestion]))
                        print((str)(len(cipher[chosenQuestion])) + " points added")
                        mainGuessed = True
                    else:
                        print("no")
            else:
                print("wrong")
                self.playerSpace.loggeDplayers[self.playersTurn].addPoints(-len(cipher[chosenQuestion]))
                print((str)(len(cipher[chosenQuestion])) + " points substracted")

            self.playersTurn = (self.playersTurn + 1) % len(self.playerSpace.loggeDplayers)

        print("")
        print("WYNIKI")
        for x in self.playerSpace.loggeDplayers:
            print(x.nick + " " + ((str)(x.points)) + " punktow")

