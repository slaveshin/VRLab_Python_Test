# ccube.c
# OpenGL SuperBible
# Demonstrates primative RGB Color Cube
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rotation amounts
xRot = 0.0
yRot = 0.0


# Called to draw scene
def RenderScene():

    global xRot, yRot

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)


    # Draw six quads
    glBegin(GL_QUADS)
    # Front Face
    # White
    glColor3ub(255, 255, 255)
    glVertex3f(50.0, 50.0, 50.0)

    # Yellow
    glColor3ub(255, 255, 0)
    glVertex3f(50.0, -50.0, 50.0)

    # Red
    glColor3ub(255, 0, 0)
    glVertex3f(-50.0, -50.0, 50.0)

    # Magenta
    glColor3ub(255, 0, 255)
    glVertex3f(-50.0, 50.0, 50.0)


    # Back Face
        # Cyan
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(50.0, 50.0, -50.0)

    # Green
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(50.0, -50.0, -50.0)

    # Black
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-50.0, -50.0, -50.0)

    # Blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-50.0, 50.0, -50.0)

    # Top Face
        # Cyan
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(50.0, 50.0, -50.0)

    # White
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(50.0, 50.0, 50.0)

    # Magenta
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-50.0, 50.0, 50.0)

    # Blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-50.0, 50.0, -50.0)

    # Bottom Face
        # Green
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(50.0, -50.0, -50.0)

    # Yellow
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(50.0, -50.0, 50.0)

    # Red
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-50.0, -50.0, 50.0)

    # Black
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-50.0, -50.0, -50.0)

    # Left face
        # White
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(50.0, 50.0, 50.0)

    # Cyan
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(50.0, 50.0, -50.0)

    # Green
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(50.0, -50.0, -50.0)

    # Yellow
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(50.0, -50.0, 50.0)

    # Right face
        # Magenta
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-50.0, 50.0, 50.0)

    # Blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-50.0, 50.0, -50.0)

    # Black
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-50.0, -50.0, -50.0)

    # Red
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-50.0, -50.0, 50.0)
    glEnd()

    glPopMatrix()

    # Show the graphics
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_DITHER)
    glShadeModel(GL_SMOOTH)

########################/
# Get Arrow Keys
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

def ChangeSize(w,  h):

    fAspect = 0.0

    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    fAspect = w / h
    gluPerspective(35.0, fAspect, 1.0, 1000.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -400.0)

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"RGB Cube")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
