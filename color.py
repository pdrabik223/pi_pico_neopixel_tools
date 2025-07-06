
class Color:
    r = 0
    g = 0
    b = 0

    def __init__(self, r: float, g: float, b: float):
        assert 0 <= r <= 255
        assert 0 <= g <= 255
        assert 0 <= b <= 255

        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def __str__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def to_tuple(self):
        return (self.r, self.g, self.b)

    @staticmethod
    def red():
        return Color(255, 0, 0)

    @staticmethod
    def orange():
        return Color(255, 50, 0)

    @staticmethod
    def yellow():
        return Color(255, 100, 0)

    @staticmethod
    def green():
        return Color(0, 255, 0)

    @staticmethod
    def blue():
        return Color(0, 0, 255)

    @staticmethod
    def indigo():
        return Color(100, 0, 90)

    @staticmethod
    def pink():
        return Color(200, 0, 100)

    @staticmethod
    def violet():
        return Color(50, 0, 100)

    @staticmethod
    def white():
        return Color(200, 255, 200)

    @staticmethod
    def black():
        return Color(0, 0, 0)
