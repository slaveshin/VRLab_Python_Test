# Tunnel.c
# Demonstrates mipmapping and using texture objects
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
zPos = -60.0
iLoop = 0.0

# Texture objects
TEXTURE_BRICK = 0
TEXTURE_FLOOR = 1
TEXTURE_CEILING = 2
TEXTURE_COUNT = 3
#GLuint  textures[TEXTURE_COUNT]
textures = [GLuint()] * TEXTURE_COUNT
#const char *szTextureFiles[TEXTURE_COUNT] = { "brick.tga", "floor.tga", "ceiling.tga" }
szTextureFiles = ["brick.tga", "floor.tga", "ceiling.tga"]

#######################################/
# Change texture filter for each texture object
def ProcessMenu(value):

	global TEXTURE_COUNT, iLoop, textures


	#for (iLoop = 0 iLoop < TEXTURE_COUNT iLoop++)
	for iLoop in range (0, TEXTURE_COUNT, 1):

		glBindTexture(GL_TEXTURE_2D, textures[iLoop])

		if (value == 0):
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

		if (value == 1):
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

		if (value == 2):
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_NEAREST)

		if (value == 3):
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_LINEAR)

		if (value == 4):
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)

		else:
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)

	# Trigger Redraw
	glutPostRedisplay()



#################################
# This function does any needed initialization on the rendering
# context.  Here it sets up and initializes the texture objects.
def SetupRC():

	global iLoop, TEXTURE_COUNT, textures

	pBytes = 0.0
	iWidth, iHeight, iComponents = [0], [0], [0]
	eFormat = [0]

	# Black background
	glClearColor(0.0, 0.0, 0.0, 1.0)

	# Textures applied as decals, no lighting or coloring effects
	glEnable(GL_TEXTURE_2D)
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

	# Load textures
	textures = glGenTextures(TEXTURE_COUNT)
	#for (iLoop = 0 iLoop < TEXTURE_COUNT iLoop++)
	for iLoop in range(0, TEXTURE_COUNT, 1):

		# Bind to next texture object
		glBindTexture(GL_TEXTURE_2D, textures[iLoop])

		# Load texture, set filter and wrap modes
		pBytes = LoadTGA(szTextureFiles[iLoop], iWidth, iHeight, iComponents, eFormat)
		gluBuild2DMipmaps(GL_TEXTURE_2D, iComponents[0], iWidth[0], iHeight[0], eFormat[0], GL_UNSIGNED_BYTE, bytes(pBytes))
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

		# Don't need original texture data any more
		del pBytes


#########################/
# Shutdown the rendering context. Just deletes the
# texture objects
def ShutdownRC():

	global TEXTURE_COUNT, textures

	glDeleteTextures(TEXTURE_COUNT, textures)

#########################/
# Respond to arrow keys, move the viewpoint back
# and forth
def SpecialKeys(key, x, y):

	global zPos

	if (key == GLUT_KEY_UP):
		zPos += 1.0

	if (key == GLUT_KEY_DOWN):
		zPos -= 1.0

	# Refresh the Window
	glutPostRedisplay()

##################################/
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
	gluPerspective(90.0, fAspect, 1, 120)


	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

###########################/
# Called to draw scene
def RenderScene():

	global zPos, textures

	z = 0.0

	# Clear the window with current clearing color
	glClear(GL_COLOR_BUFFER_BIT)

	# Save the matrix state and do the rotations
	glPushMatrix()
	# Move object back and do in place rotation
	glTranslatef(0.0, 0.0, zPos)

	# Floor
	#for (z = 60.0f z >= 0.0f z -= 10)
	for z in range(60, 0, -10):

		glBindTexture(GL_TEXTURE_2D, textures[TEXTURE_FLOOR])
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0)
		glVertex3f(-10.0, -10.0, z)

		glTexCoord2f(1.0, 0.0)
		glVertex3f(10.0, -10.0, z)

		glTexCoord2f(1.0, 1.0)
		glVertex3f(10.0, -10.0, z - 10.0)

		glTexCoord2f(0.0, 1.0)
		glVertex3f(-10.0, -10.0, z - 10.0)
		glEnd()

		# Ceiling
		glBindTexture(GL_TEXTURE_2D, textures[TEXTURE_CEILING])
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 1.0)
		glVertex3f(-10.0, 10.0, z - 10.0)

		glTexCoord2f(1.0, 1.0)
		glVertex3f(10.0, 10.0, z - 10.0)

		glTexCoord2f(1.0, 0.0)
		glVertex3f(10.0, 10.0, z)

		glTexCoord2f(0.0, 0.0)
		glVertex3f(-10.0, 10.0, z)
		glEnd()


		# Left Wall
		glBindTexture(GL_TEXTURE_2D, textures[TEXTURE_BRICK])
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0)
		glVertex3f(-10.0, -10.0, z)

		glTexCoord2f(1.0, 0.0)
		glVertex3f(-10.0, -10.0, z - 10.0)

		glTexCoord2f(1.0, 1.0)
		glVertex3f(-10.0, 10.0, z - 10.0)

		glTexCoord2f(0.0, 1.0)
		glVertex3f(-10.0, 10.0, z)
		glEnd()


		# Right Wall
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 1.0)
		glVertex3f(10.0, 10.0, z)

		glTexCoord2f(1.0, 1.0)
		glVertex3f(10.0, 10.0, z - 10.0)

		glTexCoord2f(1.0, 0.0)
		glVertex3f(10.0, -10.0, z - 10.0)

		glTexCoord2f(0.0, 0.0)
		glVertex3f(10.0, -10.0, z)
		glEnd()

	# Restore the matrix state
	glPopMatrix()

	# Buffer swap
	glutSwapBuffers()

###########################
# Program entry point
if __name__ == '__main__':

	# Standard initialization stuff
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(800, 600)
	glutCreateWindow(b"Tunnel")
	glutReshapeFunc(ChangeSize)
	glutSpecialFunc(SpecialKeys)
	glutDisplayFunc(RenderScene)

	# Add menu entries to change filter
	glutCreateMenu(ProcessMenu)
	glutAddMenuEntry("GL_NEAREST", 0)
	glutAddMenuEntry("GL_LINEAR", 1)
	glutAddMenuEntry("GL_NEAREST_MIPMAP_NEAREST", 2)
	glutAddMenuEntry("GL_NEAREST_MIPMAP_LINEAR", 3)
	glutAddMenuEntry("GL_LINEAR_MIPMAP_NEAREST", 4)
	glutAddMenuEntry("GL_LINEAR_MIPMAP_LINEAR", 5)
	glutAttachMenu(GLUT_RIGHT_BUTTON)

	# Startup, loop, shutdown
	SetupRC()
	glutMainLoop()
	ShutdownRC()
