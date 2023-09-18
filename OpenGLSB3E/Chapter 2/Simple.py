# Simple.c
# The Simplest OpenGL program with GLUT
# OpenGL SuperBible, 3rd Edition
# Richard S. Wright Jr.
# rwright@starstonesoftware.com

#include "../../Common/OpenGLSB.h"// System and OpenGL Stuff

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#############################
# Called to draw scene
def RenderScene():
    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Flush drawing commands
    glFlush()

#############################
# Setup the rendering state
def SetupRC():
    glClearColor(0.0, 0.0, 1.0, 1.0)

#############################/
# Main program entry point
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Simple")
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
