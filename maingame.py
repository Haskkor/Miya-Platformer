import pygame
import constants
import levels
import hud
from player import Player

__author__ = "Jérémy Farnault"

###########################
### FONCTION PRINCIPALE ###
###########################
            
def main():

    pygame.init()

    # Initialisation de l'écran
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption(constants.TITLE)
 
    player = Player()

    # Initialisation des niveaux
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Définition du niveau actuel
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level

    # Initialisation des HUD
    hud_list = []
    hud_list.append(hud.Level_01_Hud(current_level))
    current_hud = hud_list[current_level_no]
    player.hud = current_hud

    # Variable suivant le shift vertical des objets du jeu
    total_diff = 0

    # Initialisation du joueur
    player.rect.x = constants.PLAYERINIT
    player.true_pos_x = constants.PLAYERINIT
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - constants.TILE_HEIGHT / 2

    # Attend la fermeture du programme
    done = False
 
    clock = pygame.time.Clock()

    # Déroulement du jeu
    while not done:

        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Met à jour le joueur et les items
        player.update()
        current_level.update(ticks)
        current_hud.update()

        # Déplace le monde vers la droite
        if player.rect.right >= constants.SHIFTLIMITRIGHT and -current_level.world_shift_h + \
                constants.PLAYERINIT < current_level.level_end:
            diff = player.rect.right - constants.SHIFTLIMITRIGHT
            player.rect.right = constants.SHIFTLIMITRIGHT
            current_level.shift_world_h(-diff)

        # Déplace le monde vers la gauche si l'on a pas atteint la limite gauche
        if player.rect.left <= constants.SHIFTLIMITLEFT and current_level.world_shift_h < 0:
            diff = constants.SHIFTLIMITLEFT - player.rect.left
            player.rect.left = constants.SHIFTLIMITLEFT
            current_level.shift_world_h(diff)

        # Déplace le monde vers le haut
        if player.rect.top <= constants.SHIFTLIMITTOP:
            diff = constants.SHIFTLIMITTOP - player.rect.top
            total_diff += diff
            player.rect.top = constants.SHIFTLIMITTOP
            current_level.shift_world_v(diff)

        # Déplace le monde vers le bas si l'on a pas atteint le sol
        if player.rect.bottom >= constants.SHIFTLIMITBOTTOM and current_level.world_shift_v > 0:
            diff = constants.SHIFTLIMITBOTTOM - player.rect.bottom
            player.rect.bottom = constants.SHIFTLIMITBOTTOM
            if total_diff + diff <= 0:
                total_diff += diff
                current_level.shift_world_v(diff)
            else:
                total_diff += diff
                current_level.shift_world_v(diff)

        # Passe au niveau suivant
        # Récupère la position de la porte ouverte
        exit_door_x = 0
        for item_scenery in current_level.items_scenery_list:
            if item_scenery.rect.x > exit_door_x:
                exit_door_x = item_scenery.rect.x

        if player.rect.x < exit_door_x + 3 and player.rect.x > exit_door_x - 3 and player.rect_image.top == constants.SCREEN_HEIGHT - \
                player.rect_image.height - constants.TILE_HEIGHT / 2 and player.has_key:

            # Affiche un écran contenant les données du niveau terminé
            done = end_level_screen(screen, ticks, current_level.number_coins, current_level.picked_coins)

            if not done:
                player.rect.x = constants.PLAYERINIT
                player.true_pos_x = constants.PLAYERINIT
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    current_hud = hud_list[current_level_no]
                    player.level = current_level
                else:
                    # Si il n'y a plus de niveaux, quitte le programme
                    done = True

        # Dessin
        if not done:
            current_level.draw(screen)
            current_hud.draw(screen)
            screen.blit(player.image, (player.rect_image.x,player.rect_image.y))
            screen.blit(current_hud.score_text, (constants.POSHUDCOINTEXT_X, constants.POSHUDCOINTEXT_Y))
        # Fin dessin

        clock.tick(60)
        
        # Met à jour l'affichage
        pygame.display.flip()
 
    pygame.quit()

########################################################
### FONCTION D'AFFICHAGE DE L'ECRAN DE FIN DE NIVEAU ###
########################################################

def end_level_screen(screen,time,totalcoins,pickedupcoins):

    end = False
    done = False
    pygame.font.init()
    font_big = pygame.font.SysFont(constants.JOKERMAN, 40)
    font_small = pygame.font.SysFont(constants.JOKERMAN, 18)
    background = pygame.image.load(constants.ENDLEVELBG).convert()
    background.set_colorkey(constants.FORTRANSPARENCY)
    background_rect = background.get_rect()

    while not end:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        end = True

        screen.fill(constants.BLACK)

        score_text_coins = font_big.render(str(pickedupcoins) + " pièces récupérées sur " + str(totalcoins), 1,
                                       constants.GREY)

        score_text_time = font_big.render("Niveau terminé en " + str(time / 1000) + " secondes.", 1, constants.GREY)

        score_hit_enter = font_small.render("APPUYER SUR ENTREE POUR CONTINUER", 1, (constants.WHITE))

        textpos_coins = score_text_coins.get_rect()
        textpos_coins.centerx = screen.get_rect().centerx
        textpos_coins.centery = screen.get_rect().centery - 50
        textpos_time = score_text_time.get_rect()
        textpos_time.centerx = screen.get_rect().centerx
        textpos_time.centery = screen.get_rect().centery + 50
        textpos_enter = score_hit_enter.get_rect()
        textpos_enter.centerx = screen.get_rect().centerx
        textpos_enter.centery = screen.get_rect().centery + 250

        screen.blit(background, background_rect)
        screen.blit(score_text_coins, textpos_coins)
        screen.blit(score_text_time, textpos_time)
        screen.blit(score_hit_enter, textpos_enter)
        pygame.display.flip()

    return done

##############################
### LANCEMENT DU PROGRAMME ###
##############################

if __name__ == "__main__":
    main()
