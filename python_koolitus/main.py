import pygame
from snake import Snake
from tree import Tree
import random

class Game:
    def __init__(self):
        pygame.init()
        self.state = "game"
        self.end_counter = 0
        self.window_size = (640, 480)
        self.window = pygame.display.set_mode(self.window_size)
        self.end_surface = pygame.Surface(self.window_size)
        self.background = pygame.image.load("background.jpg")
        self.clock = pygame.time.Clock()
        self.running = True
        self.apple = None
        self.snake = Snake(120, 120, self)
        self.trees = [
                        Tree((320, 480), (0, -1), 50),
                        Tree((0, 240), (1, 0), 50),
                        Tree((320, 0), (0, 1), 50),
                        Tree((640, 240), (-1, 0), 50)
                     ]
        self.grow_apple()
        self.GAME_TIMER = 6
        self.counter = 0
        self.game_timerincreaserxdlmaoerino = 5
        self.y_xd = 5
        self.y = 480


    def event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = "end"
                elif event.key == pygame.K_RIGHT and self.snake.dir != (-1, 0):
                    self.snake.dir = (1, 0)
                elif event.key == pygame.K_LEFT and self.snake.dir != (1, 0):
                    self.snake.dir = (-1, 0)
                elif event.key == pygame.K_DOWN and self.snake.dir != (0, -1):
                    self.snake.dir = (0, 1)
                elif event.key == pygame.K_UP and self.snake.dir != (0, 1):
                    self.snake.dir = (0, -1)

    def update(self):
        self.window.blit(self.background, (0, -self.y + self.y_xd))
        self.snake.update()
        if self.state == "end":
            self.end_counter += 10
            if self.end_counter >= 200:
                self.running = False

    def render(self):
        self.window.blit(self.background, (0, 0))
        self.snake.render(self.window)
        [tree.render(self.window) for tree in self.trees]

        if self.state == "end":
            self.end_surface.set_alpha(self.end_counter)
            self.window.blit(self.end_surface, (0, 0))

        pygame.display.update()

    def run(self):
        pygame.mixer.music.load("coconut.mp3")
        pygame.mixer.music.play(-1)
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(self.GAME_TIMER)

    def grow_apple(self):
        self.apple = random.choice(self.trees).grow()
        self.snake.apple = self.apple

    def increase_timer(self):
        self.counter += 1
        if self.counter >= self.game_timerincreaserxdlmaoerino:
            self.GAME_TIMER += 1
            self.game_timerincreaserxdlmaoerino += 5

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
