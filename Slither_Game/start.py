import os
import pygame
from game import App

# Position of game screen
x_pos = 300
y_pos = 120
cmd = 'wmic desktopmonitor get screenheight, screenwidth'
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_pos, y_pos)


# Create class to show Start Window
class Initial:
    # Screen size
    windowWidth = 880
    windowHeight = 616
    # Init App() -Class
    App = App()

    # Define Start Window
    def game_intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # Start Game file in new window
                    if event.key == pygame.K_SPACE:
                        os.system("python game.py")
                        pygame.quit()
                        quit()
                    # Call Help Window
                    if event.key == pygame.K_h:
                        os.system("python Help_win.py")
                        pygame.quit()
                        quit()
                    # Quit Game
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pygame.display.set_caption('Snake game')
            # Set size of window
            self.App._display_surf = pygame.display.set_mode((self.App.windowWidth, self.App.windowHeight))
            # Load Background Image
            self.App._background_surf = pygame.image.load("start_font.jpg")
            # Set Background Image
            self.App.display_surf.blit(self.App.background_surf, (0, 0))
            # Show text on Display
            self.App.message_to_screen("It`s Slither Game", (43, 88, 12), -160, "large")
            self.App.message_to_screen("The objective of the game is to eat red apples", (0, 0, 0), -70)
            self.App.message_to_screen("The more apples you eat, the longer you get", (0, 0, 0), -30)
            self.App.message_to_screen("If you run into yourself, or the edges, you die!", (0, 0, 0), 10)
            self.App.message_to_screen("Beware of fish, it can eat you!", (0, 0, 0), 50)
            self.App.message_to_screen("Press 'Space' to play, H to Help,", (0, 0, 0), 110, "medium")
            self.App.message_to_screen("P to pause or Q to quit.", (0, 0, 0), 150, "medium")
            pygame.display.update()

# Initialise Start Window
if __name__ == "__main__":
    Start = Initial()
    Start.game_intro()