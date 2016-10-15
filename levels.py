import pygame
import constants
from sprites import SpriteSheet
import platforms
import levels_design

##############################
### DEFINITION DES NIVEAUX ###
##############################

class Level(object):

    # Liste des sprites
    platform_list = None
    keys_list = None
    items_scenery_list = None
    enemy_list = None
    coins_list = None

    # Liste des sprites des pièces
    frame_coin = 0
    coins_frame = []
    tick_count = 0

    # Fond d'écran
    background = None

    # Défilement actuel du niveau
    world_shift_h = 0
    world_shift_v = 0
    level_limit = 0
    level_end = 0

    # Nombre de clefs nécessaires pour ouvrir la porte de fin de niveau
    needed_keys = 0

    # Nombre de pièces à ramasser dans le niveau
    number_coins = 0
    picked_coins = 0
 
    def __init__(self, player):
        
        self.platform_list = pygame.sprite.Group()
        self.keys_list = pygame.sprite.Group()
        self.items_scenery_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.coins_list = pygame.sprite.Group()
        self.player = player

        # Définition des sprites des pièces
        sprite_sheet = SpriteSheet(constants.COIN_F1)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F2)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F3)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F4)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F5)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F6)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F7)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F8)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F9)
        self.coins_frame.append(sprite_sheet.image)
        sprite_sheet = SpriteSheet(constants.COIN_F10)
        self.coins_frame.append(sprite_sheet.image)
 
    def update(self, tick):
        
        self.platform_list.update()
        self.keys_list.update()
        self.items_scenery_list.update()
        self.enemy_list.update()
        self.change_coin_frame(tick)
        self.coins_list.update()
 
    def draw(self, screen):

        # Dessine l'arrière plan (ne défile pas aussi vite que les sprites)
        screen.fill(constants.BLUE)
        temp_rect = self.background.get_rect()
        screen.blit(self.background,(self.world_shift_h // 3, -(temp_rect.height - constants.SCREEN_HEIGHT -
                                                                self.world_shift_v // 3)))

        # Dessine tous les sprites
        self.platform_list.draw(screen)
        self.keys_list.draw(screen)
        self.items_scenery_list.draw(screen)
        self.enemy_list.draw(screen)
        self.coins_list.draw(screen)

    # Change l'image des pièces du niveau
    def change_coin_frame(self, tick):
        if tick - self.tick_count >= 100:
            if self.frame_coin < (len(self.coins_frame) - 1):
                self.frame_coin += 1
            else:
                self.frame_coin = 0
            for coin in self.coins_list:
                coin.image = self.coins_frame[self.frame_coin]
            self.tick_count = tick

    # Fais défiler le niveau horizontalement
    def shift_world_h(self, shift_x):
 
        self.world_shift_h += shift_x
 
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for key in self.keys_list:
            key.rect.x += shift_x

        for item_scenery in  self.items_scenery_list:
            item_scenery.rect.x += shift_x

        for coin in self.coins_list:
            coin.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    # Fait défiler le niveau verticalement
    def shift_world_v(self, shift_y):

        # Si le shift fait descendre le monde trop bas, fixe le monde à 0
        if self.world_shift_v + shift_y < 0:
            shift_y = -self.world_shift_v

        self.world_shift_v += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y
            # Shift world vertical pour les plateformes mobiles verticales
            if isinstance(platform,platforms.MovingPlatform):
                platform.boundary_top += shift_y
                platform.boundary_bottom += shift_y

        for key in self.keys_list:
            key.rect.y += shift_y

        for item_scenery in  self.items_scenery_list:
            item_scenery.rect.y += shift_y

        for coin in self.coins_list:
            coin.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

    # Rempli une liste contenant la définition des plateformes
    def fill_platforms(self, platforms):

        level_plat = platforms

        for platform in level_plat:
            block = SpriteSheet(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

    # Rempli une liste contenant la définition des plateformes mobiles
    def fill_mobil_platforms(self, platforms_lvl):

        level_plat_mobil = platforms_lvl

        for platform in level_plat_mobil:
            block = platforms.MovingPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.boundary_top = platform[3]
            block.boundary_bottom = platform[4]
            block.boundary_left = platform[5]
            block.boundary_right = platform[6]
            block.change_x = platform[7]
            block.change_y = platform[8]
            block.player = self.player
            block.level = self
            self.platform_list.add(block)

    # Rempli une liste contenant la définition des clefs
    def fill_keys(self, keys):

        level_keys = keys

        for item in level_keys:
            article = SpriteSheet(item[0])
            article.rect.x = item[1]
            article.rect.y = item[2]
            article.player = self.player
            self.keys_list.add(article)

    # Rempli une liste contenant la définition des items fixes
    def fill_items_scenery(self, items_scenery):

        level_items_scenery = items_scenery

        for item in level_items_scenery:
            article = SpriteSheet(item[0])
            article.rect.x = item[1]
            article.rect.y = item[2]
            article.player = self.player
            self.items_scenery_list.add(article)

    # Rempli une liste contenant la définition des pièces
    def fill_coins(self, coins):

        level_coins = coins

        for item in level_coins:
            article = SpriteSheet(item[0])
            article.rect.x = item[1]
            article.rect.y = item[2]
            article.player = self.player
            self.coins_list.add(article)

##############################
### DEFINITION DU NIVEAU 1 ###
##############################
        
class Level_01(Level):

    def __init__(self, player):

        Level.__init__(self, player)

        self.background = pygame.image.load(constants.LEVEL1BG).convert()
        self.background.set_colorkey(constants.FORTRANSPARENCY)
        self.level_limit = -2500
        self.needed_keys = 1
        self.picked_coins = 0
        self.number_coins = constants.LEVEL1TOTALCOIN
        self.level_end = constants.LEVEL1END

        # Plateformes du niveau
        self.fill_platforms(levels_design.level_1)

        # Tableau contenant la définition des items
        self.fill_keys(levels_design.level_1_keys)

        # Tableau contenant la définition des items fixes
        self.fill_items_scenery(levels_design.level_1_items_scenery)

        # Tableau contenant la définition des pièces
        self.fill_coins(levels_design.level_1_coins)

    def increm_coins(self, number):
        self.picked_coins += number

##############################
### DEFINITION DU NIVEAU 2 ###
##############################

class Level_02(Level):

    def __init__(self, player):

        Level.__init__(self, player)

        self.background = pygame.image.load(constants.LEVEL1BG).convert()
        self.background.set_colorkey(constants.FORTRANSPARENCY)
        self.level_limit = -2500
        self.needed_keys = 1
        self.picked_coins = 0
        self.number_coins = constants.LEVEL2TOTALCOIN
        self.level_end = constants.LEVEL2END

        # Plateformes du niveau
        self.fill_platforms(levels_design.level_2)

        # Tableau contenant la définition des plateformes mobiles
        self.fill_mobil_platforms(levels_design.level_2_mobil)

        # Tableau contenant la définition des items
        self.fill_keys(levels_design.level_2_keys)

        # Tableau contenant la définition des items fixes
        self.fill_items_scenery(levels_design.level_2_items_scenery)

        # Tableau contenant la définition des pièces
        self.fill_coins(levels_design.level_2_coins)

    def increm_coins(self, number):
        self.picked_coins += number
