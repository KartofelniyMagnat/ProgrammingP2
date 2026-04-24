"""
Racer Game - Practice 11

Coins have different weights. The enemy car becomes faster after each N
collected coin points.
"""
import random
import sys

import pygame

WIDTH, HEIGHT = 400, 600
FPS = 60
ROAD_LEFT, ROAD_RIGHT = 60, 340
CAR_W, CAR_H = 50, 80
SPEED_UP_EVERY = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (50, 50, 50)
RED = (200, 40, 40)
BLUE = (40, 80, 220)
GREEN = (60, 180, 60)
YELLOW = (255, 210, 0)
ORANGE = (255, 140, 0)
PURPLE = (165, 94, 234)


def draw_car(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, CAR_W, CAR_H), border_radius=8)
    pygame.draw.rect(surface, (180, 220, 255), (x + 8, y + 10, CAR_W - 16, 20), border_radius=4)
    pygame.draw.rect(surface, (180, 220, 255), (x + 8, y + CAR_H - 30, CAR_W - 16, 16), border_radius=4)
    for wheel_x in (x - 8, x + CAR_W - 2):
        pygame.draw.rect(surface, BLACK, (wheel_x, y + 8, 10, 22), border_radius=3)
        pygame.draw.rect(surface, BLACK, (wheel_x, y + CAR_H - 30, 10, 22), border_radius=3)


class Coin:
    OPTIONS = [(1, YELLOW, 13), (2, ORANGE, 15), (3, PURPLE, 17)]

    def __init__(self, speed):
        self.weight, self.color, self.radius = random.choice(self.OPTIONS)
        self.x = random.choice([ROAD_LEFT + 35, WIDTH // 2, ROAD_RIGHT - 35])
        self.y = -self.radius * 2
        self.speed = speed

    def update(self):
        self.y += self.speed

    def draw(self, surface, font):
        pygame.draw.circle(surface, self.color, (self.x, int(self.y)), self.radius)
        pygame.draw.circle(surface, WHITE, (self.x, int(self.y)), self.radius, 2)
        label = font.render(str(self.weight), True, BLACK)
        surface.blit(label, (self.x - label.get_width() // 2, int(self.y) - label.get_height() // 2))

    def collides(self, px, py):
        return (abs(self.x - (px + CAR_W // 2)) < CAR_W // 2 + self.radius and
                abs(self.y - (py + CAR_H // 2)) < CAR_H // 2 + self.radius)


class Racer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Practice 11 - Racer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 22, bold=True)
        self.big_font = pygame.font.SysFont("Arial", 40, bold=True)
        self.reset()

    def reset(self):
        self.player_x = WIDTH // 2 - CAR_W // 2
        self.player_y = HEIGHT - CAR_H - 20
        self.enemy_x = random.randint(ROAD_LEFT + 5, ROAD_RIGHT - CAR_W - 5)
        self.enemy_y = -CAR_H
        self.enemy_speed = 4
        self.player_speed = 5
        self.road_offset = 0
        self.coins = []
        self.coin_timer = 0
        self.coin_score = 0
        self.next_speed_goal = SPEED_UP_EVERY
        self.running = True

    def update(self):
        if not self.running:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x = max(ROAD_LEFT + 5, self.player_x - self.player_speed)
        if keys[pygame.K_RIGHT]:
            self.player_x = min(ROAD_RIGHT - CAR_W - 5, self.player_x + self.player_speed)

        self.road_offset = (self.road_offset + self.enemy_speed) % 60
        self.enemy_y += self.enemy_speed
        if self.enemy_y > HEIGHT + CAR_H:
            self.enemy_x = random.randint(ROAD_LEFT + 5, ROAD_RIGHT - CAR_W - 5)
            self.enemy_y = -CAR_H

        if (self.player_x < self.enemy_x + CAR_W and self.player_x + CAR_W > self.enemy_x and
                self.player_y < self.enemy_y + CAR_H and self.player_y + CAR_H > self.enemy_y):
            self.running = False

        self.coin_timer += 1
        if self.coin_timer >= 70:
            self.coin_timer = 0
            self.coins.append(Coin(self.enemy_speed))

        for coin in self.coins[:]:
            coin.update()
            if coin.y > HEIGHT + coin.radius:
                self.coins.remove(coin)
            elif coin.collides(self.player_x, self.player_y):
                self.coin_score += coin.weight
                self.coins.remove(coin)
                if self.coin_score >= self.next_speed_goal:
                    self.enemy_speed = min(14, self.enemy_speed + 1)
                    self.next_speed_goal += SPEED_UP_EVERY

    def draw_road(self):
        pygame.draw.rect(self.screen, DARK_GRAY, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT))
        for y in range(-60 + int(self.road_offset), HEIGHT + 60, 60):
            pygame.draw.rect(self.screen, WHITE, (WIDTH // 2 - 3, y, 6, 40))
        pygame.draw.rect(self.screen, WHITE, (ROAD_LEFT, 0, 6, HEIGHT))
        pygame.draw.rect(self.screen, WHITE, (ROAD_RIGHT - 6, 0, 6, HEIGHT))

    def draw(self):
        self.screen.fill(GREEN)
        self.draw_road()
        for coin in self.coins:
            coin.draw(self.screen, self.font)
        draw_car(self.screen, BLUE, self.player_x, self.player_y)
        draw_car(self.screen, RED, self.enemy_x, self.enemy_y)
        hud = self.font.render(f"Coins: {self.coin_score}  Speed: {self.enemy_speed}", True, WHITE)
        self.screen.blit(hud, (10, 10))

        if not self.running:
            text = self.big_font.render("GAME OVER", True, RED)
            hint = self.font.render("R - restart, Q - quit", True, WHITE)
            self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 230))
            self.screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 285))

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r and not self.running:
                        self.reset()

            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    Racer().run()
