# Create class Icon
class Icon:
    # Define main parameters
    x = 0
    y = 0
    step = 22

    # Define Icon position
    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    # Show Icon
    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))