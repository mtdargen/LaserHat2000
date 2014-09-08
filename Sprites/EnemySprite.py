__author__ = 'M.T. Dargen PHD'
__PHD__ = "Punk Hardcore Drugdealer"

import pygame
import random
import math
from Sprites import Effects, LaserSprite
from Sounds import SoundsFile

crab_images = [ "Images/spacecrab.png",
                "Images/spacecrab2.png",
                "Images/spacecrab3.png",
                "Images/headcrab.png"]

def gettheta(enemy):
        x, y = enemy.position
        tx, ty = enemy.target.position

        tx_relative = tx - x
        ty_relative = ty - y

        rads = math.atan2(-ty_relative, tx_relative)
        rads %= 2 * math.pi
        return math.degrees(rads) + 90

class SpaceCrab(pygame.sprite.Sprite):

    def __init__(self, position, target, hits):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(crab_images[hits-1])
        self.rect = self.src_image.get_rect()
        self.src_image.set_colorkey((255,255,255))
        self.position = position
        self.v = 30 * hits
        self.theta = 0
        self.target = target
        self.hits = hits

    def update(self, deltat):
        (x, y) = self.position
        (tx, ty) = self.target.position

        if(tx > x): x += self.v * deltat
        elif(tx < x): x -= self.v * deltat

        if(ty > y): y += self.v * deltat
        elif(ty < y): y -= self.v * deltat

        theta = gettheta(self)

        self.position = (x,y)
        self.src_image.set_colorkey((255,255,255))
        self.image = self.src_image.convert_alpha()
        self.image = pygame.transform.rotate(self.image, theta)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def hit(self, crit):
        self.hits -= 1
        if self.hits <= 0 or crit:
            SoundsFile.blammo.play()
            self.kill()
        else:
            SoundsFile.laser_hit.play()
            self.src_image = pygame.image.load(crab_images[self.hits-1])


class BilloProjectile(pygame.sprite.Sprite):

    def __init__(self, position, target, hits):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("Images/billo_ball.png")
        self.rect = self.src_image.get_rect()
        self.src_image.set_colorkey((255,255,255))
        self.position = position
        self.v = 500
        self.theta = 0
        self.target = target
        self.hits = hits

    def update(self, deltat):
        (x, y) = self.position
        (tx, ty) = self.target

        if(x == tx and y == ty): self.kill()

        if(tx > x): x += self.v * deltat
        elif(tx < x): x -= self.v * deltat

        y += self.v * random.uniform(-2, 2) * deltat

        self.position = (x,y)
        self.image = self.src_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def hit(self, crit):
        self.hits -= 1
        if self.hits <= 0 or crit:
            SoundsFile.blammo.play()
            self.kill()
        else:
            SoundsFile.laser_hit.play()

class BillOReilly(pygame.sprite.Sprite):

    def __init__(self, position, target, hits):
        SoundsFile.pinhead.play()
        pygame.sprite.Sprite.__init__(self)
        self.neut_img = pygame.image.load("Images/billo_neut.png")
        self.hit_img = pygame.image.load("Images/billo_hit.png")

        self.src_image = self.neut_img
        self.rect = self.src_image.get_rect()
        self.position = position
        self.state = 0
        self.hits = hits * 20
        self.is_hit = False
        self.billo_crabgroup = []
        self.billo_effectgroup = []
        self.billo_lasergroup = []
        self.dt_tot = 0
        self.dt_since_hit = 0
        self.target = target
        self.theta = 0

    def update(self, deltat):
        self.dt_tot += deltat
        self.dt_since_hit += deltat

        if(self.is_hit):
            self.src_image = self.hit_img
            self.is_hit = False
            self.dt_since_hit = 0
        else:
            if self.dt_since_hit > 0.1: self.src_image = self.neut_img

        (x,y) = self.position
        if self.state == 0:
            if(x < 50): x += 50 * deltat
            elif(x > 550): x -= 50 * deltat
            else: self.state = 1
        elif self.state == 1:
            if 0.02 > self.dt_tot%0.6 > 0:
                cx, cy = self.rect.center
                self.billo_crabgroup.append(BilloProjectile((cx, cy), self.target, 1))
            if 0.02 > self.dt_tot%5 > 0:
                SoundsFile.pinhead.play()

        self.position = (x,y)
        self.src_image.set_colorkey((255,255,255))
        self.image = self.src_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.position


    def hit(self, angle, crit):
        self.is_hit = True

        if(135 > angle > 45 or 315 > angle > 225):
            self.billo_lasergroup.append(LaserSprite.LaserSprite(self.position, 360 - angle, 100))
        else:
            self.hits -= 1
            if crit:
                self.hits -= 9

        if(self.hits <= 0):
            SoundsFile.thanks.play()
            self.state = 2
        else:
            SoundsFile.laser_hit.play()

class BilloBoss(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = (650,-220)
        self.state = 0
        self.src_image = pygame.image.load("Images/billo_boss.png")
        self.rect = self.src_image.get_rect()
        self.hits = 1000
        self.billo_bulletgroup = []
        self.billo_

