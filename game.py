#Jeff Haak
#Risk Game
from copy import deepcopy as dc
import board

class Game:

    __slots__ = ["board", "players", "playerArmies"]
    
    def __init__(self, players):
        gameMap = board.Board()
        gameMap.importMap("topBot.csv")
        self.board = gameMap
        self.players = players
        self.playerArmies = {}

        armyCount = -1
        if players == 1:
            return -1 
        elif players == 2:
            armyCount = 40
        elif players == 3:
            armyCount = 35
        elif players == 4:
            armyCount = 30
        elif players == 5:
            armyCount = 25
        elif players == 6:
            armyCount = 20
            
        
        for i in range(0, players):
            self.playerArmies[i] = armyCount

    def __str__(self):
        str1 = ""
        str1 += str(self.board)
        str1 += "\n"
        str1 += str(self.playerArmies)
        return str1 
    
if __name__ == "__main__":
    game = Game(2)
    #print game.board
    print game





