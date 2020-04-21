# Create class Fruit
class Fruit:
    # Define main parameters
    x = 0
    y = 0
    step = 44

    # Define position of Fruit
    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    # Show Fruit
    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))
