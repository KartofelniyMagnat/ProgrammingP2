import pygame
import math
import datetime
import sys
import os

WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 30

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
RED    = (220, 30,  30)
BLUE   = (30,  30,  220)
YELLOW = (255, 220, 0)
GRAY   = (150, 150, 150)


def draw_hand(surface, color, angle_deg, length, width, center):
    """Draw a clock hand rotated by angle_deg from 12-o'clock position (clockwise)."""
    rad = math.radians(angle_deg - 90)
    end_x = center[0] + length * math.cos(rad)
    end_y = center[1] + length * math.sin(rad)
    pygame.draw.line(surface, color, center, (int(end_x), int(end_y)), width)


def draw_clock_face(surface, center, radius):
    """Draw dial markings."""
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        outer = radius - 5
        inner = radius - (18 if i % 5 == 0 else 10)
        x1 = center[0] + outer * math.cos(angle)
        y1 = center[1] + outer * math.sin(angle)
        x2 = center[0] + inner * math.cos(angle)
        y2 = center[1] + inner * math.sin(angle)
        color = BLACK if i % 5 == 0 else GRAY
        width = 3 if i % 5 == 0 else 1
        pygame.draw.line(surface, color, (int(x1), int(y1)), (int(x2), int(y2)), width)


def make_mickey_hand(color, length, glove_side):
    """Create a small hand graphic that can be rotated like Mickey's arm."""
    size = length * 2 + 120
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx = cy = size // 2
    top_y = cy - length

    pygame.draw.line(surf, BLACK, (cx, cy), (cx, top_y + 34), 16)
    pygame.draw.line(surf, color, (cx, cy), (cx, top_y + 34), 10)

    glove_x = cx + (18 if glove_side == "right" else -18)
    pygame.draw.circle(surf, WHITE, (glove_x, top_y + 25), 24)
    pygame.draw.circle(surf, BLACK, (glove_x, top_y + 25), 24, 3)
    for offset in (-16, 0, 16):
        pygame.draw.circle(surf, WHITE, (glove_x + offset, top_y + 8), 9)
        pygame.draw.circle(surf, BLACK, (glove_x + offset, top_y + 8), 9, 2)
    return surf


def blit_rotated_hand(surface, hand, center, angle_deg):
    """Rotate around the image center, which is also the clock pivot."""
    rotated = pygame.transform.rotate(hand, -angle_deg)
    rect = rotated.get_rect(center=center)
    surface.blit(rotated, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock_tick = pygame.time.Clock()

    # Try to load Mickey image as background
    img_path = os.path.join(os.path.dirname(__file__), "images", "mickeyclock.jpeg")
    bg = None
    if os.path.exists(img_path):
        raw = pygame.image.load(img_path).convert()
        bg = pygame.transform.scale(raw, (WIDTH, HEIGHT))

    font_large = pygame.font.SysFont("Arial", 48, bold=True)
    font_small = pygame.font.SysFont("Arial", 24)

    CLOCK_RADIUS = 180
    CLOCK_CENTER = (WIDTH // 2, HEIGHT // 2 + 20)
    minute_hand = make_mickey_hand(BLUE, int(CLOCK_RADIUS * 0.70), "right")
    second_hand = make_mickey_hand(RED, int(CLOCK_RADIUS * 0.83), "left")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        # Angles measured clockwise from 12
        minute_angle = (minutes / 60) * 360           # 0-360
        second_angle = (seconds / 60) * 360            # 0-360

        # --- Draw ---
        if bg:
            screen.blit(bg, (0, 0))
            # Semi-transparent overlay so clock is readable
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(overlay, (255, 255, 255, 180), CLOCK_CENTER, CLOCK_RADIUS)
            screen.blit(overlay, (0, 0))
        else:
            screen.fill(WHITE)

        # Clock border
        pygame.draw.circle(screen, BLACK, CLOCK_CENTER, CLOCK_RADIUS, 4)
        draw_clock_face(screen, CLOCK_CENTER, CLOCK_RADIUS)

        # Mickey-style hands: right hand shows minutes, left hand shows seconds.
        blit_rotated_hand(screen, minute_hand, CLOCK_CENTER, minute_angle)
        blit_rotated_hand(screen, second_hand, CLOCK_CENTER, second_angle)

        # Center cap
        pygame.draw.circle(screen, BLACK, CLOCK_CENTER, 10)

        # Digital readout
        time_str = now.strftime("%H:%M:%S")
        t_surf = font_large.render(time_str, True, BLACK)
        screen.blit(t_surf, (WIDTH // 2 - t_surf.get_width() // 2, HEIGHT - 70))

        label = font_small.render("Blue = Minutes  |  Red = Seconds", True, GRAY)
        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT - 30))

        pygame.display.flip()
        clock_tick.tick(FPS)


if __name__ == "__main__":
    main()
