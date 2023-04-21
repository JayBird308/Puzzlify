import pygame, pygame_menu
import random, constants
import time
from tkinter import *
from user import *
from main import main
pygame.init()

bg_color = (192, 192, 192)
grid_color = (128, 128, 128)

game_width = 10  # Change this to increase size
game_height = 10  # Change this to increase size
numMine = 10  # Number of mines
# grid_size = 32  # Size of grid (WARNING: macke sure to change the images dimension as well)
grid_size = 32
# border = 16  # Top border
# top_border = 100  # Left, Right, Bottom border
border = 128
top_border = constants.WIDTH/6
display_width = grid_size * game_width + border * 2  # Display width
display_height = grid_size * game_height + border + top_border  # Display height
# gameDisplay = pygame.display.set_mode((display_width, display_height))  
gameDisplay = constants.SCREEN
# timer = pygame.time.Clock()  # Create timer
timer = constants.clock
pygame.display.set_caption("Minesweeper")  # S Set the caption of window

# Import files
spr_emptyGrid = pygame.image.load("main/Minesweeper/Sprites/empty.png")
spr_flag = pygame.image.load("main/Minesweeper/Sprites/flag.png")
spr_grid = pygame.image.load("main/Minesweeper/Sprites/Grid.png")
spr_grid1 = pygame.image.load("main/Minesweeper/Sprites/grid1.png")
spr_grid2 = pygame.image.load("main/Minesweeper/Sprites/grid2.png")
spr_grid3 = pygame.image.load("main/Minesweeper/Sprites/grid3.png")
spr_grid4 = pygame.image.load("main/Minesweeper/Sprites/grid4.png")
spr_grid5 = pygame.image.load("main/Minesweeper/Sprites/grid5.png")
spr_grid6 = pygame.image.load("main/Minesweeper/Sprites/grid6.png")
spr_grid7 = pygame.image.load("main/Minesweeper/Sprites/grid7.png")
spr_grid8 = pygame.image.load("main/Minesweeper/Sprites/grid8.png")
spr_grid7 = pygame.image.load("main/Minesweeper/Sprites/grid7.png")
spr_mine = pygame.image.load("main/Minesweeper/Sprites/mine.png")
spr_mineClicked = pygame.image.load("main/Minesweeper/Sprites/mineClicked.png")
spr_mineFalse = pygame.image.load("main/Minesweeper/Sprites/mineFalse.png")


# Create global values
grid = []  # The main grid
mines = []  # Pos of the mines


# Create funtion to draw texts
def drawText(txt, s, yOff=0):
    screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
    rect = screen_text.get_rect()
    rect.center = (
        (constants.WIDTH/3) + game_width * grid_size / 2 + border, 
        (constants.HEIGHT/3) + game_height * grid_size / 2 + top_border + yOff)
    gameDisplay.blit(screen_text, rect)


# Create class grid
class Grid:
    def __init__(self, xGrid, yGrid, type):
        self.xGrid = xGrid  # X pos of grid
        self.yGrid = yGrid  # Y pos of grid
        self.clicked = False  # Boolean var to check if the grid has been clicked
        self.mineClicked = False  # Bool var to check if the grid is clicked and its a mine
        self.mineFalse = False  # Bool var to check if the player flagged the wrong grid
        self.flag = False  # Bool var to check if player flagged the grid
        # Create rectObject to handle drawing and collisions
        # self.rect = pygame.Rect(
        #     border + self.xGrid * grid_size, 
        #     top_border + self.yGrid * grid_size, 
        #     grid_size, 
        #     grid_size)
        self.rect = pygame.Rect(
            (constants.WIDTH/3) + border + self.xGrid * grid_size, 
            top_border + self.yGrid * grid_size, 
            grid_size, 
            grid_size)
        
        self.val = type  # Value of the grid, -1 is mine

    def drawGrid(self):
        # Draw the grid according to bool variables and value of grid
        if self.mineFalse:
            gameDisplay.blit(spr_mineFalse, self.rect)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.mineClicked:
                        gameDisplay.blit(spr_mineClicked, self.rect)
                    else:
                        gameDisplay.blit(spr_mine, self.rect)
                else:
                    if self.val == 0:
                        gameDisplay.blit(spr_emptyGrid, self.rect)
                    elif self.val == 1:
                        gameDisplay.blit(spr_grid1, self.rect)
                    elif self.val == 2:
                        gameDisplay.blit(spr_grid2, self.rect)
                    elif self.val == 3:
                        gameDisplay.blit(spr_grid3, self.rect)
                    elif self.val == 4:
                        gameDisplay.blit(spr_grid4, self.rect)
                    elif self.val == 5:
                        gameDisplay.blit(spr_grid5, self.rect)
                    elif self.val == 6:
                        gameDisplay.blit(spr_grid6, self.rect)
                    elif self.val == 7:
                        gameDisplay.blit(spr_grid7, self.rect)
                    elif self.val == 8:
                        gameDisplay.blit(spr_grid8, self.rect)

            else:
                if self.flag:
                    gameDisplay.blit(spr_flag, self.rect)
                else:
                    gameDisplay.blit(spr_grid, self.rect)

    def revealGrid(self):
        self.clicked = True
        # Auto reveal if it's a 0
        if self.val == 0:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if not grid[self.yGrid + y][self.xGrid + x].clicked:
                                grid[self.yGrid + y][self.xGrid + x].revealGrid()
        elif self.val == -1:
            # Auto reveal all mines if it's a mine
            for m in mines:
                if not grid[m[1]][m[0]].clicked:
                    grid[m[1]][m[0]].revealGrid()

    def updateValue(self):
        # Update the value when all grid is generated
        if self.val != -1:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if grid[self.yGrid + y][self.xGrid + x].val == -1:
                                self.val += 1


def gameLoop():
    global numMine, game_width, game_height, EASYSCORE, HARDSCORE
    DIFFICULTY = constants.DIFFICULTY

    if DIFFICULTY == 0:
        game_width = 10  # Change this to increase size
        game_height = 10  # Change this to increase size
        numMine = 10  # Number of mines
        EASYSCORE = 0
    elif DIFFICULTY == 1:
        game_width = 14
        game_height = 14
        numMine = 32
        HARDSCORE = 0
    else:
        print('Minesweeper - Difficulty Error~!')
        exit(-1)

    gameState = "Playing"  # Game state
    mineLeft = numMine  # Number of mine left
    global grid  # Access global var
    grid = []
    global mines
    t = 0  # Set time to 0

    # Generating mines
    mines = [[random.randrange(0, game_width),
              random.randrange(0, game_height)]]

    for c in range(numMine - 1):
        pos = [random.randrange(0, game_width),
               random.randrange(0, game_height)]
        same = True
        while same:
            for i in range(len(mines)):
                if pos == mines[i]:
                    pos = [random.randrange(0, game_width), random.randrange(0, game_height)]
                    break
                if i == len(mines) - 1:
                    same = False
        mines.append(pos)

    # Generating entire grid
    for j in range(game_height):
        line = []
        for i in range(game_width):
            if [i, j] in mines:
                line.append(Grid(i, j, -1))
            else:
                line.append(Grid(i, j, 0))
        grid.append(line)

    # Update of the grid
    for i in grid:
        for j in i:
            j.updateValue()

    start_time = time.time()

    # Main Loop
    while gameState != "Exit":
        # Reset screen
        gameDisplay.fill(bg_color)

        # User inputs
        events = pygame.event.get()
        for event in events:
            # Check if player close window
            if event.type == pygame.QUIT:
                gameState = "Exit"

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # main_menu.enable()
                    pygame_menu.events.BACK
                    return
            
            # Check if play restart
            if gameState == "Game Over" or gameState == "Win":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameState = "Exit"
                        gameLoop()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in grid:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                if event.button == 1:
                                    # If player left clicked of the grid
                                    j.revealGrid()
                                    # Toggle flag off
                                    if j.flag:
                                        mineLeft += 1
                                        j.falg = False
                                    # If it's a mine
                                    if j.val == -1:
                                        gameState = "Game Over"
                                        j.mineClicked = True
                                elif event.button == 3:
                                    # If the player right clicked
                                    if not j.clicked:
                                        if j.flag:
                                            j.flag = False
                                            mineLeft += 1
                                        else:
                                            j.flag = True
                                            mineLeft -= 1

        # Check if won
        w = True
        for i in grid:
            for j in i:
                j.drawGrid()
                if j.val != -1 and not j.clicked:
                    w = False
        if w and gameState != "Exit":
            gameState = "Win"

        # Draw Texts
        if gameState != "Game Over" and gameState != "Win":
            t += 1
            end_time = time.time()
        elif gameState == "Game Over":
            drawText("Game Over!", 50)
            drawText("R to restart", 35, 50)
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        j.mineFalse = True
        else:
            drawText("You WON!", 50)
            drawText("R to restart", 35, 50)
        # Draw time
        s = str(t // 15)
        screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))
        gameDisplay.blit(screen_text, ((constants.WIDTH/3) + border, border))
        # Draw mine left
        screen_text = pygame.font.SysFont("Calibri", 50).render(mineLeft.__str__(), True, (0, 0, 0))
        gameDisplay.blit(screen_text, ((constants.WIDTH/3) + display_width - border - 50, border))

        pygame.display.update()  # Update screen

        timer.tick(15)  # Tick fps
    
    elapsed_time = end_time - start_time

    # pop up window for score finish
    def easy_score_popup():
        window = Tk()
        window.title('Game Score')
        msg = Label(window, text="Easy Score: " + str(EASYSCORE),
                    fg='black', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.bind("<Escape>", lambda event: main.close_window(window, event))
        window.mainloop()
    
    def hard_score_popup():
        window = Tk()
        window.title('Game Score')
        msg = Label(window, text="Advanced Score: " + str(HARDSCORE),
                    fg='black', font=("Helvetica", 16))
        msg.place(x=60, y=50)
        window.geometry("300x200+700+400")
        window.bind("<Escape>", lambda event: main.close_window(window, event))
        window.mainloop()

    if gameState == "Win":
        # push easy mode stats
        if constants.DIFFICULTY == 0:
            EASYSCORE = int(10000/elapsed_time)
            print(f"Time elapsed: {elapsed_time}")
            print(f"Your EASY score is: {EASYSCORE}")
            if EASYSCORE > currentLoggedInUser.slidingHighScore:
                currentLoggedInUser.slidingHighScore = EASYSCORE
                currentLoggedInUser.slidingGamesPlayed = currentLoggedInUser.slidingGamesPlayed + 1
            updateUser()
            easy_score_popup()
        # push advanced mode stats
        elif constants.DIFFICULTY == 1:
            HARDSCORE = int(10000/elapsed_time)
            print(f"Time elapsed: {elapsed_time}")
            print(f"Your EASY score is: {HARDSCORE}")
            if HARDSCORE > currentLoggedInUser.advSlidingHighScore:
                currentLoggedInUser.advSlidingHighScore = HARDSCORE
                currentLoggedInUser.slidingGamesPlayed = currentLoggedInUser.slidingGamesPlayed + 1
            updateUser()
            hard_score_popup()

# gameLoop()
# pygame.quit()
# quit()