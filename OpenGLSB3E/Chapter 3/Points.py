# Points.c
# OpenGL SuperBible, Chapter 3
# Demonstrates OpenGL Primative GL_POINTS
# Program by Richard S.Wright Jr.

# include "../../Common/OpenGLSB.h"	// System and OpenGL Stuff
# include <math.h>

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import*


# Define a constant for the value of PI
# define GL_PI 3.1415f

# Rotation amounts
xRot = 0.0
yRot = 0.0
GL_PI = 3.1415


# Called to draw scene
def RenderScene():
    
    global xRot, yRot, GL_PI

    x = 0.0
    y = 0.0
    z = -50.0
    angle = 0.0  # Storeage for coordinates and angles

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Save matrix state and do the rotation
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Call only once for all remaining points
    glBegin(GL_POINTS)

    #for (angle = 0.0f; angle <= (2.0f * GL_PI) * 3.0f; angle += 0.1f):
    while (angle <= (2.0 * GL_PI)):
        angle += 0.1
        if (angle <= (2.0 * GL_PI)):
            x = 50.0 * sin(angle)
            y = 50.0 * cos(angle)

            # Specify the point and move the Z value up a little
            glVertex3f(x, y, z)
            z += 0.5


    # Done drawing points
    glEnd()

    # Restore transformations
    glPopMatrix()

    # Flush drawing commands
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context.
def SetupRC():

    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Set drawing color to green
    glColor3f(0.0, 1.0, 0.0)

def SpecialKeys(key, x, y):

    global xRot, yRot

    if(key == GLUT_KEY_UP):
        xRot-= 5.0

    if(key == GLUT_KEY_DOWN):
        xRot += 5.0

    if(key == GLUT_KEY_LEFT):
        yRot -= 5.0

    if(key == GLUT_KEY_RIGHT):
        yRot += 5.0

    if(key > 356.0):
        xRot = 0.0

    if(key < -1.0):
        xRot = 355.0

    if(key > 356.0):
        yRot = 0.0

    if(key < -1.0):
        yRot = 355.0

    # Refresh the Window
    glutPostRedisplay()


def ChangeSize(w, h):

    nRange = 100.0

    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset projection matrix stack
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Establish clipping volume(left, right, bottom, top, near, far)
    if (w <= h):
        glOrtho(-nRange, nRange, -nRange * h / w, nRange * h / w, -nRange, nRange)
    else:
        glOrtho(-nRange * w / h, nRange * w / h, -nRange, nRange, -nRange, nRange)

    # Reset Model view matrix stack
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow(b"Points Example")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
