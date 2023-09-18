# MotionBlur.c
# OpenGL SuperBible
# Demonstrates Motion Blur with the Accumulation buffer
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *


# Light and material Data
fLightPos = [-100.0, 100.0, 50.0, 1.0]  # Point source
fLightPosMirror = [-100.0, -100.0, 50.0, 1.0]
fNoLight = [0.0, 0.0, 0.0, 0.0]
fLowLight = [0.25, 0.25, 0.25, 1.0]
fBrightLight = [1.0, 1.0, 1.0, 1.0]

yRot = 45.0

#################################
# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    global fLowLight, fNoLight, fBrightLight, fLightPos

    # Grayish background
    glClearColor(fLowLight[0], fLowLight[1], fLowLight[2], fLowLight[3])

    # Cull backs of polygons
    glCullFace(GL_BACK)
    glFrontFace(GL_CCW)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    # Setup light parameters
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, fNoLight)
    glLightfv(GL_LIGHT0, GL_AMBIENT, fLowLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, fBrightLight)
    glLightfv(GL_LIGHT0, GL_SPECULAR, fBrightLight)
    glLightfv(GL_LIGHT0, GL_POSITION, fLightPos)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Mostly use material tracking
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glMateriali(GL_FRONT, GL_SHININESS, 128)


#############################/
# Draw the ground as a series of triangle strips. The 
# shading model and colors are set such that we end up 
# with a black and white checkerboard pattern.
def DrawGround():

    fExtent = 20.0
    fStep = 0.5
    y = 0.0
    fColor = 0.0
    iStrip = 0.0
    iRun = 0.0
    iBounce = 0

    glShadeModel(GL_FLAT)
    #for (iStrip = -fExtent iStrip <= fExtent iStrip += fStep):
    iStrip = -fExtent
    while (iStrip <= fExtent):
        glBegin(GL_TRIANGLE_STRIP)

        #for (iRun = fExtent iRun >= -fExtent iRun -= fStep):
        iRun = fExtent
        while (iRun >= -fExtent):

            if ((iBounce % 2) == 0):
                fColor = 1.0
            else:
                fColor = 0.0

            glColor4f(fColor, fColor, fColor, 0.5)
            glVertex3f(iStrip, y, iRun)
            glVertex3f(iStrip + fStep, y, iRun)

            iBounce += 1
            iRun -= fStep

        iStrip += fStep
        glEnd()

    glShadeModel(GL_SMOOTH)


##############################/
# Draw the ground and the revolving sphere
def DrawGeometry():

    global yRot

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    DrawGround()

    # Place the moving sphere
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(0.0, 0.5, -3.5)
    glRotatef(-(yRot * 2.0), 0.0, 1.0, 0.0)
    glTranslatef(1.0, 0.0, 0.0)
    glutSolidSphere(0.1, 17, 9)
    glPopMatrix()


###################################/        
# Called to draw scene. The world is drawn multiple times with each
# frame blended with the last. The current rotation is advanced each
# time to create the illusion of motion blur.
def RenderScene():

    global yRot

    fPass = 0.0
    fPasses = 10.0

    # Set the current rotation back a few degrees
    yRot = 35.0

    #for (fPass = 0.0f fPass < fPasses fPass += 1.0)
    for fPass in range(0, int(fPasses), 1):

        yRot += .75 #1.0f / (fPass+1.0f)

        # Draw sphere
        DrawGeometry()

        # Accumulate to back buffer
        if (fPass == 0.0):
            glAccum(GL_LOAD, 0.5)
        else:
            glAccum(GL_ACCUM, 0.5 * (1.0 / fPasses))


    # copy accumulation buffer to color buffer and
    # do the buffer Swap
    glAccum(GL_RETURN, 1.0)
    glutSwapBuffers()



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
    glTranslatef(0.0, -0.4, 0.0)


##############################/
# Main program entrypoint
if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_ACCUM)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Motion Blur with the Accumulation Buffer")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)

    SetupRC()
    glutMainLoop()
