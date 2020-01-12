#game data file
#manages game state like units left in pool, turn counter etc

class GameData:
    def __init__(self):
        self.players = 0

        #current phase of the game -> buying, battling
        self.currentPhase = -1

        #is game in initialization, over, in game
        self.gameState = -1
