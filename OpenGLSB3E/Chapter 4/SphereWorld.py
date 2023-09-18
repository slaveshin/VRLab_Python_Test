# SphereWorld.c
# OpenGL SuperBible
# Demonstrates an immersive 3D environment using actors
# and a camera.
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *
import random

NUM_SPHERES = 50
spheres = [GLTFrame() for i in range(NUM_SPHERES)]
frameCamera = GLTFrame()
yRot = 0.0
#################################
# This function does any needed initialization on the rendering
# context. 
def SetupRC():
    global spheres, frameCamera, NUM_SPHERES
    iSphere = 0.0

    # Bluish background
    glClearColor(0.0, 0.0, .50, 1.0)

    # Draw everything as wire frame
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    gltInitFrame(frameCamera)  # Initialize the camera

    # Randomly place the sphere inhabitants
    #for (iSphere = 0 iSphere < NUM_SPHERES iSphere++):
    for iSphere in range(0, NUM_SPHERES, 1):

        gltInitFrame(spheres[iSphere])    # Initialize the frame
        # Pick a random location between -20 and 20 at .1 increments
        spheres[iSphere].vLocation.value[0] = float(((random.random() * 32767 % 400) - 200) * 0.1)
        spheres[iSphere].vLocation.value[1] = 0.0
        spheres[iSphere].vLocation.value[2] = float(((random.random() * 32767 % 400) - 200) * 0.1)

#############################/
# Draw a gridded ground
def DrawGround():
    fExtent = 20.0
    fStep = 1.0
    y = -0.4
    iLine = 0.0

    glBegin(GL_LINES)
    #for (iLine = -fExtent iLine <= fExtent iLine += fStep)
    iLine = -fExtent
    while (iLine <= fExtent):

        glVertex3f(iLine, y, fExtent)    # Draw Z lines
        glVertex3f(iLine, y, -fExtent)

        glVertex3f(fExtent, y, iLine)
        glVertex3f(-fExtent, y, iLine)
        iLine += fStep


    glEnd()

# Called to draw scene
def RenderScene():
    global spheres, frameCamera, NUM_SPHERES, yRot
    i = 0.0
    yRot += 0.5 # Rotation angle for animation

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    gltApplyCameraTransform(frameCamera)

    # Draw the ground
    DrawGround()

    # Draw the randomly located spheres
    #for (i = 0 i < NUM_SPHERES i++)
    for i in range(0, NUM_SPHERES, 1):

        glPushMatrix()
        gltApplyActorTransform(spheres[i])
        glutSolidSphere(0.1, 13, 26)
        glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.0, -2.5)

    glPushMatrix()
    glRotatef(-yRot * 2.0, 0.0, 1.0, 0.0)
    glTranslatef(1.0, 0.0, 0.0)
    glutSolidSphere(0.1, 13, 26)
    glPopMatrix()

    glRotatef(yRot, 0.0, 1.0, 0.0)
    gltDrawTorus(0.35, 0.15, 40, 20)
    glPopMatrix()
    glPopMatrix()

    # Do the buffer Swap
    glutSwapBuffers()

# Respond to arrow keys by moving the camera frame of reference
def SpecialKeys(key, x, y):
    global frameCamera
    if (key == GLUT_KEY_UP):
        gltMoveFrameForward(frameCamera, 0.1)

    if (key == GLUT_KEY_DOWN):
        gltMoveFrameForward(frameCamera, -0.1)

    if (key == GLUT_KEY_LEFT):
        gltRotateFrameLocalY(frameCamera, 0.1)

    if (key == GLUT_KEY_RIGHT):
        gltRotateFrameLocalY(frameCamera, -0.1)

    # Refresh the Window
    glutPostRedisplay()

#############################/
# Called by GLUT library when idle (window not being
# resized or moved)
def TimerFunction(value):

    # Redraw the scene with new coordinates
    glutPostRedisplay()
    glutTimerFunc(3, TimerFunction, 1)

def ChangeSize(w, h):

    fAspect = 0.0

    # Prevent a divide by zero, when window is too short
    # (you cant make a window of zero width).
    if (h == 0):
        h = 1

    glViewport(0, 0, w, h)

    fAspect = w / h

    # Reset the coordinate system before modifying
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set the clipping volume
    gluPerspective(35.0, fAspect, 1.0, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL SphereWorld Demo")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)
    glutSpecialFunc(SpecialKeys)

    SetupRC()
    glutTimerFunc(33, TimerFunction, 1)

    glutMainLoop()
