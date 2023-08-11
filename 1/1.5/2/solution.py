class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(2 * i + 1, 2 * i + 1) for i in range(0, 1000)]
points[1].color = 'yellow'