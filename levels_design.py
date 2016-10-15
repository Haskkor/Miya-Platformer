import constants

###############
### LEVEL 1 ###
###############

# Tableau contenant l'image, la position en x et la position en y des plateformes du niveau 1

level_1 = [ [constants.GRASS_BOTTOM, 0, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2],
            [constants.GRASS_BOTTOM, constants.GRASS_BOTTOM_WIDTH, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2],

            [constants.GRASS_LEFT, 450, 400],
            [constants.GRASS_MIDDLE, 520, 400],
            [constants.GRASS_MIDDLE, 590, 400],
            [constants.GRASS_MIDDLE, 660, 400],
            [constants.GRASS_RIGHT, 730, 400],

            [constants.BOX_CROSS, 1050, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],

            [constants.BOX_CROSS, 1300, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 1300, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],

            [constants.BOX_CROSS, 1550, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 1550, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],

            [constants.BOX_CROSS, 1800, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 1800, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 1950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 1950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 1950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 3],
            [constants.BOX_CROSS, 2020, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],

            [constants.GRASS_LEFT, 2180, 200],
            [constants.GRASS_MIDDLE, 2250, 200],
            [constants.GRASS_RIGHT, 2320, 200],

            [constants.GRASS_LEFT, 2390, 30],
            [constants.GRASS_MIDDLE, 2460, 30],
            [constants.GRASS_MIDDLE, 2530, 30],
            [constants.GRASS_MIDDLE, 2600, 30],
            [constants.GRASS_RIGHT, 2670, 30],

            [constants.GRASS_LEFT, 3070, 30],
            [constants.GRASS_MIDDLE, 3140, 30],
            [constants.GRASS_RIGHT, 3210, 30],

            [constants.GRASS_LEFT, 3280, 400],
            [constants.GRASS_MIDDLE, 3350, 400],
            [constants.GRASS_RIGHT, 3420, 400],

            [constants.GRASS, 3690, 400],

            [constants.GRASS, 3960, 400],

            [constants.GRASS, 4230, 400],

            [constants.BOX_CROSS, 4600, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 4670, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 4670, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 4740, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 4740, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 4740, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 3],
            [constants.BOX_CROSS, 4810, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 4810, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 4810, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 3],
            [constants.BOX_CROSS, 4810, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 4],
            [constants.BOX_CROSS, 4880, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 4880, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 4880, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 3],
            [constants.BOX_CROSS, 4880, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 4],
            [constants.BOX_CROSS, 4880, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 5],
            [constants.BOX_CROSS, 4950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 4950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 4950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 3],
            [constants.BOX_CROSS, 4950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 4],
            [constants.BOX_CROSS, 4950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 5],
            [constants.BOX_CROSS, 4950, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 6],
            [constants.BOX_CROSS, 5020, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 5020, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            [constants.BOX_CROSS, 5020, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 3],
            [constants.BOX_CROSS, 5020, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 4],
            [constants.BOX_CROSS, 5090, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 - constants.TILE_HEIGHT],
            [constants.BOX_CROSS, 5090, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
             constants.TILE_HEIGHT * 2],
            ]
# Tableau contenant l'image, la position en x et la position en y des items du niveau 1
level_1_keys = [ [constants.YELLOWKEY, 3153, 30 - constants.DIFF_COIN_TILE_BOT],
                 ]
# Tableau contenant l'image, la position en x et la position en y des pièces du niveau 1
level_1_coins = [   [constants.GRASS_MIDDLE, 533, 400 - constants.DIFF_COIN_TILE_BOT],
                    [constants.GRASS_MIDDLE, 603, 400 - constants.DIFF_COIN_TILE_BOT],
                    [constants.GRASS_MIDDLE, 673, 400 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 1383, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 1383, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 1633, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 1633, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 1883, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 1883, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 2193, 200 - constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 2263, 200 - constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 2333, 200 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 2473, 30 - constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 2543, 30 - constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 2613, 30 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 3083, 30 - constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 3223, 30 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 3293, 400 - constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 3363, 400 - constants.DIFF_COIN_TILE_BOT],
                    [constants.COIN_F1, 3433, 400 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 3703, 400 - constants.TILE_HEIGHT * 2 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 3973, 400 - constants.TILE_HEIGHT * 2 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 4243, 400 - constants.TILE_HEIGHT * 2 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 4613, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 4683, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT * 2 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 4753, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT * 3 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 4823, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT * 4 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 4893, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT * 5 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 4963, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT * 6 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 5033, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT * 4 - constants.DIFF_COIN_TILE_BOT],

                    [constants.COIN_F1, 5103, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2 -
                     constants.TILE_HEIGHT * 2 - constants.DIFF_COIN_TILE_BOT],
                  ]

# Tableau contenant l'image, la position en x et la position en y des items fixes du niveau 1
level_1_items_scenery = [ [constants.CLOSEDDOOR, constants.LEVEL1END, constants.SCREEN_HEIGHT -
                           constants.DOORSHEIGHT - constants.TILE_HEIGHT / 2],
                          [constants.SIGN_EXIT, constants.LEVEL1END - constants.TILE_WIDTH - constants.SEP_TILES,
                           constants.SCREEN_HEIGHT - constants.TILE_HEIGHT - constants.TILE_HEIGHT / 2],
                          [constants.OPENEDDOOR, constants.OPENEDDOORINIT, constants.SCREEN_HEIGHT -
                           constants.DOORSHEIGHT - constants.TILE_HEIGHT / 2],
                          [constants.SIGN_RIGHT, constants.OPENEDDOORINIT + constants.TILE_WIDTH +
                           constants.SEP_TILES, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT -
                           constants.TILE_HEIGHT / 2],
                          [constants.SIGN_LEFT, 2370, -270 - constants.TILE_HEIGHT],
                          ]

###############
### LEVEL 2 ###
###############

# Tableau contenant l'image, la position en x et la position en y des plateformes du niveau 2
level_2 = [ [constants.GRASS_BOTTOM, 0, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT / 2],

            [constants.GRASS_LEFT, 450, 450],
            [constants.GRASS_MIDDLE, 520, 450],
            [constants.GRASS_RIGHT, 590, 450],

            [constants.GRASS_LEFT, 800, 310],
            [constants.GRASS_MIDDLE, 870, 310],
            [constants.GRASS_RIGHT, 940, 310],

            [constants.GRASS, 1160, 240],

            [constants.GRASS, 1450, 240],

            [constants.GRASS_LEFT, 1770, 150],
            [constants.GRASS_MIDDLE, 1840, 150],
            [constants.GRASS_RIGHT, 1910, 150],

            [constants.GRASS_LEFT, 2230, 50],
            [constants.GRASS_MIDDLE, 2300, 50],
            [constants.GRASS_RIGHT, 2370, 50],

            [constants.GRASS_RIGHT, 2370, -270],
            [constants.GRASS_MIDDLE, 2300, -270],
            [constants.GRASS_LEFT, 2230, -270],

            [constants.GRASS_RIGHT, 1910, -350],
            [constants.GRASS_MIDDLE, 1840, -350],
            [constants.GRASS_LEFT, 1770, -350],

            [constants.GRASS_MIDDLE, 900, -450],
            [constants.GRASS_CENTER, 900, -380],
            [constants.GRASS_CENTER, 900, -310],
            [constants.GRASS_CENTER, 900, -240],
            [constants.GRASS_MIDDLE, 830, -240],
            [constants.GRASS_LEFT, 760, -240],

            [constants.GRASS_RIGHT, 520, -520],
            [constants.GRASS_MIDDLE, 450, -520],
            [constants.GRASS_CENTER, 380, -520],
            [constants.GRASS_CENTER, 380, -590],
            [constants.GRASS_CENTER, 380, -660],
            [constants.GRASS_MIDDLE, 380, -730],
            [constants.GRASS_CENTER, 380, -450],
            [constants.GRASS_CENTER, 380, -380],
            [constants.GRASS_CENTER, 380, -310],
            [constants.GRASS_CENTER, 380, -240],
            [constants.GRASS_MIDDLE, 310, -240],
            [constants.GRASS_MIDDLE, 240, -240],
            [constants.GRASS_LEFT, 170, -240],

            [constants.GRASS_RIGHT, 70, -70],
            [constants.GRASS_MIDDLE, 0, -70],
            [constants.BOX_CROSS, 0, -140],
            ]

# Tableau contenant la définition des plateformes mobiles du niveau 2
level_2_mobil = [ [constants.GRASS, 2600, -200, -200, 70, 0, 0, 0, -1],

                  [constants.GRASS_HALF, 1400, -400, 0, 0, 1400, 1600, 1, 0],

                  [constants.GRASS_HALF, 1300, -400, 0, 0, 1100, 1300, -2, 0],

                  [constants.GRASS_CLIFF_DOUBLE, 150, -70, 0, 0, 150, 530, 1, 0],
                  ]

# Tableau contenant l'image, la position en x et la position en y des items du niveau 2
level_2_keys = [ [constants.YELLOWKEY, 310, -270],
                 ]

# Tableau contenant l'image, la position en x et la position en y des pièces du niveau 2
level_2_coins = [ [constants.COIN_F1, 465, 380],
                  [constants.COIN_F1, 535, 380],
                  [constants.COIN_F1, 605, 380],

                  [constants.COIN_F1, 815, 240],
                  [constants.COIN_F1, 885, 240],
                  [constants.COIN_F1, 955, 240],

                  [constants.COIN_F1, 1260, 100],
                  [constants.COIN_F1, 1330, 100],
                  [constants.COIN_F1, 1400, 100],

                  [constants.COIN_F1, 2315, -20],

                  [constants.COIN_F1, 2315, -340],

                  [constants.COIN_F1, 535, -590],
                  [constants.COIN_F1, 535, -660],
                  [constants.COIN_F1, 535, -730],
                  [constants.COIN_F1, 465, -590],
                  [constants.COIN_F1, 465, -660],
                  [constants.COIN_F1, 465, -730],
                  ]

# Tableau contenant l'image, la position en x et la position en y des items fixes du niveau 2
level_2_items_scenery = [ [constants.CLOSEDDOOR, constants.LEVEL2END, constants.SCREEN_HEIGHT -
                           constants.DOORSHEIGHT - constants.TILE_HEIGHT / 2],
                          [constants.SIGN_EXIT, constants.LEVEL2END - constants.TILE_WIDTH - constants.SEP_TILES,
                           constants.SCREEN_HEIGHT - constants.TILE_HEIGHT - constants.TILE_HEIGHT / 2],
                          [constants.OPENEDDOOR, constants.OPENEDDOORINIT, constants.SCREEN_HEIGHT -
                           constants.DOORSHEIGHT - constants.TILE_HEIGHT / 2],
                          [constants.SIGN_RIGHT, constants.OPENEDDOORINIT + constants.TILE_WIDTH +
                           constants.SEP_TILES, constants.SCREEN_HEIGHT - constants.TILE_HEIGHT -
                           constants.TILE_HEIGHT / 2],
                          [constants.SIGN_LEFT, 2370, -270 - constants.TILE_HEIGHT],
                          ]
