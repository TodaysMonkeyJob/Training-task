# Create call Slither
class Slither:
    # Define Slither Parameters
    x = [220]
    y = [308]
    step = 44
    length = 0
    direction = 0
    updateCountMax = 2
    updateCount = 0

    # Define Slither Length in game
    def __init__(self, length):
        self.length = length
        for i in range(0, 280):
            self.x.append(-10000)
            self.y.append(-10000)

        # initial positions, no collision.
        self.x[1] = 1 * 44
        self.x[2] = 2 * 44

    # Define Slither Move
    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    # Check direction of Slither
    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    # Show Slither
    def draw(self, surface, image):
        if self.length <= 5:
            for i in range(0, self.length):
                surface.blit(image, (self.x[i], self.y[i]))
        else:
            for i in range(0, self.length - 5):
                surface.blit(image, (self.x[i], self.y[i]))
