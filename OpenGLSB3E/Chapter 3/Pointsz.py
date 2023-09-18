# Pointsz.c
# OpenGL SuperBible, Chapter 4
# Demonstrates OpenGL Primative GL_POINTS with point size
# Program by Richard S.Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import*


# Define a constant for the value of PI
#define GL_PI 3.1415f

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
    angle = 0.0 # Storeage for coordinates and angles
    sizes = [1.0, 0.0] # Store supported point size range
    step = 1.0# Store supported point size increments
    curSize = 0.0 # Store current size

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Save matrix state and do the rotation
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Get supported point size range and step size
    glGetFloatv(GL_POINT_SIZE_RANGE, sizes)
    glGetFloatv(GL_POINT_SIZE_GRANULARITY, step)

    # Set the initial point size
    curSize = sizes[0]

    # Loop around in a circle three times
    #for (angle = 0.0f; angle <= (2.0f * 3.1415f) * 3.0f; angle += 0.1f)
    while (angle <= (2.0 * 3.1415)):
        angle += 0.1
        if (angle <= (2.0 * 3.1415)):
            # Calculate x and y values on the circle
            x = 50.0 * sin(angle)
            y = 50.0 * cos(angle)

            # Specify the point size before the primative is specified
            glPointSize(curSize)

            # Draw the point
            glBegin(GL_POINTS)
            glVertex3f(x, y, z)
            glEnd()

            # Bump up the z value and the point size
            z += 0.5
            curSize += step

    # Restore matrix state
    glPopMatrix()

    # Flush drawing commands
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context.
def SetupRC():

    # Black background 
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Set  drawing color to green
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
    glutCreateWindow(b"Points Size Example")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
