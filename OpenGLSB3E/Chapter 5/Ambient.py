# Ambient.c
# OpenGL SuperBible
# Beginning of OpenGL lighting sample
# Demonstrates Ambient Lighting
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

    # Save the matrix state
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)

    # Nose Cone ##############/
    # Bright Green
    glColor3ub(0, 255, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 0.0, 60.0)
    glVertex3f(-15.0, 0.0, 30.0)
    glVertex3f(15.0, 0.0, 30.0)

    glVertex3f(15.0, 0.0, 30.0)
    glVertex3f(0.0, 15.0, 30.0)
    glVertex3f(0.0, 0.0, 60.0)

    glVertex3f(0.0, 0.0, 60.0)
    glVertex3f(0.0, 15.0, 30.0)
    glVertex3f(-15.0, 0.0, 30.0)

    # Body of the Plane ############
    # light gray
    glColor3ub(192, 192, 192)
    glVertex3f(-15.0, 0.0, 30.0)
    glVertex3f(0.0, 15.0, 30.0)
    glVertex3f(0.0, 0.0, -56.0)

    glVertex3f(0.0, 0.0, -56.0)
    glVertex3f(0.0, 15.0, 30.0)
    glVertex3f(15.0, 0.0, 30.0)

    glVertex3f(15.0, 0.0, 30.0)
    glVertex3f(-15.0, 0.0, 30.0)
    glVertex3f(0.0, 0.0, -56.0)


    #######################/
    # Left wing
    # Dark gray
    glColor3ub(64, 64, 64)
    glVertex3f(0.0, 2.0, 27.0)
    glVertex3f(-60.0, 2.0, -8.0)
    glVertex3f(60.0, 2.0, -8.0)

    glVertex3f(60.0, 2.0, -8.0)
    glVertex3f(0.0, 7.0, -8.0)
    glVertex3f(0.0, 2.0, 27.0)

    glVertex3f(60.0, 2.0, -8.0)
    glVertex3f(-60.0, 2.0, -8.0)
    glVertex3f(0.0, 7.0, -8.0)


    # Other wing top section
    glVertex3f(0.0, 2.0, 27.0)
    glVertex3f(0.0, 7.0, -8.0)
    glVertex3f(-60.0, 2.0, -8.0)

    # Tail section###############/
    # Bottom of back fin
    glColor3ub(255, 255, 0)
    glVertex3f(-30.0, -0.50, -57.0)
    glVertex3f(30.0, -0.50, -57.0)
    glVertex3f(0.0, -0.50, -40.0)

    # top of left side
    glVertex3f(0.0, -0.5, -40.0)
    glVertex3f(30.0, -0.5, -57.0)
    glVertex3f(0.0, 4.0, -57.0)

    # top of right side
    glVertex3f(0.0, 4.0, -57.0)
    glVertex3f(-30.0, -0.5, -57.0)
    glVertex3f(0.0, -0.5, -40.0)

    # back of bottom of tail
    glVertex3f(30.0, -0.5, -57.0)
    glVertex3f(-30.0, -0.5, -57.0)
    glVertex3f(0.0, 4.0, -57.0)


    # Top of Tail section left
    glColor3ub(255, 0, 0)
    glVertex3f(0.0, 0.5, -40.0)
    glVertex3f(3.0, 0.5, -57.0)
    glVertex3f(0.0, 25.0, -65.0)

    glVertex3f(0.0, 25.0, -65.0)
    glVertex3f(-3.0, 0.5, -57.0)
    glVertex3f(0.0, 0.5, -40.0)


    # Back of horizontal section
    glVertex3f(3.0, 0.5, -57.0)
    glVertex3f(-3.0, 0.5, -57.0)
    glVertex3f(0.0, 25.0, -65.0)
    glEnd()

    glPopMatrix()

    # Display the results
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    # Light values
    # Bright white light
    ambientLight = [1.0, 1.0, 1.0, 1.0]

    glEnable(GL_DEPTH_TEST)	# Hidden surface removal
    glEnable(GL_CULL_FACE)		# Do not calculate inside of jet
    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out

    # Lighting stuff
    glEnable(GL_LIGHTING)			# Enable lighting

    # Set light model to use ambient light specified by ambientLight
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambientLight)

    glEnable(GL_COLOR_MATERIAL)	# Enable Material color tracking

    # Front material ambient and diffuse colors track glColor
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Nice light blue
    glClearColor(0.0, 0.0, 05., 1.0)

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

    nRange = 80.0
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
        glOrtho(-nRange, nRange, -nRange * h / w, nRange*h / w, -nRange, nRange)
    else:
        glOrtho(-nRange * w / h, nRange*w / h, -nRange, nRange, -nRange, nRange)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Ambient Light Jet")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
