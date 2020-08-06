import pygame
import random
# import time


# starting game
pygame.init()

# defining screen width
screen_width = 600
screen_height = 500
window = pygame.display.set_mode((screen_width, screen_height))

# setting window title
pygame.display.set_caption("Snake")

# main game variable

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)
font2 = pygame.font.SysFont(None, 40)


def txt_scr(text, colour, x, y):
    screen_txt = font.render(text, True, colour)
    window.blit(screen_txt, [x, y])


def plot_snake(gamewindow, colour, snk_list, snk_size):
    for x, y in snk_list:
        pygame.draw.rect(window, colour, [x, y, snk_size, snk_size])

def gamehar(text, colour, x, y):
    screen_txt = font2.render(text, True, colour)
    window.blit(screen_txt, [x, y])
    exit_game = True
    game_over = True


def gameloop():
    snk_list = []
    snk_lenth = 1


    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    green = (0,255,0)
    exit_game = False
    game_over = False
    snake_x = 250
    snake_y = 240
    snake_size = 10
    x_velocity = 0
    y_velocity = 0
    food_x = random.randint(0, screen_width - 50)
    food_y = random.randint(0, screen_height - 50)
    food_size = snake_size
    score = 60
    fps = 50
    diff_to_collide = (80 / 100) * snake_size



    while not exit_game:



        if snake_x == screen_width-10 or snake_y == screen_height-10 or snake_x == 0 or snake_y == 0:
            screen_txt = font2.render("Game over!!! Press ENTER to Restart.", True, red)
            x_velocity = 0
            y_velocity = 0
            pygame.display.update()
            window.blit(screen_txt, [50, 190])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # print(event)
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        gameloop()
                        pygame.display.update()

        else:

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_x += 10
                        x_velocity = 5
                        y_velocity = 0

                    if event.key == pygame.K_LEFT:
                        snake_x -= 10
                        x_velocity = -5
                        y_velocity = 0

                    if event.key == pygame.K_UP:
                        snake_y -= 10
                        x_velocity = 0
                        y_velocity = -5

                    if event.key == pygame.K_DOWN:
                        snake_y += 10
                        x_velocity = 0
                        y_velocity = 5

                # self try


            snake_x = snake_x + x_velocity
            snake_y = snake_y + y_velocity
            if abs(snake_x - food_x) < diff_to_collide and abs(snake_y - food_y) < diff_to_collide:
                score += 10
                snk_lenth = snk_lenth + 3
                # print(f"score:{score}")
                food_x = random.randint(0, screen_width - 50)
                food_y = random.randint(0, screen_height - 50)





                # x_velocity = 0
                # y_velocity = 0
                # time.sleep(10)
                # exit()
                # quit()


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_lenth:
                del snk_list[0]

            if head in snk_list[:-1]:
                gamehar("Game Over", red, 100, 100)

            window.fill(green)
            pygame.draw.rect(window, red, [food_x, food_y, food_size, food_size])
            plot_snake(window, black, snk_list, snake_size)
            txt_scr(f"Score:{score}", black, 500, 10)
            pygame.display.update()
            clock.tick(fps)

gameloop()