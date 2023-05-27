import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5
paddle1_x = 20
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x = WIDTH - 20 - PADDLE_WIDTH
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Set up the ball
BALL_RADIUS = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-2, 2])
ball_dy = random.choice([-2, 2])

# Set up the game clock
clock = pygame.time.Clock()

# Set up the score counters
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check ball collision with paddles
    if ball_x <= paddle1_x + PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
        ball_dx = abs(ball_dx)
    if ball_x >= paddle2_x - BALL_RADIUS and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
        ball_dx = -abs(ball_dx)

    # Check ball collision with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_RADIUS:
        ball_dy = -ball_dy

    # Check ball out of bounds
    if ball_x < 0:
        score2 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = random.choice([-2, 2])
        ball_dy = random.choice([-2, 2])
    elif ball_x > WIDTH:
        score1 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = random.choice([-2, 2])
        ball_dy = random.choice([-2, 2])

    # Update the window
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(WIN, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(WIN, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw the score counters
    score_text = font.render(f"Player 1: {score1}    Player 2: {score2}", True, WHITE)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
