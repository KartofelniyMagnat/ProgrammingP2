"""
Music Player with Keyboard Controls
Controls: P=Play  S=Stop  N=Next  B=Previous  Q=Quit
Place .mp3 or .wav files inside the music/ folder.
"""
import pygame
import sys
import os
import glob

WIDTH, HEIGHT = 500, 400
FPS = 30

BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
DARK   = (20,  20,  40)
ACCENT = (80,  160, 220)
GRAY   = (120, 120, 120)
GREEN  = (60,  200, 100)
RED    = (220, 60,  60)


def load_playlist(folder):
    """Return sorted list of audio files from folder."""
    patterns = ["*.mp3", "*.wav", "*.ogg"]
    files = []
    for p in patterns:
        files.extend(glob.glob(os.path.join(folder, p)))
    return sorted(files)


def draw_ui(screen, fonts, playlist, index, playing, volume, position_ms):
    screen.fill(DARK)

    title_font, track_font, info_font, key_font = fonts

    # Title
    title = title_font.render("Music Player", True, ACCENT)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    pygame.draw.line(screen, ACCENT, (30, 65), (WIDTH - 30, 65), 2)

    if not playlist:
        msg = track_font.render("No tracks found in music/ folder", True, RED)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
    else:
        # Track list
        y = 85
        for i, path in enumerate(playlist):
            name = os.path.splitext(os.path.basename(path))[0]
            if len(name) > 40:
                name = name[:38] + "…"
            color = GREEN if i == index else GRAY
            prefix = "▶ " if (i == index and playing) else "  "
            surf = track_font.render(f"{prefix}{i+1}. {name}", True, color)
            screen.blit(surf, (40, y))
            y += 30
            if y > HEIGHT - 130:
                break

    # Status bar
    pygame.draw.rect(screen, (40, 40, 60), (0, HEIGHT - 120, WIDTH, 120))
    status = "▶ Playing" if playing else "■ Stopped"
    status_color = GREEN if playing else RED
    s_surf = info_font.render(status, True, status_color)
    screen.blit(s_surf, (30, HEIGHT - 110))

    vol_text = info_font.render(f"Volume: {int(volume * 100)}%", True, WHITE)
    screen.blit(vol_text, (WIDTH - vol_text.get_width() - 30, HEIGHT - 110))

    # Pygame cannot always read total length for every codec, so show elapsed position.
    elapsed = max(0, position_ms // 1000)
    time_text = info_font.render(f"Position: {elapsed // 60:02d}:{elapsed % 60:02d}", True, WHITE)
    screen.blit(time_text, (30, HEIGHT - 82))
    bar_rect = pygame.Rect(30, HEIGHT - 56, WIDTH - 60, 10)
    pygame.draw.rect(screen, GRAY, bar_rect, border_radius=5)
    progress_width = (position_ms // 200) % bar_rect.width if playing else 0
    pygame.draw.rect(screen, ACCENT, (bar_rect.x, bar_rect.y, progress_width, bar_rect.height), border_radius=5)

    # Key hints
    keys = "[P] Play  [S] Stop  [N] Next  [B] Prev  [↑↓] Volume  [Q] Quit"
    k_surf = key_font.render(keys, True, GRAY)
    screen.blit(k_surf, (WIDTH // 2 - k_surf.get_width() // 2, HEIGHT - 30))

    pygame.display.flip()


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()

    fonts = (
        pygame.font.SysFont("Arial", 32, bold=True),   # title
        pygame.font.SysFont("Arial", 18),               # track
        pygame.font.SysFont("Arial", 20, bold=True),    # info
        pygame.font.SysFont("Arial", 14),               # keys
    )

    music_dir = os.path.join(os.path.dirname(__file__), "music")
    os.makedirs(music_dir, exist_ok=True)
    playlist = load_playlist(music_dir)

    index = 0
    playing = False
    volume = 0.7
    pygame.mixer.music.set_volume(volume)

    def play_track(i):
        nonlocal playing
        if not playlist:
            return
        pygame.mixer.music.load(playlist[i])
        pygame.mixer.music.play()
        playing = True

    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MUSIC_END and playlist:
                # Auto-advance to next track
                index = (index + 1) % len(playlist)
                play_track(index)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_p and playlist:
                    if not playing:
                        play_track(index)
                    else:
                        pygame.mixer.music.unpause()

                elif event.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    playing = False

                elif event.key == pygame.K_n and playlist:
                    index = (index + 1) % len(playlist)
                    play_track(index)

                elif event.key == pygame.K_b and playlist:
                    index = (index - 1) % len(playlist)
                    play_track(index)

                elif event.key == pygame.K_UP:
                    volume = min(1.0, volume + 0.05)
                    pygame.mixer.music.set_volume(volume)

                elif event.key == pygame.K_DOWN:
                    volume = max(0.0, volume - 0.05)
                    pygame.mixer.music.set_volume(volume)

        position_ms = pygame.mixer.music.get_pos() if playing else 0
        draw_ui(screen, fonts, playlist, index, playing, volume, position_ms)
        clock.tick(FPS)


if __name__ == "__main__":
    main()
