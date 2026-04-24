"""
Racer Game — Practice 10
- Player car moves left/right with arrow keys
- Enemy car scrolls down; collision ends game
- Coins randomly appear on the road; collect them by driving over
- Coin counter shown in top-right corner
"""
import pygame
import sys
import random

# Window
WIDTH, HEIGHT = 400, 600
FPS = 60

# Colors
BLACK      = (0,   0,   0)
WHITE      = (255, 255, 255)
GRAY       = (80,  80,  80)
DARK_GRAY  = (50,  50,  50)
RED        = (200, 40,  40)
BLUE       = (40,  80,  220)
YELLOW     = (255, 210, 0)
GREEN      = (60,  180, 60)
ORANGE     = (255, 140, 0)

# Road layout
ROAD_LEFT  = 60
ROAD_RIGHT = 340
ROAD_WIDTH = ROAD_RIGHT - ROAD_LEFT

# Car dimensions
CAR_W, CAR_H = 50, 80


def draw_car(surface, color, x, y):
    """Draw a simple car rectangle with windows and wheels."""
    # Body
    pygame.draw.rect(surface, color, (x, y, CAR_W, CAR_H), border_radius=8)
    # Windshield
    pygame.draw.rect(surface, (180, 220, 255), (x + 8, y + 10, CAR_W - 16, 20), border_radius=4)
    # Rear window
    pygame.draw.rect(surface, (180, 220, 255), (x + 8, y + CAR_H - 30, CAR_W - 16, 16), border_radius=4)
    # Wheels
    wc = BLACK
    pygame.draw.rect(surface, wc, (x - 8,          y + 8,         10, 22), border_radius=3)
    pygame.draw.rect(surface, wc, (x + CAR_W - 2,  y + 8,         10, 22), border_radius=3)
    pygame.draw.rect(surface, wc, (x - 8,          y + CAR_H - 30, 10, 22), border_radius=3)
    pygame.draw.rect(surface, wc, (x + CAR_W - 2,  y + CAR_H - 30, 10, 22), border_radius=3)


class Coin:
    RADIUS = 14

    def __init__(self, speed):
        lane_centers = [ROAD_LEFT + 30, WIDTH // 2 - 5, ROAD_RIGHT - 35]
        self.x = random.choice(lane_centers)
        self.y = -self.RADIUS * 2
        self.speed = speed

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (self.x, int(self.y)), self.RADIUS)
        pygame.draw.circle(surface, ORANGE, (self.x, int(self.y)), self.RADIUS, 3)
        # $ symbol
        font = pygame.font.SysFont("Arial", 16, bold=True)
        sym = font.render("$", True, BLACK)
        surface.blit(sym, (self.x - sym.get_width() // 2, int(self.y) - sym.get_height() // 2))

    def is_off_screen(self):
        return self.y > HEIGHT + self.RADIUS * 2

    def collides_with_player(self, px, py):
        return (abs(self.x - (px + CAR_W // 2)) < CAR_W // 2 + self.RADIUS and
                abs(self.y - (py + CAR_H // 2)) < CAR_H // 2 + self.RADIUS)


class Game:
    COIN_SPAWN_INTERVAL = 90  # frames between coin spawns

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Racer")
        self.clock = pygame.time.Clock()

        self.font_large = pygame.font.SysFont("Arial", 42, bold=True)
        self.font_med   = pygame.font.SysFont("Arial", 26, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 20)

        self.reset()

    def reset(self):
        # Player car
        self.player_x = WIDTH // 2 - CAR_W // 2
        self.player_y = HEIGHT - CAR_H - 20
        self.player_speed = 5

        # Enemy car
        self.enemy_x = random.randint(ROAD_LEFT + 5, ROAD_RIGHT - CAR_W - 5)
        self.enemy_y = -CAR_H - 20
        self.enemy_speed = 4

        # Road scroll
        self.road_offset = 0
        self.road_speed  = 5

        # Coins
        self.coins = []
        self.coin_timer = 0
        self.coins_collected = 0

        self.score = 0
        self.running = True

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x = max(ROAD_LEFT + 5, self.player_x - self.player_speed)
        if keys[pygame.K_RIGHT]:
            self.player_x = min(ROAD_RIGHT - CAR_W - 5, self.player_x + self.player_speed)

    def update(self):
        if not self.running:
            return

        # Score
        self.score += 1

        # Scroll road markings
        self.road_offset = (self.road_offset + self.road_speed) % 60

        # Enemy
        self.enemy_y += self.enemy_speed
        if self.enemy_y > HEIGHT + CAR_H:
            self.enemy_x = random.randint(ROAD_LEFT + 5, ROAD_RIGHT - CAR_W - 5)
            self.enemy_y = -CAR_H - 20
            self.enemy_speed = min(12, self.enemy_speed + 0.3)

        # Collision with enemy
        px, py = self.player_x, self.player_y
        ex, ey = self.enemy_x, self.enemy_y
        if (px < ex + CAR_W and px + CAR_W > ex and
                py < ey + CAR_H and py + CAR_H > ey):
            self.running = False

        # Coins
        self.coin_timer += 1
        if self.coin_timer >= self.COIN_SPAWN_INTERVAL:
            self.coin_timer = 0
            self.coins.append(Coin(self.road_speed))

        for coin in self.coins[:]:
            coin.update()
            if coin.is_off_screen():
                self.coins.remove(coin)
            elif coin.collides_with_player(px, py):
                self.coins_collected += 1
                self.coins.remove(coin)

    def draw_road(self):
        # Road background
        pygame.draw.rect(self.screen, DARK_GRAY, (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

        # Center dashes
        dash_x = WIDTH // 2 - 3
        for y in range(-60 + self.road_offset, HEIGHT + 60, 60):
            pygame.draw.rect(self.screen, WHITE, (dash_x, y, 6, 40))

        # Road edges
        pygame.draw.rect(self.screen, WHITE, (ROAD_LEFT, 0, 6, HEIGHT))
        pygame.draw.rect(self.screen, WHITE, (ROAD_RIGHT - 6, 0, 6, HEIGHT))

    def draw_hud(self):
        # Score
        score_surf = self.font_small.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surf, (10, 10))

        # Coin counter — top right
        coin_surf = self.font_med.render(f"Coins: {self.coins_collected}", True, YELLOW)
        self.screen.blit(coin_surf, (WIDTH - coin_surf.get_width() - 10, 10))

    def draw(self):
        self.screen.fill(GREEN)  # Grass
        self.draw_road()

        for coin in self.coins:
            coin.draw(self.screen)

        draw_car(self.screen, BLUE, self.player_x, self.player_y)
        draw_car(self.screen, RED,  self.enemy_x,  self.enemy_y)

        self.draw_hud()
        pygame.display.flip()

    def game_over_screen(self):
        self.screen.fill(BLACK)
        over  = self.font_large.render("GAME OVER", True, RED)
        score = self.font_med.render(f"Score: {self.score}   Coins: {self.coins_collected}", True, WHITE)
        again = self.font_small.render("Press R to restart or Q to quit", True, GRAY)
        self.screen.blit(over,  (WIDTH // 2 - over.get_width()  // 2, 180))
        self.screen.blit(score, (WIDTH // 2 - score.get_width() // 2, 260))
        self.screen.blit(again, (WIDTH // 2 - again.get_width() // 2, 320))
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
                    if not self.running and event.key == pygame.K_r:
                        self.reset()

            if self.running:
                self.handle_input()
                self.update()
                self.draw()
            else:
                self.game_over_screen()

            self.clock.tick(FPS)


if __name__ == "__main__":
    Game().run()
