import pygame
import constants
from platforms import MovingPlatform
from sprites import SpriteSheet

##########################
### CONTROLE DU JOUEUR ###
##########################

class Player(pygame.sprite.Sprite):

    # Vitesse du joueur
    change_x = 0
    change_y = 0

    # Images du joueur
    walking_frames_l = []
    walking_frames_r = []
    idle_frames_l = []
    idle_frames_r = []
    jump_frames = []

    # Direction du joueur (droite/gauche)
    direction = "R"

    # Niveau courant
    level = None

    # Hud courant
    hud = None

    # Booléen indiquant si le joueur se déplace, monte ou descend
    moving = False
    upping = False
    downing = False

    # Compteur des frames
    frame = 0

    # Compteur des occurences de passage dans la fonction update
    count = 0

    # Position réelle en x
    true_pos_x = 0

    # Variable indiquant si le joueur possède la clef de sortie
    has_key = False

    def __init__(self):
        
        super().__init__()

        # Définition des sprites IDLE du joueur
        sprite_sheet = SpriteSheet(constants.FIDLE1)
        self.idle_frames_r.append(sprite_sheet.image)
        self.idle_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))
        sprite_sheet = SpriteSheet(constants.FIDLE2)
        self.idle_frames_r.append(sprite_sheet.image)
        self.idle_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))

        # Définition des sprites RUNNING du joueur
        sprite_sheet = SpriteSheet(constants.FRUN1)
        self.walking_frames_r.append(sprite_sheet.image)
        self.walking_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))
        sprite_sheet = SpriteSheet(constants.FRUN2)
        self.walking_frames_r.append(sprite_sheet.image)
        self.walking_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))
        sprite_sheet = SpriteSheet(constants.FRUN3)
        self.walking_frames_r.append(sprite_sheet.image)
        self.walking_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))
        sprite_sheet = SpriteSheet(constants.FRUN4)
        self.walking_frames_r.append(sprite_sheet.image)
        self.walking_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))
        sprite_sheet = SpriteSheet(constants.FRUN5)
        self.walking_frames_r.append(sprite_sheet.image)
        self.walking_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))
        sprite_sheet = SpriteSheet(constants.FRUN6)
        self.walking_frames_r.append(sprite_sheet.image)
        self.walking_frames_l.append(pygame.transform.flip(sprite_sheet.image, True, False))

        # Définition des sprites JUMP du joueur
        sprite_sheet = SpriteSheet(constants.FUP)
        self.jump_frames.append(sprite_sheet.image)
        self.jump_frames.append(pygame.transform.flip(sprite_sheet.image, True, False))
        sprite_sheet = SpriteSheet(constants.FDOWN)
        self.jump_frames.append(sprite_sheet.image)
        self.jump_frames.append(pygame.transform.flip(sprite_sheet.image, True, False))
        
        # Sélectionne l'image de départ
        self.image = self.idle_frames_r[0]

        # Récupère la zone de collision du personnage et la réduit à la largeur de ses pieds
        self.rect_image = self.image.get_rect()
        self.rect = pygame.Rect(constants.PLAYERLEFT,constants.PLAYERTOP,constants.PLAYERWIDTH,constants.PLAYERHEIGHT)

    def update(self):

        self.rect_image.center = self.rect.center

        self.count += 1

        # Utilisation de la gravité
        self.calc_grav()

        self.rect.x += self.change_x
        self.true_pos_x += self.change_x

        # Si le joueur atteint la limite gauche il est bloqué
        if self.rect_image.x < 0:
            self.rect_image.x = 0
            self.rect.center = self.rect_image.center

        # Si le joueur atteint la limite droite il est bloqué
        if self.true_pos_x > self.level.level_end + constants.SHIFTLIMITRIGHT:
            self.rect_image.x = constants.SCREEN_WIDTH - self.rect_image.width
            self.rect.center = self.rect_image.center
            self.true_pos_x = self.level.level_end + constants.SHIFTLIMITRIGHT

        # Vérifie une potentielle collision avec un élément du décor (en déplacement horizontal)
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)

        for block in block_hit_list:
            if self.direction == "R":
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        # Déplacement vers le haut ou vers le bas
        self.rect.y += self.change_y

        # Vérifie une potentielle collision avec un élément du décor (en déplacement vertical)
        self.rect.y += 2
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        for block in block_hit_list:

            # Si le joueur est sur un bloc mobile
            if isinstance(block, MovingPlatform):

                if self.change_x == 0:
                    self.rect.x += block.change_x
                    self.true_pos_x += block.change_x

                # Si le joueur est sur un bloc mobile vertical (permet de rester collé au bloc lors de la descente
                if block.change_y != 0:
                    self.rect.bottom = block.rect.top

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Arrête le mouvement vertical
            self.change_y = 0
            self.downing = False

        # Vérifie une potentielle collision avec une clef et la supprime de la liste le cas échéant
        keys_hit_list = pygame.sprite.spritecollide(self, self.level.keys_list, True)
        if len(keys_hit_list) > 0:
            self.hud.change_key(keys_hit_list[0])
        if len(keys_hit_list) == self.level.needed_keys:
            self.has_key = True

        # Vérifie une potentielle collision avec une pièce et la supprime de la liste le cas échéant
        coins_hit_list = pygame.sprite.spritecollide(self, self.level.coins_list, True)
        if len(coins_hit_list) > 0:
            self.hud.increm_coin(len(coins_hit_list))

        pos = self.rect.x + self.level.world_shift_h

        # Si le joueur regarde à droite
        if self.direction == "R":
            # Si le joueur se déplace
            if self.moving and not self.upping and not self.downing:
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            # Si le joueur est à l'arrêt
            elif not self.moving and not self.upping and not self.downing:
                if self.count > 30:
                    if self.frame < (len(self.idle_frames_r) - 1):
                        self.frame += 1
                    else:
                        self.frame = 0
                    self.image = self.idle_frames_r[self.frame]
                    self.count = 0
        # Si le joueur regarde à gauche
        else:
            # Si le joueur se déplace
            if self.moving and not self.upping and not self.downing:
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
            # Si le joueur est à l'arrêt
            elif not self.moving and not self.upping and not self.downing:
                if self.count > 30:
                    if self.frame < (len(self.idle_frames_l) - 1):
                        self.frame += 1
                    else:
                        self.frame = 0
                    self.image = self.idle_frames_l[self.frame]
                    self.count = 0

    # Fonctionnement de la gravité
    def calc_grav(self):
        if self.change_y != 0:
            self.change_y += constants.GRAVITY
            self.upping = False
            self.downing = True

        # Descend un peu et contrôle si il y a une plateforme en dessous
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # Si il n'y a pas de plateforme et que le joueur n'est pas au sol ni en saut, initie la chute
        if self.rect.y < constants.SCREEN_HEIGHT - self.rect.height:
            if len(platform_hit_list) == 0 and not self.upping and not self.downing:
                self.change_y = 0.01

        # Si le joueur est en train de sauter
        if self.change_y < 0:
            if self.direction == "R":
                self.image = self.jump_frames[0]
            else:
                self.image = self.jump_frames[1]
        # Si le joueur est en train de tomber
        elif self.change_y > 0:
            if self.direction == "R":
                self.image = self.jump_frames[2]
            else:
                self.image = self.jump_frames[3]

        # Contrôle si le joueur atteint le sol
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            self.downing = False

    # Gestion du saut 
    def jump(self):
        
        # Descend un peu et contrôle si il y a une plateforme en dessous
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # Si il est possible de sauter, modifie la vitesse en conséquence
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -constants.PLAYERJUMPSPEED

    # Gestion des déplacements
    def go_left(self):
        self.direction = "L"
        self.change_x = -constants.PLAYERRUNSPEED
        self.moving = True
 
    def go_right(self):
        self.direction = "R"
        self.change_x = constants.PLAYERRUNSPEED
        self.moving = True
 
    def stop(self):
        self.change_x = 0
        self.moving = False
