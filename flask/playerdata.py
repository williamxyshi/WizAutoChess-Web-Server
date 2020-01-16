
"""
player data model file
will store all player related data in this model, and easily exported
"""

class PlayerData:
	def __init__(self):
		self.username = "basename"
		self.initialized = False
		self.id = -1
		self.ready = False

		self.boardLayoutString = ""
		self.purchasableUnits = ""
		self.bench = ""

		self.health = -1

		self.lvl = -1
		self.xp = -1

		self.gold = -1


	def resetPlayer(self, playerID:int, username = "basename"):
		self.username = username
		self.id = playerID
		self.initialized = True
