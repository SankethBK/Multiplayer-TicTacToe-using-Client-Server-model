# Multiplayer-TicTacToe-using-Client-Server-model

## This is a simple TicTacToe game with multiplayer support - means two players can play from two different computers. 
## Languages and libraries : Python, socket, pygame.
- game.py : Consists a class Game which defines rules and methods to play game. 
- client.py : Creates client side UI to interact with game and constantly checks for winner or tie.
- network.py : Creates a socket for client and establishes the connection with server. It is also responsible for sending and recieving game states from server
- server.py : Creates an socket at given IP address and listens to connections, it pulls 2 clients from the waiting queue and starts a game between them. After the game is finished. it restarts the game with same 2 users.


### In order to run the game locally 
1. Install pygame.
```
$ pip install pygame
```
2. Change the IP address in network.py to 127.0.0.1.
3. Run server script. 
```
$ python3 server.py 
```
4. Run client script from two different terminals to play with each other 
```
$ python3 client.py
```

### Screenshots
