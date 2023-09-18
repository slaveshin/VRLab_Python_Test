# LitJet.c
# OpenGL SuperBible
# Demonstrates OpenGL Lighting
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *

# Rotation amounts
xRot = 0.0
yRot = 0.0


# Called to draw scene
def RenderScene():

    global xRot, yRot

    vNormal = GLTVector3()	# Storeage for calculated surface normal

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Save the matrix state and do the rotations
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 1.0, 0.0)


    # Nose Cone - Points straight down
        # Set material color
    glColor3ub(128, 128, 128)
    glBegin(GL_TRIANGLES)
    glNormal3f(0.0, -1.0, 0.0)
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 0.0, 60.0)
    glVertex3f(-15.0, 0.0, 30.0)
    glVertex3f(15.0, 0.0, 30.0)


    # Verticies for this panel
    vPoints = [GLTVector3(),
              GLTVector3(),
              GLTVector3()]

    vPoints[0].value = [15.0, 0.0, 30.0]
    vPoints[1].value = [0.0, 15.0, 30.0]
    vPoints[2].value = [0.0, 0.0, 60.0]

    # Calculate the normal for the plane
    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
              GLTVector3(),
              GLTVector3()]

    vPoints[0].value = [10.0, 0.0, 60.0]
    vPoints[1].value = [0.0, 15.0, 30.0]
    vPoints[2].value = [-15.0, 0.0, 30.0 ]

    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    # Body of the Plane ############

    vPoints = [GLTVector3(),
              GLTVector3(),
              GLTVector3()]

    vPoints[0].value = [-15.0, 0.0, 30.0]
    vPoints[1].value = [0.0, 15.0, 30.0]
    vPoints[2].value = [0.0, 0.0, -56.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [0.0, 0.0, -56.0]
    vPoints[1].value = [0.0, 15.0, 30.0]
    vPoints[2].value = [15.0,0.0,30.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)


    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(15.0, 0.0, 30.0)
    glVertex3f(-15.0, 0.0, 30.0)
    glVertex3f(0.0, 0.0, -56.0)

    #######################/
    # Left wing
    # Large triangle for bottom of wing
    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [0.0, 2.0, 27.0]
    vPoints[1].value = [-60.0, 2.0, -8.0]
    vPoints[2].value = [60.0, 2.0, -8.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [60.0, 2.0, -8.0]
    vPoints[1].value = [0.0, 7.0, -8.0]
    vPoints[2].value = [0.0, 2.0,27.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [60.0, 2.0, -8.0]
    vPoints[1].value = [-60.0, 2.0, -8.0]
    vPoints[2].value = [0.0, 7.0,-8.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [0.0, 2.0, -27.0]
    vPoints[1].value = [0.0, 7.0, -8.0]
    vPoints[2].value = [-60.0, 2.0, -8.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)


    #Tail section###############/
    # Bottom of back fin
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(-30.0, -0.50, -57.0)
    glVertex3f(30.0, -0.50, -57.0)
    glVertex3f(0.0, -0.50, -40.0)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [0.0, -0.5, -40.0]
    vPoints[1].value = [30.0, -0.5, -57.0]
    vPoints[2].value = [0.0, 4.0, -57.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [0.0, 4.0, -57.0]
    vPoints[1].value = [-30.0, -0.5, -57.0]
    vPoints[2].value = [0.0, -0.5, -40.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [30.0, -0.5, -57.0]
    vPoints[1].value = [-30.0, -0.5, -57.0]
    vPoints[2].value = [0.0, 4.0, -57.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [0.0, 0.5, -40.0]
    vPoints[1].value = [3.0, 0.5, -57.0]
    vPoints[2].value = [0.0, 25.0, -65.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [0.0, 25.0, -65.0]
    vPoints[1].value = [-3.0, 0.5, -57.0]
    vPoints[2].value = [0.0, 0.5, -40.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)

    vPoints = [GLTVector3(),
               GLTVector3(),
               GLTVector3()]

    vPoints[0].value = [3.0, 0.5, -57.0]
    vPoints[1].value = [-3.0, 0.5, -57.0]
    vPoints[2].value = [0.0, 25.0, -65.0]


    gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
    glNormal3fv(vNormal.value)
    glVertex3fv(vPoints[0].value)
    glVertex3fv(vPoints[1].value)
    glVertex3fv(vPoints[2].value)


    glEnd()

    # Restore the matrix state
    glPopMatrix()
    # Display the results
    glutSwapBuffers()

# This function does any needed initialization on the rendering
# context. 
def SetupRC():

    # Light values and coordinates
    ambientLight = [ 0.3, 0.3, 0.3, 1.0 ]
    diffuseLight = [ 0.7, 0.7, 0.7, 1.0 ]

    glEnable(GL_DEPTH_TEST)	# Hidden surface removal
    glFrontFace(GL_CCW)		# Counter clock-wise polygons face out
    glEnable(GL_CULL_FACE)		# Do not calculate inside of jet

    # Enable lighting
    glEnable(GL_LIGHTING)

    # Setup and enable light 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
    glEnable(GL_LIGHT0)

    # Enable color tracking
    glEnable(GL_COLOR_MATERIAL)

    # Set Material properties to follow glColor values
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Light blue background
    glClearColor(0.0, 0.0, 1.0, 1.0)

##########################/
# Handle arrow keys
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


#############################
# Reset projection and light position
def ChangeSize(w, h):

    fAspect = 0.0
    lightPos = [ -50., 50.0, 100.0, 1.0 ]

    # Prevent a divide by zero
    if (h == 0):
        h = 1

    # Set Viewport to window dimensions
    glViewport(0, 0, w, h)

    # Reset coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    fAspect = w / h
    gluPerspective(45.0, fAspect, 1.0, 225.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    glTranslatef(0.0, 0.0, -150.0)

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lighted Jet")
    glutReshapeFunc(ChangeSize)
    glutSpecialFunc(SpecialKeys)
    glutDisplayFunc(RenderScene)
    SetupRC()
    glutMainLoop()
