import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital Rush")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Square position and size
square_size = 50
x = WIDTH // 2 - square_size // 2
y = HEIGHT // 2 - square_size // 2
speed = 5

# Clock for controlling FPS
clock = pygame.time.Clock()

# Main game loop
while True:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  # Get pressed keys
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    x -= speed
  if keys[pygame.K_RIGHT]:
    x += speed
  if keys[pygame.K_UP]:
    y -= speed
  if keys[pygame.K_DOWN]:
    y += speed

  # Keep square within screen bounds
  x = max(0, min(x, WIDTH - square_size))
  y = max(0, min(y, HEIGHT - square_size))

  # Fill background
  screen.fill(WHITE)

  # Draw the square
  pygame.draw.rect(screen, RED, (x, y, square_size, square_size))

  # Update the display
  pygame.display.flip()

  # Limit to 60 FPS
  clock.tick(60)