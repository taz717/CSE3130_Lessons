'''
Moataz Khallaf A.K.A Hackerman
mySpriteClasses
4/15/2019
'''

import pygame

#           <<Classes>>
#       <<MommaClass>>


class myClass:

    # <<attributes>>

    def __init__(self, x=0, y=0,  width=0, height=0, xSpd=10, ySpd=10,):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA, 32)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.colour = (self.red, self.green, self.blue)
        self.xSpd = xSpd
        self.ySpd = ySpd
        self.xDir = 1
        self.yDir = 1

    # <<Getter>>

    def getSurface(self):
        return self.surface

    def getPos(self):
        return self.pos

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.surface.get_width()

    def getHeight(self):
        return self.surface.get_height()

    # <<Setter>>

    def setColour(self, colour=(0, 0, 0)):
        self.red = colour[0]
        self.green = colour[1]
        self.blue = colour[2]
        self.colour = (self.red, self.green, self.blue)

    # <<Mechanics>>

    def moveBox(self, WIDTH=800, HEIGHT=600):
        self.x += (self.xDir * self.xSpd)
        # self.pos = (self.x, self.y)
        if self.x > WIDTH - self.surface.get_width():
            self.xDir = -1
        if self.x < 0:
            self.xDir = +1

        self.y += (self.yDir * self.ySpd)
        # self.pos = (self.x, self.y)
        if self.y > HEIGHT - self.surface.get_height():
            self.yDir = -1
        if self.y < 0:
            self.yDir = +1

        self.pos = (self.x, self.y)

    def movePlayer(self, pressedKeys, WIDTH=800, HEIGHT=600):
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

        self.pos = (self.x, self.y)

    def moveStar(self, WIDTH=800):
        self.x += (self.xDir * self.xSpd)
        # self.pos = (self.x, self.y)
        if self.x > WIDTH - self.surface.get_width():
            self.x = 0
        self.pos = (self.x, self.y)

    def movePlayerStar(self, pressedKeys, WIDTH=800, HEIGHT=600):
        if pressedKeys[pygame.K_w]:
            self.y -= self.ySpd
        if pressedKeys[pygame.K_s]:
            self.y += self.ySpd
        if pressedKeys[pygame.K_a]:
            self.x -= self.xSpd
        if pressedKeys[pygame.K_d]:
            self.x += self.xSpd

        if self.y > HEIGHT - self.surface.get_height():
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT - self.surface.get_height()
        if self.x > WIDTH - self.surface.get_width():
            self.x = 0
        if self.x < 0:
            self.x = WIDTH - self.surface.get_width()
        self.pos = (self.x, self.y)
#       <<BabyClasses>>

class text(myClass):

    # <<attributes>>

    def __init__(self, content, font="BOOTLE", fontSize=24):
        myClass.__init__(self)
        self.fontFam = font
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(self.fontFam, self.fontSize)
        self.content = content
        self.surface = self.font.render(self.content, 1, self.colour)
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

    # <<Getter>>

    def getText(self):
        return myClass.getSurface(self)


    # <<Setter>>

    def setColour(self, colour=(0, 0, 0)):
        myClass.setColour(self, colour)
        self.surface = self.font.render(self.content, 1, self.colour)

    # <<Mechanics>>

class box(myClass):

    # <<attributes>>

    def __init__(self,  x, y, width, height, xSpd, ySpd):
        myClass.__init__(self, x, y, width, height, xSpd, ySpd)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.colour)
        self.dim = (self.surface.get_width(), self.surface.get_height())

    # <<Getter>>

    def getBox(self):
        return myClass.getSurface(self)

    # <<Setter>>

    def setColour(self, colour=(0, 0, 0)):
        myClass.setColour(self, colour)
        self.surface.fill(self.colour)

    # <<Mechanics>>


class mySprite(myClass):

    # <<attributes>>

    def __init__(self, fileName):
        myClass.__init__(self)
        self.surface = pygame.image.load(fileName).convert_alpha()
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

#           << Functions>>
#       <<Mechanics>>


def getSpriteColision(sprite1, sprite2):
    if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <= sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() \
    and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
        return True
    else:
        return False
