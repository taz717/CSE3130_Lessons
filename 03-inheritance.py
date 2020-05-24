'''
Moataz Khallaf A.K.A Hackerman
inheritance example
4/16/2019
'''

from myClass import text, box, getSpriteColision, mySprite
import pygame

pygame.init()  # Loads PyGame Module commands in the program

# Display Variables

TITLE = "inheritance"  # Appears in window title
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

# Create the window

screen = pygame.display.set_mode(SCREENDIM)  # creates the main surface where all assets are placed
pygame.display.set_caption(TITLE)  # updates the windows title
screen.fill(GREY)  # fills the entire surface with the colour ie. erase

clock = pygame.time.Clock()  # starts a clock object to measure time

# Code starts here
running = True

myText = text("He hit her")
myText.setColour(PINK)
myBox = box(100, 200, 300, 300, 30, 30)
myBox.setColour(RED)
bunny = mySprite("media/bunny.png")


while running:
    for event in pygame.event.get():  # returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # if red x was clicked
            running = False

    pressedKeys = pygame.key.get_pressed()

    myText.moveBox()
    bunny.movePlayer(pressedKeys)
    myBox.moveBox()
    print(getSpriteColision(bunny, myBox))
    #print('box', myBox.getHeight())
    #print('bunny', bunny.getWidth())

    screen.fill(GREY)

    screen.blit(myText.getText(), myText.getPos())
    screen.blit(myBox.getSurface(), myBox.getPos())
    screen.blit(bunny.getSurface(), bunny.getPos())

    clock.tick(FPS)  # will pause game until FPS time is reached
    pygame.display.flip()  # update screen with changes

pygame.quit()
