__author__ = 'M.T. Dargen PHD'
__PHD__ = "Punk Hardcore Drugdealer"

import pygame
from Sounds import SoundsFile

splosion_images = [pygame.image.load("Images/explosion1.png"),
                   pygame.image.load("Images/explosion2.png"),
                   pygame.image.load("Images/explosion3.png"),
                   pygame.image.load("Images/explosion4.png"),
                   pygame.image.load("Images/explosion5.png")]

shield_images = [pygame.image.load("Images/shield_down.png"),
                 pygame.image.load("Images/shield_up.png")]

crit_images = [pygame.image.load("Images/crit1.png"),
               pygame.image.load("Images/crit2.png"),
               pygame.image.load("Images/crit3.png"),
               pygame.image.load("Images/crit4.png"),
               pygame.image.load("Images/crit5.png"),
               pygame.image.load("Images/crit6.png"),
               pygame.image.load("Images/crit7.png"),
               pygame.image.load("Images/crit8.png"),
               pygame.image.load("Images/crit9.png")]



class Splosion(pygame.sprite.Sprite):

    def __init__(self, position, theta):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.position = position
        self.theta = theta
        self.state = 0
        self.image = self.src_image = splosion_images[0]

    def update(self, deltat):
        self.state += 30 * deltat
        if(self.state >= 5):
            self.kill()
        else:
            self.src_image = splosion_images[int(self.state)]
            self.src_image.set_colorkey((255,255,255))
            self.image = pygame.transform.rotate(self.src_image, self.theta).convert_alpha()

class ShieldBanner(pygame.sprite.Sprite):
    def __init__(self, position, shieldup):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.position = position
        if shieldup:
            self.src_image = shield_images[1]
        else:
            self.src_image = shield_images[0]
        self.src_image.set_colorkey((255,255,255))
        self.image = self.src_image.convert_alpha()
        self.state = 0
        self.shieldup = shieldup

    def update(self, deltat):
        self.state += 30 * deltat
        if(self.state >= 20):
            self.kill()
        else:
            (x,y) = self.position
            if self.shieldup:
                y -= 0.5
            else:
                y += 0.5

            self.rect = self.position = (x,y)


class CritBanner(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.position = position
        self.state = 0
        SoundsFile.crit.play()

    def update(self, deltat):
        self.state += 10 * deltat
        if(self.state >= 9):
            self.kill()
        else:
            (x,y) = self.position
            y -= 0.5
            self.rect = self.position = (x,y)

            self.src_image = crit_images[int(self.state)]
            self.src_image.set_colorkey((255,255,255))
            self.image = self.src_image.convert_alpha()