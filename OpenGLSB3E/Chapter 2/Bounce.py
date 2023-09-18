# Bounce.c
# Demonstrates a simple animated rectangle program with GLUT
# OpenGL SuperBible, 3rd Edition
# Richard S.Wright Jr.
# rwright @ starstonesoftware.com

# include "../../Common/OpenGLSB.h"	// System and OpenGL Stuff

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Initial square position and size
x = 0.0
y = 0.0
rsize = 25

# Step size in x and y directions
# (number of pixels to move each time)
xstep = 1.0
ystep = 1.0

# Keep track of windows changing width and height
windowWidth = 0.0
windowHeight = 0.0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Called to draw scene
def RenderScene():
    global x, y, rsize, xstep, ystep, windowWidth, windowHeight

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Set current drawing color to red
    # R     G       B
    glColor3f(1.0, 0.0, 0.0)

    # Draw a filled rectangle with current color
    glRectf(x, y, x + rsize, y - rsize)

    # Flush drawing commands and swap
    glutSwapBuffers()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Called by GLUT library when idle(window not being
# resized or moved)
def TimerFunction(value):
    global x, y, rsize, xstep, ystep, windowWidth, windowHeight

    # Reverse direction when you reach left or right edge
    if ((x > windowWidth - rsize) or (x < -windowWidth)):
        xstep = -xstep

    # Reverse direction when you reach top or bottom edge
    if ((y > windowHeight) or (y < -windowHeight + rsize)):
        ystep = -ystep

    # Actually move the square
    x += xstep
    y += ystep

    # Check bounds.This is in case the window is made \
    # smaller while the rectangle is bouncing and the
    # rectangle suddenly finds itself outside the new
    # clipping volume
    if (x > ((windowWidth - rsize) + xstep)):
        x = windowWidth - rsize - 1
    elif (x < -(windowWidth + xstep)):
        x = -windowWidth - 1

    if (y > (windowHeight + ystep)):
        y = windowHeight - 1
    elif (y < -(windowHeight - rsize + ystep)):
        y = -windowHeight + rsize - 1

    # Redraw the scene with new coordinates
    glutPostRedisplay()
    glutTimerFunc(33, TimerFunction, 1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Setup the rendering state
def SetupRC():

    # Set clear color to blue
    glClearColor(0.0, 0.0, 1.0, 1.0)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Called by GLUT library when the window has chanaged size
def ChangeSize(w, h):
    global windowWidth, windowHeight

    aspectRatio = 0.0

    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Establish clipping volume(left, right, bottom, top, near, far)
    aspectRatio = w / h
    if (w <= h):
        windowWidth = 100
        windowHeight = 100 / aspectRatio
        glOrtho(-100.0, 100.0, -windowHeight, windowHeight, 1.0, -1.0)

    else:
        windowWidth = 100 * aspectRatio
        windowHeight = 100
        glOrtho(-windowWidth, windowWidth, -100.0, 100.0, 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Main program entry point
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Bounce")
    glutDisplayFunc(RenderScene)
    glutReshapeFunc(ChangeSize)
    glutTimerFunc(33, TimerFunction, 1)
    SetupRC()
    glutMainLoop()
