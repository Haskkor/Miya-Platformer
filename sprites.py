import pygame

###############################
### IMPORTATION DES SPRITES ###
###############################

class SpriteSheet(pygame.sprite.Sprite):

    sprite = None

    def __init__(self, file_name):

        super().__init__()

        # Charge le fichier du sprite
        self.sprite = pygame.image.load(file_name)

        self.image = self.sprite

        self.rect = self.image.get_rect()