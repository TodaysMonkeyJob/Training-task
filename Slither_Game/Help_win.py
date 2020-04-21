import os
import pygame
from HelpIcons import Icon

# Position of game screen
x_pos = 300
y_pos = 120
cmd = 'wmic desktopmonitor get screenheight, screenwidth'
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_pos, y_pos)

pygame.init()

# Create class to show Help Window
class Hint:
    windowWidth = 880
    windowHeight = 616

    # Init all require Parameters
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._background_surf = None
        self._W_surf = None
        self._A_surf = None
        self._S_surf = None
        self._D_surf = None
        self._P_surf = None
        self._Q_surf = None
        self._Esc_surf = None
        self._UP_surf = None
        self._LEFT_surf = None
        self._DOWN_surf = None
        self._RIGHT_surf = None
        self._SPACE_surf = None
        self._apple_surf = None
        self._orange_surf = None
        self._fish_surf = None
        self.W = Icon(5, 4)
        self.A = Icon(5, 7)
        self.S = Icon(5, 10)
        self.D = Icon(5, 13)
        self.P = Icon(2, 16)
        self.Q = Icon(2, 19)
        self.Esc = Icon(5, 19)
        self.UP = Icon(2, 4)
        self.LEFT = Icon(2, 7)
        self.DOWN = Icon(2, 10)
        self.RIGHT = Icon(2, 13)
        self.SPACE = Icon(2, 22)
        self.apple = Icon(20, 4)
        self.orange = Icon(20, 10)
        self.fish = Icon(20, 16)

    # Load All Photos to Show
    def on_init(self):
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self._background_surf = pygame.image.load("start_font.jpg")
        self._running = True
        pygame.display.set_caption('Snake game')
        self._W_surf = pygame.image.load("W.png").convert()
        self._A_surf = pygame.image.load("A.png").convert()
        self._S_surf = pygame.image.load("S.png").convert()
        self._D_surf = pygame.image.load("D.png").convert()
        self._P_surf = pygame.image.load("P.png").convert()
        self._Q_surf = pygame.image.load("Q.png").convert()
        self._Esc_surf = pygame.image.load("Esc.png").convert()
        self._UP_surf = pygame.image.load("UP.png").convert()
        self._LEFT_surf = pygame.image.load("LEFT.png").convert()
        self._DOWN_surf = pygame.image.load("DOWN.png").convert()
        self._RIGHT_surf = pygame.image.load("RIGHT.png").convert()
        self._SPACE_surf = pygame.image.load("SPACE.png").convert()

        self._apple_surf = pygame.image.load("icon_apple.png").convert()
        self._orange_surf = pygame.image.load("icon_orange.jpg").convert()
        self._fish_surf = pygame.image.load("icon_fish.png").convert()

    # Define size and type of Text
    @staticmethod
    def text_objects(text, colour, size="medium"):
        global text_surface
        font_name = pygame.font.match_font('arial')
        small_font = pygame.font.SysFont(font_name, 35)
        med_font = pygame.font.SysFont(font_name, 45)
        large_font = pygame.font.SysFont(font_name, 95)
        if size == "small":
            text_surface = small_font.render(text, True, colour)
        if size == "medium":
            text_surface = med_font.render(text, True, colour)
        if size == "large":
            text_surface = large_font.render(text, True, colour)
        return text_surface, text_surface.get_rect()

    # Set Position of text
    def message_to_screen(self, msg, colour, x_displace=0, y_displace=0, size="medium"):
        text_surface, text_rectangle = self.text_objects(msg, colour, size)
        text_rectangle.center = (x_displace, int(self.windowHeight / 2) + y_displace)
        self._display_surf.blit(text_surface, text_rectangle)

    # Show All Loaded Photos
    def on_render(self):
        self._display_surf.blit(self._background_surf, (0, 0))
        self.W.draw(self._display_surf, self._W_surf)
        self.A.draw(self._display_surf, self._A_surf)
        self.S.draw(self._display_surf, self._S_surf)
        self.D.draw(self._display_surf, self._D_surf)
        self.P.draw(self._display_surf, self._P_surf)
        self.Q.draw(self._display_surf, self._Q_surf)
        self.Esc.draw(self._display_surf, self._Esc_surf)
        self.UP.draw(self._display_surf, self._UP_surf)
        self.LEFT.draw(self._display_surf, self._LEFT_surf)
        self.RIGHT.draw(self._display_surf, self._RIGHT_surf)
        self.DOWN.draw(self._display_surf, self._DOWN_surf)
        self.SPACE.draw(self._display_surf, self._SPACE_surf)
        self.orange.draw(self._display_surf, self._orange_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        self.fish.draw(self._display_surf, self._fish_surf)

        self.message_to_screen("Game Hint", (255, 255, 255), 440, -260, "large")
        self.message_to_screen("      - move UP                       - increase lenght by 1", (255, 255, 255), 470, -195)
        self.message_to_screen("- move LEFT", (255, 255, 255), 260, -130)
        self.message_to_screen("       - move DOWN                - increase lenght by 5", (255, 255, 255), 470, -65)
        self.message_to_screen("- move RIGHT", (255, 255, 255), 275, 0)
        self.message_to_screen(" - Pause in game                                  - will eat you", (255, 255, 255), 450, 70)
        self.message_to_screen("- Quit Game", (255, 255, 255), 270, 135)
        self.message_to_screen("- Move to main menu", (255, 255, 255), 385, 195)
        pygame.display.flip()

    # Main Loop
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        os.system("python start.py")
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_q or pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            self.on_render()

    @property
    def display_surf(self):
        return self._display_surf

    @property
    def background_surf(self):
        return self._background_surf

# Init Help Window
if __name__ == "__main__":
    Start = Hint()
    Start.on_execute()