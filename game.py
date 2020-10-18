import random
class Game:
    def __init__(self, id):
        self.gameId = id
        self.board = [-4 for i in range(9)]
        self.ready = False
        self.playerToGo = random.choice((0,1))
        self.lostConnection = False

    def move(self, p, sq):

        if (p != self.playerToGo):
            return False
        if (self.board[sq] == -4):
            self.board[sq] = p
            if (self.playerToGo == 0):
                self.playerToGo = 1
            else:
                self.playerToGo = 0
            return True 
        else:
            return False 

    def checkWinner(self):
        if (self.board[0] + self.board[1] + self.board[2] == 3):
            return 1
        if (self.board[0] + self.board[1] + self.board[2] == 0):
            return 0
        if (self.board[3] + self.board[4] + self.board[5] == 3):
            return 1
        if (self.board[3] + self.board[4] + self.board[5] == 0):
            return 0
        if (self.board[6] + self.board[7] + self.board[8] == 3):
            return 1
        if (self.board[6] + self.board[7] + self.board[8] == 0):
            return 0
        if (self.board[0] + self.board[4] + self.board[8] == 3):
            return 1
        if (self.board[0] + self.board[4] + self.board[8] == 0):
            return 0
        if (self.board[2] + self.board[4] + self.board[6] == 3):
            return 1
        if (self.board[2] + self.board[4] + self.board[6] == 0):
            return 0
        if (self.board[0] + self.board[3] + self.board[6] == 3):
            return 1
        if (self.board[0] + self.board[3] + self.board[6] == 0):
            return 0
        if (self.board[1] + self.board[4] + self.board[7] == 3):
            return 1
        if (self.board[1] + self.board[4] + self.board[7] == 0):
            return 0
        if (self.board[2] + self.board[5] + self.board[8] == 3):
            return 1
        if (self.board[2] + self.board[5] + self.board[8] == 0):
            return 0
        if -4 in self.board:
            return -1
        else:
            return 3
    

    def reset(self):
        self.board = [-4 for i in range(9)]
        self.playerToGo = random.choice((0,1))   
        self.lostConnection = False    
    

