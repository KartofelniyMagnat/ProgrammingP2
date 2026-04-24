"""
Snake Game - Practice 10

Controls: arrow keys change direction, R restarts after game over, Q quits.
The snake cannot cross walls or itself. Food is generated only on free cells.
Every three foods increase the level and the game speed.
"""
import random
import sys

import pygame

CELL = 20
COLS, ROWS = 30, 24
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL
FPS_BASE = 8

BLACK = (18, 18, 24)
WHITE = (245, 245, 245)
GREEN = (52, 168, 83)
DARK_GREEN = (29, 110, 55)
RED = (230, 72, 72)
GRAY = (60, 60, 70)


def random_free_cell(snake):
    """Return a random grid position that is not occupied by the snake."""
    occupied = set(snake)
    free = [(x, y) for x in range(COLS) for y in range(ROWS) if (x, y) not in occupied]
    return random.choice(free)


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Practice 10 - Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 18)
        self.reset()

    def reset(self):
        self.snake = [(COLS // 2, ROWS // 2), (COLS // 2 - 1, ROWS // 2), (COLS // 2 - 2, ROWS // 2)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food = random_free_cell(self.snake)
        self.score = 0
        self.level = 1
        self.game_over = False

    def handle_key(self, key):
        if key == pygame.K_q:
            pygame.quit()
            sys.exit()
        if self.game_over and key == pygame.K_r:
            self.reset()
            return

        directions = {
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),
        }
        if key in directions:
            new_direction = directions[key]
            if (new_direction[0] != -self.direction[0] or
                    new_direction[1] != -self.direction[1]):
                self.next_direction = new_direction

    def update(self):
        if self.game_over:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        hit_wall = not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS)
        hit_self = new_head in self.snake
        if hit_wall or hit_self:
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.level = self.score // 3 + 1
            self.food = random_free_cell(self.snake)
        else:
            self.snake.pop()

    def draw_grid(self):
        for x in range(0, WIDTH, CELL):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL):
            pygame.draw.line(self.screen, GRAY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()

        food_rect = pygame.Rect(self.food[0] * CELL, self.food[1] * CELL, CELL, CELL)
        pygame.draw.rect(self.screen, RED, food_rect.inflate(-4, -4), border_radius=6)

        for index, part in enumerate(self.snake):
            rect = pygame.Rect(part[0] * CELL, part[1] * CELL, CELL, CELL)
            color = GREEN if index == 0 else DARK_GREEN
            pygame.draw.rect(self.screen, color, rect.inflate(-2, -2), border_radius=5)

        hud = self.font.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        self.screen.blit(hud, (10, 8))

        if self.game_over:
            over = self.font.render("GAME OVER", True, RED)
            hint = self.small_font.render("R - restart, Q - quit", True, WHITE)
            self.screen.blit(over, (WIDTH // 2 - over.get_width() // 2, HEIGHT // 2 - 28))
            self.screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT // 2 + 8))

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)

            self.update()
            self.draw()
            self.clock.tick(FPS_BASE + self.level * 2)


if __name__ == "__main__":
    SnakeGame().run()
