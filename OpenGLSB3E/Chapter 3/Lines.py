# Lines.c
# Demonstrates primative GL_LINES
# OpenGL SuperBible, 3rd Edition
# Richard S. Wright Jr.
# rwright@starstonesoftware.com

#include "../../Common/OpenGLSB.h"	// System and OpenGL Stuff

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import*
from numpy import*


# Define a constant for the value of PI
#define GL_PI 3.1415f

# Rotation amounts
xRot = 0.0
yRot = 0.0
GL_PI = 3.1415

#############################/
# Called to draw scene
def RenderScene():

	global xRot, yRot, GL_PI

	x = 0.0
	y = 0.0
	z = 0.0
	angle = 0.0 # Storeage for coordinates and angles

	# Clear the window with current clearing color
	glClear(GL_COLOR_BUFFER_BIT)

	# Save matrix state and do the rotation
	glPushMatrix()
	glRotatef(xRot, 1.0, 0.0, 0.0)
	glRotatef(yRot, 0.0, 1.0, 0.0)

	# Call only once for all remaining points
	glBegin(GL_LINES)

	#for (angle = 0.0f; angle <= GL_PI; angle += (GL_PI / 20.0f))
	for angle in arange(0, GL_PI, (GL_PI / 20.0)):
		x = 50.0 * sin(angle)
		y = 50.0 * cos(angle)
		glVertex3f(x, y, z)

		# Bottom half of the circle
		x = 50.0 * sin(angle + GL_PI)
		y = 50.0 * cos(angle + GL_PI)
		glVertex3f(x, y, z)
	"""	
	while (angle <= GL_PI):
		angle += (GL_PI / 20.0)
		if (angle <= GL_PI):
			# Top half of the circle
			x = 50.0*sin(angle)
			y = 50.0*cos(angle)
			glVertex3f(x, y, z)

			# Bottom half of the circle
			x = 50.0*sin(angle+GL_PI)
			y = 50.0*cos(angle+GL_PI)
			glVertex3f(x, y, z)"""


	# Done drawing points
	glEnd()

	# Restore transformations
	glPopMatrix()

	# Flush drawing commands
	glutSwapBuffers()

#############################/
# This function does any needed initialization on the
# rendering context.
def SetupRC():

	# Black background
	glClearColor(0.0, 0.0, 0.0, 1.0)

	# Set drawing color to green
	glColor3f(0.0, 1.0, 0.0)


#############################/
# Respond to arrow keys
def SpecialKeys(key, x, y):

	global xRot, yRot

	if(key == GLUT_KEY_UP):
		xRot-= 5.0

	if(key == GLUT_KEY_DOWN):
		xRot += 5.0

	if(key == GLUT_KEY_LEFT):
		yRot -= 5.0

	if(key == GLUT_KEY_RIGHT):
		yRot += 5.0

	if(key > 356.0):
		xRot = 0.0

	if(key < -1.0):
		xRot = 355.0

	if(key > 356.0):
		yRot = 0.0

	if(key < -1.0):
		yRot = 355.0

	# Refresh the Window
	glutPostRedisplay()


#############################
# Window has changed size, recalculate projection
def ChangeSize(w, h):

	nRange = 100.0

	# Prevent a divide by zero
	if(h == 0):
		h = 1

	# Set Viewport to window dimensions
	glViewport(0, 0, w, h)

	# Reset coordinate system
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	# Establish clipping volume (left, right, bottom, top, near, far)
	if (w <= h):
		glOrtho (-nRange, nRange, -nRange*h/w, nRange*h/w, -nRange, nRange)
	else:
		glOrtho (-nRange*w/h, nRange*w/h, -nRange, nRange, -nRange, nRange)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()


#############################/
# Main Program Entry Point
if __name__ == '__main__':
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(800,600)
	glutCreateWindow(b"Lines Example")
	glutReshapeFunc(ChangeSize)
	glutSpecialFunc(SpecialKeys)
	glutDisplayFunc(RenderScene)
	SetupRC()
	glutMainLoop()