import pygame
import random


pygame.init()
# all colours
white = [255, 255, 255]
red = [200, 0, 0]
black = [0, 0, 0]
blue = [0, 0, 255]
purple = [75, 0, 130]

exit_game = False
screen_w = 500
screen_h = 500
in_xpos = 250
in_ypos = 450
pygame.display.set_caption("SPACE")
after_xpos = 200
after_ypos = 400
clock = pygame.time.Clock()
fps = 20


def invaders(window, colour):
    chance = random.randint(1, 100)

    if chance == 33 or 33:
        x_pos = random.randint(50, 450)
    y_pos = 50
    pygame.draw.rect(window, colour, [x_pos, y_pos, 10, 10]) #main part
    pygame.draw.rect(window, colour, [x_pos+10, y_pos, 5, 5])
    pygame.draw.rect(window, colour, [x_pos-5, y_pos, 5, 5])
    pygame.draw.rect(window, colour, [x_pos+3, y_pos+10, 3, 10])
    pygame.draw.rect(window, [255, 0, 0], [x_pos+3, y_pos, 3, 8])
    pygame.display.update()
    return x_pos


def beam(window, colour, x_pos):

    for i in range(1, 23):
        pygame.draw.rect(window, colour, [x_pos+5, in_ypos-i*20, 1, 20])
        pygame.draw.rect(window, black, [x_pos+5, in_ypos-(i-1)*20, 1, 20])
        pygame.display.update()

        clock.tick(fps*2)

    return in_ypos


def space_ship(surface, colour, x_pos, y_pos):

    pygame.draw.rect(surface, colour, [x_pos, y_pos, 10, 10])
    pygame.draw.rect(surface, colour, [x_pos+10, y_pos+5, 5, 5])
    pygame.draw.rect(surface, colour, [x_pos-5, y_pos+5, 5, 5])
    pygame.draw.rect(surface, colour, [x_pos+3, y_pos-10, 3, 10])
    pygame.draw.rect(surface, white, [x_pos+3, y_pos+5, 3, 5])

    pygame.display.update()


while not exit_game:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                in_xpos += 10

            if event.key == pygame.K_LEFT:
                in_xpos -= 10

            if event.key == pygame.K_UP:
                in_ypos -= 10

            if event.key == pygame.K_DOWN:
                in_ypos += 10

            if event.key == pygame.K_SPACE:
                beam(window, white, in_xpos)
                pygame.display.update()

        if in_xpos <= 0:
            in_xpos = 5

        if in_xpos >= 500-15:
            in_xpos = 500-15

        if in_ypos >= 500:
            in_ypos = 500 - 10

        # if after_ypos >= 350:
        #     in_ypos = 340
    window = pygame.display.set_mode((screen_w, screen_h))
    for i in range(1, 10):
        x_point = random.randint(1, 500)
        y_point = random.randint(1, 500)
        pygame.draw.rect(window, white, [x_point, y_point, 1, 1])
    inva_chance = random.randint(0, 100)
    if inva_chance ==33:
        inva_xpos = random.randint(50, 450)

    space_ship(window, purple, in_xpos, in_ypos)
    # invaders(window, white, )
    pygame.display.update()
    clock.tick(fps)
