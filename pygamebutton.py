import pygame
# import sys
#
pygame.init()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)
window = pygame.display.set_mode((500, 500))
red = [150, 0, 0]
bright_red = [255, 0, 0]
black = [0, 0, 0]
white = [255, 255, 255]
window_col = white

exit_game = False

# def scr_write(text, colour, x, y):
#     screen_txt = font.render(text, True, colour)
#     window.blit(screen_txt, [x, y])
#
#
# def game_intro():
#     exit_game = False
#     white = [255, 255, 255]
#     red = [150, 0, 0]
#     bright_red = [255, 0, 0]
#
#     while not exit_game:
#         window = pygame.display.set_mode((500, 500))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit_game = True
#
#         mouse = pygame.mouse.get_pos()
#
#         # print(mouse)
#         window.fill(white)
#         if 200 > mouse[0] > 100 and 130 > mouse[1] > 100:
#             pygame.draw.rect(window, bright_red, [100, 100, 100, 30])
#             scr_write("Start", [0, 0, 0], 120, 105)
#             # pygame.display.update()
#         else:
#             pygame.draw.rect(window, red, [100, 100, 100, 30])
#             scr_write("Start", [0, 0, 0], 120, 105)
#
#         # pygame.draw.rect(window, red, [100, 100, 100, 30])
#         pygame.display.update()
#         # print(event)
#         clock.tick(15)


def button(surface, msg, x, y, w, h, ic, ac, font_size, font_col):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        mouse = pygame.mouse.get_pos()

        font9 = pygame.font.SysFont(None, font_size)

        if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h:
            pygame.draw.rect(window, ac, [x, y, w, h])
        else:
            pygame.draw.rect(window, ic, [x, y, w, h])

        screen_txt = font9.render(msg, True, font_col)
        window.blit(screen_txt, (x+(x*(3/100)), y+(y*(3/100))))
        pygame.display.update()


# # game_intro()
# # button(window, "GO!", 200, 420, 100, 30, red, white, 20, black)
# button(window, "Ok", 200, 200, 100, 30, red, white, 20, black)
# while not exit_game:
#     mouse = pygame.mouse.get_pos()
#     for ev in pygame.event.get():
#         if ev.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#
#             if button
