class GameObject(object):
    def __init__(self, x, y, w, h, image):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
