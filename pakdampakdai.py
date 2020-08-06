import pygame
from pygamebutton import *
import pygame_gui
from pygame import mixer


pygame.init()

font = pygame.font.SysFont(None, 35)
font2 = pygame.font.SysFont(None, 50)

mixer.init


def play_music(filename):
    for i in range(1, 2):
        mixer.music.load(filename)
        mixer.music.set_volume(1)
        mixer.music.play()


def game_loop():
    # all colours
    white = [255, 255, 255]
    black = [0, 0, 0]
    red = [255, 0, 0]

    manager = pygame_gui.UIManager((500, 500))

    screen_width = 500
    screen_height = 500
    pos_x = 50
    pos_y = 70
    finder_x = 250
    finder_y = 200
    finder_size = 10
    rect_size = 10
    game_over = False
    fps = 100
    score = 0
    score2 = 0
    speed = 0.001
    clock = pygame.time.Clock()
    pygame.display.set_caption("PAKDAM PAKDAI")
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_icon(window)
    finder_range = 1



    def scr_write(text, colour, x, y):
        screen_txt = font.render(text, True, colour)
        window.blit(screen_txt, [x, y])

    while not game_over:
        window.fill(white)
        finder = pygame.draw.rect(window, black, [abs(finder_x), abs(finder_y), finder_size, finder_size])
        catcher = pygame.draw.rect(window, red, [pos_x, pos_y, rect_size, rect_size])

        for event in pygame.event.get():
            # to Quite
            if event.type == pygame.QUIT:
                game_over = True
                exit()
                break
            # key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pos_x += 20

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pos_x -= 20

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pos_y -= 20

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pos_y += 20

            # game boundries
            if pos_x <= 0:
                play_music("bump.mp3")
                pos_x = 0

            if pos_x >= screen_width:
                play_music("bump.mp3")
                pos_x = screen_width - rect_size

            if pos_y <= 0:
                play_music("bump.mp3")
                pos_y = 0

            if pos_y >= screen_height:
                play_music("bump.mp3")
                pos_y = screen_height - rect_size

        # catching player
        if pos_x < finder_x:
            finder_x -= finder_range+speed

        if pos_x > finder_x:
            finder_x += finder_range+speed

        if pos_y < finder_y:
            finder_y -= finder_range+speed

        if pos_y > finder_y:
            finder_y += finder_range+speed

        # player got caught
        if finder == catcher:
            play_music("gameover.mp3")
            # score = 0
            scr_write("GAME OVER", red, 300, 300)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()
                        pygame.display.update()

                if event.type == pygame.QUIT:
                    game_over = True



            pos_x = 50
            pos_y = 70
            finder_x = 200
            finder_y = 200

            pygame.display.update()

        score += 1
        if score % 20 == 0:
            score2 += 1
        scr_write(f"Score:{abs(score2)}", red, 10, 10)
        if score2 >= 100 and score2 % 100 == 1 :
            play_music("bonus.mp3")

        pygame.display.update()
        clock.tick(fps)


green = [0, 200, 0]
green_light = [0, 255, 0]
yellow = [255, 255, 0]


def main_menu():
    manager = pygame_gui.UIManager((500, 500))
    button1 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((160, 400), (200, 60)),
        text="Start",
        manager=manager
        )
    i = 0
    while True:

        time_delta = clock.tick(60) / 1000.0
        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("PAKDAM PAKDAI")
        window.fill([255, 255, 255])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button1:
                        game_loop()


        manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.draw.rect(window, black, [250, 200, 10, 10])
        pygame.draw.rect(window, red, [50, 70, 10, 10])
        pygame.display.update()


main_menu()

