import pygame
import constants
import levels
from sprites import SpriteSheet

#########################
### DEFINITION DU HUD ###
#########################

class Hud(object):

    # Liste des sprites
    keys_list = None

    # Police et texte pour les pièces
    pygame.font.init()
    font = pygame.font.SysFont(constants.JOKERMAN, 28)

    def __init__(self, Level):

        self.level = Level
        self.keys_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()

    def update(self):

        self.keys_list.update()
        self.coin_list.update()

    def draw(self, screen):

        # Dessine tous les sprites
        self.keys_list.draw(screen)
        self.coin_list.draw(screen)

#####################################
### DEFINITION DU HUD DU NIVEAU 1 ###
#####################################

class Level_01_Hud(Hud):

    level_keys = []
    level_coin = []
    score_text = ""

    def __init__(self, Level):

        Hud.__init__(self, Level)

        # Tableau contenant la définition des clefs
        self.level_keys = [[constants.HUDYELLOWKEY, constants.POSHUDKEY1_X, constants.POSHUDKEY_Y]]

        for key in self.level_keys:
            temp_key = SpriteSheet(key[0][0])
            temp_key.rect.x = key[1]
            temp_key.rect.y = key[2]
            self.keys_list.add(temp_key)

        self.level_coin = [[constants.HUDCOIN, constants.POSHUDCOIN_X, constants.POSHUDCOIN_Y]]

        for coin in self.level_coin:
            temp_coin = SpriteSheet(coin[0])
            temp_coin.rect.x = coin[1]
            temp_coin.rect.y = coin[2]
            self.coin_list.add(temp_coin)

        self.score_text = self.font.render(" : " + str(levels.Level_01.picked_coins) + " / " +
                                           str(constants.LEVEL1TOTALCOIN), 1, (96,96,96))

    # Supprime la clef ramassée du tableau et modifie la clef du HUD. La clef du HUD et son homologue item ramassable
    # doivent avoir la même largeur. Toutes les clefs ont une largeur différente
    def change_key(self, sprite):
        for key in self.keys_list:
            if sprite.rect.width == key.rect.width:
                self.keys_list.remove(key)
        for key in self.level_keys:
            temp_key = SpriteSheet(key[0][0])
            if sprite.rect.width == temp_key.rect.width:
                temp = key[0][0]
                key[0][0] = key[0][1]
                key[0][1] = temp
                temp_key = SpriteSheet(key[0][0])
                temp_key.rect.x = key[1]
                temp_key.rect.y = key[2]
                self.keys_list.add(temp_key)

    # Incrémente le compteur du HUD pour chaque pièce ramassée
    def increm_coin(self, number):
        levels.Level_01.picked_coins += number
        self.score_text = self.font.render(" : " + str(levels.Level_01.picked_coins) + " / " +
                                           str(constants.LEVEL1TOTALCOIN), 1, constants.GREY)
        self.level.increm_coins(number)

#####################################
### DEFINITION DU HUD DU NIVEAU 1 ###
#####################################

class Level_02_Hud(Hud):

    level_keys = []
    level_coin = []
    score_text = ""

    def __init__(self, Level):

        Hud.__init__(self, Level)

        # Tableau contenant la définition des clefs
        self.level_keys = [[constants.HUDYELLOWKEY, constants.POSHUDKEY1_X, constants.POSHUDKEY_Y]]

        for key in self.level_keys:
            temp_key = SpriteSheet(key[0][0])
            temp_key.rect.x = key[1]
            temp_key.rect.y = key[2]
            self.keys_list.add(temp_key)

        self.level_coin = [[constants.HUDCOIN, constants.POSHUDCOIN_X, constants.POSHUDCOIN_Y]]

        for coin in self.level_coin:
            temp_coin = SpriteSheet(coin[0])
            temp_coin.rect.x = coin[1]
            temp_coin.rect.y = coin[2]
            self.coin_list.add(temp_coin)

        self.score_text = self.font.render(" : " + str(levels.Level_01.picked_coins) + " / " +
                                           str(constants.LEVEL2TOTALCOIN), 1, (96,96,96))

    # Supprime la clef ramassée du tableau et modifie la clef du HUD. La clef du HUD et son homologue item ramassable
    # doivent avoir la même largeur. Toutes les clefs ont une largeur différente
    def change_key(self, sprite):
        for key in self.keys_list:
            if sprite.rect.width == key.rect.width:
                self.keys_list.remove(key)
        for key in self.level_keys:
            temp_key = SpriteSheet(key[0][0])
            if sprite.rect.width == temp_key.rect.width:
                temp = key[0][0]
                key[0][0] = key[0][1]
                key[0][1] = temp
                temp_key = SpriteSheet(key[0][0])
                temp_key.rect.x = key[1]
                temp_key.rect.y = key[2]
                self.keys_list.add(temp_key)

    # Incrémente le compteur du HUD pour chaque pièce ramassée
    def increm_coin(self, number):
        levels.Level_02.picked_coins += number
        self.score_text = self.font.render(" : " + str(levels.Level_01.picked_coins) + " / " +
                                           str(constants.LEVEL2TOTALCOIN), 1, constants.GREY)
        self.level.increm_coins(number)

