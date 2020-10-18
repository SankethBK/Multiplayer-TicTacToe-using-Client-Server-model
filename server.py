import socket
from _thread import *
import pickle
import queue
from game import Game


server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection, Server started!!!!")

gameIdQueue = queue.Queue()
globalGameId = 1
games = {}
def threaded_client(conn, p, gameId):
    global globalGameId
    print("A player with id = ",p," is created")
    print(F"gameId of player is {gameId}")
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(4096).decode()

            if games[gameId].lostConnection:
                print("other player has left the game")
                games[gameId].reset()
                gameIdQueue.put((gameId, p))
                games[gameId].ready = False
            
            if gameId in games:
                game = games[gameId]
                if data == "":
                    print(F"player {p} has left the game")
                    games[gameId].lostConnection = True
                    conn.close()
                    print("Connection closed")
                    return 

                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.move(p, int(data))
                    
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break



            

while True:
    conn, addr = s.accept()
    print(F"Connected to {addr}")

    if (gameIdQueue.empty()):
        games[globalGameId] = Game(globalGameId)
        gameIdQueue.put((globalGameId, 0))
        print("A new game is created and pushhed to the queue")
        start_new_thread(threaded_client, (conn, 0, globalGameId))
        globalGameId += 1
    else:
        gameTuple = gameIdQueue.get()
        id = gameTuple[0]
        games[id].ready = True
        print("new thread started for ",conn)
        pId = int(not gameTuple[1])
        start_new_thread(threaded_client, (conn , pId, id))
        
        



