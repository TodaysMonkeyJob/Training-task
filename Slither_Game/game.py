# Import all libraries and classes
import os
from random import randint

import pygame
from pygame.locals import *

from Collision import GameCheck
from Fish import Fish
from Fruit import Fruit
from Slither import Slither

# Position of game screen
x_pos = 300
y_pos = 120
cmd = 'wmic desktopmonitor get screenheight, screenwidth'
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_pos, y_pos)

pygame.init()
clock = pygame.time.Clock()

# Create Class with game mechanic
class App:
    windowWidth = 880
    windowHeight = 616

    # Init main parameters to work with
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._background_surf = None
        self._snake_easy_surf = None
        self._snake_normal_surf = None
        self._snake_hard_surf = None
        self._image_surf = None
        self._apple_surf = None
        self._orange_surf = None
        self._fish_surf = None
        self.game = GameCheck()
        self.slither = Slither(3)
        self.orange = Fruit(10, 5)
        self.apple = Fruit(10, 5)
        self.fish = Fish(1)
        self.FPS = 0
        self.score = 0

    # Load photos of all elements
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self._background_surf = pygame.image.load("background.jpg")

        pygame.display.set_caption('Snake game')
        self._running = True
        self._snake_easy_surf = pygame.image.load("body_easy.png").convert()
        self._snake_normal_surf = pygame.image.load("body_normal.png").convert()
        self._snake_hard_surf = pygame.image.load("body_hard.png").convert()
        self._image_surf = pygame.image.load("snake.png").convert()
        self._apple_surf = pygame.image.load("apple.png").convert()
        self._orange_surf = pygame.image.load("orange.jpg").convert()
        self._fish_surf = pygame.image.load("fish.png").convert()

    # staticmethod don`t require class commands
    @staticmethod
    # Define size and type of text
    def text_objects(text, colour, size="small"):
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

    # Set position of text on Screen
    def message_to_screen(self, msg, colour, y_displace=0, size="small"):
        text_surface, text_rectangle = self.text_objects(msg, colour, size)
        text_rectangle.center = (int(self.windowWidth / 2), int(self.windowHeight / 2) + y_displace)
        self._display_surf.blit(text_surface, text_rectangle)

    # Show Window When you Loose
    def after_game(self, way):
        after = True
        while after:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        os.system("python game.py")
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_m:
                        os.system("python start.py")
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pygame.display.set_caption('Snake game')
            self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
            self._background_surf = pygame.image.load("start_font.jpg")
            self._display_surf.blit(self._background_surf, (0, 0))
            if way == 1:
                self.message_to_screen("You hit the board", (43, 88, 12), -170, "large")
            elif way == 2:
                self.message_to_screen("You eat yourself", (43, 88, 12), -170, "large")
            else:
                self.message_to_screen("You was eaten by Fish", (43, 88, 12), -170, "large")
            self.message_to_screen('Your score: ' + str(self.score), (0, 0, 0), -100, "medium")
            # To show players score
            HiScore = 'Score.txt'
            with open(HiScore, 'r') as file:
                try:
                    high_score = str(file.read())
                except:
                    high_score = 0

            if self.score < int(high_score):
                self.message_to_screen('High Score: ' + str(high_score), (0, 0, 0), -50, "medium")
            else:
                high_score = self.score
                self.message_to_screen('New High Score: ' + str(high_score), (0, 0, 0), -50, "medium")
                with open(HiScore, 'w') as file:
                    file.write(str(self.score))
            self.message_to_screen("Can you beat your score?", (0, 0, 0), 0)
            self.message_to_screen("It`s time to show your best!", (0, 0, 0), 40)
            self.message_to_screen("Go to main Menu: Press M", (0, 0, 0), 100)
            self.message_to_screen("Press 'Space' to Start again or Q to quit.", (0, 0, 0), 140)

            pygame.display.update()

    # Check if game is on loop
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    #
    def on_loop(self):
        self.slither.update()
        self.fish.update()

        # does snake eat apple?
        for i in range(0, self.slither.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.slither.x[i], self.slither.y[i], 30):
                self.apple.x = randint(2, 18) * 44
                self.apple.y = randint(2, 12) * 44
                self.slither.length += 1
                self.score += 1

        # does snake eat orange
        for i in range(0, self.slither.length):
            if self.game.isCollision(self.orange.x, self.orange.y, self.slither.x[i], self.slither.y[i], 30):
                self.orange.x = randint(2, 18) * 44
                self.orange.y = randint(2, 12) * 44
                self.slither.length += 5
                self.score += 5

        # does snake collide with fish?
        for i in range(0, self.slither.length - 5):
            if self.game.isCollision(self.fish.x[0], self.fish.y[0], self.slither.x[i], self.slither.y[i], 30):
                if self.fish.x[0] == self.slither.x[0]:
                    self.after_game(3)
                else:
                    for lenght in range(0, self.slither.x[i]):
                        self.slither.length = i

        # does snake collide with itself?
        if self.slither.length <= 5:
            for i in range(2, self.slither.length):
                if self.game.isCollision(self.slither.x[0], self.slither.y[0], self.slither.x[i], self.slither.y[i],30):
                    self.after_game(2)
        else:
            for i in range(2, self.slither.length - 5):
                if self.game.isCollision(self.slither.x[0], self.slither.y[0], self.slither.x[i], self.slither.y[i],30):
                    self.after_game(2)

        # does snake collide with board?
        if (0 > self.slither.x[0] or self.slither.x[0] > 836) or (0 > self.slither.y[0] or self.slither.y[0] > 572):
            self.after_game(1)
        pass

    # Define Pause in Game
    def pause(self):
        paused = True
        self.message_to_screen("Paused", (0, 0, 0), -100, size="large")
        self.message_to_screen("Press C to continue playing or Q to quit", (0, 0, 0), 25)
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

    # Draw Game Score
    def draw_score(self, surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        if text == '0':
            text = 0
        curr_score = int(text)

        HiScore = 'Score.txt'
        with open(HiScore, 'r') as file:
            try:
                high_score = str(file.read())
            except:
                high_score = 0
        frame = pygame.Rect(10, 8, 145, 46)
        pygame.draw.rect(self._display_surf, [0, 0, 0], frame, 3)
        text_surface = font.render('Current score: ' + str(curr_score), True, (0, 0, 0))
        surf = self._display_surf.blit(text_surface, (x, y))

        if self.score >= int(high_score):
            high_score = curr_score
            text_surface = font.render('New High score: ' + str(high_score), True, (0, 0, 0))
            surf = self._display_surf.blit(text_surface, (x, y + 20))
        else:
            text_surface = font.render('Last high score: ' + str(high_score), True, (0, 0, 0))
            surf = self._display_surf.blit(text_surface, (x, y + 20))

    # Show all Elements of Game
    def on_render(self):
        self._display_surf.blit(self._background_surf, (0, 0))
        # If Score become Higher Game Become Harder
        if 0 <= self.score < 150:
            self.slither.draw(self._display_surf, self._snake_easy_surf)
            self.FPS = 10
        elif 150 <= self.score < 300:
            self.slither.draw(self._display_surf, self._snake_normal_surf)
            self.FPS = 17
        else:
            self.slither.draw(self._display_surf, self._snake_hard_surf)
            self.FPS = 25
        self.orange.draw(self._display_surf, self._orange_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        self.fish.draw(self._display_surf, self._fish_surf)
        self.draw_score(self._display_surf, str(self.score), 18, 20, 10)
        pygame.display.flip()

    # Close all process
    def on_cleanup(self):
        pygame.quit()

    # Main Loop
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT] or keys[K_d]):
                self.slither.moveRight()

            if (keys[K_LEFT] or keys[K_a]):
                self.slither.moveLeft()

            if (keys[K_UP] or keys[K_w]):
                self.slither.moveUp()

            if (keys[K_DOWN] or keys[K_s]):
                self.slither.moveDown()

            if (keys[K_ESCAPE] or keys[K_q]):
                self._running = False

            if (keys[K_p]):
                self.pause()

            self.on_loop()
            self.on_render()

            clock.tick(self.FPS)
        self.on_cleanup()

    # It`s just wishes of Pycharm
    @property
    def display_surf(self):
        return self._display_surf

    @property
    def background_surf(self):
        return self._background_surf


# Init Game
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
