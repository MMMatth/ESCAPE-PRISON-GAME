# import
import sys
from typing import TextIO

import pygame
from datetime import datetime

clock = pygame.time.Clock()
from pygame.locals import *


# function


def dead(x1, x2, y1, y2):
    """
    x1 = coordinate x of the left of the zone death
    x2 = coordinate x of the right of the zone death
    y1 = coordinate y of the bottom of the zone death
    y2 = coordinate y of the top of the zone death
    I take with global the position of the player , the score and the map
    if the player is in the prison ( map , map2 and map3)
    i make a interval ale with y1 , y2 and x1 ,x2 ( i make a rectangle)
    i tp my player in the first room and i + 1 the score of death
    else (outdoor) i make the same but i tp just outdoor and i reload the map4
    """
    global player_rect, score, game_map
    if game_map == load_map('map') or game_map == load_map('map2') or game_map == load_map('map3'):
        if y1 < player_rect.y < y2 and x1 < player_rect.x < x2:
            player_rect = pygame.Rect(259, 455, 30, 57)
            score = score + 1
    else:
        if y1 < player_rect.y < y2 and x1 < player_rect.x < x2:
            player_rect = pygame.Rect(3142, 263, 30, 57)
            score = score + 1
            game_map = load_map("map4")


def load_map(path):
    """
    i def f for take the path on the file map
    i def data with the .read() of the txt file
    I split data
    i make loop and make a list with the map files
    and reture the map
    """
    f = open("MAP/" + path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):  # mouvement = x and  y of the player
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


global animation_frames
animation_frames = {}


def load_animation(path, frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        # player_animations/idle/idle_0.png
        animation_image = pygame.image.load(img_loc).convert_alpha()
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data


def change_action(action_var, frame, new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame


def save_score():
    """
    i take with global the score and the time passed
    I str the time /0.001 and the score
    I take the hours, the days , the years with a biblio
    And i print in the text file all
    """
    global passed_time, score, timer_started, timer_text, score_text, dead_img, win_img
    passed_time_str = str(int(passed_time) * 0.001)
    score_str = str(score)
    date_str = str(datetime.now())
    score_txt.write(
        "\n" + "vous êtes mort " + score_str + " fois et vous avez fait cela en " + passed_time_str + " secondes. L'heure est: " + date_str)
    whileplay = True
    while whileplay:
        screen.blit(win_img, (-5, -5))
        timer_started = not timer_started  # we stop the timerp
        screen.blit(pygame.transform.scale(score_text, (50, 95)),(280 , 360))
        screen.blit(pygame.transform.scale(timer_text, (180, 95)),(280 , 270))
        screen.blit(pygame.transform.scale(dead_img, (70, 85)),(350 , 360))
        pygame.display.flip()
        for events in pygame.event.get():
            if events.type == QUIT:
                whileplay = False


# ----main---- #
datetime.now()
pygame.init()  # initiates pygame
pygame.display.set_caption('Escape prison')


# ----other variable---- #
WINDOW_SIZE = (1280, 700)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window
display = pygame.Surface((630, 300))  # used as the surface for rendering, which is scaled
moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0
true_scroll = [0, 0]
font = pygame.font.Font("Font.ttf", 40)  # we def font
score = 0
game_map = load_map('map')
dead_img = pygame.image.load("IMG/dead.png").convert_alpha()
back = pygame.image.load("IMG/background.png")
# ----timer---- #
passed_time = 0
timer_started = False
start_time = pygame.time.get_ticks()
timer_started = not timer_started
# ----animation and player---- #
animation_database = {}
animation_database['run'] = load_animation('player_animations/run', [7, 7])
animation_database['idle'] = load_animation('player_animations/idle', [7, 7, 40])
player_action = 'idle'
player_frame = 0
player_flip: bool = True
player_rect = pygame.Rect(259, 455, 30, 57)

# ----finish screen---- #
win_img = pygame.image.load("IMG/finish screen/win.jpg")
win_img = pygame.transform.scale(win_img, (1300, 720))
# ----block---- #
coble_img = pygame.image.load('IMG/coble1.png')
coble2_img = pygame.image.load('IMG/coble2.png')
table_img = pygame.image.load("IMG/table.png")
trap_img = pygame.image.load("IMG/trap.png")
lava = pygame.image.load("IMG/lava.png")
iron_door_top = pygame.image.load("IMG/iron_door_top.png")
iron_door_down = pygame.image.load("IMG/iron_door_down.png")
glasses = pygame.image.load("IMG/glasses.png")
wood_door_top = pygame.image.load("IMG/door_top.png")
wood_door_down = pygame.image.load("IMG/door_down.png")
nothing_img = pygame.image.load("IMG/invisible.png")
grass = pygame.image.load('IMG/grass.png')
grass2 = pygame.image.load('IMG/grass2.png')
torch_off = pygame.image.load("IMG/torch_off.png")
torch_on = pygame.image.load("IMG/torch_on.png")

# ----the game loop---- #

play = True
while play:
    score_txt: TextIO = open("score_txt.txt", "a")  # open the score file
    true_scroll[0] += (player_rect.x - true_scroll[0] - 152) / 20
    true_scroll[1] += (player_rect.y - true_scroll[1] - 106) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    display.blit(back, (-96 - scroll[0], -80 - scroll[1]))
    # ----function dead ---- #
    dead(1150, 1544, 610, 630)  # 2 hole start
    dead(1824, 3106, 480, 490)  # big in the prison
    dead(3456, 5378, 320, 330)  # outdoor

    # ----collision block ---- #
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':  # if in the game the character is 1
                display.blit(coble2_img, (x * 32 - scroll[0], y * 32 - scroll[
                    1]))  # i blit the image and i reform in 32x32 and i soustract the scroll ( the auto camera)
            if tile == '2':
                display.blit(coble_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == '3':
                display.blit(glasses, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == '5':
                display.blit(table_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == '6':
                display.blit(trap_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == '7':
                display.blit(lava, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == '8':
                display.blit(iron_door_top, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == '9':
                display.blit(iron_door_down, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == 'a':
                display.blit(wood_door_top, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == 'b':
                display.blit(wood_door_down, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == 'c':
                display.blit(nothing_img, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == 'd':
                display.blit(grass, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == 'e':
                display.blit(grass2, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == 'f':
                display.blit(torch_off, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile == 'g':
                display.blit(torch_on, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * 32, y * 32, 32, 32))
            x += 1
        y += 1
    # affichage du score
    score_text = font.render(str(score), 1, (255, 255, 255))  # le score
    score_text_pos = score_text.get_rect()  # on crée le get_rect
    display.blit(score_text, (10, 0))
    display.blit(dead_img, (35, 6))

    # timer
    if timer_started:
        passed_time = pygame.time.get_ticks() - start_time
    timer_text = font.render(str(passed_time / 1000), True, (255, 255, 255))
    display.blit(timer_text, (500, 0))
    if 239990 < passed_time < 240010:
        timer_started = not timer_started  # we stop the timer
        save_score()
    # ----player move---- #
    player_movement = [0, 0]
    if moving_right == True:
        player_movement[0] += 3  # we def the rapidity of the player for the rigth
    if moving_left == True:
        player_movement[0] -= 2.5  # we def the rapidity of the player for the left
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3  # is the fallen speed
    if player_movement[0] == 0:
        player_action, player_frame = change_action(player_action, player_frame, 'idle')
    if player_movement[0] > 0:
        player_flip = False
        player_action, player_frame = change_action(player_action, player_frame, 'run')
    if player_movement[0] < 0:
        player_flip = True
        player_action, player_frame = change_action(player_action, player_frame, 'run')

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        air_timer = 0
        vertical_momentum = 0
    else:
        air_timer += 1
    # fix bug fly
    if collisions['top']:
        air_timer = 0
        vertical_momentum = 0

    player_frame += 1
    if player_frame >= len(animation_database[player_action]):
        player_frame = 0
    player_img_id = animation_database[player_action][player_frame]
    player_img = animation_frames[player_img_id]
    display.blit(pygame.transform.flip(player_img, player_flip, False),
                 (player_rect.x - scroll[0], player_rect.y - scroll[1]))

    # ----We def key---- #
    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    vertical_momentum = -6
            if event.key == K_a:
                player_rect = pygame.Rect(3168, 295, 30, 57)
                game_map = load_map("map4")
            if event.key == K_s:
                print(player_rect)


            if event.key == K_e:
                if 420 < player_rect.y < 460 and 60 < player_rect.x < 100:
                    game_map = load_map("map2")
                if 230 < player_rect.y < 270 and 980 < player_rect.x < 1100:
                    game_map = load_map("map3")
                    animation_database['run'] = load_animation('player_animations 2/run', [7, 7])
                    animation_database['idle'] = load_animation('player_animations 2/idle', [7, 7, 40])
                if 260 < player_rect.y < 270 and 3104 < player_rect.x < 3113:
                    game_map = load_map("map4")
                if 290 < player_rect.y < 300 and 6294 < player_rect.x < 6477:
                    save_score()
                    play = False

                # ----seconde map---- #

                if 190 < player_rect.y < 200 and 3333 < player_rect.x < 3483:
                    game_map = load_map("map5")
                if 130 < player_rect.y < 140 and 3600 < player_rect.x < 3723:
                    game_map = load_map("map6")
                if 100 < player_rect.y < 110 and 3913 < player_rect.x < 4048:
                    game_map = load_map("map4")
                if 130 < player_rect.y < 140 and 4242 < player_rect.x < 4365:
                    game_map = load_map("map5")
                if 165 < player_rect.y < 170 and 4528 < player_rect.x < 4665:
                    game_map = load_map("map6")
                if 100 < player_rect.y < 110 and 4789 < player_rect.x < 4912:
                    game_map = load_map("map4")
                if 65 < player_rect.y < 75 and 5035 < player_rect.x < 5176:
                    game_map = load_map("map5")
                if 100 < player_rect.y < 110 and 5370 < player_rect.x < 5484:
                    game_map = load_map("map6")

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
    score_txt.close()
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)
