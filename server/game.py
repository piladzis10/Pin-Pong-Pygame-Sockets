class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        

    class Player:
        def __init__(self, x, y, p):
            self.x = x
            self.y = y
            self.width = 100
            self.height = 15
            self.vel = 5
            self.p = p
            self.looser = None
            self.ready = False



    class Ball():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.velX = 2
            self.velY = 2
            self.radius = 7

        def move(self, p1, p2):
            if self.x >= 500 or self.x <= 0:
                self.velX *= -1
            if self.y >= 500 or self.y <= 0:
                self.velY *= -1

            if (p1.x <= self.x <= p1.x + p1.width) and self.y >= p1.y: 
                self.velY *= -1
                #self.y = p1.y - self.radius

            if (p2.x <= self.x <= p2.x + p2.width) and self.y <= p2.y + p2.height: 
                self.velY *= -1
                #self.y = self.y + p2.height + self.radius

            self.x += self.velX
            self.y -= self.velY

            if p1.y + self.velY + 10  < self.y:
                p1.looser = True

            if p2.y + p2.height - self.velY - 10  > self.y:
                p2.looser = True








