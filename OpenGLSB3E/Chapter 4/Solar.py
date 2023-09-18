# Solar.c
# OpenGL SuperBible
# Demonstrates OpenGL nested coordinate transformations
# and perspective
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Lighting values
whiteLight = [0.2, 0.2, 0.2, 1.0]
sourceLight = [0.8, 0.8, 0.8, 1.0]
lightPos = [0.0, 0.0, 0.0, 1.0]
fMoonRot = 0.0
fEarthRot = 0.0

# Called to draw scene
def RenderScene():

    global lightPos, fMoonRot, fEarthRot

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Save the matrix state and do the rotations
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    # Translate the whole scene out and into view
    glTranslatef(0.0, 0.0, -300.0)

    # Set material color, Red
    # Sun
    glDisable(GL_LIGHTING)
    glColor3ub(255, 255, 0)
    glutSolidSphere(15.0, 30, 17)
    glEnable(GL_LIGHTING)

    # Move the light after we draw the sun!
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)

    # Rotate coordinate system
    glRotatef(fEarthRot, 0.0, 1.0, 0.0)

    # Draw the Earth
    glColor3ub(0, 0, 255)
    glTranslatef(105.0, 0.0, 0.0)
    glutSolidSphere(15.0, 30, 17)

    # Rotate from Earth based coordinates and draw Moon
    glColor3ub(200, 200, 200)
    glRotatef(fMoonRot, 0.0, 1.0, 0.0)
    glTranslatef(30.0, 0.0, 0.0)
    fMoonRot += 15.0
    if (fMoonRot > 360.0):
        fMoonRot = 0.0

    glutSolidSphere(6.0, 30, 17)

    # Restore the matrix state
    glPopMatrix()	# Modelview matrix

    # Step earth orbit 5 degrees
    fEarthRot += 5.0
    if (fEarthRot > 360.0):
        fEarthRot = 0.0

    # Show the image
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    global whiteLight, sourceLight, lightPos

    # Light values and coordinates
    glEnable(GL_DEPTH_TEST)	# Hidden surface removal
    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out
    glEnable(GL_CULL_FACE)		# Do not calculate inside of jet

    # Enable lighting
    glEnable(GL_LIGHTING)

    # Setup and enable light 0
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, whiteLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, sourceLight)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    glEnable(GL_LIGHT0)

    # Enable color tracking
    glEnable(GL_COLOR_MATERIAL)

    # Set Material properties to follow glColor values
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Black blue background
    glClearColor(0.0, 0.0, 0.0, 1.0)

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

    # Calculate aspect ratio of the window
    fAspect = w / h

    # Set the perspective coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # field of view of 45 degrees, near and far planes 1.0 and 425
    gluPerspective(45.0, fAspect, 1.0, 425.0)

    # Modelview matrix reset
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Earth/Moon/Sun System")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)
    glutTimerFunc(250, TimerFunc, 1)
    SetupRC()
    glutMainLoop()
