import pygame as py
from os.path import join #ao importar aquivos, deixa as barras do diretorio consistente em qualquer sistema operacional ( / e \)

from random import randint
# general setup
py.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
py.display.set_caption('Space Shooter')
running = True

# plain surface
surf = py.Surface((100,200))
surf.fill('darkorange')
x = 10

# importing an image
player_surf = py.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

star_surf = py.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))for i in range(20)]

meteor_surf = py.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = py.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = player_surf.get_frect(bottomleft = (1260, 700))

while running:
    # event loop
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgrey')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    if player_rect.right < WINDOW_WIDTH :    
        player_rect.left += 0.2
        
    elif player_rect.right >= WINDOW_WIDTH :
        player_rect.left -= 0.8
    display_surface.blit(player_surf, player_rect)



    py.display.update()        





py.quit()