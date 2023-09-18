import sys
# 개인 X3D 전체 파일 경로 추가
sys.path.append("C:\\Users\khsh5\Desktop\web3dorg\X3D_LB_Python")

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from X3DViewer_dev.X3DScene import *

m_xTranslation, m_yTranslation, m_zTranslation = 0.0, 0.0, -10.0
m_xRotation, m_yRotation, m_zRotation = 0.0, 0.0, 0.0
m_xScaling, m_yScaling, m_zScaling = 1.0, 1.0, 1.0
m_SpeedTranslation = 1.0 / 5000.0
m_SpeedZoom = 1.0 / 1.0
x_last, y_last = 0, 0
a = 0
m_pScene = X3DScene()

filepath = ""

def initFun():
    glEnable(GL_BLEND)
    #glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_AUTO_NORMAL)

    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POLYGON_SMOOTH)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_COLOR_MATERIAL)

    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT)
    glColorMaterial(GL_FRONT_AND_BACK, GL_SPECULAR)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glDepthFunc(GL_LESS)

    m_pScene.Parsing(filepath)

    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_FILL)
    #glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # 특정 광원에 소속되지 않은 전역 주변광을 설정한다.
    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [1.0, 1.0, 1.0, 0.0])
    # 물체의 뒷면에도 조명을 적용한다. 디폴트는 한쪽면에만조명이 적용된다.
    #glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    # 반사광의 각도를 어떻게 계산할 것인가를 지정한다. 이 값이 0이면 조명이 평행하게 비치고 0이 아니면 정점의 방향에 따라 비친다.
    #glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, False)

    # if m_pScene.m_LightNode.count(True) == 1: glEnable(GL_LIGHT0)
    # else: glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    # glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 5.0, 6.0, 0.0])
    # glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    # glLightfv(GL_LIGHT0, GL_AMBIENT, [1.0, 1.0, 1.0, 1.0])
    # glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    glFrontFace(GL_CCW)
    glShadeModel(GL_FLAT)

    glClearDepth(1.0)
    ##############################################
    # 참고자료 : https://m.blog.naver.com/PostView.nhn?blogId=itrainl4&logNo=90188723209&proxyReferer=https:%2F%2Fwww.google.com%2F
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    ##############################################
    glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA)

def displayFun():
    #glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glPushMatrix()
    glTranslatef(m_xTranslation, m_yTranslation, m_zTranslation)
    glRotatef(m_xRotation, 1.0, 0.0, 0.0)
    glRotatef(m_yRotation, 0.0, 1.0, 0.0)
    glRotatef(m_zRotation, 0.0, 0.0, 1.0)
    glScalef(m_xScaling, m_yScaling, m_zScaling)
    
    m_pScene.Draw()
    glPopMatrix()

    glutPostRedisplay()
    glFlush()

def reshapeFunc(w, h):
    glGetError()  # uncomment this line when error occurs here
    width, height = 400, 400

    aspect = width if (height == 0) else width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect, 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def MyMouseClick(Button, State, x, y):
    global m_zTranslation, x_last, y_last
    if Button == 0:
        x_last, y_last = x, y
    else:
        m_pScene.m_TouchSensor = True

    glutPostRedisplay()

def MyMouseMove(x, y):
    global m_xRotation, m_yRotation, x_last, y_last
    m_speedRotation = (1.0 / 100.0)
    m_xRotation -= (float)(y - y_last) * m_speedRotation
    m_yRotation += (float)(x - x_last) * m_speedRotation
    glutPostRedisplay()


def MyMouseWheelFunc(wheel, direction, x, y):
    width = 400
    height = 400
    x = x - width // 2
    y = y - height // 2
    global m_zTranslation, m_SpeedZoom, m_xTranslation, m_yTranslation, m_SpeedTranslation
    if direction == -1:
        m_zTranslation -= m_SpeedZoom
    elif direction == 1:
        m_zTranslation += m_SpeedZoom
    m_xTranslation += x * m_SpeedTranslation
    m_yTranslation -= y * m_SpeedTranslation

    glutPostRedisplay()

def ProcessMenu(value):
    if value == 1:
        glPolygonMode(GL_FRONT, GL_POINT)
        glPolygonMode(GL_BACK, GL_POINT)
    elif value == 2:
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_LINE)
    elif value == 3:
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)
    elif value == 4:
        glShadeModel(GL_SMOOTH)
    elif value == 5:
        glShadeModel(GL_FLAT)
    elif value == 6:
        glEnable(GL_LIGHTING)
    elif value == 7:
        glDisable(GL_LIGHTING)

    glutPostRedisplay()


if __name__=='__main__':
    
    filepath = sys.argv[1]
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
    print(filepath)

    glutInit()
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(800, 600)
    glutCreateWindow(b"TEST")
    glutDisplayFunc(displayFun)
    glutReshapeFunc(reshapeFunc)
    glutMouseFunc(MyMouseClick)
    glutMotionFunc(MyMouseMove)
    glutMouseWheelFunc(MyMouseWheelFunc)

    # Create Menu (Mouse Right Button)
    nMenu = glutCreateMenu(ProcessMenu)
    glutAddMenuEntry("GL_POINT", 1)
    glutAddMenuEntry("GL_LINE", 2)
    glutAddMenuEntry("GL_POLYGON", 3)
    glutAddMenuEntry("GL_SMOOTH", 4)
    glutAddMenuEntry("GL_FLAT", 5)
    glutAddMenuEntry("LIGHT_ON", 6)
    glutAddMenuEntry("LIGHT_OFF", 7)

    glutAttachMenu(GLUT_RIGHT_BUTTON)
    initFun()
    glutMainLoop()