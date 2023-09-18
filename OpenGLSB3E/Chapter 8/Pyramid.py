# Pyramid.c
# Demonstrates Simple Texture Mapping
# OpenGL SuperBible
# Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *
from Common.TGACommon import *


# Rotation amounts
xRot = 0.0
yRot = 0.0


# Change viewing volume and viewport.  Called when window is resized
def ChangeSize(w, h):

	fAspect = 0.0

	# Prevent a divide by zero
	if (h == 0):
		h = 1

	# Set Viewport to window dimensions
	glViewport(0, 0, w, h)

	fAspect = w / h

	# Reset coordinate system
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	# Produce the perspective projection
	gluPerspective(35.0, fAspect, 1.0, 40.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()


# This function does any needed initialization on the rendering
# context.  Here it sets up and initializes the lighting for
# the scene.
def SetupRC():

	pBytes = 0.0
	iWidth, iHeight, iComponents = [0], [0], [0]
	eFormat = [0]

	# Light values and coordinates
	whiteLight = [0.05, 0.05, 0.05, 1.0]
	sourceLight = [0.25, 0.25, 0.25, 1.0]
	lightPos = [-10., 5.0, 5.0, 1.0]

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

	# Load texture
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	pBytes = LoadTGA("Stone.tga", iWidth, iHeight, iComponents, eFormat)
	glTexImage2D(GL_TEXTURE_2D, 0, iComponents[0], iWidth[0], iHeight[0], 0, eFormat[0], GL_UNSIGNED_BYTE, pBytes)
	del pBytes

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	glEnable(GL_TEXTURE_2D)


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

	xRot = xRot % 360
	yRot = yRot % 360

	# Refresh the Window
	glutPostRedisplay()


# Called to draw scene
def RenderScene():

	vNormal = GLTVector3()
	vCorners = [GLTVector3(),
				GLTVector3(),
				GLTVector3(),
				GLTVector3(),
				GLTVector3()]

	vCorners[0].value = [0.0, .80, 0.0]    #Top
	vCorners[1].value = [-0.5, 0.0, -.50]  #Back left
	vCorners[2].value = [0.5, 0.0, -0.50]  #Back right
	vCorners[3].value = [0.5, 0.0, 0.5]    #Front right
	vCorners[4].value = [-0.5, 0.0, 0.5]    #Front left

	# Clear the window with current clearing color
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Save the matrix state and do the rotations
	glPushMatrix()
	# Move object back and do in place rotation
	glTranslatef(0.0, -0.25, -4.0)
	glRotatef(xRot, 1.0, 0.0, 0.0)
	glRotatef(yRot, 0.0, 1.0, 0.0)

	# Draw the Pyramid
	glColor3f(1.0, 1.0, 1.0)
	glBegin(GL_TRIANGLES)
	# Bottom section - two triangles
	glNormal3f(0.0, -1.0, 0.0)
	glTexCoord2f(1.0, 1.0)
	glVertex3fv(vCorners[2].value)

	glTexCoord2f(0.0, 0.0)
	glVertex3fv(vCorners[4].value)

	glTexCoord2f(0.0, 1.0)
	glVertex3fv(vCorners[1].value)


	glTexCoord2f(1.0, 1.0)
	glVertex3fv(vCorners[2].value)

	glTexCoord2f(1.0, 0.0)
	glVertex3fv(vCorners[3].value)

	glTexCoord2f(0.0, 0.0)
	glVertex3fv(vCorners[4].value)

	# Front Face
	gltGetNormalVector(vCorners[0], vCorners[4], vCorners[3], vNormal)
	glNormal3fv(vNormal.value)
	glTexCoord2f(0.5, 1.0)
	glVertex3fv(vCorners[0].value)
	glTexCoord2f(0.0, 0.0)
	glVertex3fv(vCorners[4].value)
	glTexCoord2f(1.0, 0.0)
	glVertex3fv(vCorners[3].value)

	# Left Face
	gltGetNormalVector(vCorners[0], vCorners[1], vCorners[4], vNormal)
	glNormal3fv(vNormal.value)
	glTexCoord2f(0.5, 1.0)
	glVertex3fv(vCorners[0].value)
	glTexCoord2f(0.0, 0.0)
	glVertex3fv(vCorners[1].value)
	glTexCoord2f(1.0, 0.0)
	glVertex3fv(vCorners[4].value)

	# Back Face
	gltGetNormalVector(vCorners[0], vCorners[2], vCorners[1], vNormal)
	glNormal3fv(vNormal.value)
	glTexCoord2f(0.5, 1.0)
	glVertex3fv(vCorners[0].value)

	glTexCoord2f(0.0, 0.0)
	glVertex3fv(vCorners[2].value)

	glTexCoord2f(1.0, 0.0)
	glVertex3fv(vCorners[1].value)

	# Right Face
	gltGetNormalVector(vCorners[0], vCorners[3], vCorners[2], vNormal)
	glNormal3fv(vNormal.value)
	glTexCoord2f(0.5, 1.0)
	glVertex3fv(vCorners[0].value)
	glTexCoord2f(0.0, 0.0)
	glVertex3fv(vCorners[3].value)
	glTexCoord2f(1.0, 0.0)
	glVertex3fv(vCorners[2].value)
	glEnd()


	# Restore the matrix state
	glPopMatrix()

	# Buffer swap
	glutSwapBuffers()


if __name__ == '__main__':

	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(800, 600)
	glutCreateWindow(b"Textured Pyramid")
	glutReshapeFunc(ChangeSize)
	glutSpecialFunc(SpecialKeys)
	glutDisplayFunc(RenderScene)
	SetupRC()
	glutMainLoop()