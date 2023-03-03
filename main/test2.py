import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

# initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)

# initialize OpenGL
glClearColor(0, 0, 0, 1)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, 800/600, 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_DEPTH_TEST)

# create the cube
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# main loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glRotatef(5, 0, 1, 0)
            elif event.key == pygame.K_RIGHT:
                glRotatef(-5, 0, 1, 0)
            elif event.key == pygame.K_UP:
                glRotatef(5, 1, 0, 0)
            elif event.key == pygame.K_DOWN:
                glRotatef(-5, 1, 0, 0)

    # clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # draw the cube
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    draw_cube()

    # update the screen
    pygame.display.flip()
