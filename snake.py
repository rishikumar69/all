import pygame

pygame.init()

exit_game = False

screen_width = 500
screen_height = 500
screen_color = white = [255, 255, 255]
red = [255, 0, 0]
fps = 30

init_xpos = 0
init_ypos = 0
speed_x = 0
speed_y = 0
size = 10
velocity = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game Made By Rishi")
clock = pygame.time.Clock()
while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                init_xpos += velocity
                init_ypos = 0

            if event.key == pygame.K_LEFT:
                init_xpos -= velocity
                init_ypos = 0

            if event.key == pygame.K_UP:
                init_ypos -= velocity
                init_xpos = 0

            if event.key == pygame.K_DOWN:
                init_ypos += velocity
                init_xpos = 0

            if speed_x >= 490:
                speed_x = 15

            if speed_y >= screen_height:
                speed_y = speed_y


    speed_x += init_xpos
    speed_y += init_ypos
    screen.fill(screen_color)
    pygame.draw.rect(screen, red, [speed_x, speed_y, size, size])

    pygame.display.update()
    clock.tick(30)

exit()
