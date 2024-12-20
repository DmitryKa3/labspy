import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, i, j):
        self.x += i
        self.y += j

    def dist(self, self2):
        distanse = math.sqrt((self.x - self2.x)**2 + (self.y - self2.y)**2)
        return distanse


point1 = Point(3,4)
point2 = Point(1,9)

print("Первые корды:", point1.show())
point1.move(2,2)
print("Добавляем по два:",point1.show())
distance = point1.dist(point2)
print("Дистанция:", distance)
