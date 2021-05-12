import socket
from _thread import *
import pickle
from game import Game


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.102"
port = 5558
adr = (server, port)

s.bind(adr)
s.listen()
print("Server is working!")

p = 0
gameId = 0
games = {}
playerId = 0
idCount = 0


def client(conn, p, gameId, players, ball):
    global idCount
    conn.send(pickle.dumps([players[p], ball]))

    while True:
        try:

            data = pickle.loads(conn.recv(2048*8))
            players[p]= data

            if players[0].ready and players[1].ready:
                ball.move(players[0], players[1])

            if players[0].looser == True or players[1].looser == True:
                break

            if not data:
                print("Disconnected")
                break
            else:
                if p == 0:
                    reply = [players[1], ball]
                else:
                    reply = [players[0], ball]

            conn.sendall(pickle.dumps(reply))
        except:
            break
    
    print("Lost connection")
    try:
        del games[gameId]
        print("Closing game", gameId)
    except:
        pass

    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        players = [games[gameId].Player(200,465, 0), games[gameId].Player(200,15, 1)]
        ball = games[gameId].Ball(170,140)
        print("Creating a new game...")
    else:
        p = 1

    start_new_thread(client, (conn, p, gameId, players, ball))
