# Smoother.c
# OpenGL SuperBible
# Demonstrates point, line, and polygon smoothing
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *
from math import *
import random

# Array of small stars
SMALL_STARS = 100
#GLTVector2  vSmallStars[SMALL_STARS]
vSmallStars = []
for _ in range(SMALL_STARS): vSmallStars.append(GLTVector2())

MEDIUM_STARS = 40
#GLTVector2 vMediumStars[MEDIUM_STARS]
vMediumStars = []
for _ in range(MEDIUM_STARS): vMediumStars.append(GLTVector2())

LARGE_STARS =  15
#GLTVector2 vLargeStars[LARGE_STARS]
vLargeStars = []
for _ in range(LARGE_STARS): vLargeStars.append(GLTVector2())

SCREEN_X = 800
SCREEN_Y = 600

###################################/
# Reset flags as appropriate in response to menu selections
def ProcessMenu(value):

    if (value == 1):
        # Turn on antialiasing, and give hint to do the best
        # job possible.
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_POINT_SMOOTH)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_POLYGON_SMOOTH)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)

    if (value == 2):
        # Turn off blending and all smoothing
        glDisable(GL_BLEND)
        glDisable(GL_LINE_SMOOTH)
        glDisable(GL_POINT_SMOOTH)
        glDisable(GL_POLYGON_SMOOTH)


    # Trigger a redraw
    glutPostRedisplay()


#########################/
# Called to draw scene
def RenderScene():

    global SMALL_STARS, MEDIUM_STARS, vSmallStars, vMediumStars, LARGE_STARS, vLargeStars

    i = 0.0                # Loop variable
    x = 700.0     # Location and radius o moon
    y = 500.0
    r = 50.0
    angle = 0.0   # Another looping variable

    # Clear the window
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Everything is white
    glColor3f(1.0, 1.0, 1.0)

    # Draw small stars
    glPointSize(1.0)
    glBegin(GL_POINTS)
    #for (i = 0 i < SMALL_STARS i++)
    for i in range(0, SMALL_STARS, 1):
        glVertex2fv(vSmallStars[i].value)
    glEnd()

    # Draw medium sized stars
    glPointSize(3.05)
    glBegin(GL_POINTS)
    #for (i = 0 i < MEDIUM_STARS i++)
    for i in range(0, MEDIUM_STARS, 1):
        glVertex2fv(vMediumStars[i].value)
    glEnd()

    # Draw largest stars
    glPointSize(5.5)
    glBegin(GL_POINTS)
    #for (i = 0 i < LARGE_STARS i++)
    for i in range(0, LARGE_STARS, 1):
        glVertex2fv(vLargeStars[i].value)
    glEnd()

    # Draw the "moon"
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    #for (angle = 0 angle < 2.0 * 3.141592 angle += 0.1)
    angle = 0
    while (angle < 2.0 * 3.141592):
        glVertex2f(x + float(cos(angle)) * r, y + float(sin(angle) * r))
        angle += 0.1
    glVertex2f(x + r, y)
    glEnd()

	# Draw distant horizon
    glLineWidth(3.5)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 25.0)
    glVertex2f(50.0, 100.0)
    glVertex2f(100.0, 25.0)
    glVertex2f(225.0, 125.0)
    glVertex2f(300.0, 50.0)
    glVertex2f(375.0, 100.0)
    glVertex2f(460.0, 25.0)
    glVertex2f(525.0, 100.0)
    glVertex2f(600.0, 20.0)
    glVertex2f(675.0, 70.0)
    glVertex2f(750.0, 25.0)
    glVertex2f(800.0, 90.0)
    glEnd()


    # Swap buffers
    glutSwapBuffers()



# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    global SMALL_STARS, vSmallStars, MEDIUM_STARS, vMediumStars, LARGE_STARS, vLargeStars, SCREEN_X, SCREEN_Y

    i = 0.0

    # Populate star list
	#for (i = 0 i < SMALL_STARS i++)
    for i in range(0, SMALL_STARS, 1):

        vSmallStars[i].value[0] = (random.random() * SCREEN_X)
        vSmallStars[i].value[1] = (random.random() * (SCREEN_Y - 100)) + 100.0


    # Populate star list
    #for (i = 0 i < MEDIUM_STARS i++)
    for i in range(0, MEDIUM_STARS, 1):

        vMediumStars[i].value[0] = (random.random() * SCREEN_X * 10) / 10.0
        vMediumStars[i].value[1] = (random.random() * (SCREEN_Y - 100)) + 100.0


    # Populate star list
    #for (i = 0 i < LARGE_STARS i++)
    for i in range(0, LARGE_STARS, 1):

        vLargeStars[i].value[0] = (random.random() * SCREEN_X * 10) / 10.0
        vLargeStars[i].value[1] = (random.random() * (SCREEN_Y - 100)*10.0) / 10.0 + 100.0



    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Set drawing color to white
    glColor3f(0.0, 0.0, 0.0)




def ChangeSize(w, h):

    global SCREEN_X, SCREEN_Y

    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset projection matrix stack
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Establish clipping volume (left, right, bottom, top, near, far)
    gluOrtho2D(0.0, SCREEN_X, 0.0, SCREEN_Y)


    # Reset Model view matrix stack
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Smoothing Out The Jaggies")

    # Create the Menu
    glutCreateMenu(ProcessMenu)
    glutAddMenuEntry("Antialiased Rendering", 1)
    glutAddMenuEntry("Normal Rendering", 2)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
