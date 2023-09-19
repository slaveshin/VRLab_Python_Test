from anytree import Node, RenderTree
from collections import deque
from PythonSAI.common import X3D_CONSTANT
import PythonSAI.x3d as x3d
import xml.etree.ElementTree as ET
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np


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
        elif element == "Cylinder":
            self.ElementCylinderNode(current_, p_head_)
        elif element == "Cone":
            self.ElementConeNode(current_, p_head_)
        elif element == "Sphere":
            self.ElementSphereNode(current_, p_head_)
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
        elif element == "Transform":
            self.ElementTransformNode(current_, p_head_)
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

    def ElementConeNode(self, current_, p_head_):
        currentNode = x3d.Cone()

        node = current_.attrib
        for key in node.keys():
            if key == "solid":
                if node[key] == "true":
                    currentNode.solid = True
                else:
                    currentNode.solid = False
            if key == "bottom":
                if node[key] == "true":
                    currentNode.bottom = True
                else:
                    currentNode.bottom = False
            if key == "side":
                if node[key] == "true":
                    currentNode.side = True
                else:
                    currentNode.side = False
            elif key == "height":
                currentNode.height = float(node[key])
            elif key == "DEF":
                currentNode.DEF = node[key]
            elif key == "USE":
                currentNode.USE = node[key]
            elif key == "bottomRadius":
                currentNode.bottomRadius = float(node[key])

        Node(current_.tag, parent=p_head_, data=currentNode)

    def ElementCylinderNode(self, current_, p_head_):
        currentNode = x3d.Cylinder()

        node = current_.attrib
        for key in node.keys():
            if key == "solid":
                if node[key] == "true":
                    currentNode.solid = True
                else:
                    currentNode.solid = False
            if key == "side":
                if node[key] == "true":
                    currentNode.side = True
                else:
                    currentNode.side = False
            if key == "top":
                if node[key] == "true":
                    currentNode.top = True
                else:
                    currentNode.top = False
            if key == "bottom":
                if node[key] == "true":
                    currentNode.bottom = True
                else:
                    currentNode.bottom = False
            elif key == "radius":
                currentNode.radius = float(node[key])
            elif key == "height":
                currentNode.height = float(node[key])
            elif key == "DEF":
                currentNode.DEF = node[key]
            elif key == "USE":
                currentNode.USE = node[key]

        Node(current_.tag, parent=p_head_, data=currentNode)

    def ElementSphereNode(self, current_, p_head_):
        currentNode = x3d.Sphere()

        node = current_.attrib
        for key in node.keys():
            if key == "solid":
                if node[key] == "true":
                    currentNode.solid = True
                else:
                    currentNode.solid = False
            elif key == "radius":
                currentNode.radius = float(node[key])
            elif key == "DEF":
                currentNode.DEF = node[key]
            elif key == "USE":
                currentNode.USE = node[key]

        Node(current_.tag, parent=p_head_, data=currentNode)

    def ElementTransformNode(self, current_, p_head_):
        currentNode = x3d.Transform()
        node = current_.attrib
        for key in node.keys():
            if key == "center":
                currentNode.center = list(map(float, node[key].split()))
            elif key == "children":
                currentNode.children = list(node[key])
            elif key == "rotation":
                currentNode.rotation = list(map(float, node[key].split()))
            elif key == "scale":
                currentNode.scale = list(map(float, node[key].split()))
            elif key == "scaleOrientation":
                currentNode.scaleOrientation = list(
                    map(float, node[key].split()))
            elif key == "translation":
                currentNode.translation = list(map(float, node[key].split()))
            elif key == "bboxCenter":
                currentNode.bboxCenter = list(map(float, node[key].split()))
            elif key == "bboxSize":
                currentNode.bboxSize = list(map(float, node[key].split()))
            elif key == "DEF":
                currentNode.DEF = node[key]
            elif key == "USE":
                currentNode.USE = node[key]

        Node(current_.tag, parent=p_head_, data=currentNode)

    def Draw(self):
        pNode = X3DScene.treeNode
        self.DrawOpenGL(pNode)

    def DrawOpenGL(self, pNode):

        if pNode.name == "Transform":
            glPushMatrix()
            translation = pNode.data.translation
            scale = pNode.data.scale
            rotation = pNode.data.rotation

            glTranslatef(translation[0], translation[1], translation[2])
            glScalef(scale[0], scale[1], scale[2])
            glRotatef(rotation[3] / X3D_CONSTANT["PI"] *
                      180.0, rotation[0], rotation[1], rotation[2])

        elif pNode.name == "Viewpoint":
            # TODO Viewpoint 구현
            glPushMatrix()
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

        elif pNode.name == "Cylinder":
            # 참고자료 https://gist.github.com/nikAizuddin/5ea402e9073f1ef76ba6
            radius = pNode.data.radius
            height = pNode.data.height

            x = 0.0
            y = 0.0
            angle = 0.0
            angle_stepsize = 0.1

            # Draw the tube
            glBegin(GL_QUAD_STRIP)
            angle = 0.0
            while(angle < 2*math.pi):
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                glVertex3f(x, y, height)
                glVertex3f(x, y, 0.0)
                angle = angle + angle_stepsize

            glVertex3f(radius, 0.0, height)
            glVertex3f(radius, 0.0, 0.0)
            glEnd()

            # Draw the circle on top of cylinder

            glBegin(GL_POLYGON)
            angle = 0.0
            while(angle < 2*math.pi):
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                glVertex3f(x, y, height)
                angle = angle + angle_stepsize

            glVertex3f(radius, 0.0, height)
            glEnd()

        elif pNode.name == "Sphere":

            lats = 30
            longs = 30
            r = pNode.data.radius

            for i in range(lats):
                lat0 = math.pi * (-0.5 + i / lats)
                z0 = math.sin(lat0)
                zr0 = math.cos(lat0)

                lat1 = math.pi * (-0.5 + (i+1) / lats)
                z1 = math.sin(lat1)
                zr1 = math.cos(lat1)

                glBegin(GL_QUAD_STRIP)
                for j in range(longs+1):
                    lng = 2 * math.pi * (j+1) / longs
                    x = math.cos(lng)
                    y = math.sin(lng)
                    glVertex(r * x * zr0, r * y * zr0, r * z0)
                    glVertex(r * x * zr1, r * y * zr1, r * z1)
                glEnd()

        elif pNode.name == "Cone":
            # 참고자료 https://gist.github.com/davidwparker/1195852
            cone_height = pNode.data.height
            cone_radius = pNode.data.bottomRadius

            # /* sides */
            glBegin(GL_TRIANGLES)
            for k in range(0, 360, 5):
                glVertex3f(0, 0, cone_height)
                glVertex3f(cone_radius*math.cos(k),
                           cone_radius*math.sin(k), cone_height)
                glVertex3f(cone_radius*math.cos(k+5),
                           cone_radius*math.sin(k+5), cone_height)
            glEnd()
            # /* bottom circle */
            # /* rotate back */

            glRotated(90, 1, 0, 0)
            glBegin(GL_TRIANGLES)
            for k in range(0, 360, 3):
                glVertex3f(0, 0, 0)
                glVertex3f(cone_radius*math.cos(k),
                           cone_height, cone_radius*math.sin(k))
                glVertex3f(cone_radius*math.cos(k+5),
                           cone_height, cone_radius*math.sin(k+5))
            glEnd()

        for child in pNode.children:
            self.DrawOpenGL(child)

        if pNode.name in ["Transform", "Viewpoint"]:
            glPopMatrix()
