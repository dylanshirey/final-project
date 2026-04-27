import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Table Tennis Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

player = pygame.Rect(30, HEIGHT // 2 - 50, 15, 100)
computer = pygame.Rect(WIDTH - 45, HEIGHT // 2 - 50, 15, 100)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

player_score = 0
computer_score = 0


def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = 5 * random.choice((1, -1))
    ball_speed_y = 5 * random.choice((1, -1))


running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 7
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 7

    # Computer paddle movement
    if computer.centery < ball.centery and computer.bottom < HEIGHT:
        computer.y += 5
    if computer.centery > ball.centery and computer.top > 0:
        computer.y -= 5

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce off top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Bounce off paddles
    if ball.colliderect(player) or ball.colliderect(computer):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        computer_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        player_score += 1
        reset_ball()

    # Draw 
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, computer)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    score_text = font.render(f"{player_score}   {computer_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 20))

    pygame.display.flip()

pygame.quit()
