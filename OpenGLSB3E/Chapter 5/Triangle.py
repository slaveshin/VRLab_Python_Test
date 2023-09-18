# Triangle.c
# OpenGL SuperBible
# Demonstrates OpenGL color triangle
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Called to draw scene
def RenderScene():

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Enable smooth shading
    glShadeModel(GL_SMOOTH)

    # Draw the triangle
    glBegin(GL_TRIANGLES)
    # Red Apex
    glColor3ub(255, 0, 0)
    glVertex3f(0.0, 200.0, 0.0)

    # Green on the right bottom corner
    glColor3ub(0, 255, 0)
    glVertex3f(200.0, -70.0, 0.0)

    # Blue on the left bottom corner
    glColor3ub(0, 0, 255)
    glVertex3f(-200.0, -70.0, 0.0)
    glEnd()

    # Flush drawing commands
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)


def ChangeSize(w, h):

    windowHeight = 0.0
    windowWidth = 0.0

    # Prevent a divide by zero, when window is too short
    # (you cant make a window of zero width).
    if (h == 0):
        h = 1

    # Set the viewport to be the entire window
    glViewport(0, 0, w, h)

    # Reset the coordinate system before modifying
    glLoadIdentity()


    # Keep the square square.

    # Window is higher than wide
    if (w <= h):
        windowHeight = 250.0*h / w
        windowWidth = 250.0
    else:
        # Window is wider than high
        windowWidth = 250.0*w / h
        windowHeight = 250.0

    # Set the clipping volume
    glOrtho(-windowWidth, windowWidth, -windowHeight, windowHeight, 1.0, -1.0)

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"RGB Triangle")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
