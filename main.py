import pygame

pygame.init()

# sizes and positions
WINDOW_HEIGHT, WINDOW_WIDTH = 1000, 600
ball_radius = 15
ball_x, ball_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2

# Colors
WHITE = (255, 255, 255)

# Create the screen
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pyPong")
ball_color = WHITE
game_is_running = True

# main game loop
while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
    pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.update()
