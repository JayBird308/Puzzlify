import pygame

pygame.init()

# Set up the window
WINDOW_SIZE = (400, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Countdown Timer")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the timer
duration = 60000  # 1 minute in milliseconds
start_time = pygame.time.get_ticks()

# Set up the clock
clock = pygame.time.Clock()

def wait():
    # Wait for approximately 2000 ticks
    ticks_to_wait = 2000
    while pygame.time.get_ticks() - start_time < ticks_to_wait:
        clock.tick(60)  # Limit the frame rate to 60 FPS
        print(". . .")

wait_num = 0

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_time = pygame.time.get_ticks()

    if wait_num == 0:
        wait()
        wait_num = 1
        print("Waiting over.")

    # Calculate the time remaining
    time_elapsed = pygame.time.get_ticks()
