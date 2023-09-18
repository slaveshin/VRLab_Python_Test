# Star.c
# OpenGL SuperBible, Chapter4
# Demonstrates OpenGL Primative GL_POINTS with point size
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

# Flags for effects
MODE_SOLID = 0.0
MODE_LINE = 1.0
MODE_POINT = 2.0

iMode = MODE_SOLID
bEdgeFlag = True

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Reset flags as appropriate in response to menu selections
def ProcessMenu(value):

    global iMode, bEdgeFlag, MODE_SOLID, MODE_LINE, MODE_POINT

    if (value == 1):
        iMode = MODE_SOLID

    if (value == 2):
        iMode = MODE_LINE

    if (value == 3):
        iMode = MODE_POINT

    if (value == 4):
        bEdgeFlag = True

    else:
        bEdgeFlag = False


    glutPostRedisplay()

# Called to draw scene
def RenderScene():

    global xRot, yRot, iMode, bEdgeFlag, MODE_SOLID, MODE_LINE, MODE_POINT

    # Clear the window
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw back side as a polygon only, if flag is set
    if (iMode == MODE_LINE):
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    if (iMode == MODE_POINT):
        glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)

    if (iMode == MODE_SOLID):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # Save matrix state and do the rotation
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Begin the triangles
    glBegin(GL_TRIANGLES)

    glEdgeFlag(bEdgeFlag)
    glVertex2f(-20.0, 0.0)
    glEdgeFlag(True)
    glVertex2f(20.0, 0.0)
    glVertex2f(0.0, 40.0)

    glVertex2f(-20.0, 0.0)
    glVertex2f(-60.0, -20.0)
    glEdgeFlag(bEdgeFlag)
    glVertex2f(-20.0, -40.0)
    glEdgeFlag(True)

    glVertex2f(-20.0, -40.0)
    glVertex2f(0.0, -80.0)
    glEdgeFlag(bEdgeFlag)
    glVertex2f(20.0, -40.0)
    glEdgeFlag(True)

    glVertex2f(20.0, -40.0)
    glVertex2f(60.0, -20.0)
    glEdgeFlag(bEdgeFlag)
    glVertex2f(20.0, 0.0)
    glEdgeFlag(True)

    # Center square as two triangles
    glEdgeFlag(bEdgeFlag)
    glVertex2f(-20.0, 0.0)
    glVertex2f(-20.0, -40.0)
    glVertex2f(20.0, 0.0)

    glVertex2f(-20.0, -40.0)
    glVertex2f(20.0, -40.0)
    glVertex2f(20.0, 0.0)
    glEdgeFlag(True)

    # Done drawing Triangles
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

    # Establish clipping volume (left, right, bottom, top, near, far)
    if (w <= h):
        glOrtho (-nRange, nRange, -nRange * h / w, nRange * h / w, -nRange, nRange)
    else:
        glOrtho (-nRange * w / h, nRange * w / h, -nRange, nRange, -nRange, nRange)

    # Reset Model view matrix stack
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == '__main__':

    nModeMenu = 0.0
    nEdgeMenu = 0.0
    nMainMenu =0.0

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow(b"Solid and Outlined Star")

    # Create the Menu
    nModeMenu = glutCreateMenu(ProcessMenu)
    glutAddMenuEntry("Solid", 1)
    glutAddMenuEntry("Outline", 2)
    glutAddMenuEntry("Points", 3)

    nEdgeMenu = glutCreateMenu(ProcessMenu)
    glutAddMenuEntry("On", 4)
    glutAddMenuEntry("Off", 5)

    nMainMenu = glutCreateMenu(ProcessMenu)
    glutAddSubMenu("Mode", nModeMenu)
    glutAddSubMenu("Edges", nEdgeMenu)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()

