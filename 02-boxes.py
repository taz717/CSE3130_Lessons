'''
Moataz Khallaf A.K.A Hackerman
Boxes
4/8/2019
'''

import pygame, random
pygame.init  # Loads PyGame Module commands in the program

# Display Variables

TITLE = "BoxHead"  # Appears in window title
FPS = 30
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Colour variables

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 53, 127)

# classes
class box:
    def __init__(self, height, width, colour=WHITE, x=0, y=0, xSpd=0, ySpd=0):
        self.height = height
        self.width = width
        self.DIM = (self.width, self.height)
        self.x = x
        self.y = y
        self.POS = (x, y)
        self.colour = colour
        self.xSpd = xSpd
        self.ySpd = ySpd
        self.xDir = 1
        self.yDir = 1
        self.surface = pygame.Surface(self.DIM, pygame.SRCALPHA, 32)
        self.surface.fill(self.colour)

    def setColour(self, colour):
        self.colour = colour
        self.surface = pygame.Surface(self.DIM, pygame.SRCALPHA, 32)
        self.surface.fill(self.colour)

    def setPOS(self, x, y):
        self.x = x
        self.y = y
        self.POS = (x, y)
        self.surface = pygame.Surface(self.DIM, pygame.SRCALPHA, 32)
        self.surface.fill(self.colour)

    def setDIM(self, width, height):
        self.width = width
        self.height = height
        self.DIM = (self.width, self.height)
        self.surface = pygame.Surface(self.DIM, pygame.SRCALPHA, 32)
        self.surface.fill(self.colour)

    def getSurface(self):
        return self.surface

    def getDIM(self):
        return self.DIM

    def getPos(self):
        return self.POS

    def moveBox(self):
        self.x += (self.xDir * self.xSpd)
        self.POS = (self.x, self.y)
        if self.x > WIDTH - self.surface.get_width():
            self.xDir = -1
        if self.x < 0:
            self.xDir = +1

        self.y += (self.yDir * self.ySpd)
        self.POS = (self.x, self.y)
        if self.y > HEIGHT - self.surface.get_height():
            self.yDir = -1
        if self.y < 0:
            self.yDir = +1

    def movePlayer(self, pressedKeys):
        if pressedKeys[pygame.K_w]:
            self.y -= self.ySpd
        if pressedKeys[pygame.K_s]:
            self.y += self.ySpd
        if pressedKeys[pygame.K_a]:
            self.x -= self.xSpd
        if pressedKeys[pygame.K_d]:
            self.x += self.xSpd

        if self.x > WIDTH - self.surface.get_width():
            self.x = WIDTH - self.surface.get_width()
        if self.x < 0:
            self.x = 0
        if self.y > HEIGHT - self.surface.get_height():
            self.y = HEIGHT - self.surface.get_height()
        if self.y < 0:
            self.y = 0

        self.POS = (self.x, self.y)

# functions

def checkCol(box1, box2):
    if box1.x < box2.x or box1.x + box1.width > box2.x + box2.width and box1.y < box2.y or box1.y + box1.height > box2.y + box2.height:
        return True

# Create the window

screen = pygame.display.set_mode(SCREENDIM)  # creates the main surface where all assets are placed
pygame.display.set_caption(TITLE)  # updates the windows title
screen.fill(GREY)  # fills the entire surface with the colour ie. erase

clock = pygame.time.Clock()  # starts a clock object to measure time

# Code starts here
running = True

whiteBox = box(1, 100, YELLOW, 20, 20, 12, 12)
make1 = box(25, 30, PINK, 30, 30, 12, 12)
make2 = box(50, 20, PINK, 124, 300, 12, 12)
make3 = box(300, 40, PINK, 60, 360, 12, 12)
make4 = box(125, 25, PINK, 235, 30, 12, 12)

whiteBox.setDIM(10, 20)
make2.setPOS(20, 300)
make3.setDIM(400, 500)


while running:
    for event in pygame.event.get():  # returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # if red x was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()

    make1.moveBox()
    make2.moveBox()
    make3.moveBox()
    make4.moveBox()
    whiteBox.movePlayer(pressedKeys)

   # print(checkCol(whiteBox, make1))
   # print(checkCol(whiteBox, make2))
    print(checkCol(whiteBox, make3))
    #print(checkCol(whiteBox, make4))


    screen.fill(GREY)

    screen.blit(whiteBox.surface, whiteBox.POS)
    screen.blit(make1.surface, make1.getPos())
    screen.blit(make2.surface, make2.POS)
    screen.blit(make3.surface, make3.POS)
    screen.blit(make4.surface, make4.POS)


    clock.tick(FPS)  # will pause game until FPS time is reached
    pygame.display.flip()  # update screen with changes

pygame.quit()