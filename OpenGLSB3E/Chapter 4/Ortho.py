# Ortho.c
# OpenGL SuperBible
# Richard S. Wright Jr.
# Demonstrates Orthographic Projection

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rotation amounts
xRot = 0.0
yRot = 0.0

# Change viewing volume and viewport.  Called when window is resized
def ChangeSize(w, h):

    nRange = 120.0
    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Establish clipping volume (left, right, bottom, top, near, far)
    if (w <= h):
        glOrtho(-nRange, nRange, -nRange * h / w, nRange*h / w, -nRange * 2.0, nRange*2.0)
    else:
        glOrtho(-nRange * w / h, nRange*w / h, -nRange, nRange, -nRange * 2.0, nRange*2.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# This function does any needed initialization on the rendering
# context.  Here it sets up and initializes the lighting for
# the scene.
def SetupRC():

    # Light values and coordinates
    whiteLight = [ 0.45, 0.45, 0.45, 1.0 ]
    sourceLight = [ 0.25, 0.25, 0.25, 1.0 ]
    lightPos = [ -50., 25.0, 250.0, 0.0 ]

    glEnable(GL_DEPTH_TEST)	# Hidden surface removal
    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out
    glEnable(GL_CULL_FACE)		# Do not calculate inside of jet

    # Enable lighting
    glEnable(GL_LIGHTING)

    # Setup and enable light 0
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, whiteLight)
    glLightfv(GL_LIGHT0, GL_AMBIENT, sourceLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, sourceLight)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    glEnable(GL_LIGHT0)

    # Enable color tracking
    glEnable(GL_COLOR_MATERIAL)

    # Set Material properties to follow glColor values
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Black blue background
    glClearColor(0.0, 0.0, 0.0, 1.0)

# Respond to arrow keys
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

    xRot = int(xRot % 360)
    yRot = int(yRot % 360)

    # Refresh the Window
    glutPostRedisplay()

# Called to draw scene
def RenderScene():

    global xRot, yRot

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    fZ = 100.0
    bZ = -100.0

    # Save the matrix state and do the rotations
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Set material color, Red
    glColor3f(1.0, 0.0, 0.0)

    # Front Face #################/
    glBegin(GL_QUADS)
    # Pointing straight out Z
    glNormal3f(0.0, 0.0, 1.0)

    # Left Panel
    glVertex3f(-50.0, 50.0, fZ)
    glVertex3f(-50.0, -50.0, fZ)
    glVertex3f(-35.0, -50.0, fZ)
    glVertex3f(-35.0, 50.0, fZ)

    # Right Panel
    glVertex3f(50.0, 50.0, fZ)
    glVertex3f(35.0, 50.0, fZ)
    glVertex3f(35.0, -50.0, fZ)
    glVertex3f(50.0, -50.0, fZ)

    # Top Panel
    glVertex3f(-35.0, 50.0, fZ)
    glVertex3f(-35.0, 35.0, fZ)
    glVertex3f(35.0, 35.0, fZ)
    glVertex3f(35.0, 50.0, fZ)

    # Bottom Panel
    glVertex3f(-35.0, -35.0, fZ)
    glVertex3f(-35.0, -50.0, fZ)
    glVertex3f(35.0, -50.0, fZ)
    glVertex3f(35.0, -35.0, fZ)

    # Top length section ##############
    # Normal points up Y axis
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(-50.0, 50.0, fZ)
    glVertex3f(50.0, 50.0, fZ)
    glVertex3f(50.0, 50.0, bZ)
    glVertex3f(-50.0, 50.0, bZ)

    # Bottom section
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(-50.0, -50.0, fZ)
    glVertex3f(-50.0, -50.0, bZ)
    glVertex3f(50.0, -50.0, bZ)
    glVertex3f(50.0, -50.0, fZ)

    # Left section
    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(50.0, 50.0, fZ)
    glVertex3f(50.0, -50.0, fZ)
    glVertex3f(50.0, -50.0, bZ)
    glVertex3f(50.0, 50.0, bZ)

    # Right Section
    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(-50.0, 50.0, fZ)
    glVertex3f(-50.0, 50.0, bZ)
    glVertex3f(-50.0, -50.0, bZ)
    glVertex3f(-50.0, -50.0, fZ)
    glEnd()

    glFrontFace(GL_CW)		# clock-wise polygons face out

    glBegin(GL_QUADS)
    # Back section
    # Pointing straight out Z
    glNormal3f(0.0, 0.0, -1.0)

    # Left Panel
    glVertex3f(-50.0, 50.0, bZ)
    glVertex3f(-50.0, -50.0, bZ)
    glVertex3f(-35.0, -50.0, bZ)
    glVertex3f(-35.0, 50.0, bZ)

    # Right Panel
    glVertex3f(50.0, 50.0, bZ)
    glVertex3f(35.0, 50.0, bZ)
    glVertex3f(35.0, -50.0, bZ)
    glVertex3f(50.0, -50.0, bZ)

    # Top Panel
    glVertex3f(-35.0, 50.0, bZ)
    glVertex3f(-35.0, 35.0, bZ)
    glVertex3f(35.0, 35.0, bZ)
    glVertex3f(35.0, 50.0, bZ)

    # Bottom Panel
    glVertex3f(-35.0, -35.0, bZ)
    glVertex3f(-35.0, -50.0, bZ)
    glVertex3f(35.0, -50.0, bZ)
    glVertex3f(35.0, -35.0, bZ)

    # Insides ##############/
    glColor3f(0.75, 0.75, 0.75)

    # Normal points up Y axis
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(-35.0, 35.0, fZ)
    glVertex3f(35.0, 35.0, fZ)
    glVertex3f(35.0, 35.0, bZ)
    glVertex3f(-35.0, 35.0, bZ)

    # Bottom section
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(-35.0, -35.0, fZ)
    glVertex3f(-35.0, -35.0, bZ)
    glVertex3f(35.0, -35.0, bZ)
    glVertex3f(35.0, -35.0, fZ)

    # Left section
    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(-35.0, 35.0, fZ)
    glVertex3f(-35.0, 35.0, bZ)
    glVertex3f(-35.0, -35.0, bZ)
    glVertex3f(-35.0, -35.0, fZ)

    # Right Section
    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(35.0, 35.0, fZ)
    glVertex3f(35.0, -35.0, fZ)
    glVertex3f(35.0, -35.0, bZ)
    glVertex3f(35.0, 35.0, bZ)
    glEnd()

    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out

    # Restore the matrix state
    glPopMatrix()

    # Buffer swap
    glutSwapBuffers()

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Orthographic Projection")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()