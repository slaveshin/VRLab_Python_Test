# Spot.c
# OpenGL SuperBible
# Demonstrates OpenGL Spotlight
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Rotation amounts
xRot = 0.0
yRot = 0.0

# Light values and coordinates
lightPos = [0.0, 0.0, 75.0, 1.0]
specular = [1.0, 1.0, 1.0, 1.0]
specref = [1.0, 1.0, 1.0, 1.0]
ambientLight = [0.5, 0.5, 0.5, 1.0]
spotDir = [0.0, 0.0, -1.0]

# Flags for effects
MODE_FLAT = 1
MODE_SMOOTH = 2
MODE_VERYLOW = 3
MODE_MEDIUM = 4
MODE_VERYHIGH = 5

iShade = MODE_FLAT
iTess = MODE_VERYLOW

#######################################/
# Reset flags as appropriate in response to menu selections
def ProcessMenu(value):

    global MODE_FLAT, MODE_SMOOTH, MODE_VERYHIGH, MODE_MEDIUM, MODE_VERYHIGH, iShade, iTess

    if (value == 1):
        iShade = MODE_FLAT

    if (value == 2):
        iShade = MODE_SMOOTH

    if (value == 3):
        iTess = MODE_VERYLOW

    if (value == 4):
        iTess = MODE_MEDIUM

    else:
        iTess = MODE_VERYHIGH

    glutPostRedisplay()


# Called to draw scene
def RenderScene():

    global xRot, yRot, lightPos, spotDir, MODE_FLAT, MODE_SMOOTH, MODE_VERYLOW, MODE_MEDIUM, MODE_VERYHIGH, iShade, iTess

    if (iShade == MODE_FLAT):
        glShadeModel(GL_FLAT)
    else: # 	iShade = MODE_SMOOTH
        glShadeModel(GL_SMOOTH)

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # First place the light
    # Save the coordinate transformation
    glPushMatrix()
    # Rotate coordinate system
    glRotatef(yRot, 0.0, 1.0, 0.0)
    glRotatef(xRot, 1.0, 0.0, 0.0)

    # Specify new position and direction in rotated coords.
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, spotDir)

    # Draw a red cone to enclose the light source
    glColor3ub(255, 0, 0)

    # Translate origin to move the cone out to where the light
    # is positioned.
    glTranslatef(lightPos[0], lightPos[1], lightPos[2])
    glutSolidCone(4.0, 6.0, 15, 15)

    # Draw a smaller displaced sphere to denote the light bulb
    # Save the lighting state variables
    glPushAttrib(GL_LIGHTING_BIT)

    # Turn off lighting and specify a bright yellow sphere
    glDisable(GL_LIGHTING)
    glColor3ub(255, 255, 0)
    glutSolidSphere(3.0, 15, 15)

    # Restore lighting state variables
    glPopAttrib()

    # Restore coordinate transformations
    glPopMatrix()


    # Set material color and draw a sphere in the middle
    glColor3ub(0, 0, 255)

    if (iTess == MODE_VERYLOW):
        glutSolidSphere(30.0, 7, 7)
    else:
        if (iTess == MODE_MEDIUM):
            glutSolidSphere(30.0, 15, 15)
        else: #  iTess = MODE_MEDIUM
            glutSolidSphere(30.0, 50, 50)

    # Display the results
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    global ambientLight, specular, lightPos, specref

    glEnable(GL_DEPTH_TEST)	# Hidden surface removal
    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out
    glEnable(GL_CULL_FACE)		# Do not try to display the back sides

    # Enable lighting
    glEnable(GL_LIGHTING)

    # Setup and enable light 0
    # Supply a slight ambient light so the objects can be seen
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambientLight)

    # The light is composed of just a diffuse and specular components
    glLightfv(GL_LIGHT0, GL_DIFFUSE, ambientLight)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)

    # Specific spot effects
    # Cut off angle is 60 degrees
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 50.0)

    # Enable this light in particular
    glEnable(GL_LIGHT0)

    # Enable color tracking
    glEnable(GL_COLOR_MATERIAL)

    # Set Material properties to follow glColor values
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # All materials hereafter have full specular reflectivity
    # with a high shine
    glMaterialfv(GL_FRONT, GL_SPECULAR, specref)
    glMateriali(GL_FRONT, GL_SHININESS, 128)


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

    # Establish viewing volume
    fAspect = w / h
    gluPerspective(35.0, fAspect, 1.0, 500.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -250.0)

if __name__ == '__main__':

    nMenu = 0.0

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Spot Light")

    # Create the Menu
    nMenu = glutCreateMenu(ProcessMenu)
    glutAddMenuEntry("Flat Shading", 1)
    glutAddMenuEntry("Smooth Shading", 2)
    glutAddMenuEntry("VL Tess", 3)
    glutAddMenuEntry("MD Tess", 4)
    glutAddMenuEntry("VH Tess", 5)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
