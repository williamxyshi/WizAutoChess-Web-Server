#source virt/Scripts/activate
#eb create flask-env

from playerdata import PlayerData
from gamedata import GameData
# from flask_pymongo import PyMongo
import constants
import db
from flask import Flask
from flask import jsonify, request, json

#connection string mongodb+srv://wazord:<password>@wizautochess-hodzs.mongodb.net/test?retryWrites=true&w=majority

# # EB looks for an 'application' callable by default.
application = Flask(__name__)
#
# mongo = pymongo.MongoClient('mongodb+srv://wazord:EaCxw2BHWU4FvC5w@myInstance-gktww.gcp.mongodb.net/admin', maxPoolSize=50, connect=False)
#
# db = pymongo.database.Database(mongo, 'mydatabase')
# col = pymongo.collection.Collection(db, 'mycollection')


# application.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)

#stores playerId's
playerIDs = []

#list of all player data objects
players = []

#stores game data
gamedata = GameData()


def restartGame():
    player = PlayerData()
    gamedata = GameData()


def setPlayer(playerID: int, username: str = "basename"):
    player = PlayerData()

    player.resetPlayer(playerID, username)
    players.append(player)
    gamedata.players = gamedata.players + 1
    return jsonify(result=player.username)

def updatePlayer(playerID: int, newUsername: str):
    for player in players:
        if player.id == playerID:
            player.username = newUsername
            return True
    return False


@application.route("/insertplayercount")
def test():
    db.db.collection.insert_one({"player": str(players)})
    return jsonify(result = "successfully inserted into database")


@application.route('/start', methods=['GET'])
def home():
    if(len(playerIDs) == 0):
        restartGame()
        
    id = len(playerIDs)
    playerIDs.append(id)

    return jsonify(id=str(id))


@application.route('/lobby/adduser', methods=['GET'])
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
        if updatePlayer(id, username) == False:
            return setPlayer(id, username)
        else:
            return jsonify(result=username)
    else:
        return jsonify(result=str(-1))


@application.route("/lobby/ready")
def readyPlayer():
    """Todo: implement readying method
    """


@application.route("/lobby/getplayers")
def getPlayers():
    playerList = []
    for player in players:
        playerList.append( { "username": player.username, "ready": player.ready})


    returnJson = {
        "playercount": len(players),
        "players" : playerList
    }
    return jsonify(
        result = returnJson
    )

@application.route("/game/gamestate")
def gameState():
    """
    main function where the client transmits their game state and server
    saves to mongodb

    :return:
    """


# run the app.
if __name__ == "__main__":
    
    #remove before production
    application.debug = True

    application.run()