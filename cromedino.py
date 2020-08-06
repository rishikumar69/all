import pyautogui
from PIL import ImageGrab  # pip install pillow
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def iscollide(data):
    # Draw the rectangle for cactus
    for i in range(500, 525):
        for j in range(203, 237):
            if data[i, j] < 100:
                hit("up")
                return

    # for i in range(300, 415):
    #     for j in range(563, 650):
    #         if data[i, j] < 100:
    #             hit("up")
    #             return

    for i in range(573, 630):
        for j in range(145, 190):
            if data[i, j] < 100:
                hit(" ")
                return

    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # iscollide(data)
        # q = input("Enter q to 'exit': ")
        # if q != 'q':
        #     continue
        #
        # else:
        #     quit()
        #     break
        # Draw the rectangle for cactus
        for i in range(500, 565):
            for j in range(203, 237):
                if data[i, j] < 100:
                    hit(" ")



        for i in range(500, 565):
            for j in range(203, 237):
                if data[i, j] < 100:
                    hit(" ")



        # # Draw the rectangle for birds
        # for i in range(573, 630):
        #     for j in range(145, 190):
        #         data[i, j] = 171
        #
        # image.show()
        # break
        # for i in range(573, 600):
        #     for j in range(155, 190):
        #         if data[i, j] = 0
        # image.show()
        # break
