__author__ = 'M.T. Dargen PHD'
__PHD__ = "Punk Hardcore Drugdealer"

import pygame, random

class CritPickup(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("Images/pickup_crit.png")
        self.src_image.set_colorkey((255,255,255))
        self.image = self.src_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.position = position
        tx = int(random.uniform(0,650))
        ty = int(random.uniform(0,650))
        self.target = (tx, ty)

    def update(self, deltat):
        (tx, ty) = self.target
        (x, y) = self.position

        if x < tx: x += 20 * deltat
        elif x > tx: x -= 20 * deltat

        if y < ty: y += 20 * deltat
        elif y > ty: y -= 20 * deltat

        self.rect.center = self.position = (x,y)

        if int(x) == tx and int(y) == ty:
            tx = int(random.uniform(0,650))
            ty = int(random.uniform(0,650))
            self.target = (tx, ty)

class BombPickup(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("Images/pickup_bomb.png")
        self.src_image.set_colorkey((255,255,255))
        self.image = self.src_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.position = position
        tx = int(random.uniform(0,650))
        ty = int(random.uniform(0,650))
        self.target = (tx, ty)

    def update(self, deltat):
        (tx, ty) = self.target
        (x, y) = self.position

        if x < tx: x += 20 * deltat
        elif x > tx: x -= 20 * deltat

        if y < ty: y += 20 * deltat
        elif y > ty: y -= 20 * deltat

        self.rect.center = self.position = (x,y)

        if int(x) == tx and int(y) == ty:
            tx = int(random.uniform(0,650))
            ty = int(random.uniform(0,650))
            self.target = (tx, ty)