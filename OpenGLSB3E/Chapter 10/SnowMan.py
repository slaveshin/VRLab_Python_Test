# Snowman.c
# Demonstrates using Quadric Objects
# OpenGL SuperBible
# Richard S. Wright Jr.

#include "../../Common/OpenGLSB.h"	# System and OpenGL Stuff
#include "../../Common/GLTools.h"   # GLTools

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *
from Common.TGACommon import *

# Rotation amounts
xRot = 0.0
yRot = 0.0


######################################
# Change viewing volume and viewport.  Called when window is resized
def ChangeSize(w, h):

    fAspect = 0.0

    # Prevent a divide by zero
    if(h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    fAspect = w/h

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Produce the perspective projection
    gluPerspective(35.0, fAspect, 1.0, 40.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# This function does any needed initialization on the rendering
# context.  Here it sets up and initializes the lighting for
# the scene.
def SetupRC():

    # Light values and coordinates
    whiteLight = [ 0.05, 0.05, 0.05, 1.0 ]
    sourceLight = [ 0.25, 0.25, 0.25, 1.0 ]
    lightPos = [ -10., 5.0, 5.0, 1.0 ]

    glEnable(GL_DEPTH_TEST)	# Hidden surface removal
    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out
    glEnable(GL_CULL_FACE)		# Do not calculate inside

    # Enable lighting
    glEnable(GL_LIGHTING)

    # Setup and enable light 0
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT,whiteLight)
    glLightfv(GL_LIGHT0,GL_AMBIENT,sourceLight)
    glLightfv(GL_LIGHT0,GL_DIFFUSE,sourceLight)
    glLightfv(GL_LIGHT0,GL_POSITION,lightPos)
    glEnable(GL_LIGHT0)

    # Enable color tracking
    glEnable(GL_COLOR_MATERIAL)

    # Set Material properties to follow glColor values
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Black blue background
    glClearColor(0.25, 0.25, 0.50, 1.0 )

# Respond to arrow keys
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

    xRot = xRot % 360
    yRot = yRot % 360

    # Refresh the Window
    glutPostRedisplay()

# Called to draw scene
def RenderScene():

    global xRot, yRot

    pObj= 0.0 # Quadric Object

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Save the matrix state and do the rotations
    glPushMatrix()
    # Move object back and do in place rotation
    glTranslatef(0.0, -1.0, -5.0)
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Draw something
    pObj = gluNewQuadric()
    gluQuadricNormals(pObj, GLU_SMOOTH)

    # Main Body
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    gluSphere(pObj, .40, 26, 13)  # Bottom

    glTranslatef(0.0, .550, 0.0) # Mid section
    gluSphere(pObj, .3, 26, 13)

    glTranslatef(0.0, 0.45, 0.0) # Head
    gluSphere(pObj, 0.24, 26, 13)

    # Eyes
    glColor3f(0.0, 0.0, 0.0)
    glTranslatef(0.1, 0.1, 0.21)
    gluSphere(pObj, 0.02, 26, 13)

    glTranslatef(-0.2, 0.0, 0.0)
    gluSphere(pObj, 0.02, 26, 13)

    # Nose
    glColor3f(1.0, 0.3, 0.3)
    glTranslatef(0.1, -0.12, 0.0)
    gluCylinder(pObj, 0.04, 0.0, 0.3, 26, 13)
    glPopMatrix()

    # Hat
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glTranslatef(0.0, 1.17, 0.0)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    gluCylinder(pObj, 0.17, 0.17, 0.4, 26, 13)

    # Hat brim
    glDisable(GL_CULL_FACE)
    gluDisk(pObj, 0.17, 0.28, 26, 13)
    glEnable(GL_CULL_FACE)

    glTranslatef(0.0, 0.0, 0.40)
    gluDisk(pObj, 0.0, 0.17, 26, 13)
    glPopMatrix()

    # Restore the matrix state
    glPopMatrix()

    # Buffer swap
    glutSwapBuffers()

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Modeling with Quadrics")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()