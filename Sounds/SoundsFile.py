__author__ = 'M.T. Dargen PHD'
__PHD__ = "Punk Hardcore Drugdealer"

__vocaltalents__ = "Katie Schmarr, M.D."
__MD__ = "Matt Dargensgirlfriend"

import pygame

pygame.mixer.init(22050,-16,2,1024)

#main gameloop sounds
crit = pygame.mixer.Sound("Sounds/crit.wav")
crit.set_volume(0.5)
recharge_sounds = [pygame.mixer.Sound("Sounds/recharge0.wav"),
                       pygame.mixer.Sound("Sounds/recharge1.wav"),
                       pygame.mixer.Sound("Sounds/recharge2.wav")]
pickup_get = pygame.mixer.Sound("Sounds/pickup_get.wav")
pickup_appear = pygame.mixer.Sound("Sounds/pickup_appear.wav")
critspree = pygame.mixer.Sound("Sounds/critspree.wav")

#hat sounds
shield_hit = pygame.mixer.Sound("Sounds/shield_hit.wav")
shield_down = pygame.mixer.Sound("Sounds/shield_down.wav")
health_hit = pygame.mixer.Sound("Sounds/health_hit.wav")
hatmove = pygame.mixer.Sound("Sounds/hatmove.wav")
hatdeath = pygame.mixer.Sound("Sounds/hatdeath.wav")
hatmove.set_volume(0.3)

#laser sounds
bomb = pygame.mixer.Sound("Sounds/bomb.wav")
pew = pygame.mixer.Sound("Sounds/laser.wav")
pew_crit = pygame.mixer.Sound("Sounds/laser_crit.wav")
pew.set_volume(0.6)
pew_crit.set_volume(0.4)

#enemy sounds
blammo = pygame.mixer.Sound("Sounds/blammo.wav")
laser_hit = pygame.mixer.Sound("Sounds/laser_hit.wav")
pinhead = pygame.mixer.Sound("Sounds/pinhead.wav")
thanks = pygame.mixer.Sound("Sounds/thanks.wav")
laser_hit.set_volume(0.5)