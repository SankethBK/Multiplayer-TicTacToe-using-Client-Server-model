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
![tic-tac-toe-1](https://user-images.githubusercontent.com/51091231/129674799-b43c5191-c776-439a-af40-35d3bca825bf.png)
![tic-tac-toe-2](https://user-images.githubusercontent.com/51091231/129674804-cf72c8ce-4814-4d9a-8577-672079ddb0c3.png)
![tic-tac-toe-3](https://user-images.githubusercontent.com/51091231/129674820-dc37928e-8fef-4fc1-a2ff-02a238feb736.png)
