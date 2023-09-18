# GLRect.c
# Just draw a single rectangle in the middle of the screen
# OpenGL SuperBible, 3rd Edition
# Richard S. Wright Jr.
# rwright@starstonesoftware.com

##include "../../Common/OpenGLSB.h"	# System and OpenGL Stuff
#include <gl/glut.h>
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#############################/
# Called to draw scene
def RenderScene():

	# Clear the window with current clearing color
	glClear(GL_COLOR_BUFFER_BIT)

	# Set current drawing color to red
	#		   R	 G	   B
	glColor3f(1.0, 0.0, 0.0)

	# Draw a filled rectangle with current color
	glRectf(-25.0, 25.0, 25.0, -25.0)

	# Flush drawing commands
	glFlush()

#############################/
# Setup the rendering state
def SetupRC():
	# Set clear color to blue
	glClearColor(0.0, 0.0, 1.0, 1.0)



#############################/
# Called by GLUT library when the window has chanaged size
def ChangeSize(w, h):

	aspectRatio = 0.0

	# Prevent a divide by zero
    # if h is 0:
	if h == 0:
		h = 1

	# Set Viewport to window dimensions
	glViewport(0, 0, w, h)

	# Reset coordinate system
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	# Establish clipping volume (left, right, bottom, top, near, far)
	aspectRatio = w / h
	if (w <= h):
		glOrtho(-100.0, 100.0, -100 / aspectRatio, 100.0 / aspectRatio, 1.0, -1.0)
	else:
		glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0, 1.0, -1.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()


#############################/
# Main program entry point
if __name__=='__main__':
	glutInit()
	glutInitWindowSize(800, 600)
	glutCreateWindow(b"GLRect")
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutDisplayFunc(RenderScene)
	glutReshapeFunc(ChangeSize)
	SetupRC()
	glutMainLoop()
