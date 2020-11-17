import pygame
from settings import *
import random

class snake:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.screen.fill(BACKGROUNG_COLOR)
        self.clock = pygame.time.Clock()
        self.game = True
        self.mapping = []
        for i in range(START_X, DISPLAY_SIZE[0], BLOCK_SIZE + MARGIN):
            self.mapping.append([])
            for j in range(START_Y, DISPLAY_SIZE[1], BLOCK_SIZE + MARGIN):
                self.mapping[-1].append(pygame.Rect((i, j, BLOCK_SIZE, BLOCK_SIZE)))
        self.snake_map = [[0 for i in range(len(self.mapping[0]))] for j in range(len(self.mapping))]
        self.snake = []
        for i in range(3):
            self.snake_map[len(self.mapping)//2][len(self.mapping[0])//2 + i] = 1
            self.snake.append((len(self.mapping)//2, len(self.mapping[0])//2 + i))
        self.naprav = "W"
        self.eat = (len(self.mapping)//2, len(self.mapping[0])//2)

    def map(self):
        for _id1, i in enumerate(self.mapping):
            for _id2, j in enumerate(i):
                pygame.draw.rect(self.screen, COLOR[self.snake_map[_id1][_id2]], j)

    def muv_snake(self):
        start = 0
        end = self.snake.pop()
        if self.naprav == "W":
            start = (self.snake[0][0], self.snake[0][1] - 1)
        elif self.naprav == "A":
            start = (self.snake[0][0] - 1, self.snake[0][1])
        elif self.naprav == "D":
            start = (self.snake[0][0] + 1, self.snake[0][1])
        elif self.naprav == "S":
            start = (self.snake[0][0], self.snake[0][1] + 1)

        #проверка врезалась ли змея в себя
        if start not in self.snake:
            self.snake.insert(0, start)
        else:
            pygame.quit()
            self.game = False

        #проверка взяла ли змея еду
        if start == self.eat:
            self.snake.append(end)
        else:
            self.snake_map[end[0]][end[1]] = 0

        #проверка не вышла ли змея за поле
        if start[0] < 0 or start[1] < 0:
            pygame.quit()
            self.game = False

        self.snake_map[start[0]][start[1]] = 1

    def spawn_eat(self):
        while self.eat in self.snake:
            self.eat = (random.randint(0, len(self.snake_map) - 1), random.randint(0, len(self.snake_map[0]) - 1))
        self.snake_map[self.eat[0]][self.eat[1]] = 2

    def main(self):
        while self.game:
            self.clock.tick(SNAKE_SPEED)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if self.naprav != "S":
                            self.naprav = "W"
                    elif event.key == pygame.K_a:
                        if self.naprav != "D":
                            self.naprav = "A"
                    elif event.key == pygame.K_s:
                        if self.naprav != "W":
                            self.naprav = "S"
                    elif event.key == pygame.K_d:
                        if self.naprav != "A":
                            self.naprav = "D"
                    break
            self.spawn_eat()
            self.muv_snake()
            self.map()
            pygame.display.update()