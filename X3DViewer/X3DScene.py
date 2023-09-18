from anytree import Node, RenderTree
import PythonSAI.x3d as x3d
import xml.etree.ElementTree as ET
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class X3DScene:

    treeNode = Node("X3D")

    def SearchX3DNode(self, node_, p_head_):
        index = 0
        for child in node_:
            self.CreateNode(child, p_head_)
            if len(p_head_.children) > index:
                self.SearchX3DNode(child, p_head_.children[index])
                index += 1

    def Parsing(self, filepath_):
        self.X3D_parse(filepath_)

        glClearColor(0.0, 0.0, 0.6, 1.0)
        glColor(0.7, 0.7, 0.7)

    def X3D_parse(self, filepath_):
        X3DScene.treeNode = Node("X3D")
        p_head = X3DScene.treeNode
        tree = ET.parse(filepath_)
        self.SearchX3DNode(tree.getroot(), p_head)

    def CreateNode(self, current_, p_head_):
        element = current_.tag

        if element == "Appearance":
            self.ElementAppearanceNode(current_, p_head_)
        elif element == "Box":
            self.ElementBoxNode(current_, p_head_)
        elif element == "head":
            self.ElementHeadNode(current_, p_head_)
        elif element == "meta":
            self.ElementMetaNode(current_, p_head_)
        elif element == "Scene":
            self.ElementSceneNode(current_, p_head_)
        elif element == "WorldInfo":
            self.ElementWorldInfoNode(current_, p_head_)
        elif element == "Background":
            self.ElementBackgroundNode(current_, p_head_)
        elif element == "Viewpoint":
            self.ElementViewpointNode(current_, p_head_)
        elif element == "Shape":
            self.ElementShapeNode(current_, p_head_)
        elif element == "Material":
            self.ElementMaterialNode(current_, p_head_)

    def ElementAppearanceNode(self, current_, p_head_):
        currentNode = x3d.Appearance()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementHeadNode(self, current_, p_head_):
        currentNode = x3d.Head()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementMetaNode(self, current_, p_head_):
        currentNode = x3d.Meta()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementSceneNode(self, current_, p_head_):
        currentNode = x3d.Scene()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementWorldInfoNode(self, current_, p_head_):
        currentNode = x3d.WorldInfo()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementMaterialNode(self, current_, p_head_):
        currentNode = x3d.Material()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementBackgroundNode(self, current_, p_head_):
        currentNode = x3d.Background()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementViewpointNode(self, current_, p_head_):
        currentNode = x3d.Viewpoint()
        Node(current_.tag, parent=p_head_, data=currentNode)
    def ElementShapeNode(self, current_, p_head_):
        currentNode = x3d.Shape()
        Node(current_.tag, parent=p_head_, data=currentNode)

    def ElementBoxNode(self, current_, p_head_):
        currentNode = x3d.Box()

        node = current_.attrib
        for key in node.keys():
            if key == "solid":
                if node[key] == "true":
                    currentNode.solid = True
                else:
                    currentNode.solid = False
            elif key == "size":
                currentNode.size = list(map(float, node[key].split()))
            elif key == "DEF":
                currentNode.DEF = node[key]
            elif key == "USE":
                currentNode.USE = node[key]

        Node(current_.tag, parent=p_head_, data=currentNode)

    def Draw(self):
        pNode = X3DScene.treeNode
        self.DrawOpenGL(pNode)

    def DrawOpenGL(self, pNode):
        #print(pNode, pNode.__dict__)
        if pNode.name == "Box":
            point = pNode.data.size
            point1 = [point[0] / 2.0, point[1] / 2.0, point[2] / -2.0]
            point2 = [point[0] / 2.0, point[1] / 2.0, point[2] / 2.0]
            point3 = [point[0] / 2.0, point[1] / -2.0, point[2] / 2.0]
            point4 = [point[0] / 2.0, point[1] / -2.0, point[2] / -2.0]
            point5 = [point[0] / -2.0, point[1] / -2.0, point[2] / 2.0]
            point6 = [point[0] / -2.0, point[1] / 2.0, point[2] / 2.0]
            point7 = [point[0] / -2.0, point[1] / 2.0, point[2] / -2.0]
            point8 = [point[0] / -2.0, point[1] / -2.0, point[2] / -2.0]

            glBegin(GL_QUADS)
            glNormal3fv(point1)
            glVertex3fv(point1)  # TOP
            glNormal3fv(point2)
            glVertex3fv(point2)
            glNormal3fv(point6)
            glVertex3fv(point6)
            glNormal3fv(point7)
            glVertex3fv(point7)

            glNormal3fv(point3)
            glVertex3fv(point3)  # Bottom
            glNormal3fv(point4)
            glVertex3fv(point4)
            glNormal3fv(point8)
            glVertex3fv(point8)
            glNormal3fv(point5)
            glVertex3fv(point5)

            glNormal3fv(point2)
            glVertex3fv(point2)  # Front
            glNormal3fv(point3)
            glVertex3fv(point3)
            glNormal3fv(point5)
            glVertex3fv(point5)
            glNormal3fv(point6)
            glVertex3fv(point6)

            glNormal3fv(point7)
            glVertex3fv(point7)  # Back
            glNormal3fv(point8)
            glVertex3fv(point8)
            glNormal3fv(point4)
            glVertex3fv(point4)
            glNormal3fv(point1)
            glVertex3fv(point1)

            glNormal3fv(point6)
            glVertex3fv(point6)  # Left
            glNormal3fv(point5)
            glVertex3fv(point5)
            glNormal3fv(point8)
            glVertex3fv(point8)
            glNormal3fv(point7)
            glVertex3fv(point7)

            glNormal3fv(point1)
            glVertex3fv(point1)  # Right
            glNormal3fv(point4)
            glVertex3fv(point4)
            glNormal3fv(point3)
            glVertex3fv(point3)
            glNormal3fv(point2)
            glVertex3fv(point2)

            glEnd()

        for child in pNode.children:
            self.DrawOpenGL(child)