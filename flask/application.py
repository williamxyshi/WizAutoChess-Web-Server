#source virt/Scripts/activate
#eb create flask-env

from playerdata import PlayerData
from gamedata import GameData
from flask import Flask
from flask import jsonify, request

# EB looks for an 'application' callable by default.
application = Flask(__name__)

#stores playerId's
playerIDs = []

#list of all player data objects
players = []

gamedata = GameData()


def restartGame():
    player = PlayerData()
    gamedata = GameData()


def setPlayer(playerID: int, username: str = "basename"):
    player = PlayerData()

    player.resetPlayer(playerID, username)
    players.append(player)
    return jsonify(player.username)




@application.route('/', methods=['GET'])
def home():
    if(len(playerIDs) == 0):
        restartGame()
        
    id = len(playerIDs)
    playerIDs.append(id)

    return jsonify(str(id))


@application.route('/adduser', methods=['GET'])
def addUser():
    if 'username' in request.args:
        username = request.args['username']
    else:
        return "Error: No username field provided. Please specify an username."

    if 'id' in request.args:
        id = int(request.args['id'])

    print(username)
    print(id)

    if id in playerIDs:
        return setPlayer(id, username)
    else:
        return jsonify(str(-1))





# run the app.
if __name__ == "__main__":
    
    #remove before production
    application.debug = True

    application.run()