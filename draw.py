import pygame


pygame.init()
# all colour
black = [0, 0, 0]
white = [255, 255, 255]

# clock//
clock = pygame.time.Clock()

# main game variables //

size = 2
plot_x = 100
plot_y = 100
screen_width = 600
screen_height = 600
init_x = 100
init_y = 100
fps = 60
body_x_velocity = 2
body_y_velocity = 2

def plot_body(window, colour, list, size):

    for x, y in list:
        pygame.draw.rect(window, colour, [x, y, size, size])


body2 = []

window = pygame.display.set_mode((screen_width, screen_height))
exit_game = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                plot_x += 2
                body_x_velocity = 2
                body_y_velocity = 0


            if event.key == pygame.K_LEFT:
                plot_x -= 2
                body_x_velocity = -2
                body_y_velocity = 0

            if event.key == pygame.K_UP:
                plot_y -= 2
                body_y_velocity = -1
                body_x_velocity = 0

            if event.key == pygame.K_DOWN:
                plot_y += 2
                body_y_velocity = 2
                body_x_velocity = 0



    plot_x += body_x_velocity
    plot_y += body_y_velocity
    body = []
    body.append(plot_x)
    body.append(plot_y)
    # body.append(size)
    # body.append(size)
    body2.append(body)
    window.fill(white)
    plot_body(window, black, body2, size)
    pygame.display.update()
    clock.tick(fps)