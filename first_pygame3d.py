from direct.showbase.ShowBase import ShowBase


class Myapp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)


app = Myapp()
app.run()

