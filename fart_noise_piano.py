import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fart Noise Piano")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

fart_sounds = [
    pygame.mixer.Sound("fart1.wav"),
    pygame.mixer.Sound("fart2.wav"),
    pygame.mixer.Sound("fart3.wav"),
    pygame.mixer.Sound("fart4.wav"),
    pygame.mixer.Sound("fart5.wav"),
]

KEY_ALPHABET_MAP = {
    pygame.K_a: 'A',
    pygame.K_s: 'S',
    pygame.K_d: 'D',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'H',
    pygame.K_j: 'J',
    pygame.K_k: 'K',
    pygame.K_l: 'L',
    pygame.K_SEMICOLON: ';',
}

def play_fart_sound():
    fart_sound = random.choice(fart_sounds)
    fart_sound.set_volume(0.5)  
    fart_sound.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in KEY_ALPHABET_MAP:
                key_letter = KEY_ALPHABET_MAP[event.key]
                print(f"Key pressed: {key_letter}")
                play_fart_sound()

    screen.fill(WHITE)

    font = pygame.font.Font(None, 36)
    for key, letter in KEY_ALPHABET_MAP.items():
        text = font.render(letter, True, BLACK)
        text_rect = text.get_rect(center=(50 + (key - pygame.K_a) * 60, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
