from modularKrzyrzówka.Game import Game
from modularKrzyrzówka.PlayerSpace import PlayerSpace

if __name__ == '__main__':
    questions = []
    loggedPlayers =[]

    playerSpace = PlayerSpace(loggedPlayers,"Gracze.txt")

    game = Game(playerSpace,questions)
    game.setRandomCathegory("Pytania.txt")
    playersPrepared=game.preparePlayers()
    while not playersPrepared:
        playersPrepared = game.preparePlayers()
    game.setRandomTurn()
    game.play()

    #MAKE WORDS TOLOVER CASE AND REPLACE SPACES WITH _
