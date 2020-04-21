from random import randint


# Create class Fish
class Fish:
    # Define main parameters
    x = [44]
    y = [44]
    step = 11
    length = 0
    updateCountMax = 2
    updateCount = 0

    # Define Fish Size
    def __init__(self, length):
        self.length = length
        for i in range(0, 280):
            self.x.append(-10000)
            self.y.append(-10000)

    # Define Fish Move
    def update(self):
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
            self.x[0] = self.x[0] + self.step
            if self.x[0] > 836:
                self.x[0] = 22
                self.y[0] = randint(2, 12) * 44

    # Show Fish
    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))
