# Scissor.c
# OpenGL SuperBible, 3rd Edition
# Richard S.Wright Jr.
# rwright @ starstonesoftware.com

# include "../../Common/OpenGLSB.h"	// System and OpenGL Stuff

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Called to draw scene
def RenderScene():

    # Clear blue window
    glClearColor(0.0, 0.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # Now set scissor to smaller red sub region
    glClearColor(1.0, 0.0, 0.0, 0.0)
    glScissor(100, 100, 600, 400)
    glEnable(GL_SCISSOR_TEST)
    glClear(GL_COLOR_BUFFER_BIT)

    # Finally, an even smaller green rectangle
    glClearColor(0.0, 1.0, 0.0, 0.0)
    glScissor(200, 200, 400, 200)
    glClear(GL_COLOR_BUFFER_BIT)

    # Turn scissor back off for next render
    glDisable(GL_SCISSOR_TEST)
    glutSwapBuffers()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Set viewport and projection
def ChangeSize(w, h):

    # Prevent divide by zero
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
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Scissor")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)
    glutMainLoop()
