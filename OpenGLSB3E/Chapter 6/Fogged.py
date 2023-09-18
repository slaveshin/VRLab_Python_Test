# SphereWorld.c
# OpenGL SuperBible
# Demonstrates an immersive 3D environment using actors
# and a camera. This version adds lights and material properties
# and shadows.
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *
import random

NUM_SPHERES  = 30
spheres = [GLTFrame() for i in range(NUM_SPHERES)]
frameCamera = GLTFrame()
yRot = 0.0

# Light and material Data
fLightPos = GLTVector4()
fLightPos.value = [-100.0, 100.0, 50.0, 1.0]  # Point source
fNoLight = [0.0, 0.0, 0.0, 0.0]
fLowLight = [0.25, 0.25, 0.25, 1.0]
fBrightLight = [1.0, 1.0, 1.0, 1.0]

mShadowMatrix = GLTMatrix()


#################################
# This function does any needed initialization on the rendering
# context.
def SetupRC():

	global NUM_SPHERES, spheres, mShadowMatrix, fLightPos, fNoLight, fLowLight, fBrightLight

	# Calculate shadow matrix
	vPoints = [GLTVector3(),
			   GLTVector3(),
			   GLTVector3()]

	vPoints[0].value = [0.0, -0.4, 0.0]
	vPoints[1].value = [10.0, -0.4, 0.0]
	vPoints[2].value = [5.0, -0.4, -5.0]

	iSphere = 0.0

	# Grayish background
	glClearColor(fLowLight[0], fLowLight[1], fLowLight[2], fLowLight[3])

	# Setup Fog parameters
	glEnable(GL_FOG)                   # Turn Fog on
	glFogfv(GL_FOG_COLOR, fLowLight)   # Set fog color to match background
	glFogf(GL_FOG_START, 5.0)         # How far away does the fog start
	glFogf(GL_FOG_END, 30.0)          # How far away does the fog stop
	glFogi(GL_FOG_MODE, GL_LINEAR)     # Which fog equation do I use?

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
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)


	gltMakeShadowMatrix(vPoints, fLightPos, mShadowMatrix)

	# Mostly use material tracking
	glEnable(GL_COLOR_MATERIAL)
	glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
	glMateriali(GL_FRONT, GL_SHININESS, 128)

	gltInitFrame(frameCamera)  # Initialize the camera

	# Randomly place the sphere inhabitants
	for iSphere in range(0, NUM_SPHERES, 1):

		gltInitFrame(spheres[iSphere])    # Initialize the frame

		# Pick a random location between -20 and 20 at .1 increments
		spheres[iSphere].vLocation.value[0] = float(((random.random() * 32767 % 400) - 200) * 0.1)
		spheres[iSphere].vLocation.value[1] = 0.0
		spheres[iSphere].vLocation.value[2] = float(((random.random() * 32767 % 400) - 200) * 0.1)



#############################/
# Draw the ground as a series of triangle strips
def DrawGround():

	fExtent = 20.0
	fStep = 1.0
	y = -0.4
	iStrip = 0.0
	iRun = 0.0

	#for (iStrip = -fExtent ; iStrip <= fExtent ; iStrip += fStep)
	iStrip = -fExtent
	while (iStrip <= fExtent):

		glBegin(GL_TRIANGLE_STRIP)
		glNormal3f(0.0, 1.0, 0.0)   # All Point up

		#for (iRun = fExtent iRun >= -fExtent iRun -= fStep)
		iRun = fExtent
		while (iRun >= -fExtent):

			glVertex3f(iStrip, y, iRun)
			glVertex3f(iStrip + fStep, y, iRun)
			iRun -= fStep

		iStrip += fStep

		glEnd()
	

###################################/
# Draw random inhabitants and the rotating torus/sphere duo
def DrawInhabitants(nShadow):

	global NUM_SPHERES, spheres, fBrightLight, fNoLight, yRot

	i = 0.0

	if (nShadow == 0):
		yRot += 0.5
	else:
		glColor3f(0.0, 0.0, 0.0)

	# Draw the randomly located spheres
	if (nShadow == 0):
		glColor3f(0.0, 1.0, 0.0)


	#for (i = 0 i < NUM_SPHERES i++)
	for i in range (0, NUM_SPHERES, 1):

		glPushMatrix()
		gltApplyActorTransform(spheres[i])
		glutSolidSphere(0.3, 17, 9)
		glPopMatrix()


	glPushMatrix()
	glTranslatef(0.0, 0.1, -2.5)

	if (nShadow == 0):
		glColor3f(0.0, 0.0, 1.0)

	glPushMatrix()
	glRotatef(-yRot * 2.0, 0.0, 1.0, 0.0)
	glTranslatef(1.0, 0.0, 0.0)
	glutSolidSphere(0.1, 17, 9)
	glPopMatrix()

	if (nShadow == 0):

		# Torus alone will be specular
		glColor3f(1.0, 0.0, 0.0)
		glMaterialfv(GL_FRONT, GL_SPECULAR, fBrightLight)


	glRotatef(yRot, 0.0, 1.0, 0.0)
	gltDrawTorus(0.35, 0.15, 61, 37)
	glMaterialfv(GL_FRONT, GL_SPECULAR, fNoLight)
	glPopMatrix()



# Called to draw scene
def RenderScene():

	global frameCamera, fLightPos, mShadowMatrix

	# Clear the window with current clearing color
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_ACCUM_BUFFER_BIT)

	glPushMatrix()
	gltApplyCameraTransform(frameCamera)

	# Position light before any other transformations
	glLightfv(GL_LIGHT0, GL_POSITION, fLightPos.value)

	# Draw the ground
	glColor3f(0.60, .40, .10)
	DrawGround()

	# Draw shadows irst
	glDisable(GL_DEPTH_TEST)
	glDisable(GL_LIGHTING)
	glPushMatrix()
	glMultMatrixf(mShadowMatrix.value)
	DrawInhabitants(1)
	glPopMatrix()
	glEnable(GL_LIGHTING)
	glEnable(GL_DEPTH_TEST)

	# Draw inhabitants normally
	DrawInhabitants(0)

	glPopMatrix()

	# Do the buffer Swap
	glutSwapBuffers()



# Respond to arrow keys by moving the camera frame of reference
def SpecialKeys(key, x, y):

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
	glutCreateWindow(b"OpenGL SphereWorld Demo + Lights and Shadow")
	glutReshapeFunc(ChangeSize)
	glutDisplayFunc(RenderScene)
	glutSpecialFunc(SpecialKeys)

	SetupRC()
	glutTimerFunc(33, TimerFunction, 1)

	glutMainLoop()
