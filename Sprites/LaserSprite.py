__author__ = 'M.T. Dargen PHD'
__PHD__ = "Punk Hardcore Drugdealer"

import pygame, math, random
from Sounds import SoundsFile

pygame.mixer.init(22050,-16,2,1024)


class LaserSprite(pygame.sprite.Sprite):
    def __init__(self, position, theta, critrate=10):
        pygame.sprite.Sprite.__init__(self)
        self.theta = theta
        self.src_image = pygame.image.load("Images/laserblast.png")
        self.rect = self.src_image.get_rect()
        self.src_image.set_colorkey((255,255,255))
        self.position = position
        self.hit_list = []
        self.crit = (int(random.uniform(1,critrate)) == 1)
        if self.crit: SoundsFile.pew_crit.play()
        SoundsFile.pew.play()

        SPEED = 2000

        self.vx = SPEED * math.cos(math.radians(theta))
        self.vy = -SPEED * math.sin(math.radians(theta))

    def update(self, deltat, enemygroup):

        x, y = self.position
        x += self.vx * deltat
        y += self.vy * deltat

        if x < -100: self.kill()
        if x > 650:  self.kill()
        if y < -100: self.kill()
        if y > 650:  self.kill()

        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.theta).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.hit_list = pygame.sprite.spritecollide(self, enemygroup, False)
        for e in self.hit_list:
            if e.__class__.__name__ == "BillOReilly":
                e.hit(self.theta, self.crit)
            elif e.__class__.__name__ == "HatSprite":
                e.hit(1, self.crit)
            else:
                e.hit(self.crit)

class BombFire(LaserSprite):
    def __init__(self, position, theta):
        LaserSprite.__init__(self, position, theta)
        SPEED = 500

        self.vx = SPEED * math.cos(math.radians(theta))
        self.vy = -SPEED * math.sin(math.radians(theta))

    def update(self, deltat, enemygroup):
        LaserSprite.update(self, deltat, enemygroup)

