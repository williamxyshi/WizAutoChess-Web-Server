#game data file
#manages game state like units left in pool, turn counter etc
import constants

#design document: https://docs.google.com/drawings/d/1K3MR1KInLj4RHeOvckLlO3PXg0-V1QQFiSV9cGJXp6k/edit?usp=sharing
#all units and synergies document: https://docs.google.com/document/d/1Z0yYKKRqPNVp3rsUC41YxwmvzPFuUmgIC3EHxx9IkzE/edit?usp=sharing

#list of all synergies in the game
synergies = [

]

#list of all units in the game
units = [

]



class GameData:
    def __init__(self):
        self.players = 0

        #current phase of the game -> buying, battling
        self.currentPhase = -1

        #is game in initialization, over, in game
        self.gameState = constants.GAME_STATE_UNINITIALIZED
