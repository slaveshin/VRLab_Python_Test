# Linesw.c
# OpenGL SuperBible, Chapter 4
# Demonstrates primative GL_LINES with line widths
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Define a constant for the value of PI
#define GL_PI 3.1415f

# Rotation amounts
xRot = 0.0
yRot = 0.0


# Called to draw scene
def RenderScene():

    global xRot, yRot

    y = -90.0					# Storeage for varying Y coordinate
    fSizes = [1.0, 0.0]		# Line width range metrics
    fCurrSize = 0.0			# Save current size


    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Save matrix state and do the rotation
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Get line size metrics and save the smallest value
    glGetFloatv(GL_LINE_WIDTH_RANGE,fSizes)
    fCurrSize = fSizes[0]

    # Step up Y axis 20 units at a time
    while (y < 90.0):
        y += 20.0
        if (y < 90.0):
            # Set the line width
            glLineWidth(fCurrSize)

            # Draw the line
            glBegin(GL_LINES)
            glVertex2f(-80.0, y)
            glVertex2f(80.0, y)
            glEnd()

            # Increase the line width
            fCurrSize += 1.0

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
    if(h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Establish clipping volume (left, right, bottom, top, near, far)
    if (w <= h):
        glOrtho (-nRange, nRange, -nRange*h/w, nRange*h/w, -nRange, nRange)
    else:
        glOrtho (-nRange*w/h, nRange*w/h, -nRange, nRange, -nRange, nRange)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow(b"Line Width Example")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
