# Scissor.c
# OpenGL SuperBible, 3rd Edition
# Richard S.Wright Jr.
# rwright @ starstonesoftware.com

# include "../../Common/OpenGLSB.h"	// System and OpenGL Stuff
# include <math.h>

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import*

dRadius = 0.1
dAngle = 0.0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Called to draw scene
def RenderScene():

    global dRadius, dAngle

    # Clear blue window
    glClearColor(0.0, 0.0, 1.0, 0.0)

    if (dAngle == 0.0):
        glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)
    glVertex2d(dRadius * cos(dAngle), dRadius * sin(dAngle))
    glEnd()

    dRadius *= 1.01
    dAngle += 0.1

    if (dAngle > 30.0):
        dRadius = 0.1
        dAngle = 0.0

    glFlush()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Triggerb a repaint
def Timer(value):

    glutTimerFunc(50, Timer, 0)
    glutPostRedisplay()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Set viewport and projection
def ChangeSize(w, h):

    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Set the perspective coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set 2D Coordinate system
    gluOrtho2D(-4.0, 4.0, -3.0, 3.0)

    # Modelview matrix reset
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Program entry point
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Single Buffered")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)
    glutTimerFunc(50, Timer, 0)
    glutMainLoop()

