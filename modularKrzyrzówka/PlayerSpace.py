from modularKrzyrzówka import Player
from modularKrzyrzówka import Utility

class PlayerSpace:
    def __init__(self, loggeDplayers,playersFile):
        self.loggeDplayers=loggeDplayers
        self.playersFile=playersFile

    def register(self,nick, mail, password):
        try:
            if len(nick) == 0 or len(mail) == 0 or len(password) == 0:
                return -1
            with open(self.playersFile, 'r') as file:
                line = file.readline()
                while line:
                    uncoded = line.split("\t")
                    for i in range(len(uncoded)):
                        uncoded[i] = Utility.Utility.shift(uncoded[i], 5)
                    if uncoded[0] == nick:
                        return -2
                    line = file.readline()
            file = open(self.playersFile, 'a')
            file.write(Utility.Utility.shift(nick, -5) + "\t" + Utility.Utility.shift(mail, -5) + "\t" + Utility.Utility.shift(password, -5) + "\n")
            file.close()
            return 0
        except Exception:
             return -1

    def login(self,nick, password):
        try:
            with open(self.playersFile, 'r') as file:
                line = file.readline()
                while line:
                    line = line.strip()
                    if Utility.Utility.shift(line.split("\t")[0], 5) == nick and Utility.Utility.shift(line.split("\t")[2], 5) == password:
                        self.loggeDplayers.append(Player.Player(nick))
                        return True
                    line = file.readline()
            return False
        except Exception:
            print("invalid formating")
            return False