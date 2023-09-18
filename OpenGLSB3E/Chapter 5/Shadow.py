# Shadow.c
# OpenGL SuperBible
# Demonstrates simple planar shadows
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *

# Rotation amounts
xRot = 0.0
yRot = 0.0

# These values need to be available globally
# Light values and coordinates
ambientLight = [ 0.3, 0.3, 0.3, 1.0 ]
diffuseLight = [ 0.7, 0.7, 0.7, 1.0 ]
specular = [ 1.0, 1.0, 1.0, 1.0 ]
lightPos = GLTVector4()
lightPos.value = [ -75.0, 150.0, -50.0, 0.0 ]
specref = [ 1.0, 1.0, 1.0, 1.0 ]

# Transformation matrix to project shadow
shadowMat = GLTMatrix()


########################
# This function just specifically draws the jet
def DrawJet(nShadow):

	vNormal	= GLTVector3() # Storeage for calculated surface normal

	# Nose Cone ##############/
	# Set material color, note we only have to set to black
	# for the shadow once
	if (nShadow == 0):
		glColor3ub(128, 128, 128)
	else:
		glColor3ub(0, 0, 0)


	# Nose Cone - Points straight down
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

	vPoints[0].value = [0.0, 0.0, 60.0]
	vPoints[1].value = [0.0, 15.0, 30.0]
	vPoints[2].value = [-15.0, 0.0, 30.0]

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
	vPoints[2].value = [15.0, 0.0, 30.0]

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
	vPoints[2].value = [0.0, 2.0, 27.0]

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
	vPoints[2].value = [0.0, 7.0, -8.0]

	gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
	glNormal3fv(vNormal.value)
	glVertex3fv(vPoints[0].value)
	glVertex3fv(vPoints[1].value)
	glVertex3fv(vPoints[2].value)


	vPoints = [GLTVector3(),
			   GLTVector3(),
			   GLTVector3()]

	vPoints[0].value = [0.0, 2.0, 27.0]
	vPoints[1].value = [0.0, 7.0, -8.0]
	vPoints[2].value = [-60.0, 2.0, -8.0]

	gltGetNormalVector(vPoints[0], vPoints[1], vPoints[2], vNormal)
	glNormal3fv(vNormal.value)
	glVertex3fv(vPoints[0].value)
	glVertex3fv(vPoints[1].value)
	glVertex3fv(vPoints[2].value)


	# Tail section###############/
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

	vPoints[0].value = [30.0, 0-0.5, -57.0]
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

# Called to draw scene
def RenderScene():

	global xRot, yRot, shadowMat, lightPos

	# Clear the window with current clearing color
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Draw the ground, we do manual shading to a darker green
	# in the background to give the illusion of depth
	glBegin(GL_QUADS)
	glColor3ub(0, 32, 0)
	glVertex3f(400.0, -150.0, -200.0)
	glVertex3f(-400.0, -150.0, -200.0)
	glColor3ub(0, 255, 0)
	glVertex3f(-400.0, -150.0, 200.0)
	glVertex3f(400.0, -150.0, 200.0)
	glEnd()

	# Save the matrix state and do the rotations
	glPushMatrix()

	# Draw jet at new orientation, put light in correct position
	# before rotating the jet
	glEnable(GL_LIGHTING)
	glLightfv(GL_LIGHT0, GL_POSITION, lightPos.value)
	glRotatef(xRot, 1.0, 0.0, 0.0)
	glRotatef(yRot, 0.0, 1.0, 0.0)

	DrawJet(0)

	# Restore original matrix state
	glPopMatrix()


	# Get ready to draw the shadow and the ground
	# First disable lighting and save the projection state
	glDisable(GL_DEPTH_TEST)
	glDisable(GL_LIGHTING)
	glPushMatrix()

	# Multiply by shadow projection matrix
	glMultMatrixf(shadowMat.value)

	# Now rotate the jet around in the new flattend space
	glRotatef(xRot, 1.0, 0.0, 0.0)
	glRotatef(yRot, 0.0, 1.0, 0.0)

	# Pass true to indicate drawing shadow
	DrawJet(1)

	# Restore the projection to normal
	glPopMatrix()

	# Draw the light source
	glPushMatrix()
	glTranslatef(lightPos.value[0], lightPos.value[1], lightPos.value[2])
	glColor3ub(255, 255, 0)
	glutSolidSphere(5.0, 10, 10)
	glPopMatrix()

	# Restore lighting state variables
	glEnable(GL_DEPTH_TEST)

	# Display the results
	glutSwapBuffers()

# This function does any needed initialization on the rendering
# context.
def SetupRC():

	global ambientLight, diffuseLight, specular, lightPos, specref, shadowMat

	# Any three points on the ground (counter clockwise order)
	points = [GLTVector3(),
			  GLTVector3(),
			  GLTVector3()]

	points[0].value = [-30.0, -149.0, -20.0]
	points[1].value = [-30.0, -149.0, 20.0]
	points[2].value = [40.0, -149.0, 20.0]

	glEnable(GL_DEPTH_TEST)	# Hidden surface removal
	glFrontFace(GL_CCW)		# Counter clock-wise polygons face out
	glEnable(GL_CULL_FACE)		# Do not calculate inside of jet

	# Setup and enable light 0
	glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
	glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
	glLightfv(GL_LIGHT0, GL_POSITION, lightPos.value)
	glEnable(GL_LIGHT0)

	# Enable color tracking
	glEnable(GL_COLOR_MATERIAL)

	# Set Material properties to follow glColor values
	glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

	# All materials hereafter have full specular reflectivity
	# with a high shine
	glMaterialfv(GL_FRONT, GL_SPECULAR, specref)
	glMateriali(GL_FRONT, GL_SHININESS, 128)

	# Light blue background
	glClearColor(0.0, 0.0, 1.0, 1.0)

	# Calculate projection matrix to draw shadow on the ground
	gltMakeShadowMatrix(points, lightPos, shadowMat)


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

	global lightPos

	fAspect = 0.0

	# Prevent a divide by zero
	if (h == 0):
		h = 1


	# Set Viewport to window dimensions
	glViewport(0, 0, w, h)

	# Reset coordinate system
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	fAspect = w / h
	gluPerspective(60.0, fAspect, 200.0, 500.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	# Move out Z axis so we can see everything
	glTranslatef(0.0, 0.0, -400.0)
	glLightfv(GL_LIGHT0, GL_POSITION, lightPos.value)


if __name__ == '__main__':

	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(800, 600)
	glutCreateWindow(b"Shadow")
	glutReshapeFunc(ChangeSize)
	glutSpecialFunc(SpecialKeys)
	glutDisplayFunc(RenderScene)
	SetupRC()
	glutMainLoop()
