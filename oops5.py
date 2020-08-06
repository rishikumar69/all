class Electronic_device:
    speaker = 1
    bluetooth = 1
    reciver = 1
    body = 1
    programe = 1
    button = 1



class Pocket_device(Electronic_device):
    screen = 1
    speaker = 2
    programe = 3
    button = 2


class Phone(Pocket_device):
    screen = 2
    programe = 100
    button = 3
    bluetooth = 3
    reciver = 3

phone = Phone

print(phone.screen)


