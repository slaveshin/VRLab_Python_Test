#Operations.c
#OpenGL SuperBible
#DemonsTrates Imaging Dperations
#Program by Richard S. Wright Jr.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Common.OpenGLCommon import *
from Common.TGACommon import *

pImage = None

iWidth, iHeight, iComponents = [0], [0], [0]
eFormat = [0]
iRenderMode = 1

def SetupRC():
    global pImage, iWidth, iHeight, iComponents, eFormat

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    #pImage = LoadTGA("horse.tga", [iWidth], [iHeight], [iComponents], [eFormat])
    pImage = LoadTGA("horse.tga", iWidth, iHeight, iComponents, eFormat)

def ShutdownRC():
    del pImage

def ProcessMenu(value):
    global iRenderMode

    if (value == 0):
        WriteTGA("ScreenShot.tga")
    else:
        iRenderMode = value

    glutPostRedisplay()

def RenderScene():

    global iRenderMode, iWidth, iHeight, eFormat, pImage

    iViewport = [0] * 4
    pModifiedBytes = None
    invertMap = [0] * 256
    i = 0.0

    # Clear the window with current clearing color
    glClear(GL_COLOR_BUFFER_BIT)

    # Current Raster Position always at bottom left hand corner of window
    glRasterPos2i(0, 0)

    if (iRenderMode == 2):
        glPixelZoom(-1.0, -1.0)
        glRasterPos2i(iWidth, iHeight)

    if (iRenderMode == 3):
        glGetIntegerv(GL_VIEWPORT, iViewport)
        glPixelZoom(iViewport[2] /  iWidth, iViewport[3] / iHeight)

    if (iRenderMode == 4):
        glPixelTransferf(GL_RED_SCALE, 1.0)
        glPixelTransferf(GL_GREEN_SCALE, 0.0)
        glPixelTransferf(GL_BLUE_SCALE, 0.0)

    if (iRenderMode == 5):
        glPixelTransferf(GL_RED_SCALE, 0.0)
        glPixelTransferf(GL_GREEN_SCALE, 1.0)
        glPixelTransferf(GL_BLUE_SCALE, 0.0)

    if (iRenderMode == 6):
        glPixelTransferf(GL_RED_SCALE, 0.0)
        glPixelTransferf(GL_GREEN_SCALE, 0.0)
        glPixelTransferf(GL_BLUE_SCALE, 1.0)

    if (iRenderMode == 7):
        glDrawPixels(iWidth, iHeight, eFormat, GL_UNSIGNED_BYTE, pImage)

        pModifiedBytes = [0] * iWidth * iHeight

        glPixelTransferf(GL_RED_SCALE, 0.3)
        glPixelTransferf(GL_GREEN_SCALE, 0.59)
        glPixelTransferf(GL_BLUE_SCALE, 0.11)

        glReadPixels(0, 0, iWidth, iHeight, GL_LUMINANCE, GL_UNSIGNED_BYTE, pModifiedBytes)

        glPixelTransferf(GL_RED_SCALE, 1.0)
        glPixelTransferf(GL_GREEN_SCALE, 1.0)
        glPixelTransferf(GL_BLUE_SCALE, 1.0)

    if (iRenderMode == 8):
        invertMap[0] = 1.0
        for i in range(1, 256):
            invertMap[i] = 1.0 - (1.0 / 255 * i)

        glPixelMapfv(GL_PIXEL_MAP_R_TO_R, 255, invertMap)
        glPixelMapfv(GL_PIXEL_MAP_R_TO_G, 255, invertMap)
        glPixelMapfv(GL_PIXEL_MAP_R_TO_B, 255, invertMap)
        glPixelTransferi(GL_MAP_COLOR, GL_TRUE)

    if (pModifiedBytes == None):
        glDrawPixels(iWidth[0], iHeight[0], eFormat[0], GL_UNSIGNED_BYTE, pImage)
    else:
        glDrawPixels(iWidth, iHeight, GL_LUMINANCE, GL_UNSIGNED_BYTE, pModifiedBytes)
        del pModifiedBytes

    glPixelTransferi(GL_MAP_COLOR, GL_FALSE)
    glPixelTransferf(GL_RED_SCALE, 1.0)
    glPixelTransferf(GL_GREEN_SCALE, 1.0)
    glPixelTransferf(GL_BLUE_SCALE, 1.0)
    glPixelZoom(1.0, 1.0)

    glutSwapBuffers()

def ChangeSize(w, h):
    if (h == 0):
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0.0, w, 0.0, h)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == '__main__':

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Image Operations")
    glutReshapeFunc(ChangeSize)
    glutDisplayFunc(RenderScene)

    glutCreateMenu(ProcessMenu)
    glutAddMenuEntry("Save Image", 0)
    glutAddMenuEntry("Draw Pixels", 1)
    glutAddMenuEntry("Flip Pixels", 2)
    glutAddMenuEntry("Zoom Pixels", 3)
    glutAddMenuEntry("Just Red Channel", 4)
    glutAddMenuEntry("Just Green Channel", 5)
    glutAddMenuEntry("Just Blue Channel", 6)
    glutAddMenuEntry("Black and White", 7)
    glutAddMenuEntry("Invert Colors", 8)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

    SetupRC()

    glutMainLoop()

    ShutdownRC()


