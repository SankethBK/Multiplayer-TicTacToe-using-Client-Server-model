import pygame
import time 
from network import Network

width = 800
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac toe")
pygame.font.init()

class Button:
    def __init__(self, text, x, y, color, id):
        self.text = text
        self.x = x
        self.y = y
        self.id = id
        self.color = color
        self.width = 100
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.width, self.height),1)
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):

        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


images = [pygame.transform.scale(pygame.image.load("X.jpeg"),(98,98)),pygame.transform.scale(pygame.image.load("O.jpeg"),(98,98))]
buttons = [Button("",150,200,(186,232,212),0), Button("",250,200,(186,232,212),1),Button("",350,200,(186,232,212),2),Button("",150,300,(186,232,212),3), Button("",250,300,(186,232,212),4), Button("",350,300,(186,232,212),5),Button("",150,400,(186,232,212),6), Button("",250,400,(186,232,212),7), Button("",350,400,(186,232,212),8)]

def redrawWindow(win, game, player, flag = True):
    font = pygame.font.SysFont("comicsans",60)
    win.fill((109 , 57 , 125))

    if not game.ready:
        text = font.render("Waiting for other players to join ", True, (37, 176 , 184))
        win.blit(text, (100,50))
        pygame.display.update()
        return
    
    for btn in buttons:
        btn.draw(win)
    
    gameboard = game.board
    for i in range(9):
        if gameboard[i] != -4:
            x = buttons[i].x + 1
            y = buttons[i].y + 1
            win.blit(images[gameboard[i]], (x,y))
    if flag:
        if game.playerToGo == player:
            text = font.render("Your turn ", True, (37, 176 , 184))
        else:
            text = font.render("Opponents turn", True, (37, 176 , 184))
        win.blit(text, (100,50))
    pygame.display.update()
    
def main():
    run = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans",60)
    n = Network()

    player = int(n.getP())
    player = int(player)
  #  print("You are player ",player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
      #      print(F"game is {game.ready} player = {player} , playertogo = {game.playerToGo}")
        except:
      #      print("Couldn't fetch game")
             break
        if game.ready:
      #      print("game is ready")
    
            status = game.checkWinner()
            reset = False
            if (status == player):
                text = font.render("You Won!!!" , True , (37, 176 , 184))
                reset = True
            elif status == 3:
                text = font.render("Tie Game" , True , (37, 176 , 184))
                reset = True
            elif status != -1:
                text = font.render("You Lost" , True , (37, 176 , 184))
                reset = True
            if reset:
                redrawWindow(win, game, player, False)
                win.blit(text , (200,100))
                pygame.display.update()
                time.sleep(5)
                n.send("reset")
                continue 
      

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and game.ready:
                if game.playerToGo == player:
                    pos = pygame.mouse.get_pos()
                    for btn in buttons:
                        if btn.click(pos):
                        #    print(F"button with {btn.id} is clicked")
                            n.send(str(btn.id))
        redrawWindow(win, game, player)



def main_menu():

    run = True
    font = pygame.font.SysFont("comicsans",60)
    text = font.render("Click here to Start!!",True,(37, 176, 184))

    while run:
        win.fill((109, 57, 125))
        win.blit(text, (200,400))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    main()

main_menu()