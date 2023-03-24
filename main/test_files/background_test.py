import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the display
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Falling Objects")

# Set up the clock
clock = pygame.time.Clock()

class FallingObject(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("main\\images\\puzzle.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        
    def update(self):
        self.rect.y += self.speed
        
        # If the object goes off the screen, reset its position
        if self.rect.y > size[1]:
            self.rect.y = 0
            self.rect.x = random.randint(0, size[0] - 50)

# Set up the falling objects group
falling_objects = pygame.sprite.Group()

def random_float(start, end):
    return random.uniform(start, end)

# Create some falling objects with random speeds
for i in range(20):
    x = random.randint(0, size[0] - 50)
    y = random.randint(0, size[1] - 50)
    speed = random_float(1.0, 3.0)
    print(speed)
    obj = FallingObject(x, y, speed)
    falling_objects.add(obj)

# Start game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update falling objects
    falling_objects.update()
        
    # Draw objects and update display
    screen.fill(WHITE)
    falling_objects.draw(screen)
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
