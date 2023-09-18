# ImageLoad.c
# OpenGL SuperBible
# Demonstrates loading a color image
# Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *
from Common.TGACommon import *

#################################
# This function does any needed initialization on the rendering
# context. 
def SetupRC():
    
    # Black background
    glClearColor(0.0, 0.0, 0.0, 0.0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Called to draw scene
def RenderScene():

    pImage = None
    iWidth, iHeight, iComponents = [0], [0], [0]
    eFormat = [0]

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Targa's are 1 byte aligned
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    # Load the TGA file, get width, height, and component / format information
    pImage = LoadTGA("fire.tga", iWidth, iHeight, iComponents, eFormat)

    # Use Window coordinates to set raster position
    glRasterPos2i(0, 0)

    # Draw the pixmap
    if (pImage != None):
        glDrawPixels(iWidth[0], iHeight[0], eFormat[0], GL_UNSIGNED_BYTE, pImage)

    # Don't need the image data anymore
    del pImage

    # Do the buffer Swap
    glutSwapBuffers()

###############################
# For this example, it really doesn't matter what the 
# projection is since we are using glWindowPos
def ChangeSize(w, h):

    # Prevent a divide by zero, when window is too short
    # (you cant make a window of zero width).
    if(h == 0):
        h = 1

    glViewport(0, 0, w, h)

    # Reset the coordinate system before modifying
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set the clipping volume
    gluOrtho2D(0.0, w, 0.0, h)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # /
# Main program entrypoint
if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GL_DOUBLE)
    glutInitWindowSize(512, 512)
    glutCreateWindow(b"OpenGL Image Loading")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)

    SetupRC()
    glutMainLoop()