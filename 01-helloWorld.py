'''
Moataz Khallaf A.K.A Hackerman
Hello World
4/8/2019
'''

import pygame, random

# loads pygame module commands in the program
pygame.init()

# display variables

# window title
TITLE = 'Hello World'

# frames/sec
FPS = 30

WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# colour variables!!!
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 53, 127)

# create the window

screen = pygame.display.set_mode(SCREENDIM)  # creates the main surface where other assets are placed
pygame.display.set_caption(TITLE)  # updates the window title with TITLE
screen.fill(PINK)  # fills the surface with a colour (erase or clear)

# starts a clock object to measure time
clock = pygame.time.Clock()


# add text
class text:
    def __init__(self, text='hello world', pos=(0, 0)):
        self.text = text
        self.color = (255, 255, 255)
        self.size = 28
        self.x = pos[0]
        self.y = pos[1]
        self.xDir = 1
        self.yDir = 1
        self.pos = (self.x, self.y)
        self.fontFam = 'Arial'
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def setColor(self, color):
        self.color = color
        self.surface = self.font.render(self.text, 1, self.color)


    def setSize(self, size):
        self.size = size
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def setPos(self, pos):
        self.pos = pos
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def setFont(self, fontFam):
        self.fontFam = fontFam
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def setText(self, text):
        self.text = text
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def moveText(self, xSpd=0, ySpd=0):
        self.x += (self.xDir * xSpd)
        self.pos = (self.x, self.y)
        if self.x > WIDTH - self.surface.get_width():
            self.xDir = -1
        if self.x < 0:
            self.xDir = +1

        self.y += (self.yDir * ySpd)
        self.pos = (self.x, self.y)
        if self.y > HEIGHT - self.surface.get_height():
            self.yDir = -1
        if self.y < 0:
            self.yDir = +1

    def movePlayer(self, pressedKeys, spd=5,):
        if pressedKeys[pygame.K_w]:
            self.y -= spd
        if pressedKeys[pygame.K_s]:
            self.y += spd
        if pressedKeys[pygame.K_a]:
            self.x -= spd
        if pressedKeys[pygame.K_d]:
            self.x += spd

        if self.x > WIDTH - self.surface.get_width():
            self.x = WIDTH - self.surface.get_width()
        if self.x < 0:
            self.x = 0
        if self.y > HEIGHT - self.surface.get_height():
            self.y = HEIGHT - self.surface.get_height()
        if self.y < 0:
            self.y = 0

        self.pos = (self.x, self.y)



    def getText(self):
        return self.surface

    def getPos(self):
        return self.pos


# --CODE STARTS HERE-- #

myText = text('TOO BIG', (SCREENDIM[0] / 2, SCREENDIM[1] / 2))
myText.setPos((WIDTH/2 - myText.getText().get_width()/2, HEIGHT/2 - myText.getText().get_height()/2))
myText.setColor(YELLOW)
myText.setSize(42)

newText = text('world', (0, 0))
newText.setFont("BOOTLE")
newText.setText("boot")
newText.setPos((100, 100))

make1 = text("for he", (1150, 150))
make1.setColor(RED)

make2 = text("gotdamn", (75, 75))
make2.setColor(RED)

make3 = text("feet", (225, 50))
make3.setColor(RED)


running = True

while running:
    # quite important
    for event in pygame.event.get():  # returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # if [x] button is clicked
            running = False

    pressedKeys = pygame.key.get_pressed()

    RAINBOW = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

    make1.moveText(3)
    make2.moveText(12, 2)
    make3.moveText(0, 17)
    newText.movePlayer(pressedKeys, 10)

    screen.fill(GREY)
    newText.setColor(RAINBOW)

    screen.blit(myText.getText(), myText.getPos())
    screen.blit(newText.getText(), newText.getPos())
    screen.blit(make1.getText(), make1.getPos())
    screen.blit(make2.getText(), make2.getPos())
    screen.blit(make3.getText(), make3.getPos())

    clock.tick(FPS)  # pause the game until the FPS time is reached
    pygame.display.flip()  # update the surface with changes

pygame.quit()
