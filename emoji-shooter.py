import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Emoji Shooter Game")

emoji_images = [
    pygame.image.load("emoji1.png"),
    pygame.image.load("emoji2.png"),
    pygame.image.load("emoji3.png"),
    pygame.image.load("emoji4.png"),
    pygame.image.load("emoji5.png")

]

emoji_images = [pygame.transform.scale(emoji, (50, 50)) for emoji in emoji_images]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

class Emoji:
    def __init__(self):
        self.image = random.choice(emoji_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randint(1, 3)

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

emojis = [Emoji() for _ in range(5)]
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for emoji in emojis:
                if emoji.rect.collidepoint(mouse_pos):
                    score += 1
                    emoji.rect.y = -emoji.rect.height
                    emoji.rect.x = random.randint(0, SCREEN_WIDTH - emoji.rect.width)

    screen.fill(WHITE)

    for emoji in emojis:
        emoji.move()
        emoji.draw(screen)

    display_score(score)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
