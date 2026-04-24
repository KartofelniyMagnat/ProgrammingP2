"""
Paint - Practice 10

Tools: free brush, rectangle, circle, eraser, and color selection.
Keys: B brush, R rectangle, C circle, E eraser, number keys choose colors.
"""
import sys

import pygame

WIDTH, HEIGHT = 900, 640
TOOLBAR_H = 70
FPS = 60

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GRAY = (210, 210, 210)
DARK = (45, 45, 52)
BLUE = (65, 132, 243)
COLORS = [
    (20, 20, 20),
    (230, 57, 70),
    (29, 140, 80),
    (42, 111, 219),
    (252, 186, 3),
    (157, 78, 221),
]


def draw_toolbar(screen, font, tool, color):
    pygame.draw.rect(screen, DARK, (0, 0, WIDTH, TOOLBAR_H))
    title = font.render(f"Tool: {tool.upper()}", True, WHITE)
    screen.blit(title, (16, 22))

    for i, swatch in enumerate(COLORS):
        rect = pygame.Rect(160 + i * 44, 18, 30, 30)
        pygame.draw.rect(screen, swatch, rect, border_radius=4)
        border = WHITE if swatch == color else GRAY
        pygame.draw.rect(screen, border, rect, 3, border_radius=4)

    hint = font.render("B brush  R rectangle  C circle  E eraser  1-6 colors", True, GRAY)
    screen.blit(hint, (460, 22))


def normalize_rect(start, end):
    x1, y1 = start
    x2, y2 = end
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Practice 10 - Paint")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20, bold=True)

    canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H))
    canvas.fill(WHITE)
    tool = "brush"
    color = COLORS[0]
    brush_size = 6
    drawing = False
    start_pos = None
    last_pos = None

    while True:
        mouse_pos = pygame.mouse.get_pos()
        canvas_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_H)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_b:
                    tool = "brush"
                elif event.key == pygame.K_r:
                    tool = "rectangle"
                elif event.key == pygame.K_c:
                    tool = "circle"
                elif event.key == pygame.K_e:
                    tool = "eraser"
                elif pygame.K_1 <= event.key <= pygame.K_6:
                    color = COLORS[event.key - pygame.K_1]

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_pos[1] >= TOOLBAR_H:
                drawing = True
                start_pos = canvas_pos
                last_pos = canvas_pos

            if event.type == pygame.MOUSEMOTION and drawing and tool in ("brush", "eraser"):
                draw_color = WHITE if tool == "eraser" else color
                pygame.draw.line(canvas, draw_color, last_pos, canvas_pos, brush_size * (3 if tool == "eraser" else 1))
                last_pos = canvas_pos

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
                drawing = False
                if tool == "rectangle":
                    pygame.draw.rect(canvas, color, normalize_rect(start_pos, canvas_pos), 3)
                elif tool == "circle":
                    radius = int(((canvas_pos[0] - start_pos[0]) ** 2 + (canvas_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, color, start_pos, radius, 3)

        screen.fill(WHITE)
        screen.blit(canvas, (0, TOOLBAR_H))

        if drawing and tool in ("rectangle", "circle"):
            preview = screen.copy()
            if tool == "rectangle":
                pygame.draw.rect(preview, color, normalize_rect((start_pos[0], start_pos[1] + TOOLBAR_H), mouse_pos), 3)
            else:
                radius = int(((canvas_pos[0] - start_pos[0]) ** 2 + (canvas_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(preview, color, (start_pos[0], start_pos[1] + TOOLBAR_H), radius, 3)
            screen.blit(preview, (0, 0))

        draw_toolbar(screen, font, tool, color)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
