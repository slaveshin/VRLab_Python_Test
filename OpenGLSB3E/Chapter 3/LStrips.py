# LStrips.c
# OpenGL SuperBible, Chapter 4
# Demonstrates primative GL_LINE_STRIP
# Program by Richard S.Wright Jr.

# include "../../Common/OpenGLSB.h"	# System and OpenGL Stuff
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

# Called to draw scene
def RenderScene():

    global xRot, yRot, GL_PI

    x = 0.0
    y = 0.0
    z = 0.0
    angle = 0.0 # Storeage for coordinates and angles

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Save matrix state and do the rotation
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Call only once for all remaining points
    glBegin(GL_LINE_STRIP)

    z = -50.0
    while (angle <= (3.0 * 3.1415)): #위아래 원래 2.0 * 3.1415인데 내가 바꿈
        angle += 0.1
        if (angle <= (3.0 * 3.1415)):
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

    if (key == GLUT_KEY_UP):
        xRot -= 5.0


    if (key == GLUT_KEY_DOWN):
        xRot += 5.0


    if (key == GLUT_KEY_LEFT):
        yRot -= 5.0
        

    if (key == GLUT_KEY_RIGHT):
        yRot += 5.0


    if (key > 356.0):
        xRot = 0.0


    if (key < -1.0):
        xRot = 355.0


    if (key > 356.0):
        yRot = 0.0


    if (key < -1.0):
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

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Establish clipping volume(left, right, bottom, top, near, far)
    if (w <= h):
        glOrtho(-nRange, nRange, -nRange * h / w, nRange * h / w, -nRange, nRange)
    else:
        glOrtho(-nRange * w / h, nRange * w / h, -nRange, nRange, -nRange, nRange)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow(b"Line Strips Example")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
