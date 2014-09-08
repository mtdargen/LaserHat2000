__author__ = 'M.T. Dargen PHD'
__PHD__ = "Punk Hardcore Drugdealer"

import pygame
from Sprites import Effects
from Sounds import SoundsFile

class HatSprite(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load("Images/laserhat_shielded.png")
        self.src_image.set_colorkey((255,255,255))
        self.rect = self.src_image.get_rect()
        self.position = position
        self.vx = self.vy = 0
        self.theta = 0
        self.health = 3
        self.shield = 3
        self.is_hit = False
        self.bomb = False
        self.hat_effectsgroup = []

    def update(self, deltat, enemygroup):
        x, y = self.position
        x += self.vx * deltat
        y += self.vy * deltat

        if x < -50: x = 650
        if x > 650: x = -50
        if y < -50: y = 650
        if y > 650: y = -50

        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.theta).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        collisions = pygame.sprite.spritecollide(self, enemygroup, False)
        if collisions != []:
            for enemy in collisions:
                self.hit(enemy.hits, False)
                if(enemy.__class__.__name__ != 'BillOReilly'):
                    enemy.kill()

    def hit(self, damage, crit):
        self.is_hit = True
        if crit:
            self.shield = 0
            self.health = 0
        if self.shield > 0:
            self.shield -= damage
            if self.shield <= 0:
                SoundsFile.shield_down.play()
                self.hat_effectsgroup.append(Effects.ShieldBanner(self.position, False))
                self.src_image = pygame.image.load("Images/laserhat.png")
                self.src_image.set_colorkey((255,255,255))
            else:
                SoundsFile.shield_hit.play()

            if self.shield < 0:
                self.health += self.shield
                self.shield = 0
                if(self.health <= 0):
                    SoundsFile.hatdeath.play()
                    self.kill()
                    self.is_hit = False
                else:
                    SoundsFile.health_hit.play()
        else:
            self.health -= damage
            if(self.health <= 0):
                SoundsFile.hatdeath.play()
                self.kill()
            else:
                SoundsFile.health_hit.play()
