# Atom2.c
# OpenGL SuperBible
# Demonstrates OpenGL coordinate transformation
# and perspective
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rotation amounts
xRot = 0.0
yRot = 0.0
fElect1 = 0.0

# Called to draw scene
def RenderScene():

    global fElect1

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Red Nucleus
    glColor3ub(255, 0, 0)
    glutSolidSphere(10.0, 15, 15)

    # Yellow Electrons
    glColor3ub(255, 255, 0)

    # First Electron Orbit
    # Save viewing transformation
    glPushMatrix()

    # Rotate by angle of revolution
    glRotatef(fElect1, 0.0, 1.0, 0.0)

    # Translate out from origin to orbit distance
    glTranslatef(90.0, 0.0, 0.0)

    # Draw the electron
    glutSolidSphere(6.0, 15, 15)

    # Restore the viewing transformation
    glPopMatrix()

    # Second Electron Orbit
    glPushMatrix()
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glRotatef(fElect1, 0.0, 1.0, 0.0)
    glTranslatef(-70.0, 0.0, 0.0)
    glutSolidSphere(6.0, 15, 15)
    glPopMatrix()

    # Third Electron Orbit
    glPushMatrix()
    glRotatef(360.0 - 45.0, 0.0, 0.0, 1.0)
    glRotatef(fElect1, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, 60.0)
    glutSolidSphere(6.0, 15, 15)
    glPopMatrix()

    # Increment the angle of revolution
    fElect1 += 10.0
    if (fElect1 > 360.0):
        fElect1 = 0.0

    # Show the image
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    glEnable(GL_DEPTH_TEST)	# Hidden surface removal
    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out
    glEnable(GL_CULL_FACE)		# Do not calculate inside of jet

    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

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

def TimerFunc(value):

    glutPostRedisplay()
    glutTimerFunc(100, TimerFunc, 1)

def ChangeSize(w, h):

    fAspect = 0.0

    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    fAspect = float(w) / float(h)
    gluPerspective(45.0, fAspect, 1.0, 500.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -250.0)

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Atom - Part Duex")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    glutTimerFunc(500, TimerFunc, 1)
    SetupRC()
    glutMainLoop()