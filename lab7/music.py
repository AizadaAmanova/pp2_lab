import pygame
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MUSIC_FOLDER = "C:/Users/Acer/Desktop/pp2_lab/lab7/music"
BACKGROUND_IMAGE = "C:/Users/Acer/Desktop/pp2_lab/lab7/Music image/TAU.jpeg"
BUTTONS_FOLDER = "C:/Users/Acer/Desktop/pp2_lab/lab7/Music buttons"


BUTTON_SIZE = (70, 70)

WHITE = (255, 255, 255)
NAVY_BLUE = (20, 20, 50)
SEMI_TRANSPARENT_BLACK = (0, 0, 0, 150)

pygame.init()

def load_playlist(music_folder):
    return [os.path.join(music_folder, song) for song in os.listdir(music_folder) if song.endswith(".mp3")]


def load_button_images(folder_path):
    return {
        'play': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "play.png")), BUTTON_SIZE),
        'pause': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "pause.png")), BUTTON_SIZE),
        'next': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "next.jpeg")), BUTTON_SIZE),
        'previous': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "back.jpeg")), BUTTON_SIZE),
    }


def draw_text(surface, text, font, color, x, y):
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, (x, y))


def draw_buttons(surface, buttons, is_playing, button_rects):
    play_x = SCREEN_WIDTH // 2 - 35
    play_y = SCREEN_HEIGHT - 100
    next_x = play_x + 90
    prev_x = play_x - 90

    button_rects['play'] = pygame.Rect(play_x, play_y, BUTTON_SIZE[0], BUTTON_SIZE[1])
    button_rects['next'] = pygame.Rect(next_x, play_y, BUTTON_SIZE[0], BUTTON_SIZE[1])
    button_rects['previous'] = pygame.Rect(prev_x, play_y, BUTTON_SIZE[0], BUTTON_SIZE[1])

    surface.blit(buttons['pause'] if is_playing else buttons['play'], (play_x, play_y))
    surface.blit(buttons['next'], (next_x, play_y))
    surface.blit(buttons['previous'], (prev_x, play_y))


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Aizada - Playlist")

    playlist = load_playlist(MUSIC_FOLDER)
    button_images = load_button_images(BUTTONS_FOLDER)
    background = pygame.image.load(BACKGROUND_IMAGE)
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  

    font_song_name = pygame.font.SysFont(None, 24)

    current_index = 0
    is_playing = True
    pygame.mixer.music.load(playlist[current_index])
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    running = True

    button_rects = {}

    while running:
        screen.blit(background, (0, 0))

        overlay = pygame.Surface((SCREEN_WIDTH, 120), pygame.SRCALPHA)
        overlay.fill(SEMI_TRANSPARENT_BLACK)  
        screen.blit(overlay, (0, SCREEN_HEIGHT - 120))

        current_song_name = os.path.basename(playlist[current_index])
        draw_text(screen, f"Қазір ойнап жатыр: {current_song_name}", font_song_name, WHITE, 20, SCREEN_HEIGHT - 110)

        draw_buttons(screen, button_images, is_playing, button_rects)

        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    if is_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    is_playing = not is_playing

                elif event.key == pygame.K_RIGHT: 
                    current_index = (current_index + 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

                elif event.key == pygame.K_LEFT:  
                    current_index = (current_index - 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                
                if button_rects['play'].collidepoint(mouse_pos): 
                    if is_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    is_playing = not is_playing

                elif button_rects['next'].collidepoint(mouse_pos):  
                    current_index = (current_index + 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

                elif button_rects['previous'].collidepoint(mouse_pos):  
                    current_index = (current_index - 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

    pygame.quit()


if __name__ == "__main__":
    main()