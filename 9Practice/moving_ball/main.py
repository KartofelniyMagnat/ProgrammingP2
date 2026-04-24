"""
Moving Ball Game
Arrow keys move the red ball by 20 pixels.
Ball cannot leave the screen boundaries.
"""
import pygame
import sys

WIDTH, HEIGHT = 600, 600
RADIUS = 25
STEP = 20
FPS = 60

WHITE = (255, 255, 255)
RED   = (220, 50,  50)
GRAY  = (200, 200, 200)
BLACK = (0,   0,   0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    # Ball starts in the center
    ball_x = WIDTH  // 2
    ball_y = HEIGHT // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                new_x, new_y = ball_x, ball_y

                if event.key == pygame.K_UP:
                    new_y -= STEP
                elif event.key == pygame.K_DOWN:
                    new_y += STEP
                elif event.key == pygame.K_LEFT:
                    new_x -= STEP
                elif event.key == pygame.K_RIGHT:
                    new_x += STEP

                # Only move if the ball stays inside boundaries
                if RADIUS <= new_x <= WIDTH - RADIUS:
                    ball_x = new_x
                if RADIUS <= new_y <= HEIGHT - RADIUS:
                    ball_y = new_y

        # --- Draw ---
        screen.fill(WHITE)

        # Grid lines for reference
        for x in range(0, WIDTH, 50):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, 50):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y), 1)

        # Ball
        pygame.draw.circle(screen, RED, (ball_x, ball_y), RADIUS)
        pygame.draw.circle(screen, BLACK, (ball_x, ball_y), RADIUS, 2)

        # Position label
        pos_text = font.render(f"Position: ({ball_x}, {ball_y})", True, BLACK)
        screen.blit(pos_text, (10, 10))

        hint = font.render("Arrow keys to move  |  Q to quit", True, (100, 100, 100))
        screen.blit(hint, (10, HEIGHT - 30))

        pygame.display.flip()
        clock.tick(FPS)

        # Q to quit (also handle keydown above via event)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
