__author__ = 'M.T. Dargen PHD'
__PHD__ = "Punk Hardcore Drugdealer"

import os
import pygame
import random
from Sprites import HatSprite, LaserSprite, EnemySprite, Effects, Pickups
from Sounds import SoundsFile

shield_huds = ["Images/shieldempty.png",
               "Images/shield1.png",
               "Images/shield2.png",
               "Images/shieldfull.png"]

health_huds = ["Images/healthempty.png",
               "Images/health1.png",
               "Images/health2.png",
               "Images/healthfull.png"]

def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (10,30)
    gamestate = 0

    pygame.init()
    pygame.display.set_caption("LASERHAT 2000 PRO EDITION")

    clock = pygame.time.Clock()

    bg = pygame.image.load("Images/start1.png")
    bgrect = bg.get_rect()
    WINDOW_SIZE = (WIDTH, HEIGHT) = bg.get_size()

    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.DOUBLEBUF)

    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/vexations64.wav")
    pygame.mixer.music.set_volume(0.65)

    #hud1 = pygame.image.load("Images/hudblank.png")
    #hud1_rect = (0, HEIGHT - 70)

    hud_sh = pygame.image.load("Images/shieldfull.png")
    hud_sh_rect = (WIDTH / 2, HEIGHT - 70)

    hud_he = pygame.image.load("Images/healthfull.png")
    hud_he_rect = (WIDTH / 2, HEIGHT - 35)

    rect = screen.get_rect()
    our_hero = HatSprite.HatSprite(rect.center)
    alive = True


    hatgroup = pygame.sprite.RenderPlain(our_hero)
    lasergroup = pygame.sprite.RenderPlain()
    billo_lasergroup = pygame.sprite.RenderPlain()
    enemygroup = pygame.sprite.RenderPlain()
    effectsgroup = pygame.sprite.RenderPlain()
    pickupsgroup = pygame.sprite.RenderPlain()

    dt_tot = 0
    dt_tot_sincehit = 0

    critrate = 10
    in_detonation = False
    bonus_timer = 0
    bomb_drop = random.uniform(0.4,0.8)
    enemyrate = 0.8
    toughness = 1
    billotime = 0.4
    billo_in_effect = False

    while True:
        dt = clock.tick() / 1000
        dt_tot += dt
        dt_tot_sincehit += dt

        for event in pygame.event.get():
            if not hasattr(event, "key"): continue

            down = event.type == pygame.KEYDOWN

            if event.key == pygame.K_ESCAPE:
                exit(0)
            elif event.key == pygame.K_SPACE and gamestate != 1:
                pygame.mixer.music.play(-1)
                bg = pygame.image.load("Images/SPACE.png")
                if gamestate == 2:
                    critrate = 10
                    in_detonation = False
                    bonus_timer = 0
                    bomb_drop = random.uniform(0.4,0.8)

                    enemyrate = 0.8
                    toughness = 1
                    billotime = 0.4
                    billo_in_effect = False

                    our_hero = HatSprite.HatSprite(rect.center)
                    alive = True
                    hatgroup = pygame.sprite.RenderPlain(our_hero)

                    hud_sh = pygame.image.load(shield_huds[our_hero.shield])
                    hud_he = pygame.image.load(health_huds[our_hero.health])
                gamestate = 1

            #hat control keys
            elif event.key == pygame.K_LEFT:
                our_hero.vx -= down * 30
                our_hero.theta = down * -5
                if down: SoundsFile.hatmove.play()
            elif event.key == pygame.K_RIGHT:
                our_hero.vx += down * 30
                our_hero.theta = down * 5
                if down: SoundsFile.hatmove.play()
            elif event.key == pygame.K_UP:
                our_hero.vy -= down * 30
                if down: SoundsFile.hatmove.play()
            elif event.key == pygame.K_DOWN:
                our_hero.vy += down * 30
                if down: SoundsFile.hatmove.play()

            #laser keys
            if alive:
                if event.key == pygame.K_q and our_hero.bomb:
                    SoundsFile.bomb.play()
                    in_detonation = True
                    our_hero.bomb = False
                elif event.key == pygame.K_a:
                    position = our_hero.position
                    our_hero.theta = -90 - down * 5
                    our_hero.vx += 5
                    if down: lasergroup.add(LaserSprite.LaserSprite(position,180, critrate))
                elif event.key == pygame.K_d:
                    position = our_hero.position
                    our_hero.theta = 90 + down * 5
                    our_hero.vx -= 5
                    if down: lasergroup.add(LaserSprite.LaserSprite(position,0 , critrate))
                elif event.key == pygame.K_w:
                    position = our_hero.position
                    our_hero.theta = 180 + down * 5
                    our_hero.vy += 5
                    if down: lasergroup.add(LaserSprite.LaserSprite(position,90, critrate))
                elif event.key == pygame.K_s:
                    position = our_hero.position
                    our_hero.theta = down * 5
                    our_hero.vy -= 5
                    if down: lasergroup.add(LaserSprite.LaserSprite(position,270, critrate))
                #elif event.key == pygame.K_c and down:
                #    pickupsgroup.add(Pickups.BombPickup((325,325)))
                #    pickupsgroup.add(Pickups.CritPickup((325,325)))


        if(gamestate == 1 and dt_tot > enemyrate):
            if(enemyrate <= bomb_drop):
                drop_position = (random.uniform(0,650), random.uniform(0,650))
                pickupsgroup.add(Pickups.BombPickup(drop_position))
                bomb_drop = 0
                SoundsFile.pickup_appear.play()
            if(enemyrate > billotime):
                (rx, ry) = (0,0)
                while(bgrect.collidepoint((rx,ry))):
                    rx = random.uniform(-50,700)
                    ry = random.uniform(-50,700)
                if(toughness <= 3):
                    enemygroup.add(EnemySprite.SpaceCrab((rx, ry), our_hero, toughness))
                    dt_tot = 0
                    enemyrate -= 0.008
                #elif(toughness > 3):

            else:
                if(not billo_in_effect):
                    bx = 0
                    by = 500 * random.random()
                    if(int(2 * random.random()) == 1): bx = 650

                    if(bx == 0): tx = 750
                    else: tx = -100
                    billo_sprite = EnemySprite.BillOReilly((bx,by),(tx, 0), toughness)
                    enemygroup.add(billo_sprite)
                    billo_in_effect = True

        if dt_tot_sincehit > 5:
            if(our_hero.shield == 0):
                our_hero.src_image = pygame.image.load("Images/laserhat_shielded.png")
                our_hero.src_image.set_colorkey((255,255,255))
            if(our_hero.shield < 3):
                SoundsFile.recharge_sounds[our_hero.shield].set_volume(0.6)
                SoundsFile.recharge_sounds[our_hero.shield].play()
                our_hero.shield += 1
                if(our_hero.shield == 3):
                    effectsgroup.add(Effects.ShieldBanner(our_hero.position, True))
                hud_sh = pygame.image.load(shield_huds[our_hero.shield])
            dt_tot_sincehit = 3.5


        screen.blit(bg, bgrect)

        if billo_in_effect:
            for c in billo_sprite.billo_crabgroup:
                enemygroup.add(c)
            for crit in billo_sprite.billo_effectgroup:
                effectsgroup.add(crit)
            for l in billo_sprite.billo_lasergroup:
                billo_lasergroup.add(l)
            billo_sprite.billo_crabgroup.clear()
            if(billo_sprite.state == 2):
                billo_in_effect = False
                pickupsgroup.add(Pickups.CritPickup(billo_sprite.position))
                billo_sprite.kill()
                toughness += 1
                enemyrate = 0.8
                billotime = 0.4
                bomb_drop = random.uniform(0.4,0.8)

        if critrate == 1:
            if SoundsFile.critspree.get_num_channels() == 0:
                critrate = 10
        if in_detonation:
            position = our_hero.position
            lasergroup.add(LaserSprite.BombFire(our_hero.position, bonus_timer * 10))
            lasergroup.add(LaserSprite.BombFire(our_hero.position, bonus_timer * 10 + 90))
            lasergroup.add(LaserSprite.BombFire(our_hero.position, bonus_timer * 10 + 180))
            lasergroup.add(LaserSprite.BombFire(our_hero.position, bonus_timer * 10 + 270))
            bonus_timer += 1
            if bonus_timer == 55:
                in_detonation = False
                bonus_timer = 0


        for e in our_hero.hat_effectsgroup:
            effectsgroup.add(e)

        for p in pygame.sprite.spritecollide(our_hero, pickupsgroup, False):
            if p.__class__.__name__ == "CritPickup":
                critrate = 1
                SoundsFile.critspree.play()
                bonus_timer = 0
            elif p.__class__.__name__ == "BombPickup":
                our_hero.bomb = True
            p.kill()
            SoundsFile.pickup_get.play()

        for l in lasergroup:
            if l.hit_list == []:
                continue
            else:
                for e in l.hit_list:
                    effectsgroup.add(Effects.Splosion(e.position, e.theta))
                    if l.crit:
                        effectsgroup.add(Effects.CritBanner(e.position))
                l.kill()

        for l in billo_lasergroup:
            if l.hit_list == []:
                continue
            else:
                for e in l.hit_list:
                    effectsgroup.add(Effects.Splosion(e.position, e.theta))
                    if l.crit:
                        effectsgroup.add(Effects.CritBanner(e.position))
                l.kill()



        if(our_hero.is_hit):
            dt_tot_sincehit = 0
            if(our_hero.health <= 0):
                hud_he = pygame.image.load(health_huds[0])
                alive = False
                gamestate = 2
            else:
                hud_sh = pygame.image.load(shield_huds[our_hero.shield])
                hud_he = pygame.image.load(health_huds[our_hero.health])
            our_hero.is_hit = False

        pickupsgroup.draw(screen)
        pickupsgroup.update(dt)

        lasergroup.update(dt, enemygroup)
        lasergroup.draw(screen)

        hatgroup.update(dt, enemygroup)
        hatgroup.draw(screen)

        enemygroup.update(dt)
        enemygroup.draw(screen)

        billo_lasergroup.update(dt, hatgroup)
        billo_lasergroup.draw(screen)

        effectsgroup.update(dt)
        effectsgroup.draw(screen)

        if gamestate == 1:
            hud_sh.set_colorkey((255,255,255))
            hud_sh.convert_alpha()
            screen.blit(hud_sh, hud_sh_rect)

            hud_he.set_colorkey((255,255,255))
            hud_he.convert_alpha()
            screen.blit(hud_he, hud_he_rect)

        if gamestate == 2:
            bg = pygame.image.load("Images/deadscreen.png")
            for e in enemygroup:
                e.kill()
            for p in pickupsgroup:
                p.kill()

        pygame.display.flip()



main()