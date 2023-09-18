# -*- coding: utf-8 -*-
from .abstract import *
from .field import *
import math

class Contact(X3DNode):
    """
    Contact : X3DNode {
        MFString [in,out] appliedParameters        "BOUNCE"
        SFNode   [in,out] body1                    NULL     [RigidBody]
        SFNode   [in,out] body2                    NULL     [RigidBody]
        SFFloat  [in,out] bounce                   0        [0,1]
        SFVec3f  [in,out] contactNormal            0 1 0    (-∞,∞)
        SFFloat  [in,out] depth                    0        (-∞,∞)
        SFVec2f  [in,out] frictionCoefficients     0 0      [0,∞)
        SFVec3f  [in,out] frictionDirection        0 1 0    (-∞,∞)
        SFNode   [in,out] geometry1                NULL     [X3DNBodyCollidableNode]
        SFNode   [in,out] geometry2                NULL     [X3DNBodyCollidableNode]
        SFNode   [in,out] metadata                 NULL     [X3DMetadataObject]
        SFFloat  [in,out] minbounceSpeed           0        [0,∞)
        SFVec3f  [in,out] position                 0 0 0    (-∞,∞)
        SFVec2f  [in,out] slipCoefficients         0 0      (-∞,∞)
        SFFloat  [in,out] softnessConstantForceMix 0.0001   [0,1]
        SFFloat  [in,out] softnessErrorCorrection  0.8      [0,1]
        SFVec2f  [in,out] surfaceSpeed             0 0      (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            appliedParameters=["BOUNCE"],
            body1=None,
            body2=None,
            bounce=0.0,
            contactNormal=[0.0, 1.0, 0.0],
            depth=0.0,
            frictionCoefficients=[0.0, 0.0],
            frictionDirection=[0.0, 1.0, 0.0],
            geomtry1=None,
            geomtry2=None,
            minBounceSpeed=0.1,
            position=[0.0, 0.0, 0.0],
            slipCoefficients=[0.0, 0.0],
            softnessConstantForceMix=0.0001,
            softnessErrorCorrection=0.8,
            surfaceSpeed=[0.0, 0.0], 
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.appliedParameters = appliedParameters
        self.body1 = body1
        self.body2 = body2
        self.bounce = bounce
        self.contactNormal = contactNormal
        self.depth = depth
        self.frictionCoefficients = frictionCoefficients
        self.frictionDirection = frictionDirection
        self.geomtry1 = geomtry1
        self.geomtry2 = geomtry2
        self.minBounceSpeed = minBounceSpeed
        self.position = position
        self.slipCoefficients = slipCoefficients
        self.softnessConstantForceMix = softnessConstantForceMix
        self.softnessErrorCorrection = softnessErrorCorrection
        self.surfaceSpeed = surfaceSpeed

    @property
    def appliedParameters(self):
        return self.__appliedParameters

    @appliedParameters.setter
    def appliedParameters(self, appliedParameters):
        if appliedParameters is None:
            appliedParameters = ["BOUNCE"]
        assertValidCollisionAppliedParameters(appliedParameters)
        self.__appliedParameters = appliedParameters

    @property
    def body1(self):
        return self.__body1

    @body1.setter
    def body1(self, body1):
        if body1 is None:
            body1 = None
        assertSFNode(body1, RigidBody)
        self.__body1 = body1

    @property
    def body2(self):
        return self.__body2

    @body2.setter
    def body2(self, body2):
        if body2 is None:
            body2 = None
        assertSFNode(body2, RigidBody)
        self.__body2 = body2

    @property
    def bounce(self):
        return self.__bounce

    @bounce.setter
    def bounce(self, bounce):
        if bounce is None:
            bounce = 0.0
        assertSFFloat(bounce)
        assertValidGreaterThanEquals(bounce, 0)
        assertValidLessThanEquals(bounce, 1)
        self.__bounce = bounce
    
    @property
    def contactNormal(self):
        return self.__contactNormal

    @contactNormal.setter
    def contactNormal(self, contactNormal):
        if contactNormal is None:
            contactNormal = [0.0, 1.0, 0.0]
        assertSFVec3f(contactNormal)
        self.__contactNormal = contactNormal

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth):
        if depth is None:
            depth = 0.0
        assertSFFloat
        self.__depth = depth

    @property
    def frictionCoefficients(self):
        return self.__frictionCoefficients

    @frictionCoefficients.setter
    def frictionCoefficients(self, frictionCoefficients):
        if frictionCoefficients is None:
            frictionCoefficients = [0.0, 0.0]
        assertSFVec2f(frictionCoefficients)
        assertValidGreaterThanEquals(frictionCoefficients, 0)
        self.__frictionCoefficients = frictionCoefficients

    @property
    def frictionDirection(self):
        return self.__frictionDirection

    @frictionDirection.setter
    def frictionDirection(self, frictionDirection):
        if frictionDirection is None:
            frictionDirection = [0.0, 1.0, 0.0]
        assertSFVec3f(frictionDirection)
        self.__frictionDirection = frictionDirection

    @property
    def geometry1(self):
        return self.__geometry1

    @geometry1.setter
    def geometry1(self, geometry1):
        if geometry1 is None:
            geometry1 = None
        assertSFNode(geometry1, X3DNBodyCollidableNode)
        self.__geometry1 = geometry1

    @property
    def geometry2(self):
        return self.__geometry2

    @geometry2.setter
    def geometry2(self, geometry2):
        if geometry2 is None:
            geometry2 = None
        assertSFNode(geometry2, X3DNBodyCollidableNode)
        self.__geometry2 = geometry2

    @property
    def minBounceSpeed(self):
        return self.__minBounceSpeed

    @minBounceSpeed.setter
    def minBounceSpeed(self, minBounceSpeed):
        if minBounceSpeed is None:
            minBounceSpeed = [0.0, 0.0]
        assertSFFloat(minBounceSpeed)
        assertValidGreaterThanEquals(minBounceSpeed, 0)
        self.__minBounceSpeed = minBounceSpeed

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position is None:
            position = [0.0, 0.0, 0.0]
        assertSFVec3f(position)
        self.__position = position

    @property
    def slipCoefficients(self):
        return self.__slipCoefficients

    @slipCoefficients.setter
    def slipCoefficients(self, slipCoefficients):
        if slipCoefficients is None:
            slipCoefficients = [0.0, 0.0]
        assertSFVec2f(slipCoefficients)
        self.__slipCoefficients = slipCoefficients
    
    @property
    def softnessConstantForceMix(self):
        return self.__softnessConstantForceMix

    @softnessConstantForceMix.setter
    def softnessConstantForceMix(self, softnessConstantForceMix):
        if softnessConstantForceMix is None:
            softnessConstantForceMix = 0.0001
        assertSFFloat(softnessConstantForceMix)
        assertValidGreaterThanEquals(softnessConstantForceMix, 0)
        assertValidLessThanEquals(softnessConstantForceMix, 1)
        self.__softnessConstantForceMix = softnessConstantForceMix

    @property
    def softnessErrorCorrection(self):
        return self.__softnessErrorCorrection

    @softnessErrorCorrection.setter
    def softnessErrorCorrection(self, softnessErrorCorrection):
        if softnessErrorCorrection is None:
            softnessErrorCorrection = 0.8
        assertSFFloat(softnessErrorCorrection)
        assertValidGreaterThanEquals(softnessErrorCorrection, 0)
        assertValidLessThanEquals(softnessErrorCorrection, 1)
        self.__softnessErrorCorrection = softnessErrorCorrection

    @property
    def surfaceSpeed(self):
        return self.__surfaceSpeed

    @surfaceSpeed.setter
    def surfaceSpeed(self, surfaceSpeed):
        if surfaceSpeed is None:
            surfaceSpeed = [0.0, 0.0]
        assertSFVec2f(surfaceSpeed)
        self.__surfaceSpeed = surfaceSpeed

class Contour2D(X3DNode):
    """
    Contour2D : X3DNode { 
        MFNode [in]     addChildren         [NurbsCurve2D|ContourPolyline2D]
        MFNode [in]     removeChildren      [NurbsCurve2D|ContourPolyline2D]
        MFNode [in,out] children       []   [NurbsCurve2D|ContourPolyline2D]
        SFNode [in,out] metadata       NULL [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.children = children

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        if children is None:
            children = 1.0
        assertMFNode(children, NurbsCurve2D, ContourPolyline2D)
        self.__children = children

class EaseInEaseOut(X3DInterpolatorNode):
    """
    EaseInEaseOut : X3DNode {
        SFFloat [in]     set_fraction                  (-∞,∞)
        MFVec2f [in,out] easeInEaseOut            []   (-∞,∞)
        MFFloat [in,out] key                      []   (-∞,∞) 
        SFNode  [in,out] metadata                 NULL [X3DMetadataObject]
        SFFloat [out]    modifiedFraction_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            easeInEaseOut=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.easeInEaseOut = easeInEaseOut

    @property
    def easeInEaseOut(self):
        return self.__easeInEaseOut
    
    @easeInEaseOut.setter
    def easeInEaseOut(self, easeInEaseOut):
        if easeInEaseOut is None:
            easeInEaseOut = []
        assertMFVec2f(easeInEaseOut)
        self.__easeInEaseOut = easeInEaseOut

class GeoOrigin(X3DNode):
    """
    GeoOrigin : X3DNode {
        SFVec3d  [in,out] geoCoords 0 0 0       (-∞,∞)
        SFNode   [in,out] metadata  NULL        [X3DMetadataObject]
        MFString []       geoSystem ["GD","WE"] [see 25.2.3]
        SFBool   []       rotateYUp FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            geoCoords=[0.0, 0.0, 0.0],
            geoSystem=["GD", "WE"],
            rotateyUp=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.geoCoords = geoCoords
        self.geoSystem = geoSystem
        self.rotateyUp = rotateyUp

    @property
    def geoCoords(self):
        return self.__geoCoords

    @geoCoords.setter
    def geoCoords(self, geoCoords):
        if geoCoords is None:
            geoCoords = [0.0, 0.0, 0.0]
        assertSFVec3d(geoCoords)
        self.__geoCoords = geoCoords

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

    @property
    def rotateYUp(self):
        return self.__rotateYUp

    @rotateYUp.setter
    def rotateYUp(self, rotateYUp):
        if rotateYUp is None:
            rotateYUp = False
        assertSFBool(rotateYUp)
        self.__rotateYUp = rotateYUp

class LayerSet(X3DNode):
    """
    LayerSet : X3DNode { 
        SFInt32 [in,out]  activeLayer 0    (0,∞)
        MFNode  [in,out]  layers      []   [X3DLayerNode]
        SFNode  [in,out]  metadata    NULL [X3DMetadataObject]
        MFInt32 [in,out]  order       [0]   (0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            activeLayer=0,
            layers=[],
            order=[0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            **kwargs
        )
        self.activeLayer = activeLayer
        self.layers = layers
        self.order = order

    @property
    def activeLayer(self):
        return self.__activeLayer

    @activeLayer.setter
    def activeLayer(self, activeLayer):
        if activeLayer is None:
            activeLayer = 0
        assertSFInt32(activeLayer)
        assertValidGreaterThan(activeLayer, 0)
        self.__activeLayer = activeLayer

    @property
    def layers(self):
        return self.__layers

    @layers.setter
    def layers(self, layers):
        if layers is None:
            layers = []
        assertMFNode(layers, X3DLayerNode)
        self.__layers = layers

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if order is None:
            order = [0]
        assertMFInt32(order)
        assertValidGreaterThan(order, 0)
        self.__order = order
    
class MetadataBoolean(X3DNode, X3DMetadataObject):
    """
    MetadataBoolean : X3DNode, X3DMetadataObject {
      SFNode   [in,out] metadata  NULL [X3DMetadataObject]
      SFString [in,out] name      ""
      SFString [in,out] reference ""
      MFBool   [in,out] value     []
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=[],
            name="",
            reference="",
            value=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            reference=reference,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFBool(value)
        self.__value = value

class MetadataDouble(X3DMetadataObject):
    """
    MetadataDouble : X3DNode, X3DMetadataObject {
      SFNode   [in,out] metadata  NULL [X3DMetadataObject]
      SFString [in,out] name      ""
      SFString [in,out] reference ""
      MFDouble [in,out] value     []
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=[],
            name="",
            reference="",
            value=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            reference=reference,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFDouble(value)
        self.__value = value

class MetadataFloat(X3DMetadataObject):
    """
    MetadataFloat : X3DNode, X3DMetadataObject {
      SFNode   [in,out] metadata  NULL [X3DMetadataObject]
      SFString [in,out] name      ""
      SFString [in,out] reference ""
      MFFloat  [in,out] value     []
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=[],
            name="",
            reference="",
            value=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            reference=reference,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFFloat(value)
        self.__value = value

class MetadataInteger(X3DMetadataObject):
    """
    MetadataInteger : X3DNode, X3DMetadataObject {
      SFNode   [in,out] metadata  NULL [X3DMetadataObject]
      SFString [in,out] name      ""
      SFString [in,out] reference ""
      MFInt32  [in,out] value     []
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=[],
            name="",
            reference="",
            value=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            reference=reference,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFInt32(value)
        self.__value = value

class MetadataSet(X3DMetadataObject):
    """
    MetadataSet : X3DNode, X3DMetadataObject {
      SFNode   [in,out] metadata  NULL [X3DMetadataObject]
      SFString [in,out] name      ""
      SFString [in,out] reference ""
      MFNode   [in,out] value     [] [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=[],
            name="",
            reference="",
            value=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            reference=reference,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFNode(value, X3DMetadataObject)
        self.__value = value

class MetadataString(X3DMetadataObject):
    """
    MetadataString : X3DNode, X3DMetadataObject {
      SFNode   [in,out] metadata  NULL [X3DMetadataObject]
      SFString [in,out] name      ""
      SFString [in,out] reference ""
      MFString [in,out] value     []
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=[],
            name="",
            reference="",
            value=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            reference=reference,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFString(value)
        self.__value = value

class NurbsTextureCoordinate(X3DNode):
    """
    NurbsTextureCoordinate : X3DNode { 
        MFVec2f  [in,out] controlPoint []   (-∞,∞)
        SFNode   [in,out] metadata     NULL [X3DMetadataObject]
        MFFloat  [in,out] weight       []   (0,∞)
        SFInt32  []       uDimension   0    [0,∞)
        MFDouble []       uKnot        []   (-∞,∞)
        SFInt32  []       uOrder       3    [2,∞)
        SFInt32  []       vDimension   0    [0,∞)
        MFDouble []       vKnot        []   (-∞,∞)
        SFInt32  []       vOrder       3    [2,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=None,
            weight=[],
            uDimension=0,
            uKnot=[],
            uOrder=3,
            vDimension=0,
            vKnot=[],
            vOrder=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.controlPoint = controlPoint
        self.weight = weight
        self.uDimension = uDimension
        self.uKnot = uKnot
        self.uOrder = uOrder
        self.vDimension = vDimension
        self.vKnot = vKnot
        self.vOrder = vOrder

    @property
    def controlPoint(self):
        return self.__controlPoint

    @controlPoint.setter
    def controlPoint(self, controlPoint):
        if controlPoint is None:
            controlPoint = None
        assertSFNode(controlPoint, X3DCoordinateNode)
        self.__controlPoint = controlPoint

    @property
    def uDimension(self):
        return self.__uDimension

    @uDimension.setter
    def uDimension(self, uDimension):
        if uDimension is None:
            uDimension = 0
        assertSFInt32(uDimension)
        assertValidGreaterThanEquals(uDimension, 0)
        self.__uDimension = uDimension

    @property
    def uKnot(self):
        return self.__uKnot

    @uKnot.setter
    def uKnot(self, uKnot):
        if uKnot is None:
            uKnot = []
        assertMFDouble(uKnot)
        self.__uKnot = uKnot

    @property
    def uOrder(self):
        return self.__uOrder

    @uOrder.setter
    def uOrder(self, uOrder):
        if uOrder is None:
            uOrder = 3
        assertSFInt32(uOrder)
        assertValidGreaterThanEquals(uOrder, 2)
        self.__uOrder = uOrder

    @property
    def vDimension(self):
        return self.__vDimension

    @vDimension.setter
    def vDimension(self, vDimension):
        if vDimension is None:
            vDimension = 0
        assertSFInt32(vDimension)
        assertValidGreaterThanEquals(vDimension, 0)
        self.__vDimension = vDimension

    @property
    def vKnot(self):
        return self.__vKnot

    @vKnot.setter
    def vKnot(self, vKnot):
        if vKnot is None:
            vKnot = []
        assertMFDouble(vKnot)
        self.__vKnot = vKnot

    @property
    def vOrder(self):
        return self.__vOrder

    @vOrder.setter
    def vOrder(self, vOrder):
        if vOrder is None:
            vOrder = 3
        assertSFInt32(vOrder)
        assertValidGreaterThanEquals(vOrder, 2)
        self.__vOrder = vOrder

class RigidBody(X3DNode):
    """
    RigidBody : X3DNode {
        SFFloat    [in,out] angularDampingFactor 0.001   [0,1]
        SFVec3f    [in,out] angularVelocity      0 0 0   (-∞,∞)
        SFBool     [in,out] autoDamp             FALSE
        SFBool     [in,out] autoDisable          FALSE
        SFVec3f    [in,out] centerOfMass         0 0 0   (-∞,∞)
        SFFloat    [in,out] disableAngularSpeed  0       [0,∞)
        SFFloat    [in,out] disableLinearSpeed   0       [0,∞)
        SFFloat    [in,out] disableTime          0       [0,∞)
        SFBool     [in,out] enabled              TRUE
        SFVec3f    [in,out] finiteRotationAxis   0 0 0   [-1,1]
        SFBool     [in,out] fixed                FALSE
        MFVec3f    [in,out] forces               []
        MFNode     [in,out] geometry             []      [X3DNBodyCollidableNode]
        SFMatrix3f [in,out] inertia	           1 0 0
                                                0 1 0
                                                0 0 1
        SFFloat    [in,out] linearDampingFactor  0.001   [0,1]
        SFVec3f    [in,out] linearVelocity       0 0 0   (-∞,∞)
        SFFloat    [in,out] mass                 1       (0,∞)
        SFNode     [in,out] massDensityModel     NULL    [Sphere, Box, Cone]
        SFNode     [in,out] metadata             NULL    [X3DMetadataObject]
        SFRotation [in,out] orientation          0 0 1 0 [0,1]
        SFVec3f    [in,out] position             0 0 0   (-∞,∞)
        MFVec3f    [in,out] torques              []
        SFBool     [in,out] useFiniteRotation    FALSE
        SFBool     [in,out] useGlobalGravity     TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            angularDampingFactor=0.001,
            angularVelocity=[0.0, 0.0, 0.0],
            autoDamp=False,
            autoDisable=False,
            centerOfMass=[0.0, 0.0, 0.0],
            disableAngularSpeed=0.0,
            disableLinearSpeed=0.0,
            disableTime=0.0,
            enabled=True,
            finiteRotationAxis=[0.0, 0.0, 0.0],
            fixed=False,
            forces=[],
            geometry=[],
            inertia=[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
            linearDampingFactor=[0.001],
            linearVelocity=[0.0, 0.0, 0.0],
            mass=1.0,
            massDensityModel=None,
            orientation=[0.0, 0.0, 1.0, 0.0],
            position=[0.0, 0.0, 0.0],
            torques=[],
            useFiniteRotation=False,
            useGlobalGravity=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.angularDampingFactor = angularDampingFactor
        self.angularVelocity = angularVelocity
        self.autoDamp = autoDamp
        self.autoDisable = autoDisable
        self.centerOfMass = centerOfMass
        self.disableAngularSpeed = disableAngularSpeed
        self.disableLinearSpeed = disableLinearSpeed
        self.disableTime = disableTime
        self.enabled = enabled
        self.finiteRotationAxis = finiteRotationAxis
        self.fixed = fixed
        self.forces = forces
        self.geometry = geometry
        self.inertia = inertia
        self.linearDampingFactor = linearDampingFactor
        self.linearVelocity = linearVelocity
        self.mass = mass
        self.massDensityModel = massDensityModel
        self.orientation = orientation
        self.position = position
        self.torques = torques
        self.useFiniteRotation = useFiniteRotation
        self.useGlobalGravity = useGlobalGravity

    @property
    def angularDampingFactor(self):
        return self.__angularDampingFactor

    @angularDampingFactor.setter
    def angularDampingFactor(self, angularDampingFactor):
        if angularDampingFactor is None:
            angularDampingFactor = 0.0001
        assertSFFloat(angularDampingFactor)
        assertValidGreaterThanEquals(angularDampingFactor, 0)
        assertValidLessThanEquals(angularDampingFactor, 1)
        self.__angularDampingFactor = angularDampingFactor

    @property
    def angularVelocity(self):
        return self.__angularVelocity

    @angularVelocity.setter
    def angularVelocity(self, angularVelocity):
        if angularVelocity is None:
            angularVelocity = [0.0, 0.0, 0.0]
        assertSFVec3f(angularVelocity)
        self.__angularVelocity = angularVelocity

    @property
    def autoDamp(self):
        return self.__autoDamp

    @autoDamp.setter
    def autoDamp(self, autoDamp):
        if autoDamp is None:
            autoDamp = False
        assertSFBool(autoDamp)
        self.__autoDamp = autoDamp

    @property
    def autoDisable(self):
        return self.__autoDisable

    @autoDisable.setter
    def autoDisable(self, autoDisable):
        if autoDisable is None:
            autoDisable = False
        assertSFBool(autoDisable)
        self.__autoDisable = autoDisable

    @property
    def centerOfMass(self):
        return self.__centerOfMass

    @centerOfMass.setter
    def centerOfMass(self, centerOfMass):
        if centerOfMass is None:
            centerOfMass = [0.0, 0.0, 0.0]
        assertSFVec3f(centerOfMass)
        self.__centerOfMass = centerOfMass

    @property
    def disableAngularSpeed(self):
        return self.__disableAngularSpeed

    @disableAngularSpeed.setter
    def disableAngularSpeed(self, disableAngularSpeed):
        if disableAngularSpeed is None:
            disableAngularSpeed = 0.0
        assertSFFloat(disableAngularSpeed)
        assertValidGreaterThanEquals(disableAngularSpeed, 0)
        self.__disableAngularSpeed = disableAngularSpeed

    @property
    def disableLinearSpeed(self):
        return self.__disableLinearSpeed

    @disableLinearSpeed.setter
    def disableLinearSpeed(self, disableLinearSpeed):
        if disableLinearSpeed is None:
            disableLinearSpeed = 0.0
        assertSFFloat(disableLinearSpeed)
        assertValidGreaterThanEquals(disableLinearSpeed, 0)
        self.__disableLinearSpeed = disableLinearSpeed

    @property
    def disableTime(self):
        return self.__disableTime

    @disableTime.setter
    def disableTime(self, disableTime):
        if disableTime is None:
            disableTime = 0.0
        assertSFFloat(disableTime)
        assertValidGreaterThanEquals(disableTime, 0)
        self.__disableTime = disableTime

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

    @property
    def finiteRotationAxis(self):
        return self.__finiteRotationAxis

    @finiteRotationAxis.setter
    def finiteRotationAxis(self, finiteRotationAxis):
        if finiteRotationAxis is None:
            finiteRotationAxis = [0.0, 0.0, 0.0]
        assertSFVec3f(finiteRotationAxis)
        assertValidGreaterThanEquals(finiteRotationAxis, -1)
        assertValidLessThanEquals(finiteRotationAxis, 1)
        self.__finiteRotationAxis = finiteRotationAxis

    @property
    def fixed(self):
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed):
        if fixed is None:
            fixed = False
        assertSFBool(fixed)
        self.__fixed = fixed

    @property
    def forces(self):
        return self.__forces

    @forces.setter
    def forces(self, forces):
        if forces is None:
            forces = []
        assertMFVec3f(forces)
        self.__forces = forces

    @property
    def geometry(self):
        return self.__geometry

    @geometry.setter
    def geometry(self, geometry):
        if geometry is None:
            geometry = []
        assertMFNode(geometry, X3DNBodyCollidableNode)
        self.__geometry = geometry

    @property
    def inertia(self):
        return self.__inertia

    @inertia.setter
    def inertia(self, inertia):
        if inertia is None:
            inertia = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        assertMFMatrix3f(inertia)
        self.__inertia = inertia

    @property
    def linearDampingFactor(self):
        return self.__linearDampingFactor

    @linearDampingFactor.setter
    def linearDampingFactor(self, linearDampingFactor):
        if linearDampingFactor is None:
            linearDampingFactor = 0.0001
        assertSFFloat(linearDampingFactor)
        assertValidGreaterThanEquals(linearDampingFactor, 0)
        assertValidLessThanEquals(linearDampingFactor, 1)
        self.__linearDampingFactor = linearDampingFactor

    @property
    def linearVelocity(self):
        return self.__linearVelocity

    @linearVelocity.setter
    def linearVelocity(self, linearVelocity):
        if linearVelocity is None:
            linearVelocity = [0.0, 0.0, 0.0]
        assertSFVec3f(linearVelocity)
        self.__linearVelocity = linearVelocity

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        if mass is None:
            mass = 1.0
        assertSFFloat(mass)
        assertValidGreaterThan(mass, 0)
        self.__mass = mass

    @property
    def massDensityModel(self):
        return self.__massDensityModel

    @massDensityModel.setter
    def massDensityModel(self, massDensityModel):
        if massDensityModel is None:
            massDensityModel = None
        assertSFNode(massDensityModel, Sphere, Box, Cone)
        self.__massDensityModel = massDensityModel

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        if orientation is None:
            orientation = [0.0, 0.0, 0.0, 1.0]
        assertSFRotation(orientation)
        assertValidGreaterThanEquals(orientation, 0)
        assertValidLessThanEquals(orientation, 1)
        self.__orientation = orientation

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position is None:
            position = [0.0, 0.0, 0.0]
        assertSFVec3f(position)
        self.__position = position

    @property
    def torques(self):
        return self.__torques

    @torques.setter
    def torques(self, torques):
        if torques is None:
            torques = []
        assertMFVec3f(torques)
        self.__torques = torques

    @property
    def useFiniteRotation(self):
        return self.__useFiniteRotation

    @useFiniteRotation.setter
    def useFiniteRotation(self, useFiniteRotation):
        if useFiniteRotation is None:
            useFiniteRotation = False
        assertSFBool(useFiniteRotation)
        self.__useFiniteRotation = useFiniteRotation

    @property
    def useGlobalGravity(self):
        return self.__useGlobalGravity

    @useGlobalGravity.setter
    def useGlobalGravity(self, useGlobalGravity):
        if useGlobalGravity is None:
            useGlobalGravity = True
        assertSFBool(useGlobalGravity)
        self.__useGlobalGravity = useGlobalGravity

class ShaderPart(X3DNode, X3DUrlObject):
    """
    ShaderPart : X3DNode, X3DUrlObject {
        SFNode   [in,out] metadata NULL       [X3DMetadataObject]
        MFString [in,out] url      []         [URI]
        SFString []       type     "VERTEX"   ["VERTEX"|"FRAGMENT"]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
            type_="VERTEX",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            url=url,
            **kwargs
        )
        self.type_ = type_

    @property
    def type_(self):
        return self.__type_

    @type_.setter
    def type_(self, type_):
        if type_ is None:
            type_ = "VERTEX"
        assertValidShaderType(type_)
        self.__type_ = type_

class ShaderProgram(X3DNode, X3DUrlObject, X3DProgrammableShaderObject):
    """
    ShaderProgram : X3DNode, X3DUrlObject, X3DProgrammableShaderObject {
        SFNode    [in,out] metadata  NULL         [X3DMetadataObject]
        MFString  [in,out] url       []           [URI]
        SFString  []       type      "VERTEX"     ["VERTEX"|"FRAGMENT"]

        # And any number of:
        fieldType [in]     fieldName
        fieldType [in,out] fieldName initialValue
        fieldType [out]    fieldName
        fieldType []       fieldName initialValue
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
            type_="VERTEX",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            url=url,
            **kwargs
        )
        self.type_ = type_

    @property
    def type_(self):
        return self.__type_

    @type_.setter
    def type_(self, type_):
        if type_ is None:
            type_ = "VERTEX"
        assertValidShaderType(type_)
        self.__type_ = type_

class TextureProperties(X3DNode): 
    """
    TextureProperties : X3DNode
        SFFloat     [in,out] anisotropicDegree   1.0       [1,∞)
        SFColorRGBA [in,out] borderColor         0 0 0 0   [0,1]
        SFInt32     [in,out] borderWidth         0         [0,1]
        SFString    [in,out] boundaryModeS       "REPEAT"  [see Table 18.7]
        SFString    [in,out] boundaryModeT       "REPEAT"  [see Table 18.7]
        SFString    [in,out] boundaryModeR       "REPEAT"  [see Table 18.7]
        SFString    [in,out] magnificationFilter "FASTEST" [see Table 18.8]
        SFNode      [in,out] metadata            NULL      [X3DMetadataObject]
        SFString    [in,out] minificationFilter  "FASTEST" [see Table 18.9]
        SFString    [in,out] textureCompression  "FASTEST" [see Table 18.10]
        SFFloat     [in,out] texturePriority     0         [0,1]
        SFBool      []       generateMipMaps     FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            anisotropicDegree=1.0,
            borderColor=[0.0, 0.0, 0.0, 0.0],
            borderWidth=0,
            boundaryModeS="REPEAT",
            boundaryModeT="REPEAT",
            boundaryModeR="REPEAT",
            magnificationFilter="FASTEST",
            minificationFilter="FASTEST",
            textureCompression="FASTEST",
            texturePriority=0.0,
            generateMipMaps=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.anisotropicDegree = anisotropicDegree
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.boundaryModeS = boundaryModeS
        self.boundaryModeT = boundaryModeT
        self.boundaryModeR = boundaryModeR
        self.magnificationFilter = magnificationFilter
        self.minificationFilter = minificationFilter
        self.textureCompression = textureCompression
        self.texturePriority = texturePriority
        self.generateMipMaps = generateMipMaps

    @property
    def anisotropicDegree(self):
        return self.__anisotropicDegree

    @anisotropicDegree.setter
    def anisotropicDegree(self, anisotropicDegree):
        if anisotropicDegree is None:
            anisotropicDegree = 1.0
        assertSFFloat(anisotropicDegree)
        assertValidGreaterThanEquals(anisotropicDegree, 1)
        self.__anisotropicDegree = anisotropicDegree

    @property
    def borderColor(self):
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor):
        if borderColor is None:
            borderColor = [0.0, 0.0, 0.0, 0.0]
        assertSFColorRGBA(borderColor)
        assertValidGreaterThanEquals(borderColor, 0)
        assertValidLessThanEquals(borderColor, 1)
        self.__borderColor = borderColor

    @property
    def borderWidth(self):
        return self.__borderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth):
        if borderWidth is None:
            borderWidth = 0
        assertMFInt32(borderWidth)
        assertValidGreaterThanEquals(borderWidth, 0)
        assertValidLessThanEquals(borderWidth, 1)
        self.__borderWidth = borderWidth

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 1.0
        assertSFFloat(radius)
        self.__radius = radius

    @property
    def boundaryModeS(self):
        return self.__boundaryModeS

    @boundaryModeS.setter
    def boundaryModeS(self, boundaryModeS):
        if boundaryModeS is None:
            boundaryModeS = "REPEAT"
        assertValidTextureBoundaryModes(boundaryModeS)
        self.__boundaryModeS = boundaryModeS

    @property
    def boundaryModeT(self):
        return self.__boundaryModeT

    @boundaryModeT.setter
    def boundaryModeT(self, boundaryModeT):
        if boundaryModeT is None:
            boundaryModeT = "REPEAT"
        assertValidTextureBoundaryModes(boundaryModeT)
        self.__boundaryModeT = boundaryModeT

    @property
    def boundaryModeR(self):
        return self.__boundaryModeR

    @boundaryModeR.setter
    def boundaryModeR(self, boundaryModeR):
        if boundaryModeR is None:
            boundaryModeR = "REPEAT"
        assertValidTextureBoundaryModes(boundaryModeR)
        self.__boundaryModeR = boundaryModeR

    @property
    def magnificationFilter(self):
        return self.__magnificationFilter

    @magnificationFilter.setter
    def magnificationFilter(self, magnificationFilter):
        if magnificationFilter is None:
            magnificationFilter = "FASTEST"
        assertValidTextureMagnificationModes(magnificationFilter)
        self.__magnificationFilter = magnificationFilter

    @property
    def minificationFilter(self):
        return self.__minificationFilter

    @minificationFilter.setter
    def minificationFilter(self, minificationFilter):
        if minificationFilter is None:
            minificationFilter = "FASTEST"
        assertValidTextureMinificationModes(minificationFilter)
        self.__minificationFilter = minificationFilter

    @property
    def textureCompression(self):
        return self.__textureCompression

    @textureCompression.setter
    def textureCompression(self, textureCompression):
        if textureCompression is None:
            textureCompression = "FASTEST"
        assertValidTextureCompressionModes(textureCompression)
        self.__textureCompression = textureCompression
    
    @property
    def texturePriority(self):
        return self.__texturePriority

    @texturePriority.setter
    def texturePriority(self, texturePriority):
        if texturePriority is None:
            texturePriority = 0.0
        assertSFFloat(texturePriority)
        assertValidGreaterThanEquals(texturePriority, 0)
        assertValidLessThanEquals(texturePriority, 1)
        self.__texturePriority = texturePriority

    @property
    def generateMipMaps(self):
        return self.__generateMipMaps

    @generateMipMaps.setter
    def generateMipMaps(self, generateMipMaps):
        if generateMipMaps is None:
            generateMipMaps = False
        assertSFBool(generateMipMaps)
        self.__generateMipMaps = generateMipMaps

class Appearance(X3DAppearanceNode):
    """
    Appearance : X3DAppearanceNode { 
        SFNode [in,out] fillProperties   NULL [FillProperties]
        SFNode [in,out] lineProperties   NULL [LineProperties]
        SFNode [in,out] material         NULL [X3DMaterialNode]
        SFNode [in,out] metadata         NULL [X3DMetadataObject]
        MFNode [in,out] shaders          []   [X3DShaderNode]
        SFNode [in,out] texture          NULL [X3DTextureNode]
        SFNode [in,out] textureTransform NULL [X3DTextureTransformNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            fillProperties=None,
            lineProperties=None,
            material=None,
            shaders=[],
            texture=None,
            textureTransform=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.fillProperties = fillProperties
        self.lineProperties = lineProperties
        self.material = material
        self.shaders = shaders
        self.texture = texture
        self.textureTransform = textureTransform

    @property
    def fillProperties(self):
        return self.__fillProperties

    @fillProperties.setter
    def fillProperties(self, fillProperties):
        if fillProperties is None:
            fillProperties = None
        assertSFNode(fillProperties, FillProperties)
        self.__fillProperties = fillProperties

    @property
    def lineProperties(self):
        return self.__lineProperties

    @lineProperties.setter
    def lineProperties(self, lineProperties):
        if lineProperties is None:
            lineProperties = None
        assertSFNode(lineProperties, LineProperties)
        self.__lineProperties = lineProperties

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        if material is None:
            material = None
        assertSFNode(material, X3DMaterialNode)
        self.__material = material

    @property
    def shaders(self):
        return self.__shaders

    @shaders.setter
    def shaders(self, shaders):
        if shaders is None:
            shaders = []
        assertMFNode(shaders, X3DShaderNode)
        self.__shaders = shaders

    @property
    def texture(self):
        return self.__texture

    @texture.setter
    def texture(self, texture):
        if texture is None:
            texture = None
        assertSFNode(texture, X3DTextureNode)
        self.__texture = texture

    @property
    def textureTransform(self):
        return self.__textureTransform

    @textureTransform.setter
    def textureTransform(self, textureTransform):
        if textureTransform is None:
            textureTransform = None
        assertSFNode(textureTransform, X3DTextureTransformNode)
        self.__textureTransform = textureTransform

class FillProperties(X3DAppearanceChildNode):
    """
    FillProperties : X3DAppearanceChildNode { 
        SFBool  [in,out] filled     TRUE
        SFColor [in,out] hatchColor 1 1 1 [0,1]
        SFBool  [in,out] hatched    TRUE
        SFInt32 [in,out] hatchStyle 1     [0,∞)
        SFNode  [in,out] metadata   NULL  [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            filled=True,
            hatchColor=[1.0, 1.0, 1.0],
            hatched=True,
            hatchStyle=1,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.filled = filled
        self.hatchColor = hatchColor
        self.hatched = hatched
        self.hatchStyle = hatchStyle

    @property
    def filled(self):
        return self.__filled

    @filled.setter
    def filled(self, filled):
        if filled is None:
            filled = True
        assertSFBool(filled)
        self.__filled = filled

    @property
    def hatchColor(self):
        return self.__hatchColor

    @hatchColor.setter
    def hatchColor(self, hatchColor):
        if hatchColor is None:
            hatchColor = [1.0, 1.0, 1.0]
        assertSFColor(hatchColor)
        assertValidGreaterThanEquals(hatchColor, 0)
        assertValidLessThanEquals(hatchColor, 1)
        self.__hatchColor = hatchColor

    @property
    def hatched(self):
        return self.__hatched

    @hatched.setter
    def hatched(self, hatched):
        if hatched is None:
            hatched = True
        assertSFBool(hatched)
        self.__hatched = hatched

    @property
    def hatchStyle(self):
        return self.__hatchStyle

    @hatchStyle.setter
    def hatchStyle(self, hatchStyle):
        if hatchStyle is None:
            hatchStyle = 1
        assertSFInt32(hatchStyle)
        assertValidGreaterThanEquals(hatchStyle, 0)
        self.__hatchStyle = hatchStyle
class LineProperties(X3DAppearanceChildNode):
    """
    LineProperties : X3DAppearanceChildNode { 
        SFBool  [in,out] applied              TRUE
        SFInt32 [in,out] linetype             1    [1,∞)
        SFFloat [in,out] linewidthScaleFactor 0    (-∞,∞)
        SFNode  [in,out] metadata             NULL [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            applied=True,
            linetype=1,
            linewidthScaleFactor=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.applied = applied
        self.linetype = linetype
        self.linewidthScaleFactor = linewidthScaleFactor

    @property
    def applied(self):
        return self.__applied

    @applied.setter
    def applied(self, applied):
        if applied is None:
            applied = True
        assertSFBool(applied)
        self.__applied = applied

    @property
    def linetype(self):
        return self.__linetype

    @linetype.setter
    def linetype(self, linetype):
        if linetype is None:
            linetype = 1
        assertSFInt32(linetype)
        assertValidGreaterThanEquals(linetype, 1)
        self.__linetype = linetype

    @property
    def linewidthScaleFactor(self):
        return self.__linewidthScaleFactor

    @linewidthScaleFactor.setter
    def linewidthScaleFactor(self, linewidthScaleFactor):
        if linewidthScaleFactor is None:
            linewidthScaleFactor = 0.0
        assertSFFloat(linewidthScaleFactor)
        self.__linewidthScaleFactor = linewidthScaleFactor

class Material(X3DMaterialNode): 
    """
    Material : X3DMaterialNode { 
        SFFloat [in,out] ambientIntensity 0.2         [0,1]
        SFColor [in,out] diffuseColor     0.8 0.8 0.8 [0,1]
        SFColor [in,out] emissiveColor    0 0 0       [0,1]
        SFNode  [in,out] metadata         NULL        [X3DMetadataObject]
        SFFloat [in,out] shininess        0.2         [0,1]
        SFColor [in,out] specularColor    0 0 0       [0,1]
        SFFloat [in,out] transparency     0           [0,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            ambientIntensity=0.2,
            diffuseColor=[0.8, 0.8, 0.8],
            emissiveColor=[0.0, 0.0, 0.0],
            shininess=0.2,
            specularColor=[0.0, 0.0, 0.0],
            transparency=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.ambientIntensity = ambientIntensity
        self.diffuseColor = diffuseColor
        self.emissiveColor = emissiveColor
        self.shininess = shininess
        self.specularColor = specularColor
        self.transparency = transparency

    @property
    def ambientIntensity(self):
        return self.__ambientIntensity

    @ambientIntensity.setter
    def ambientIntensity(self, ambientIntensity):
        if ambientIntensity is None:
            ambientIntensity = 0.2
        assertSFFloat(ambientIntensity)
        assertValidGreaterThanEquals(ambientIntensity, 0)
        assertValidLessThanEquals(ambientIntensity, 1)
        self.__ambientIntensity = ambientIntensity

    @property
    def diffuseColor(self):
        return self.__diffuseColor

    @diffuseColor.setter
    def diffuseColor(self, diffuseColor):
        if diffuseColor is None:
            diffuseColor = [0.8, 0.8, 0.8]
        assertSFColor(diffuseColor)
        assertValidGreaterThanEquals(diffuseColor, 0)
        assertValidLessThanEquals(diffuseColor, 1)
        self.__diffuseColor = diffuseColor

    @property
    def emissiveColor(self):
        return self.__emissiveColor

    @emissiveColor.setter
    def emissiveColor(self, emissiveColor):
        if emissiveColor is None:
            emissiveColor = [0.0, 0.0, 0.0]
        assertSFColor(emissiveColor)
        assertValidGreaterThanEquals(emissiveColor, 0)
        assertValidLessThanEquals(emissiveColor, 1)
        self.__emissiveColor = emissiveColor

    @property
    def shininess(self):
        return self.__shininess

    @shininess.setter
    def shininess(self, shininess):
        if shininess is None:
            shininess = 0.2
        assertSFFloat(shininess)
        assertValidGreaterThanEquals(shininess, 0)
        assertValidLessThanEquals(shininess, 1)
        self.__shininess = shininess

    @property
    def specularColor(self):
        return self.__specularColor

    @specularColor.setter
    def specularColor(self, specularColor):
        if specularColor is None:
            specularColor = [0.0, 0.0, 0.0]
        assertSFColor(specularColor)
        assertValidGreaterThanEquals(specularColor, 0)
        assertValidLessThanEquals(specularColor, 1)
        self.__specularColor = specularColor

    @property
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, transparency):
        if transparency is None:
            transparency = 0.0
        assertSFFloat(transparency)
        assertValidGreaterThanEquals(transparency, 0)
        assertValidLessThanEquals(transparency, 1)
        self.__transparency = transparency

class TwoSidedMaterial(X3DMaterialNode): 
    """
    TwoSidedMaterial : X3DMaterialNode {
        SFFloat [in,out] ambientIntensity     0.2         [0,1]
        SFFloat [in,out] backAmbientIntensity 0.2         [0,1]
        SFColor [in,out] backDiffuseColor     0.8 0.8 0.8 [0,1]
        SFColor [in,out] backEmissiveColor    0 0 0       [0,1]
        SFFloat [in,out] backShininess        0.2         [0,1]
        SFColor [in,out] backSpecularColor    0 0 0       [0,1]
        SFFloat [in,out] backTransparency     0           [0,1]
        SFColor [in,out] diffuseColor         0.8 0.8 0.8 [0,1]
        SFColor [in,out] emissiveColor        0 0 0       [0,1]
        SFNode  [in,out] metadata             NULL        [X3DMetadataObject]
        SFFloat [in,out] shininess            0.2         [0,1]
        SFBool  [in,out] separateBackColor    FALSE
        SFColor [in,out] specularColor        0 0 0       [0,1]
        SFFloat [in,out] transparency         0           [0,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            ambientIntensity=0.2,
            backAmbientIntensity=0.2,
            backDiffuseColor=[0.8, 0.8, 0.8],
            backEmissiveColor=[0.0, 0.0, 0.0],
            backShininess=0.2,
            backSpecularColor=[0.0, 0.0, 0.0],
            backTransparency=0,
            diffuseColor=[0.8, 0.8, 0.8],
            emissiveColor=[0.0, 0.0, 0.0],
            shininess=0.2,
            separateBackColor=False,
            specularColor=[0.0, 0.0, 0.0],
            transparency=0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.ambientIntensity = ambientIntensity
        self.backAmbientIntensity = backAmbientIntensity
        self.backDiffuseColor = backDiffuseColor
        self.backEmissiveColor = backEmissiveColor
        self.backShininess = backShininess
        self.backSpecularColor = backSpecularColor
        self.backTransparency = backTransparency
        self.diffuseColor = diffuseColor
        self.emissiveColor = emissiveColor
        self.shininess = shininess
        self.separateBackColor = separateBackColor
        self.specularColor = specularColor
        self.transparency = transparency
    
    @property
    def ambientIntensity(self):
        return self.__ambientIntensity

    @ambientIntensity.setter
    def ambientIntensity(self, ambientIntensity):
        if ambientIntensity is None:
            ambientIntensity = 0.2
        assertSFFloat(ambientIntensity)
        assertValidGreaterThanEquals(ambientIntensity, 0)
        assertValidLessThanEquals(ambientIntensity, 1)
        self.__ambientIntensity = ambientIntensity

    @property
    def backAmbientIntensity(self):
        return self.__backAmbientIntensity

    @backAmbientIntensity.setter
    def backAmbientIntensity(self, backAmbientIntensity):
        if backAmbientIntensity is None:
            backAmbientIntensity = 0.2
        assertSFFloat(backAmbientIntensity)
        assertValidGreaterThanEquals(backAmbientIntensity, 0)
        assertValidLessThanEquals(backAmbientIntensity, 1)
        self.__backAmbientIntensity = backAmbientIntensity

    @property
    def backDiffuseColor(self):
        return self.__backDiffuseColor

    @backDiffuseColor.setter
    def backDiffuseColor(self, backDiffuseColor):
        if backDiffuseColor is None:
            backDiffuseColor = [0.8, 0.8, 0.8]
        assertSFColor(backDiffuseColor)
        assertValidGreaterThanEquals(backDiffuseColor, 0)
        assertValidLessThanEquals(backDiffuseColor, 1)
        self.__backDiffuseColor = backDiffuseColor

    @property
    def backEmissiveColor(self):
        return self.__backEmissiveColor

    @backEmissiveColor.setter
    def backEmissiveColor(self, backEmissiveColor):
        if backEmissiveColor is None:
            backEmissiveColor = [0.0, 0.0, 0.0]
        assertSFColor(backEmissiveColor)
        assertValidGreaterThanEquals(backEmissiveColor, 0)
        assertValidLessThanEquals(backEmissiveColor, 1)
        self.__backEmissiveColor = backEmissiveColor

    @property
    def backShininess(self):
        return self.__backShininess

    @backShininess.setter
    def backShininess(self, backShininess):
        if backShininess is None:
            backShininess = 0.2
        assertSFFloat(backShininess)
        assertValidGreaterThanEquals(backShininess, 0)
        assertValidLessThanEquals(backShininess, 1)
        self.__backShininess = backShininess

    @property
    def backSpecularColor(self):
        return self.__backSpecularColor

    @backSpecularColor.setter
    def backSpecularColor(self, backSpecularColor):
        if backSpecularColor is None:
            backSpecularColor = [0.0, 0.0, 0.0]
        assertSFColor(backSpecularColor)
        assertValidGreaterThanEquals(backSpecularColor, 0)
        assertValidLessThanEquals(backSpecularColor, 1)
        self.__backSpecularColor = backSpecularColor

    @property
    def backTransparency(self):
        return self.__backTransparency

    @backTransparency.setter
    def backTransparency(self, backTransparency):
        if backTransparency is None:
            backTransparency = 0.0
        assertSFFloat(backTransparency)
        assertValidGreaterThanEquals(backTransparency, 0)
        assertValidLessThanEquals(backTransparency, 1)
        self.__backTransparency = backTransparency


    @property
    def diffuseColor(self):
        return self.__diffuseColor

    @diffuseColor.setter
    def diffuseColor(self, diffuseColor):
        if diffuseColor is None:
            diffuseColor = [0.8, 0.8, 0.8]
        assertSFColor(diffuseColor)
        assertValidGreaterThanEquals(diffuseColor, 0)
        assertValidLessThanEquals(diffuseColor, 1)
        self.__diffuseColor = diffuseColor

    @property
    def emissiveColor(self):
        return self.__emissiveColor

    @emissiveColor.setter
    def emissiveColor(self, emissiveColor):
        if emissiveColor is None:
            emissiveColor = [0.0, 0.0, 0.0]
        assertSFColor(emissiveColor)
        assertValidGreaterThanEquals(emissiveColor, 0)
        assertValidLessThanEquals(emissiveColor, 1)
        self.__emissiveColor = emissiveColor

    @property
    def shininess(self):
        return self.__shininess

    @shininess.setter
    def shininess(self, shininess):
        if shininess is None:
            shininess = 0.2
        assertSFFloat(shininess)
        assertValidGreaterThanEquals(shininess, 0)
        assertValidLessThanEquals(shininess, 1)
        self.__shininess = shininess

    @property
    def separateBackColor(self):
        return self.__separateBackColor

    @separateBackColor.setter
    def separateBackColor(self, separateBackColor):
        if separateBackColor is None:
            separateBackColor = False
        assertSFBool(separateBackColor)
        self.__separateBackColor = separateBackColor

    @property
    def specularColor(self):
        return self.__specularColor

    @specularColor.setter
    def specularColor(self, specularColor):
        if specularColor is None:
            specularColor = [0.0, 0.0, 0.0]
        assertSFColor(specularColor)
        assertValidGreaterThanEquals(specularColor, 0)
        assertValidLessThanEquals(specularColor, 1)
        self.__specularColor = specularColor

    @property
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, transparency):
        if transparency is None:
            transparency = 0.0
        assertSFFloat(transparency)
        assertValidGreaterThanEquals(transparency, 0)
        assertValidLessThanEquals(transparency, 1)
        self.__transparency = transparency

class ComposedShader(X3DShaderNode, X3DProgrammableShaderObject):
    """
    ComposedShader : X3DShaderNode, X3DProgrammableShaderObject {
        SFBool    [in]     activate
        SFNode    [in,out] metadata   NULL [X3DMetadataObject]
        MFNode    [in,out] parts      []   [ShaderPart]
        SFBool    [out]    isSelected
        SFBool    [out]    isValid
        SFString []        language   ""   ["Cg"|"GLSL"|"HLSL"|...]

        # And any number of:
        fieldType []       fieldName
        fieldType [in]     fieldName
        fieldType [out]    fieldName
        fieldType [in,out] fieldName
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            parts=[],
            language="",
            **kwargs
    ):
        super().__init__(
            self,
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            language=language,
            **kwargs
        )
        self.parts = parts

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, parts):
        if parts is None:
            parts = []
        assertMFNode(parts, ShaderPart)
        self.__parts = parts

class PackagedShader(X3DShaderNode, X3DUrlObject, X3DProgrammableShaderObject):
    """
    PackagedShader : X3DShaderNode, X3DUrlObject, X3DProgrammableShaderObject {
        SFBool    [in]     activate
        SFNode    [in,out] metadata   NULL [X3DMetadataObject]
        MFString  [in,out] url        []   [URI]
        SFBool    [out]    isSelected
        SFBool    [out]    isValid
        SFString []        language   ""   ["Cg"|"GLSL"|"HLSL"|...]

        # And any number of:
        fieldType [in]     fieldName
        fieldType [in,out] fieldName initialValue
        fieldType [out]    fieldName
        fieldType []       fieldName initialValue
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
            language="",
            **kwargs
    ):
        super().__init__(
            self,
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            language=language,
            url=url,
            **kwargs
        )

class ProgramShader(X3DShaderNode):
    """
    ProgramShader : X3DShaderNode {
        SFBool   [in]     activate
        SFNode   [in,out] metadata   NULL [X3DMetadataObject]
        MFNode   [in,out] programs   []   [ShaderProgram]
        SFBool   [out]    isSelected
        SFBool   [out]    isValid
        SFString []       language   ""   ["Cg"|"GLSL"|"HLSL"|...]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            programs=[],
            language="",
            **kwargs
    ):
        super().__init__(
            self,
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            language=language,
            **kwargs
        )
        self.programs = programs

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def prorgams(self, prorgams):
        if prorgams is None:
            prorgams = []
        assertMFNode(prorgams, ShaderProgram)
        self.__prorgams = prorgams

class MultiTexture(X3DTextureNode):
    """
    MultiTexture : X3DTextureNode {
        SFFloat  [in,out] alpha    1     [0,1]
        SFColor  [in,out] color    1 1 1 [0,1] 
        MFString [in,out] function []
        SFNode   [in,out] metadata NULL  [X3DMetadataObject]
        MFString [in,out] mode     []
        MFString [in,out] source   []
        MFNode   [in,out] texture  []    [X3DTextureNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            alpha=1.0,
            color=[1.0, 1.0, 1.0],
            function=[],
            mode=[],
            source=[],
            texture=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.alpha = alpha
        self.color = color
        self.function = function
        self.mode = mode
        self.source = source
        self.texture = texture

    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha):
        if alpha is None:
            alpha = 1.0
        assertSFFloat(alpha)
        assertValidGreaterThanEquals(alpha, 0)
        assertValidLessThanEquals(alpha, 1)
        self.__alpha = alpha

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = [1.0, 1.0, 1.0]
        assertSFColor(color)
        assertValidGreaterThanEquals(color, 0)
        assertValidLessThanEquals(color, 1)
        self.__color = color

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function):
        if function is None:
            function = []
        assertValidMultiTextureFunction(function)
        self.__function = function

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        if mode is None:
            mode = []
        assertValidMultiTextureModes(mode)
        self.__mode = mode

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        if source is None:
            source = []
        assertValidMultiTextureSource(source)
        self.__source = source

    @property
    def texture(self):
        return self.__texture

    @texture.setter
    def texture(self, texture):
        if texture is None:
            texture = []
        assertMFNode(texture, X3DTextureNode)
        self.__texture = texture

class ComposedCubeMapTexture(X3DEnvironmentTextureNode):
    """
    ComposedCubeMapTexture : X3DEnvironmentTextureNode {
        SFNode [in,out] back     NULL [X3DTexture2DNode]
        SFNode [in,out] bottom   NULL [X3DTexture2DNode]
        SFNode [in,out] front    NULL [X3DTexture2DNode]
        SFNode [in,out] left     NULL [X3DTexture2DNode]
        SFNode [in,out] metadata NULL [X3DMetadataObject]
        SFNode [in,out] right    NULL [X3DTexture2DNode]
        SFNode [in,out] top      NULL [X3DTexture2DNode]
    }
    """

class GeneratedCubeMapTexture(X3DEnvironmentTextureNode):
    """
    GeneratedCubeMapTexture : X3DEnvironmentTextureNode {
        SFNode   [in,out] metadata          NULL   [X3DMetadataObject]
        SFString [in,out] update            "NONE" ["NONE"|"NEXT_FRAME_ONLY"|"ALWAYS"]
        SFInt32  []       size              128    (0,∞)
        SFNode   []       textureProperties NULL   [TextureProperties]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            size=128,
            update="NONE",
            url=[],
            textureProperties=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            url=url,
            textureProperties=textureProperties,
            **kwargs
        )
        self.size = size
        self.update = update

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size is None:
            size = 128
        assertSFInt32(size)
        assertValidGreaterThan(size, 0)
        self.__size = size

    @property
    def update(self):
        return self.__update

    @update.setter
    def update(self, update):
        if update is None:
            update = "NONE"
        assertValidGenerateCubeMapTextureUpdate(update)
        self.__update = update

    @property
    def textureProperties(self):
        return self.__textureProperties

    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = None
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class ImageCubeMapTexture(X3DEnvironmentTextureNode, X3DUrlObject):
    """
    ImageCubeMapTexture : X3DEnvironmentTextureNode, X3DUrlObject {
        SFNode   [in,out] metadata          NULL [X3DMetadataObject]
        MFString [in,out] url               []   [URI]
        SFNode   []       textureProperties NULL [TextureProperties]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
            textureProperties=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            url=url,
            textureProperties=textureProperties,
            **kwargs
        )

    @property
    def textureProperties(self):
        return self.__textureProperties

    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = None
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class ImageTexture(X3DTexture2DNode, X3DUrlObject):
    """
    ImageTexture : X3DTexture2DNode, X3DUrlObject { 
        SFNode   [in,out] metadata          NULL [X3DMetadataObject]
        MFString [in,out] url               []   [URI]
        SFBool   []       repeatS           TRUE 
        SFBool   []       repeatT           TRUE
        SFNode   []       textureProperties NULL [TextureProperties]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
            repeatS=True,
            repeatT=True,
            textureProperties=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            url=url,
            repeatS=repeatS,
            repeatT=repeatT,
            **kwargs
        )
        self.textureProperties = textureProperties

    @property
    def textureProperties(self):
        return self.__textureProperties

    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = []
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class MovieTexture(X3DTexture2DNode, X3DSoundSourceNode, X3DUrlObject):
    """
    MovieTexture : X3DTexture2DNode, X3DSoundSourceNode, X3DUrlObject { 
        SFString [in,out] description       ""
        SFBool   [in,out] loop              FALSE
        SFNode   [in,out] metadata          NULL  [X3DMetadataObject]
        SFTime   [in,out] pauseTime         0     (-∞,∞)
        SFFloat  [in,out] pitch             1.0   (0,∞)
        SFTime   [in,out] resumeTime        0     (-∞,∞)
        SFFloat  [in,out] speed             1.0   (-∞,∞)
        SFTime   [in,out] startTime         0     (-∞,∞)
        SFTime   [in,out] stopTime          0     (-∞,∞)
        MFString [in,out] url               []    [URI]
        SFTime   [out]    duration_changed
        SFTime   [out]    elapsedTime
        SFBool   [out]    isActive
        SFBool   [out]    isPaused
        SFBool   []       repeatS           TRUE
        SFBool   []       repeatT           TRUE
        SFNode   []       textureProperties NULL [TextureProperties]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            description="",
            loop=False,
            pauseTime=0.0,
            pitch=1.0,
            resumeTime=0.0,
            startTime=0.0,
            stopTime=0.0,
            url=[],
            repeatS=True,
            repeatT=True,
            textureProperties=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            description=description,
            loop=loop,
            pauseTime=pauseTime,
            pitch=pitch,
            resumeTime=resumeTime,
            startTime=startTime,
            stopTime=stopTime,
            url=url,
            repeatS=repeatS,
            repeatT=repeatT,
            **kwargs
        )
        self.textureProperties = textureProperties

    @property
    def textureProperties(self):
        return self.__textureProperties

    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = []
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class PixelTexture(X3DTexture2DNode):
    """
    PixelTexture : X3DTexture2DNode { 
        SFImage [in,out] image             0 0 0
        SFNode  [in,out] metadata          NULL  [X3DMetadataObject]
        SFBool  []       repeatS           TRUE
        SFBool  []       repeatT           TRUE
        SFNode  []       textureProperties NULL  [TextureProperties]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            image=[0.0, 0.0, 0.0],
            repeatS=True,
            repeatT=True,
            textureProperties=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            repeatT=repeatT,
            repeatS=repeatS,
            **kwargs
        )
        self.image = image
        self.textureProperties = textureProperties

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        if image is None:
            image = None
        assertSFImage(image)
        self.__image = image

    @property
    def textureProperties(self):
        return self.__textureProperties

    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = []
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class ComposedTexture3D(X3DTexture3DNode): 
    """
    ComposedTexture3D : X3DTexture3DNode {
        SFNode [in,out] metadata          NULL  [X3DMetadataObject]
        MFNode [in,out] texture           []    [X3DTexture2DNode]
        SFNode []       textureProperties NULL  [TextureProperties]
        SFBool []       repeatS           FALSE
        SFBool []       repeatR           FALSE
        SFBool []       repeatT           FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            repeatS=False,
            repeatT=False,
            repeatR=False,
            texture=[],
            textureProperties=None,
            **kwargs
    ):
        super().__init__(
            self,
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            repeatS=repeatS,
            repeatR=repeatR,
            repeatT=repeatT,
            **kwargs
        )
        self.texture = texture
        self.textureProperties = textureProperties

    @property
    def texture(self):
        return self.__texture

    @texture.setter
    def texture(self, texture):
        if texture is None:
            texture = None
        assertMFNode(texture, X3DTexture2DNode)
        self.__texture = texture

    @property
    def textureProperties(self):
        return self.__textureProperties

    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = []
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class ImageTexture3D(X3DTexture3DNode, X3DUrlObject):
    """
    ImageTexture3D : X3DTexture3DNode, X3DUrlObject {
        SFNode   [in,out] metadata          NULL  [X3DMetadataObject]
        MFString [in,out] url               []    [URI]
        SFBool   []       repeatS           FALSE
        SFBool   []       repeatT           FALSE
        SFBool   []       repeatR           FALSE
        SFNode   []       textureProperties NULL  [TextureProperties]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            repeatS=False,
            repeatT=False,
            repeatR=False,
            textureProperties=None,
            url=[],
            **kwargs
    ):
        super().__init__(
            self,
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            repeatS=repeatS,
            repeatR=repeatR,
            repeatT=repeatT,
            url=url,
            **kwargs
        )
        self.textureProperties = textureProperties

    @property
    def textureProperties(self):
        return self.__textureProperties
        
    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = []
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class PixelTexture3D(X3DTexture3DNode):
    """
    PixelTexture3D : X3DTexture3DNode {
        SFNode  [in,out] metadata          NULL      [X3DMetadataObject]
        MFInt32 [in,out] image             [0 0 0 0]
        SFBool  []       repeatS           FALSE
        SFBool  []       repeatR           FALSE
        SFBool  []       repeatT           FALSE
        SFNode  []       textureProperties NULL      [TextureProperties]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            repeatS=False,
            repeatT=False,
            repeatR=False,
            textureProperties=None,
            image=[0, 0, 0, 0],
            **kwargs
    ):
        super().__init__(
            self,
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            repeatS=repeatS,
            repeatR=repeatR,
            repeatT=repeatT,
            **kwargs
        )
        self.image = image
        self.textureProperties = textureProperties

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        if image is None:
            image = None
        assertMFInt32(image)
        self.__image = image

    @property
    def textureProperties(self):
        return self.__textureProperties
        
    @textureProperties.setter
    def textureProperties(self, textureProperties):
        if textureProperties is None:
            textureProperties = []
        assertSFNode(textureProperties, TextureProperties)
        self.__textureProperties = textureProperties

class MultiTextureTransform(X3DTextureTransformNode):
    """
    MultiTextureTransform : X3DTextureTransformNode { 
        SFNode [in,out] metadata         NULL [X3DMetadataObject]
        MFNode [in,out] textureTransform NULL [X3DTextureTransformNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            textureTransform=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.textureTransform = textureTransform

    @property
    def textureTransform(self):
        return self.__textureTransform

    @textureTransform.setter
    def textureTransform(self, textureTransform):
        if textureTransform is None:
            textureTransform = None
        assertMFNode(textureTransform, X3DTextureTransformNode)
        self.__textureTransform = textureTransform

class TextureTransform(X3DTextureTransformNode):
    """
    TextureTransform : X3DTextureTransformNode { 
        SFVec2f [in,out] center      0 0  (-∞,∞)
        SFNode  [in,out] metadata    NULL [X3DMetadataObject]
        SFFloat [in,out] rotation    0    (-∞,∞)
        SFVec2f [in,out] scale       1 1  (-∞,∞)
        SFVec2f [in,out] translation 0 0  (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0],
            rotation=0.0,
            scale=[1.0, 1.0],
            translation=[0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.center = center
        self.rotation = rotation
        self.scale = scale
        self.translation = translation

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0]
        assertSFVec2f(center)
        self.__center = center

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = 0.0
        assertSFFloat(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0]
        assertSFVec2f(scale)
        self.__scale = scale

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0]
        assertSFVec2f(translation)
        self.__translation = translation


class TextureTransformMatrix3D(X3DTextureTransformNode):
    """
    TextureTransformMatrix3D : X3DTextureTransformNode {
        SFNode     [in,out] metadata    NULL    [X3DMetadataObject]
        SFMatrix4f [in,out] matrix      1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1  (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            matrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.matrix = matrix

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix):
        if matrix is None:
            matrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        assertSFFloat(matrix)
        self.__matrix = matrix

class TextureTransform3D(X3DTextureTransformNode): 
    """
    TextureTransform3D : X3DTextureTransformNode {
        SFVec3f    [in,out] center      0 0 0   (-∞,∞)
        SFNode     [in,out] metadata    NULL    [X3DMetadataObject]
        SFRotation [in,out] rotation    0 0 1 0 (-∞,∞)
        SFVec3f    [in,out] scale       1 1 1   (-∞,∞)
        SFVec3f    [in,out] translation 0 0 0   (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            translation=[0.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.center = center
        self.rotation = rotation
        self.scale = scale
        self.translation = translation

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        assertSFVec3f(scale)
        self.__scale = scale

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

class FontStyle(X3DFontStyleNode):
    """
    FontStyle : X3DFontStyleNode {
        SFNode   [in,out] metadata    NULL    [X3DMetadataObject]
        MFString []       family      "SERIF"
        SFBool   []       horizontal  TRUE
        MFString []       justify     "BEGIN" ["BEGIN","END","FIRST","MIDDLE",""]
        SFString []       language    ""
        SFBool   []       leftToRight TRUE
        SFFloat  []       size        1.0     (0,∞)
        SFFloat  []       spacing     1.0     [0,∞)
        SFString []       style       "PLAIN" ["PLAIN"|"BOLD"|"ITALIC"|"BOLDITALIC"|""]
        SFBool   []       topToBottom TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            family=["SERIF"],
            horizontal=True,
            justify=["BEGIN"],
            language="",
            leftToRight=True,
            size=1.0,
            spacing=1.0,
            style="PLAIN",
            topToBottom=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.family = family
        self.horizontal = horizontal
        self.justify = justify
        self.language = language
        self.leftToRight = leftToRight
        self.size = size
        self.spacing = spacing
        self.style = style
        self.topToBottom = topToBottom

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family):
        if family is None:
            family = ["SERIF"]
        assertValidFontFamily(family)
        self.__family = family

    @property
    def horizontal(self):
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal):
        if horizontal is None:
            horizontal = True
        assertSFBool(horizontal)
        self.__horizontal = horizontal

    @property
    def justify(self):
        return self.__justify

    @justify.setter
    def justify(self, justify):
        if justify is None:
            justify = ["BEGIN"]
        assertValidFontJustify(justify)
        self.__justify = justify

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language is None:
            language = ""
        assertSFString(language)
        self.__language = language

    @property
    def leftToRight(self):
        return self.__leftToRight

    @leftToRight.setter
    def leftToRight(self, leftToRight):
        if leftToRight is None:
            leftToRight= True
        assertSFBool(leftToRight)
        self.__leftToRight = leftToRight

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size is None:
            size = 1.0
        assertSFFloat(size)
        assertValidGreaterThan(size, 0)
        self.__size = size

    @property
    def spacing(self):
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing):
        if spacing is None:
            spacing = 1.0
        assertSFFloat(spacing)
        assertValidGreaterThanEquals(spacing, 0)
        self.__spacing = spacing

    @property
    def topToBottom(self):
        return self.__topToBottom

    @topToBottom.setter
    def topToBottom(self, topToBottom):
        if topToBottom is None:
            topToBottom= True
        assertSFBool(topToBottom)
        self.__topToBottom = topToBottom

class ScreenFontStyle(X3DFontStyleNode):
    """
    ScreenFontStyle : X3DFontStyleNode {
        SFNode   [in,out] metadata    NULL    [X3DMetadataObject]
        MFString []       family      "SERIF"
        SFBool   []       horizontal  TRUE
        MFString []       justify     "BEGIN" ["BEGIN","END","FIRST","MIDDLE",""]
        SFString []       language    ""
        SFBool   []       leftToRight TRUE
        SFFloat  []       pointSize   12.0    (0,∞)
        SFFloat  []       spacing     1.0     [0,∞)
        SFString []       style       "PLAIN" ["PLAIN"|"BOLD"|"ITALIC"|"BOLDITALIC"|""]
        SFBool   []       topToBottom TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            family=["SERIF"],
            horizontal=True,
            justify=["BEGIN"],
            language="",
            leftToRight=True,
            pointSize=12.0,
            spacing=1.0,
            style="PLAIN",
            topToBottom=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.family = family
        self.horizontal = horizontal
        self.justify = justify
        self.language = language
        self.leftToRight = leftToRight
        self.pointSize = pointSize
        self.spacing = spacing
        self.style = style
        self.topToBottom = topToBottom

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family):
        if family is None:
            family = ["SERIF"]
        assertValidFontFamily(family)
        self.__family = family

    @property
    def horizontal(self):
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal):
        if horizontal is None:
            horizontal = True
        assertSFBool(horizontal)
        self.__horizontal = horizontal

    @property
    def justify(self):
        return self.__justify

    @justify.setter
    def justify(self, justify):
        if justify is None:
            justify = ["BEGIN"]
        assertValidFontJustify(justify)
        self.__justify = justify

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language is None:
            language = ""
        assertSFString(language)
        self.__language = language

    @property
    def leftToRight(self):
        return self.__leftToRight

    @leftToRight.setter
    def leftToRight(self, leftToRight):
        if leftToRight is None:
            leftToRight= True
        assertSFBool(leftToRight)
        self.__leftToRight = leftToRight

    @property
    def pointSize(self):
        return self.__pointSize

    @pointSize.setter
    def pointSize(self, pointSize):
        if pointSize is None:
            pointSize = 12.0
        assertSFFloat(pointSize)
        assertValidGreaterThan(pointSize, 0)
        self.__pointSize = pointSize

    @property
    def spacing(self):
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing):
        if spacing is None:
            spacing = 1.0
        assertSFFloat(spacing)
        assertValidGreaterThanEquals(spacing, 0)
        self.__spacing = spacing

    @property
    def topToBottom(self):
        return self.__topToBottom

    @topToBottom.setter
    def topToBottom(self, topToBottom):
        if topToBottom is None:
            topToBottom= True
        assertSFBool(topToBottom)
        self.__topToBottom = topToBottom

class Arc2D(X3DGeometryNode):
    """
    Arc2D : X3DGeometryNode {
      SFNode  [in,out] metadata   NULL  [X3DMetadataObject]
      SFFloat []       endAngle   π/2   [-2π,2π]
      SFFloat []       radius     1     (0,∞)
      SFFloat []       startAngle 0     [-2π,2π]
    }
    """
    def __init__(
            self,
            endAngle=math.pi/2,
            radius=1.0,
            startAngle=0.0,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.endAngle = endAngle
        self.radius = radius
        self.startAngle = startAngle

    @property
    def endAngle(self):
        return self.__endAngle

    @endAngle.setter
    def endAngle(self, endAngle):
        if endAngle is None:
            endAngle = math.pi/2
        assertSFFloat(endAngle)
        assertValidGreaterThanEquals(endAngle, math.pi * -2)
        assertValidLessThanEquals(endAngle, math.pi * 2)
        self.__endAngle = endAngle

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 1.0
        assertSFFloat(radius)
        assertValidGreaterThan(radius, 0)
        self.__radius = radius

    @property
    def startAngle(self):
        return self.__startAngle

    @startAngle.setter
    def startAngle(self, startAngle):
        if startAngle is None:
            startAngle = 0.0
        assertSFFloat(startAngle)
        assertValidGreaterThanEquals(startAngle, math.pi * -2)
        assertValidLessThanEquals(startAngle, math.pi * 2)
        self.__startAngle = startAngle

class ArcClose2D(X3DGeometryNode):
    """
    ArcClose2D : X3DGeometryNode {
      SFNode   [in,out] metadata    NULL  [X3DMetadataObject]
      SFString []       closureType "PIE" ["PIE"|"CHORD"]
      SFFloat  []       endAngle    π/2   [-2π,2π]
      SFFloat  []       radius      1     (0,∞)
      SFBool   []       solid       FALSE
      SFFloat  []       startAngle  0     [-2π,2π]
    }
    """
    def __init__(
            self,
            closureType="PIE",
            endAngle=math.pi / 2,
            radius=1.0,
            solid=False,
            startAngle=0.0,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.closureType = closureType
        self.endAngle = endAngle
        self.radius = radius
        self.solid = solid
        self.startAngle = startAngle

    @property
    def closureType(self):
        return self.__closureType

    @closureType.setter
    def closureType(self, closureType):
        if closureType is None:
            closureType = "PIE"
        assertSFString(closureType)
        self.__closureType = closureType

    @property
    def endAngle(self):
        return self.__endAngle

    @endAngle.setter
    def endAngle(self, endAngle):
        if endAngle is None:
            endAngle = math.pi/2
        assertSFFloat(endAngle)
        assertValidGreaterThanEquals(endAngle, math.pi * -2)
        assertValidLessThanEquals(endAngle, math.pi * 2)
        self.__endAngle = endAngle

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 1.0
        assertSFFloat(radius)
        assertValidGreaterThan(radius, 0)
        self.__radius = radius

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = False
        assertSFBool(solid)
        self.__solid = solid

    @property
    def startAngle(self):
        return self.__startAngle

    @startAngle.setter
    def startAngle(self, startAngle):
        if startAngle is None:
            startAngle = 0.0
        assertSFFloat(startAngle)
        assertValidGreaterThanEquals(startAngle, math.pi * -2)
        assertValidLessThanEquals(startAngle, math.pi * 2)
        self.__startAngle = startAngle

class Box(X3DGeometryNode):
    """
    Box : X3DGeometryNode {
      SFNode  [in,out] metadata NULL  [X3DMetadataObject]
      SFVec3f []       size     2 2 2 (0,∞)
      SFBool  []       solid    TRUE
    }
    """
    def __init__(
            self,
            size=[2.0, 2.0, 2.0],
            solid=True,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.size = size
        self.solid = solid

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size is None:
            size = [2.0, 2.0, 2.0]
        assertSFVec3f(size)
        assertValidGreaterThan(size, 0)
        self.__size = size

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

class Circle2D(X3DGeometryNode):
    """
    Circle2D : X3DGeometryNode {
      SFNode  [in,out] metadata NULL  [X3DMetadataObject]
      SFFloat []       radius   1     (0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            radius=1.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 1.0
        assertSFFloat(radius)
        assertValidGreaterThan(radius, 0)
        self.__radius = radius

class Cone(X3DGeometryNode):
    """
    Cone : X3DGeometryNode { 
    SFNode  [in,out] metadata     NULL [X3DMetadataObject]
    SFBool  []       bottom       TRUE
    SFFloat []       bottomRadius 1    (0,∞)
    SFFloat []       height       2    (0,∞)
    SFBool  []       side         TRUE
    SFBool  []       solid        TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            bottom=True,
            bottomRadius=1.0,
            height=2.0,
            side=True,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.bottom = bottom
        self.bottomRadius = bottomRadius
        self.height = height
        self.side = side
        self.solid = solid

    @property
    def bottom(self):
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom):
        if bottom is None:
            bottom = True
        assertSFBool(bottom)
        self.__bottom = bottom

    @property
    def bottomRadius(self):
        return self.__bottomRadius

    @bottomRadius.setter
    def bottomRadius(self, bottomRadius):
        if bottomRadius is None:
            bottomRadius = 1.0
        assertSFFloat(bottomRadius)
        assertValidGreaterThan(bottomRadius, 0)
        self.__bottomRadius = bottomRadius

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height is None:
            height = 2.0
        assertSFFloat(height)
        assertValidGreaterThan(height, 0)
        self.__height = height

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        if side is None:
            side = True
        assertSFBool(side)
        self.__side = side

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

class Cylinder(X3DGeometryNode):
    """
    Cylinder : X3DGeometryNode {
    SFNode  [in,out] metadata NULL [X3DMetadataObject]
    SFBool  []       bottom   TRUE
    SFFloat []       height   2    (0,∞)
    SFFloat []       radius   1    (0,∞)
    SFBool  []       side     TRUE
    SFBool  []       solid    TRUE
    SFBool  []       top      TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            bottom=True,
            height=2.0,
            radius=1.0,
            side=True,
            solid=True,
            top=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.bottom = bottom
        self.height = height
        self.radius = radius
        self.side = side
        self.solid = solid
        self.top = top

    @property
    def bottom(self):
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom):
        if bottom is None:
            bottom = True
        assertSFBool(bottom)
        self.__bottom = bottom

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height is None:
            height = 2.0
        assertSFFloat(height)
        assertValidGreaterThan(height, 0)
        self.__height = height

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 1.0
        assertSFFloat(radius)
        assertValidGreaterThan(radius, 0)
        self.__radius = radius

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        if side is None:
            side = True
        assertSFBool(side)
        self.__side = side

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top):
        if top is None:
            top = True
        assertSFBool(top)
        self.__top = top

class Disk2D(X3DGeometryNode):
    """
    Disk2D : X3DGeometryNode {
     SFNode  [in,out] metadata    NULL  [X3DMetadataObject]
     SFFloat []       innerRadius 0     [0,∞)
     SFFloat []       outerRadius 1     (0,∞)
     SFBool  []       solid       FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            innerRadius=0.0,
            outerRadius=1.0,
            solid=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.solid = solid

    @property
    def innerRadius(self):
        return self.__innerRadius

    @innerRadius.setter
    def innerRadius(self, innerRadius):
        if innerRadius is None:
            innerRadius = 0.0
        assertSFFloat(innerRadius)
        assertValidGreaterThanEquals(innerRadius, 0)
        self.__innerRadius = innerRadius

    @property
    def outerRadius(self):
        return self.__outerRadius

    @outerRadius.setter
    def outerRadius(self, outerRadius):
        if outerRadius is None:
            outerRadius = 1.0
        assertSFFloat(outerRadius)
        assertValidGreaterThan(outerRadius, 0)
        self.__outerRadius = outerRadius

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = False
        assertSFBool(solid)
        self.__solid = solid

class ElevationGrid(X3DGeometryNode):
    """
    ElevationGrid : X3DGeometryNode {
    MFFloat [in]     set_height
    MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
    SFNode  [in,out] color           NULL [X3DColorNode]
    SFNode  [in,out] fogCoord        NULL [FogCoordinate]
    SFNode  [in,out] metadata        NULL [X3DMetadataObject]
    SFNode  [in,out] normal          NULL [X3DNormalNode]
    SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
    SFBool  []       ccw             TRUE
    SFBool  []       colorPerVertex  TRUE
    SFFloat []       creaseAngle     0    [0,∞)
    MFFloat []       height          []   (-∞,∞)
    SFBool  []       normalPerVertex TRUE
    SFBool  []       solid           TRUE
    SFInt32 []       xDimension      0    [0,∞)
    SFFloat []       xSpacing        1.0  (0,∞)
    SFInt32 []       zDimension      0    [0,∞)
    SFFloat []       zSpacing        1.0  (0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            creaseAngle=0.0,
            height=[],
            normalPerVertex=True,
            solid=True,
            xDimension=0,
            xSpacing=1.0,
            zDimension=0,
            zSpacing=1.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.attrib = attrib
        self.color = color
        self.fogCoord = fogCoord
        self.normal = normal
        self.texCoord = texCoord
        self.ccw = ccw
        self.colorPerVertex = colorPerVertex
        self.creaseAngle = creaseAngle
        self.height = height
        self.normalPerVertex = normalPerVertex
        self.solid = solid
        self.xDimension = xDimension
        self.xSpacing = xSpacing
        self.zDimension = zDimension
        self.zSpacing = zSpacing

    @property
    def attrib(self):
        return self.__attrib

    @attrib.setter
    def attrib(self, attrib):
        if attrib is None:
            attrib = []
        assertMFNode(attrib, X3DVertexAttributeNode)
        self.__attrib = attrib

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = None
        assertSFNode(color, X3DColorNode)
        self.__color = color

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def normal(self):
        return self.__normal

    @normal.setter
    def normal(self, normal):
        if normal is None:
            normal = None
        assertSFNode(normal, X3DNormalNode)
        self.__normal = normal

    @property
    def texCoord(self):
        return self.__texCoord

    @texCoord.setter
    def texCoord(self, texCoord):
        if texCoord is None:
            texCoord = None
        assertSFNode(texCoord, X3DTextureCoordinateNode)
        self.__texCoord = texCoord

    @property
    def ccw(self):
        return self.__ccw

    @ccw.setter
    def ccw(self, ccw):
        if ccw is None:
            ccw = True
        assertSFBool(ccw)
        self.__ccw = ccw

    @property
    def colorPerVertex(self):
        return self.__colorPerVertex

    @colorPerVertex.setter
    def colorPerVertex(self, colorPerVertex):
        if colorPerVertex is None:
            colorPerVertex = True
        assertSFBool(colorPerVertex)
        self.__colorPerVertex = colorPerVertex

    @property
    def creaseAngle(self):
        return self.__creaseAngle

    @creaseAngle.setter
    def creaseAngle(self, creaseAngle):
        if creaseAngle is None:
            creaseAngle = 0.0
        assertSFFloat(creaseAngle)
        assertValidGreaterThanEquals(creaseAngle, 0)
        self.__creaseAngle = creaseAngle

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height is None:
            height = []
        assertMFFloat(height)
        self.__height = height

    @property
    def normalPerVertex(self):
        return self.__normalPerVertex

    @normalPerVertex.setter
    def normalPerVertex(self, normalPerVertex):
        if normalPerVertex is None:
            normalPerVertex = True
        assertSFBool(normalPerVertex)
        self.__normalPerVertex = normalPerVertex

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

    @property
    def xDimension(self):
        return self.__xDimension

    @xDimension.setter
    def xDimension(self, xDimension):
        if xDimension is None:
            xDimension = 0
        assertSFInt32(xDimension)
        assertValidGreaterThanEquals(xDimension, 0)
        self.__xDimension = xDimension

    @property
    def xSpacing(self):
        return self.__xSpacing

    @xSpacing.setter
    def xSpacing(self, xSpacing):
        if xSpacing is None:
            xSpacing = 1.0
        assertSFFloat(xSpacing)
        assertValidGreaterThan(xSpacing, 0)
        self.__xSpacing = xSpacing

    @property
    def zDimension(self):
        return self.__zDimension

    @zDimension.setter
    def zDimension(self, zDimension):
        if zDimension is None:
            zDimension = 0
        assertSFInt32(zDimension)
        assertValidGreaterThanEquals(zDimension, 0)
        self.__zDimension = zDimension

    @property
    def zSpacing(self):
        return self.__zSpacing

    @zSpacing.setter
    def zSpacing(self, zSpacing):
        if zSpacing is None:
            zSpacing = 1.0
        assertSFFloat(zSpacing)
        assertValidGreaterThan(zSpacing, 0)
        self.__zSpacing = zSpacing

class Extrusion(X3DGeometryNode):
    """
    Extrusion : X3DGeometryNode {
      MFVec2f    [in]     set_crossSection
      MFRotation [in]     set_orientation
      MFVec2f    [in]     set_scale
      MFVec3f    [in]     set_spine
      SFNode     [in,out] metadata         NULL                      [X3DMetadataObject]
      SFBool     []       beginCap         TRUE
      SFBool     []       ccw              TRUE
      SFBool     []       convex           TRUE
      SFFloat    []       creaseAngle      0                         [0,∞)
      MFVec2f    []       crossSection     [1 1 1 -1 -1 -1 -1 1 1 1] (-∞,∞)
      SFBool     []       endCap           TRUE
      MFRotation []       orientation      0 0 1 0                   [-1,1] or (-∞,∞)
      MFVec2f    []       scale            1 1                       (0,∞)
      SFBool     []       solid            TRUE
      MFVec3f    []       spine            [0 0 0 0 1 0]             (-∞,∞)
    }
    """

    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            beginCap=True,
            ccw=True,
            convex=True,
            creaseAngle=0.0,
            crossSection=[[1.0, 1.0], [1.0, -1.0], [-1.0, -1.0], [-1.0, 1.0], [1.0, 1.0]],
            endCap=True,
            orientation=[[0.0, 0.0, 1.0, 0.0]],
            scale=[[1.0, 1.0]],
            solid=True,
            spine=[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.beginCap = beginCap
        self.ccw = ccw
        self.convex = convex
        self.creaseAngle = creaseAngle
        self.crossSection = crossSection
        self.endCap = endCap
        self.orientation = orientation
        self.scale = scale
        self.solid = solid
        self.spine = spine

    @property
    def beginCap(self):
        return self.__beginCap

    @beginCap.setter
    def beginCap(self, beginCap):
        if beginCap is None:
            beginCap = True
        assertSFBool(beginCap)
        self.__beginCap = beginCap

    @property
    def ccw(self):
        return self.__ccw

    @ccw.setter
    def ccw(self, ccw):
        if ccw is None:
            ccw = True
        assertSFBool(ccw)
        self.__ccw = ccw

    @property
    def convex(self):
        return self.__convex

    @convex.setter
    def convex(self, convex):
        if convex is None:
            convex = True
        assertSFBool(convex)
        self.__convex = convex

    @property
    def creaseAngle(self):
        return self.__creaseAngle

    @creaseAngle.setter
    def creaseAngle(self, creaseAngle):
        if creaseAngle is None:
            creaseAngle = 0.0
        assertSFFloat(creaseAngle)
        assertValidGreaterThanEquals(creaseAngle, 0)
        self.__creaseAngle = creaseAngle

    @property
    def crossSection(self):
        return self.__crossSection

    @crossSection.setter
    def crossSection(self, crossSection):
        if crossSection is None:
            crossSection = [[1.0, 1.0], [1.0, -1.0], [-1.0, -1.0], [-1.0, 1.0], [1.0, 1.0]]
        assertMFVec2f(crossSection)
        self.__crossSection = crossSection

    @property
    def endCap(self):
        return self.__endCap

    @endCap.setter
    def endCap(self, endCap):
        if endCap is None:
            endCap = True
        assertSFBool(endCap)
        self.__endCap = endCap

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        if orientation is None:
            orientation = [[0.0, 0.0, 1.0, 0.0]]
        assertMFRotation(orientation)
        self.__orientation = orientation
    

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [[1.0, 1.0]]
        assertMFVec2f(scale)
        assertValidGreaterThan(scale, 0)
        self.__scale = scale

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

    @property
    def spine(self):
        return self.__spine

    @spine.setter
    def spine(self, spine):
        if spine is None:
            spine = [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
        assertMFVec3f(spine)
        self.__spine = spine

class GeoElevationGrid(X3DGeometryNode): 
    """
    GeoElevationGrid : X3DGeometryNode {
        MFDouble [in]     set_height
        SFNode   [in,out] color           NULL        [X3DColorNode]
        SFNode   [in,out] metadata        NULL        [X3DMetadataObject]
        SFNode   [in,out] normal          NULL        [X3DNormalNode]
        SFNode   [in,out] texCoord        NULL        [X3DTextureCoordinateNode]
        SFFloat  [in,out] yScale          1.0         [0,∞)
        SFBool   []       ccw             TRUE
        SFBool   []       colorPerVertex  TRUE
        SFDouble []       creaseAngle     0           [0,∞)
        SFVec3d  []       geoGridOrigin   0 0 0       (-∞,∞)
        SFNode   []       geoOrigin       NULL        [GeoOrigin] (deprecated)
        MFString []       geoSystem       ["GD","WE"] [see 25.2.3]
        MFDouble []       height          [0 0]       (-∞,∞)
        SFBool   []       normalPerVertex TRUE
        SFBool   []       solid           TRUE
        SFInt32  []       xDimension      0           (0,∞)
        SFDouble []       xSpacing        1.0         [0,∞)
        SFInt32  []       zDimension      0           (0,∞)
        SFDouble []       zSpacing        1.0         [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            color=None,
            normal=None,
            texCoord=None,
            yScale=1.0,
            ccw=True,
            colorPerVertex=True,
            creaseAngle=0.0,
            geoGridOrigin=[0.0, 0.0, 0.0],
            geoOrigin=None,
            geoSystem=["GD", "WE"],
            height=[[0.0, 0.0]],
            normalPerVetex=True,
            solid=True,
            xDimension=0.0,
            xSpacing=1.0,
            zDimension=0.0,
            zSpacing=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.color = color
        self.normal = normal
        self.texCoord = texCoord
        self.yScale = yScale
        self.ccw = ccw
        self.colorPerVertex = colorPerVertex
        self.creaseAngle = creaseAngle
        self.geoGridOrigin = geoGridOrigin
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem
        self.height = height
        self.normalPerVetex = normalPerVetex
        self.solid = solid
        self.xDimension = xDimension
        self.xSpacing = xSpacing
        self.zDimension = zDimension
        self.zSpacing = zSpacing

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = None
        assertSFNode(color, X3DColorNode)
        self.__color = color

    @property
    def normal(self):
        return self.__normal

    @normal.setter
    def normal(self, normal):
        if normal is None:
            normal = None
        assertSFNode(normal, X3DNormalNode)
        self.__normal = normal

    @property
    def texCoord(self):
        return self.__texCoord

    @texCoord.setter
    def texCoord(self, texCoord):
        if texCoord is None:
            texCoord = None
        assertSFNode(texCoord, X3DTextureCoordinateNode)
        self.__texCoord = texCoord

    @property
    def yScale(self):
        return self.__yScale

    @yScale.setter
    def yScale(self, yScale):
        if yScale is None:
            yScale = 1.0
        assertSFFloat(yScale)
        assertValidGreaterThanEquals(yScale, 0)
        self.__yScale = yScale

    @property
    def ccw(self):
        return self.__ccw

    @ccw.setter
    def ccw(self, ccw):
        if ccw is None:
            ccw = True
        assertSFBool(ccw)
        self.__ccw = ccw

    @property
    def colorPerVertex(self):
        return self.__colorPerVertex

    @colorPerVertex.setter
    def colorPerVertex(self, colorPerVertex):
        if colorPerVertex is None:
            colorPerVertex = True
        assertSFBool(colorPerVertex)
        self.__colorPerVertex = colorPerVertex

    @property
    def creaseAngle(self):
        return self.__creaseAngle

    @creaseAngle.setter
    def creaseAngle(self, creaseAngle):
        if creaseAngle is None:
            creaseAngle = 0.0
        assertSFFloat(creaseAngle)
        assertValidGreaterThanEquals(creaseAngle, 0)
        self.__creaseAngle = creaseAngle

    @property
    def geoGridOrigin(self):
        return self.__geoGridOrigin

    @geoGridOrigin.setter
    def geoGridOrigin(self, geoGridOrigin):
        if geoGridOrigin is None:
            geoGridOrigin = None
        assertSFVec3d(geoGridOrigin)
        self.__geoGridOrigin = geoGridOrigin

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height is None:
            height = [[0.0, 0.0]]
        assertMFDouble(height)
        self.__height = height
    
    @property
    def normalPerVertex(self):
        return self.__normalPerVertex

    @normalPerVertex.setter
    def normalPerVertex(self, normalPerVertex):
        if normalPerVertex is None:
            normalPerVertex = True
        assertSFBool(normalPerVertex)
        self.__normalPerVertex = normalPerVertex

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

    @property
    def xDimension(self):
        return self.__xDimension

    @xDimension.setter
    def xDimension(self, xDimension):
        if xDimension is None:
            xDimension = 0
        assertSFInt32(xDimension)
        assertValidGreaterThan(xDimension, 0)
        self.__xDimension = xDimension

    @property
    def xSpacing(self):
        return self.__xSpacing

    @xSpacing.setter
    def xSpacing(self, xSpacing):
        if xSpacing is None:
            xSpacing = 1.0
        assertSFFloat(xSpacing)
        assertValidGreaterThanEquals(xSpacing, 0)
        self.__xSpacing = xSpacing

    @property
    def zDimension(self):
        return self.__zDimension

    @zDimension.setter
    def zDimension(self, zDimension):
        if zDimension is None:
            zDimension = 0
        assertSFInt32(zDimension)
        assertValidGreaterThan(zDimension, 0)
        self.__zDimension = zDimension

    @property
    def zSpacing(self):
        return self.__zSpacing

    @zSpacing.setter
    def zSpacing(self, zSpacing):
        if zSpacing is None:
            zSpacing = 1.0
        assertSFFloat(zSpacing)
        assertValidGreaterThanEquals(zSpacing, 0)
        self.__zSpacing = zSpacing

class IndexedLineSet(X3DGeometryNode):
    """
    IndexedLineSet : X3DGeometryNode {
        MFInt32 [in]     set_colorIndex
        MFInt32 [in]     set_coordIndex
        MFNode  [in,out] attrib         []   [X3DVertexAttributeNode]
        SFNode  [in,out] color          NULL [X3DColorNode]
        SFNode  [in,out] coord          NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord       NULL [FogCoordinate]
        SFNode  [in,out] metadata       NULL [X3DMetadataObject]
        MFInt32 []       colorIndex     []   [0,∞) or -1
        SFBool  []       colorPerVertex TRUE
        MFInt32 []       coordIndex     []   [0,∞) or -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            colorIndex=[],
            colorPerVertex=True,
            coordIndex=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.attrib = attrib
        self.color = color
        self.coord = coord
        self.fogCoord = fogCoord
        self.colorIndex = colorIndex
        self.colorPerVertex = colorPerVertex
        self.coordIndex = coordIndex

    @property
    def attrib(self):
        return self.__attrib

    @attrib.setter
    def attrib(self, attrib):
        if attrib is None:
            attrib = []
        assertMFNode(attrib, X3DVertexAttributeNode)
        self.__attrib = attrib

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = None
        assertSFNode(color, X3DColorNode)
        self.__color = color
    
    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, coord):
        if coord is None:
            coord = None
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def colorIndex(self):
        return self.__colorIndex

    @colorIndex.setter
    def colorIndex(self, colorIndex):
        if colorIndex is None:
            colorIndex = []
        assertMFInt32(colorIndex)
        assertValidGreaterThanEquals(colorIndex, -1)
        self.__colorIndex = colorIndex

    @property
    def colorPerVertex(self):
        return self.__colorPerVertex

    @colorPerVertex.setter
    def colorPerVertex(self, colorPerVertex):
        if colorPerVertex is None:
            colorPerVertex = True
        assertSFBool(colorPerVertex)
        self.__colorPerVertex = colorPerVertex

    @property
    def coordIndex(self):
        return self.__coordIndex

    @coordIndex.setter
    def coordIndex(self, coordIndex):
        if coordIndex is None:
            coordIndex = []
        assertMFInt32(coordIndex)
        assertValidGreaterThanEquals(coordIndex, -1)
        self.__coordIndex = coordIndex

class LineSet(X3DGeometryNode):
    """
    LineSet : X3DGeometryNode {
        MFNode  [in,out] attrib         []   [X3DVertexAttributeNode]
        SFNode  [in,out] color          NULL [X3DColorNode]
        SFNode  [in,out] coord          NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord       NULL [FogCoordinate]
        SFNode  [in,out] metadata       NULL [X3DMetadataObject]
        MFInt32 [in,out] vertexCount    []   [2,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            vertexCount=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.attrib = attrib
        self.color = color
        self.coord = coord
        self.fogCoord = fogCoord
        self.vertexCount = vertexCount

    @property
    def attrib(self):
        return self.__attrib

    @attrib.setter
    def attrib(self, attrib):
        if attrib is None:
            attrib = []
        assertMFNode(attrib, X3DVertexAttributeNode)
        self.__attrib = attrib

    @property
    def color(self):
        return self.__color

    @attrib.setter
    def color(self, color):
        if color is None:
            color = None
        assertSFNode(color, X3DColorNode)
        self.__color = color
    
    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, coord):
        if coord is None:
            coord = None
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def vertexCount(self):
        return self.__vertexCount

    @vertexCount.setter
    def vertexCount(self, vertexCount):
        if vertexCount is None:
            vertexCount = []
        assertMFInt32(vertexCount)
        assertValidGreaterThanEquals(vertexCount, 2)
        self.__vertexCount = vertexCount

class PointSet(X3DGeometryNode):
    """
    PointSet : X3DGeometryNode { 
        MFNode [in,out] attrib   []   [X3DVertexAttributeNode]
        SFNode [in,out] color    NULL [X3DColorNode]
        SFNode [in,out] coord    NULL [X3DCoordinateNode]
        SFNode [in,out] fogCoord NULL [FogCoordinate]
        SFNode [in,out] metadata NULL [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.attrib = attrib
        self.color = color
        self.coord = coord
        self.fogCoord = fogCoord

    @property
    def attrib(self):
        return self.__attrib

    @attrib.setter
    def attrib(self, attrib):
        if attrib is None:
            attrib = []
        assertMFNode(attrib, X3DVertexAttributeNode)
        self.__attrib = attrib

    @property
    def color(self):
        return self.__color

    @attrib.setter
    def color(self, color):
        if color is None:
            color = None
        assertSFNode(color, X3DColorNode)
        self.__color = color
    
    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, coord):
        if coord is None:
            coord = None
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

class Polyline2D(X3DGeometryNode):
    """
    Polyline2D : X3DGeometryNode {
      SFNode  [in,out] metadata     NULL  [X3DMetadataObject]
      MFVec2f []       lineSegments []    (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            lineSegments=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.lineSegments = lineSegments

    @property
    def lineSegments(self):
        return self.__lineSegments

    @lineSegments.setter
    def lineSegments(self, lineSegments):
        if lineSegments is None:
            lineSegments = []
        assertMFVec2f(lineSegments)
        self.__lineSegments = lineSegments

class Polypoint2D(X3DGeometryNode):
    """
    Polypoint2D : X3DGeometryNode {
      SFNode  [in,out] metadata NULL [X3DMetadataObject]
      MFVec2f [in,out] point    []    (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            point=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.point = point

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if point is None:
            point = []
        assertMFVec2f(point)
        self.__point = point

class Rectangle2D(X3DGeometryNode):
    """
    Rectangle2D : X3DGeometryNode {
      SFNode  [in,out] metadata NULL  [X3DMetadataObject]
      SFVec2f []       size     2 2   (0,∞)
      SFBool  []       solid    FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            size=[2.0, 2.0],
            solid=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.size = size
        self.solid = solid

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size is None:
            size = [2.0, 2.0]
        assertSFVec2f(size)
        assertValidGreaterThan(size, 0)
        self.__size = size

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = False
        assertSFBool(solid)
        self.__solid = solid

class Sphere(X3DGeometryNode):
    """
    Sphere : X3DGeometryNode {
    SFNode  [in,out] metadata NULL [X3DMetadataObject]
    SFFloat []       radius   1    (0,∞)
    SFBool  []       solid    TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            radius=1.0,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.radius = radius
        self.solid = solid

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 1.0
        assertSFFloat(radius)
        assertValidGreaterThan(radius, 0)
        self.__radius = radius

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

class Text(X3DGeometryNode):
    """
    Text : X3DGeometryNode {
        SFNode   [in,out] fontStyle  NULL  [X3DFontStyleNode]
        MFFloat  [in,out] length     []    [0,∞)
        SFFloat  [in,out] maxExtent  0.0   [0,∞)
        SFNode   [in,out] metadata   NULL  [X3DMetadataObject]
        MFString [in,out] string     []
        MFVec2f  [out]    lineBounds
        SFVec3f  [out]    origin
        SFVec2f  [out]    textBounds
        SFBool   []       solid      FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            fontStyle=None,
            length=[],
            maxExtent=0.0,
            string=[],
            solid=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.fontStyle = fontStyle
        self.length = length
        self.maxExtent = maxExtent
        self.string = string
        self.solid = solid

    @property
    def fontStyle(self):
        return self.__fontStyle

    @fontStyle.setter
    def fontStyle(self, fontStyle):
        if fontStyle is None:
            fontStyle = []
        assertSFNode(fontStyle, X3DFontStyleNode)
        self.__fontStyle = fontStyle
    
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length is None:
            length = []
        assertMFFloat(length)
        assertValidGreaterThanEquals(length, 0)
        self.__length = length

    @property
    def maxExtent(self):
        return self.__maxExtent

    @maxExtent.setter
    def maxExtent(self, maxExtent):
        if maxExtent is None:
            maxExtent = 0.0
        assertSFFloat(maxExtent)
        assertValidGreaterThanEquals(maxExtent, 0)
        self.__maxExtent = maxExtent

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        if string is None:
            string = []
        assertMFString(string)
        self.__string = string

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = False
        assertSFBool(solid)
        self.__solid = solid

class TriangleSet2D(X3DGeometryNode):
    """
    TriangleSet2D : X3DGeometryNode {
      SFNode  [in,out] metadata NULL  [X3DMetadataObject]
      MFVec2f [in,out] vertices []    (-∞,∞)
      SFBool  []       solid    FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            vertices=[],
            solid=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.vertices = vertices
        self.solid = solid

    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, vertices):
        if vertices is None:
            vertices = []
        assertMFVec2f(vertices)
        self.__vertices = vertices

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = False
        assertSFBool(solid)
        self.__solid = solid

class IndexedFaceSet(X3DComposedGeometryNode):
    """
    IndexedFaceSet : X3DComposedGeometryNode {
      MFInt32 [in]     set_colorIndex
      MFInt32 [in]     set_coordIndex
      MFInt32 [in]     set_normalIndex
      MFInt32 [in]     set_texCoordIndex
      MFNode  [in,out] attrib            []   [X3DVertexAttributeNode]
      SFNode  [in,out] color             NULL [X3DColorNode]
      SFNode  [in,out] coord             NULL [X3DCoordinateNode]
      SFNode  [in,out] fogCoord          NULL [FogCoordinate]
      SFNode  [in,out] metadata          NULL [X3DMetadataObject]
      SFNode  [in,out] normal            NULL [X3DNormalNode]
      SFNode  [in,out] texCoord          NULL [X3DTextureCoordinateNode]
      SFBool  []       ccw               TRUE
      MFInt32 []       colorIndex        []   [0,∞) or -1
      SFBool  []       colorPerVertex    TRUE
      SFBool  []       convex            TRUE
      MFInt32 []       coordIndex        []   [0,∞) or -1
      SFFloat []       creaseAngle       0    [0,∞)
      MFInt32 []       normalIndex       []   [0,∞) or -1
      SFBool  []       normalPerVertex   TRUE
      SFBool  []       solid             TRUE
      MFInt32 []       texCoordIndex     []   [-1,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorIndex=[],
            colorPerVertex=True,
            convex=True,
            coordIndex=[],
            creaseAngle=0.0,
            normalIndex=[],
            normalPerVertex=True,
            solid=True,
            texCoordIndex=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.colorIndex = colorIndex
        self.convex = convex
        self.coordIndex = coordIndex
        self.creaseAngle = creaseAngle
        self.fogCoord = fogCoord
        self.normalIndex = normalIndex
        self.texCoordIndex = texCoordIndex

    @property
    def colorIndex(self):
        return self.__colorIndex

    @colorIndex.setter
    def colorIndex(self, colorIndex):
        if colorIndex is None:
            colorIndex = []
        assertMFInt32(colorIndex)
        assertValidGreaterThanEquals(colorIndex, -1)
        self.__colorIndex = colorIndex
    
    @property
    def convex(self):
        return self.__convex

    @convex.setter
    def convex(self, convex):
        if convex is None:
            convex = True
        assertSFBool(convex)
        self.__convex = convex

    @property
    def coordIndex(self):
        return self.__coordIndex

    @coordIndex.setter
    def coordIndex(self, coordIndex):
        if coordIndex is None:
            coordIndex = []
        assertMFInt32(coordIndex)
        assertValidGreaterThanEquals(coordIndex, -1)
        self.__coordIndex = coordIndex

    @property
    def creaseAngle(self):
        return self.__creaseAngle

    @creaseAngle.setter
    def creaseAngle(self, creaseAngle):
        if creaseAngle is None:
            creaseAngle = 0.0
        assertSFFloat(creaseAngle)
        assertValidGreaterThanEquals(creaseAngle, 0)
        self.__creaseAngle = creaseAngle

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def normalIndex(self):
        return self.__normalIndex

    @normalIndex.setter
    def normalIndex(self, normalIndex):
        if normalIndex is None:
            normalIndex = []
        assertMFInt32(normalIndex)
        assertValidGreaterThanEquals(normalIndex, -1)
        self.__normalIndex = normalIndex

    @property
    def texCoordIndex(self):
        return self.__texCoordIndex

    @texCoordIndex.setter
    def texCoordIndex(self, texCoordIndex):
        if texCoordIndex is None:
            texCoordIndex = []
        assertMFInt32(texCoordIndex)
        assertValidGreaterThanEquals(texCoordIndex, -1)
        self.__texCoordIndex = texCoordIndex

class IndexedTriangleFanSet(X3DComposedGeometryNode):
    """
    IndexedTriangleFanSet : X3DComposedGeometryNode {
        MFInt32 [in]     set_index       []   [0,∞) or -1
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
        MFInt32 []       index           []   [0,∞) or -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            index=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fogCoord = fogCoord
        self.index = index
        
    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        if index is None:
            index = []
        assertMFInt32(index)
        assertValidGreaterThanEquals(index, -1)
        self.__index = index

class IndexedTriangleSet(X3DComposedGeometryNode):
    """
    IndexedTriangleSet : X3DComposedGeometryNode {
        MFInt32 [in]     set_index       []   [0,∞)
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
        MFInt32 []       index           []   [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            index=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fogCoord = fogCoord
        self.index = index
    
    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        if index is None:
            index = []
        assertMFInt32(index)
        assertValidGreaterThanEquals(index, -1)
        self.__index = index

class IndexedTriangleStripSet(X3DComposedGeometryNode):
    """
    IndexedTriangleStripSet : X3DComposedGeometryNode {
        MFInt32 [in]     set_index       []   [0,∞) or −1
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
        MFInt32 []       index           []   [0,∞) or −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            index=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fogCoord = fogCoord
        self.index = index
        
    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        if index is None:
            index = []
        assertMFInt32(index)
        assertValidGreaterThanEquals(index, -1)
        self.__index = index

class IndexedQuadSet(X3DComposedGeometryNode):
    """
    IndexedQuadSet : X3DComposedGeometryNode {
        MFInt32 [in]     set_index       []   [0,∞)
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
        MFInt32 []       index           []   [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            index=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fogCoord = fogCoord
        self.index = index

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        if index is None:
            index = []
        assertMFInt32(index)
        assertValidGreaterThanEquals(index, -1)
        self.__index = index

class QuadSet(X3DComposedGeometryNode):
    """
    QuadSet : X3DComposedGeometryNode {
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fogCoord = fogCoord
    
    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

class TriangleFanSet(X3DComposedGeometryNode):
    """
    TriangleFanSet : X3DComposedGeometryNode {
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        MFInt32 [in,out] fanCount        []   [3,∞)
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fanCount=[],
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fanCount = fanCount
        self.fogCoord = fogCoord

    @property
    def fanCount(self):
        return self.__fanCount

    @fanCount.setter
    def fanCount(self, fanCount):
        if fanCount is None:
            fanCount = []
        assertMFInt32(fanCount)
        assertValidGreaterThanEquals(fanCount, 3)
        self.__fanCount = fanCount

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

class TriangleSet(X3DComposedGeometryNode): 
    """
    TriangleSet : X3DComposedGeometryNode {
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            fogCoord=fogCoord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fogCoord = fogCoord

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord

class TriangleStripSet(X3DComposedGeometryNode):
    """
    TriangleStripSet : X3DComposedGeometryNode {
        MFNode  [in,out] attrib          []   [X3DVertexAttributeNode]
        SFNode  [in,out] color           NULL [X3DColorNode]
        SFNode  [in,out] coord           NULL [X3DCoordinateNode]
        SFNode  [in,out] fogCoord        NULL [FogCoordinate]
        SFNode  [in,out] metadata        NULL [X3DMetadataObject]
        SFNode  [in,out] normal          NULL [X3DNormalNode]
        MFInt32 [in,out] stripCount      []   [3,∞)
        SFNode  [in,out] texCoord        NULL [X3DTextureCoordinateNode]
        SFBool  []       ccw             TRUE
        SFBool  []       colorPerVertex  TRUE
        SFBool  []       normalPerVertex TRUE
        SFBool  []       solid           TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            attrib=[],
            color=None,
            coord=None,
            fogCoord=None,
            normal=None,
            stripCount=[],
            texCoord=None,
            ccw=True,
            colorPerVertex=True,
            normalPerVertex=True,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            attrib=attrib,
            color=color,
            coord=coord,
            normal=normal,
            texCoord=texCoord,
            ccw=ccw,
            colorPerVertex=colorPerVertex,
            normalPerVertex=normalPerVertex,
            solid=solid,
            **kwargs
        )
        self.fogCoord = fogCoord
        self.stripCount = stripCount

    @property
    def fogCoord(self):
        return self.__fogCoord

    @fogCoord.setter
    def fogCoord(self, fogCoord):
        if fogCoord is None:
            fogCoord = None
        assertSFNode(fogCoord, FogCoordinate)
        self.__fogCoord = fogCoord
        
    @property
    def stripCount(self):
        return self.__stripCount

    @stripCount.setter
    def stripCount(self, stripCount):
        if stripCount is None:
            stripCount = []
        assertMFInt32(stripCount)
        assertValidGreaterThanEquals(stripCount, 3)
        self.__stripCount = stripCount
    
class NurbsCurve(X3DParametricGeometryNode):
    """
    NurbsCurve : X3DParametricGeometryNode {
        SFNode   [in,out] controlPoint NULL  [X3DCoordinateNode]
        SFNode   [in,out] metadata     NULL  [X3DMetadataObject]
        SFInt32  [in,out] tessellation 0     (-∞,∞)
        MFDouble [in,out] weight       []    (0,∞)
        SFBool   []       closed       FALSE 
        MFDouble []       knot         []    (-∞,∞)
        SFInt32  []       order        3     [2,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=None,
            tessellation=0,
            weight=[],
            closed=False,
            knot=[],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.controlPoint = controlPoint
        self.tessellation = tessellation
        self.weight = weight
        self.closed = closed
        self.knot = knot
        self.order = order

    @property
    def controlPoint(self):
        return self.__controlPoint

    @controlPoint.setter
    def controlPoint(self, controlPoint):
        if controlPoint is None:
            controlPoint = None
        assertSFNode(controlPoint, X3DCoordinateNode)
        self.__controlPoint = controlPoint

    @property
    def tessellation(self):
        return self.__tessellation

    @tessellation.setter
    def tessellation(self, tessellation):
        if tessellation is None:
            tessellation = 0
        assertSFInt32(tessellation)
        self.__tessellation = tessellation

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight is None:
            weight = []
        assertMFDouble(weight)
        assertValidGreaterThan(weight, 0)
        self.__weight = weight

    @property
    def closed(self):
        return self.__closed

    @closed.setter
    def closed(self, closed):
        if closed is None:
            closed = False
        assertSFBool(closed)
        self.__closed = closed

    @property
    def knot(self):
        return self.__knot

    @knot.setter
    def knot(self, knot):
        if knot is None:
            knot = []
        assertMFDouble(knot)
        self.__knot = knot

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if order is None:
            order = 3
        assertSFInt32(order)
        assertValidGreaterThanEquals(order, 2)
        self.__order = order
        
class NurbsSweptSurface(X3DParametricGeometryNode):
    """
    NurbsSweptSurface : X3DParametricGeometryNode { 
        SFNode [in,out] crossSectionCurve NULL [X3DNurbsControlCurveNode]
        SFNode [in,out] metadata          NULL [X3DMetadataObject]
        SFNode [in,out] trajectoryCurve   NULL [NurbsCurve]
        SFBool []       ccw               TRUE
        SFBool []       solid             TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            crossSectionCurve=None,
            trajectoryCurve=None,
            ccw=True,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata
            **kwargs
        )
        self.crossSectionCurve = crossSectionCurve
        self.trajectoryCurve = trajectoryCurve
        self.ccw = ccw
        self.solid = solid

    @property
    def crossSectionCurve(self):
        return self.__crossSectionCurve

    @crossSectionCurve.setter
    def crossSectionCurve(self, crossSectionCurve):
        if crossSectionCurve is None:
            crossSectionCurve = None
        assertSFNode(crossSectionCurve, X3DNurbsControlCurveNode)
        self.__crossSectionCurve = crossSectionCurve

    @property
    def trajectoryCurve(self):
        return self.__trajectoryCurve

    @trajectoryCurve.setter
    def trajectoryCurve(self, trajectoryCurve):
        if trajectoryCurve is None:
            trajectoryCurve = None
        assertSFNode(trajectoryCurve, NurbsCurve)
        self.__trajectoryCurve = trajectoryCurve

    @property
    def ccw(self):
        return self.__ccw

    @ccw.setter
    def ccw(self, ccw):
        if ccw is None:
            ccw = True
        assertSFBool(ccw)
        self.__ccw = ccw

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

class NurbsSwungSurface(X3DParametricGeometryNode):
    """
    NurbsSwungSurface : X3DParametricGeometryNode { 
        SFNode [in,out] metadata          NULL [X3DMetadataObject]
        SFNode [in,out] profileCurve      NULL [X3DNurbsControlCurveNode]
        SFNode [in,out] trajectoryCurve   NULL [X3DNurbsControlCurveNode]
        SFBool []       ccw               TRUE
        SFBool []       solid             TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            profileCurve=None,
            trajectoryCurve=None,
            ccw=True,
            solid=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata
            **kwargs
        )
        self.profileCurve = profileCurve
        self.trajectoryCurve = trajectoryCurve
        self.ccw = ccw
        self.solid = solid

    @property
    def profileCurve(self):
        return self.__profileCurve

    @profileCurve.setter
    def profileCurve(self, profileCurve):
        if profileCurve is None:
            profileCurve = None
        assertSFNode(profileCurve, X3DNurbsControlCurveNode)
        self.__profileCurve = profileCurvee

    @property
    def trajectoryCurve(self):
        return self.__trajectoryCurve

    @trajectoryCurve.setter
    def trajectoryCurve(self, trajectoryCurve):
        if trajectoryCurve is None:
            trajectoryCurve = None
        assertSFNode(trajectoryCurve, NurbsCurve)
        self.__trajectoryCurve = trajectoryCurve

    @property
    def ccw(self):
        return self.__ccw

    @ccw.setter
    def ccw(self, ccw):
        if ccw is None:
            ccw = True
        assertSFBool(ccw)
        self.__ccw = ccw

    @property
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = True
        assertSFBool(solid)
        self.__solid = solid

class NurbsPatchSurface(X3DNurbsSurfaceGeometryNode):
    """
    NurbsPatchSurface : X3DNurbsSurfaceGeometryNode { 
        SFNode   [in,out] controlPoint  NULL  [X3DCoordinateNode]
        SFNode   [in,out] metadata      NULL  [X3DMetadataObject]
        SFNode   [in,out] texCoord      NULL  [X3DTextureCoordinateNode|NurbsTextureCoordinate]
        SFInt32  [in,out] uTessellation 0     (-∞,∞)
        SFInt32  [in,out] vTessellation 0     (-∞,∞)
        MFDouble [in,out] weight        []    (0,∞)
        SFBool   []       solid         TRUE
        SFBool   []       uClosed       FALSE 
        SFInt32  []       uDimension    0     [0,∞)
        MFDouble []       uKnot         []    (-∞,∞)
        SFInt32  []       uOrder        3     [2,∞)
        SFBool   []       vClosed       FALSE 
        SFInt32  []       vDimension    0     [0,∞)
        MFDouble []       vKnot         []    (-∞,∞)
        SFInt32  []       vOrder        3     [2,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=None,
            texCoord=None,
            uTessellation=0,
            vTessellation=0,
            weight=[],
            solid=True,
            uClosed=True,
            uDimension=0,
            uKnot=[],
            uOrder=3,
            vClosed=False,
            vDimension=0,
            vKnot=[],
            vOrder=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            controlPoint=controlPoint,
            texCoord=texCoord,
            uTessellation=uTessellation,
            vTessellation=vTessellation,
            weight=weight,
            solid=solid,
            uClosed=uClosed,
            uDimension=uDimension,
            uKnot=uKnot,
            uOrder=uOrder,
            vClosed=vClosed,
            vDimension=vDimension,
            vKnot=vKnot,
            vOrder=vOrder,
            **kwargs
        )

class NurbsTrimmedSurface(X3DNurbsSurfaceGeometryNode):
    """
    NurbsTrimmedSurface : X3DNurbsSurfaceGeometryNode { 
        MFNode   [in]     addTrimmingContour          [Contour2D]
        MFNode   [in]     removeTrimmingContour       [Contour2D]
        SFNode   [in,out] controlPoint          NULL  [X3DCoordinateNode]
        SFNode   [in,out] metadata              NULL  [X3DMetadataObject]
        SFNode   [in,out] texCoord              NULL  [X3DTextureCoordinateNode|NurbsTextureCoordinate]
        MFNode   [in,out] trimmingContour       []    [Contour2D]
        SFInt32  [in,out] uTessellation         0     (-∞,∞)
        SFInt32  [in,out] vTessellation         0     (-∞,∞)
        MFDouble [in,out] weight                []    (0,∞)
        SFBool   []       solid                 TRUE
        SFBool   []       uClosed               FALSE 
        SFInt32  []       uDimension            0     [0,∞)
        MFDouble []       uKnot                 []    (-∞,∞)
        SFInt32  []       uOrder                3     [2,∞)
        SFBool   []       vClosed               FALSE 
        SFInt32  []       vDimension            0     [0,∞)
        MFDouble []       vKnot                 []    (-∞,∞)
        SFInt32  []       vOrder                3     [2,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=None,
            texCoord=None,
            trimmingContour=[],
            uTessellation=0,
            vTessellation=0,
            weight=[],
            solid=True,
            uClosed=True,
            uDimension=0,
            uKnot=[],
            uOrder=3,
            vClosed=False,
            vDimension=0,
            vKnot=[],
            vOrder=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            controlPoint=controlPoint,
            texCoord=texCoord,
            uTessellation=uTessellation,
            vTessellation=vTessellation,
            weight=weight,
            solid=solid,
            uClosed=uClosed,
            uDimension=uDimension,
            uKnot=uKnot,
            uOrder=uOrder,
            vClosed=vClosed,
            vDimension=vDimension,
            vKnot=vKnot,
            vOrder=vOrder,
            **kwargs
        )
        self.trimmingContour = trimmingContour
    
    @property
    def trimmingContour(self):
        return self.__trimmingContour

    @trimmingContour.setter
    def trimmingContour(self, trimmingContour):
        if trimmingContour is None:
            trimmingContour = []
        assertMFNode(trimmingContour, Contour2D)
        self.__trimmingContour = trimmingContour

class FogCoordinate(X3DGeometricPropertyNode): 
    """
    FogCoordinate : X3DGeometricPropertyNode {
        MFFloat [in,out] depth    []   [0,1]
        SFNode  [in,out] metadata NULL [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            depth=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.depth = depth

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth):
        if depth is None:
            depth = []
        assertMFFloat(depth)
        assertValidGreaterThanEquals(depth, 0)
        assertValidLessThanEquals(depth, 1)
        self.__depth = depth
    
class HAnimDisplacer(X3DGeometricPropertyNode):
    """
    HAnimDisplacer : X3DGeometricPropertyNode {
        MFInt32  [in,out] coordIndex    []   [0,∞) or -1
        MFVec3f  [in,out] displacements []
        SFNode   [in,out] metadata      NULL [X3DMetadataObject]
        SFString [in,out] name          ""
        SFFloat  [in,out] weight        0.0  (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",  
            metadata=None,
            coordIndex=[],
            displacements=[],
            name="",
            weight=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.coordIndex = coordIndex
        self.displacements = displacements
        self.name = name
        self.weight = weight

    @property
    def coordIndex(self):
        return self.__coordIndex
        
    @coordIndex.setter
    def coordIndex(self, coordIndex):
        if coordIndex is None:
            coordIndex = []
        assertMFInt32(coordIndex)
        assertValidGreaterThanEquals(coordIndex, -1)
        self.__coordIndex = coordIndex

    @property
    def displacements(self):
        return self.__displacements
        
    @displacements.setter
    def displacements(self, displacements):
        if displacements is None:
            displacements = []
        assertMFVec3f(displacements)
        self.__displacements = displacements

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            name = ""
        assertSFString(name)
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight is None:
            weight = 0.0
        assertSFFloat(weight)
        self.__weight = weight

class Color(X3DColorNode):
    """
    Color : X3DColorNode { 
        MFColor [in,out] color    [NULL] [0,1]
        SFNode  [in,out] metadata NULL   [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            color=[],
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = []
        assertMFColor(color)
        assertValidGreaterThanEquals(color, 0)
        assertValidLessThanEquals(color, 1)
        self.__color = color

class ColorRGBA(X3DColorNode):
    """
    ColorRGBA : X3DColorNode { 
        MFColorRGBA [in,out] color    [NULL] [0,1]
        SFNode      [in,out] metadata NULL   [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            color=[],
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = []
        assertMFColorRGBA(color)
        assertValidGreaterThanEquals(color, 0)
        assertValidLessThanEquals(color, 1)
        self.__color = color

class Coordinate(X3DCoordinateNode): 
    """
    Coordinate : X3DCoordinateNode { 
        SFNode  [in,out] metadata NULL   [X3DMetadataObject]
        MFVec3f [in,out] point    []     (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            point=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            point=point,
            **kwargs
        )
        self.point = point

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if point is None:
            point = []
        assertMFVec3f(point)
        self.__point = point
    
class CoordinateDouble(X3DCoordinateNode):
    """
    CoordinateDouble : X3DCoordinateNode { 
        SFNode  [in,out] metadata NULL [X3DMetadataObject]
        MFVec3d [in,out] point    []   (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            point=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.point = point

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if point is None:
            point = []
        assertMFVec3d(point)
        self.__point = point

class GeoCoordinate(X3DCoordinateNode):
    """
    GeoCoordinate : X3DCoordinateNode {
        SFNode   [in,out] metadata  NULL        [X3DMetadataObject]
        MFVec3d  [in,out] point     []          (-∞,∞)
        SFNode   []       geoOrigin NULL        [GeoOrigin] (deprecated)
        MFString []       geoSystem ["GD","WE"] [see 25.2.3]  
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            point=[],
            geoOrigin=None,
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.point = point
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if point is None:
            point = 1.0
        assertMFVec3d(point)
        self.__point = point

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class Normal(X3DNormalNode):
    """
    Normal : X3DNormalNode { 
        SFNode  [in,out] metadata NULL [X3DMetadataObject]
        MFVec3f [in,out] vector   []   [-1,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            vector=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.vector = vector

    @property
    def vector(self):
        return self.__vector

    @vector.setter
    def vector(self, vector):
        if vector is None:
            vector = []
        assertMFVec3f(vector)
        assertValidGreaterThanEquals(vector, -1)
        assertValidLessThanEquals(vector, 1)
        self.__vector = vector

class MultiTextureCoordinate(X3DTextureCoordinateNode):
    """
    MultiTextureCoordinate : X3DTextureCoordinateNode {
        SFNode [in,out] metadata NULL [X3DMetadataObject]
        MFNode [in,out] texCoord NULL [X3DTextureCoordinateNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            texCoord=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.texCoord = texCoord

    @property
    def texCoord(self):
        return self.__texCoord

    @texCoord.setter
    def texCoord(self, texCoord):
        if texCoord is None:
            texCoord = None
        assertMFNode(texCoord, X3DTextureCoordinateNode)
        self.__texCoord = texCoord

class TextureCoordinate(X3DTextureCoordinateNode):
    """
    TextureCoordinate : X3DTextureCoordinateNode { 
        SFNode  [in,out] metadata NULL [X3DMetadataObject]
        MFVec2f [in,out] point    []   (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            point=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.point = point

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if point is None:
            point = 1.0
        assertMFVec2f(point)
        self.__point = point

class TextureCoordinate3D(X3DTextureCoordinateNode):
    """
    TextureCoordinate3D : X3DTextureCoordinateNode {
        SFNode  [in,out] metadata NULL [X3DMetadataObject]
        MFVec3f [in,out] point    []   (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            point=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.point = point
    
    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if point is None:
            point = []
        assertMFVec3f(point)
        self.__point = point

class TextureCoordinate4D(X3DTextureCoordinateNode):
    """
    TextureCoordinate4D : X3DTextureCoordinateNode {
        SFNode  [in,out] metadata NULL [X3DMetadataObject]
        MFVec4f [in,out] point    []   (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            point=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.point = point
    
    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if point is None:
            point = []
        assertMFVec4f(point)
        self.__point = point

class TextureCoordinateGenerator(X3DTextureCoordinateNode):
    """
    TextureCoordinateGenerator : X3DTextureCoordinateNode {
        SFNode   [in,out] metadata  NULL     [X3DMetadataObject]
        SFString [in,out] mode      "SPHERE" [see Table 18.6]
        MFFloat  [in,out] parameter []       [see Table 18.6]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            mode="SPHERE",
            parameter=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.mode = mode
        self.parameter = parameter

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        if mode is None:
            mode = "SPHERE"
        assertValidTextureCoordinateGenerationModes(mode)
        self.__mode = mode

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter):
        if parameter is None:
            parameter = []
        assertMFFloat(parameter)
        self.__parameter = parameter

class FloatVertexAttribute(X3DVertexAttributeNode):
    """
    FloatVertexAttribute : X3DVertexAttributeNode {
        SFNode   [in,out] metadata      NULL [X3DMetadataObject]
        MFFloat  [in,out] value  		  []   (-∞,∞)
        SFString []       name          ""
        SFInt32  []       numComponents 4    [1..4]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            value=[],
            name="",
            numComponents=4,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            **kwargs
        )
        self.value = value
        self.numComponents = numComponents

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFFloat(value)
        self.__value = value

    @property
    def numComponents(self):
        return self.__numComponents

    @numComponents.setter
    def numComponents(self, numComponents):
        if numComponents is None:
            numComponents = 4
        assertSFInt32(numComponents)
        assertValidGreaterThanEquals(numComponents, 1)
        assertValidLessThanEquals(numComponents, 4)
        self.__numComponents = numComponents

class Matrix3VertexAttribute(X3DVertexAttributeNode):
    """
    Matrix3VertexAttribute : X3DVertexAttributeNode {
        SFNode     [in,out] metadata NULL [X3DMetadataObject]
        MFMatrix3f [in,out] value    []   (-∞,∞)
        SFString   []       name     ""
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            value=[],
            name="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFMatrix3f(value)
        self.__value = value

class Matrix4VertexAttribute(X3DVertexAttributeNode):
    """
    Matrix4VertexAttribute : X3DVertexAttributeNode {
        SFNode     [in,out] metadata NULL [X3DMetadataObject]
        MFMatrix4f [in,out] value    []   (-∞,∞)
        SFString   []       name     ""
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            value=[],
            name="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            name=name,
            **kwargs
        )
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = []
        assertMFMatrix4f(value)
        self.__value = value

class Layer(X3DLayerNode):
    """
    Layer : X3DLayerNode { 
        MFNode [in]     addChildren          [X3DChildNode]
        MFNode [in]     removeChildren       [X3DChildNode]
        MFNode [in,out] children       []    [X3DChildNode]
        SFBool [in,out] isPickable     TRUE
        SFNode [in,out] metadata       NULL  [X3DMetadataObject]
        SFNode [in,out] viewport       NULL  [X3DViewportNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            isPickable=True,
            viewport=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            isPickable=isPickable,
            viewport=viewport,
            **kwargs
        )
        self.children = children

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        if children is None:
            children = []
        assertMFNode(children, X3DChildNode)
        self.__children = children

class LayoutLayer(X3DLayerNode):
    """
    LayoutLayer : X3DLayerNode { 
        MFNode [in]     addChildren         [X3DChildNode]
        MFNode [in]     removeChildren      [X3DChildNode]
        MFNode [in,out] children       []   [X3DChildNode]
        SFBool [in,out] isPickable     TRUE
        SFNode [in,out] layout         NULL [X3DLayoutNode]
        SFNode [in,out] metadata       NULL [X3DMetadataObject]
        SFNode [in,out] viewport       NULL [X3DViewportNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            layout=None,
            isPickable=True,
            viewport=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            isPickable=isPickable,
            viewport=viewport,
            **kwargs
        )
        self.children = children
        self.layout = layout

    @property
    def children(self):
        return self.__children
    
    @children.setter
    def children(self, children):
        if children is None:
            children = []
        assertMFNode(children, X3DChildNode)
        self.__children = children

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout):
        if layout is None:
            layout = None
        assertSFNode(layout, X3DLayoutNode)
        self.__layout = layout

class CollisionSpace(X3DNBodyCollisionSpaceNode):
    """
    CollisionSpace : X3DNBodyCollisionSpaceNode {
        MFNode  [in,out] collidables NULL     [X3DNBodyCollisionSpaceNode,
                                                X3DNBodyCollidableNode]
        SFBool  [in,out] enabled     TRUE
        SFNode  [in,out] metadata    NULL     [X3DMetadataObject]
        SFBool  [in,out] useGeometry FALSE
        SFVec3f []       bboxCenter  0 0 0    (-∞,∞)
        SFVec3f []       bboxSize    -1 -1 -1 [0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            collidables=None,
            enabled=True,
            useGeometry=False,
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.collidables = collidables
        self.useGeometry = useGeometry

    @property
    def collidables(self):
        return self.__collidables

    @collidables.setter
    def collidables(self, collidables):
        if collidables is None:
            collidables = [None]
        assertSFNode(collidables, X3DNBodyCollisionSpaceNode, X3DNBodyCollidableNode)
        self.__collidables = collidables

    @property
    def useGeometry(self):
        return self.__useGeometry

    @useGeometry.setter
    def useGeometry(self, useGeometry):
        if useGeometry is None:
            useGeometry = False
        assertSFBool(useGeometry)
        self.__useGeometry = useGeometry

class ContourPolyline2D(X3DNurbsControlCurveNode):
    """
    ContourPolyline2D : X3DNurbsControlCurveNode {
        SFNode  [in,out] metadata     NULL [X3DMetadataObject]
        MFVec2d [in,out] controlPoint []   (-∞, ∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            controlPoint=controlPoint,
            **kwargs
        )

class NurbsCurve2D(X3DNurbsControlCurveNode):
    """
    NurbsCurve2D : X3DNurbsControlCurveNode {
        MFVec2d  [in,out] controlPoint []    (-∞,∞)
        SFNode   [in,out] metadata     NULL  [X3DMetadataObject]
        SFInt32  [in,out] tessellation 0     (-∞,∞)
        MFDouble [in,out] weight       []    (0,∞)
        SFBool   []       closed       FALSE 
        MFDouble []       knot         []    (-∞,∞)
        SFInt32  []       order        3     [2,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=[],
            tessellation=0,
            weight=[],
            closed=False,
            knot=[],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.controlPoint = controlPoint
        self.tessellation = tessellation
        self.weight = weight
        self.closed = closed
        self.knot = knot
        self.order = order

    @property
    def controlPoint(self):
        return self.__controlPoint

    @controlPoint.setter
    def controlPoint(self, controlPoint):
        if controlPoint is None:
            controlPoint = []
        assertMFVec2d(controlPoint)
        self.__controlPoint = controlPoint

    @property
    def tessellation(self):
        return self.__tessellation

    @tessellation.setter
    def tessellation(self, tessellation):
        if tessellation is None:
            tessellation = 0
        assertSFInt32(tessellation)
        self.__tessellation = tessellation

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight is None:
            weight = []
        assertMFDouble(weight)
        assertValidGreaterThan(weight, 0)
        self.__weight = weight

    @property
    def closed(self):
        return self.__closed

    @closed.setter
    def closed(self, closed):
        if closed is None:
            closed = False
        assertSFBool(closed)
        self.__closed = closed

    @property
    def knot(self):
        return self.__knot

    @knot.setter
    def knot(self, knot):
        if knot is None:
            knot = []
        assertMFDouble(knot)
        self.__knot = knot

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if order is None:
            order = 3
        assertSFInt32(order)
        assertValidGreaterThanEquals(order, 2)
        self.__order = order

class ConeEmitter(X3DParticleEmitterNode):
    """
    ConeEmitter : X3DParticleEmitterNode { 
        SFFloat [in,out] angle       π/4   [0,π]
        SFVec3f [in,out] direction   0 1 0 
        SFNode  [in,out] metadata    NULL  [X3DMetadataObject]
        SFVec3f [in,out] position    0 0 0
        SFFloat [in,out] speed       0     [0,∞)
        SFFloat [in,out] variation   0.25  [0,∞)
        SFFloat []       mass        0     [0,∞)
        SFFloat []       surfaceArea 0     [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            angle=math.pi/4,
            direction=[0.0, 1.0, 0.0],
            position=[0.0, 0.0, 0.0],
            speed=0.0,
            variation=0.25,
            mass=0.0,
            surfaceArea=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            speed=speed,
            variation=variation,
            mass=mass,
            surfaceArea=surfaceArea,
            **kwargs
        )
        self.angle = angle
        self.direction = direction
        self.position = position

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        if angle is None:
            angle = math.pi/4
        assertSFFloat(angle)
        assertValidGreaterThanEquals(angle, 0)
        assertValidLessThanEquals(angle, math.pi)
        self.__angle = angle

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 1.0, 0.0]
        assertSFVec3f(direction)
        self.__direction = direction

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position is None:
            position = [0.0, 0.0, 0.0]
        assertSFVec3f(position)
        self.__position = position
        
class ExplosionEmitter(X3DParticleEmitterNode):
    """
    ExplosionEmitter : X3DParticleEmitterNode { 
        SFNode  [in,out] metadata    NULL  [X3DMetadataObject]
        SFVec3f [in,out] position    0 0 0
        SFFloat [in,out] speed       0     [0,∞)
        SFFloat [in,out] variation   0.25  [0,∞)
        SFFloat []       mass        0     [0,∞)
        SFFloat []       surfaceArea 0     [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            angle=math.pi/4,
            position=[0.0, 0.0, 0.0],
            speed=0.0,
            variation=0.25,
            mass=0.0,
            surfaceArea=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            speed=speed,
            variation=variation,
            mass=mass,
            surfaceArea=surfaceArea,
            **kwargs
        )
        self.angle = angle
        self.position = position

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        if angle is None:
            angle = math.pi/4
        assertSFFloat(angle)
        assertValidGreaterThanEquals(angle, 0)
        assertValidLessThanEquals(angle, math.pi)
        self.__angle = angle

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position is None:
            position = [0.0, 0.0, 0.0]
        assertSFVec3f(position)
        self.__position = position

class PointEmitter(X3DParticleEmitterNode):
    """
    PointEmitter : X3DParticleEmitterNode { 
        SFVec3f [in,out] direction   0 1 0
        SFNode  [in,out] metadata    NULL  [X3DMetadataObject]
        SFVec3f [in,out] position    0 0 0
        SFFloat [in,out] speed       0     [0,∞)
        SFFloat [in,out] variation   0.25  [0,∞)
        SFFloat []       mass        0     [0,∞)
        SFFloat []       surfaceArea 0     [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            angle=math.pi/4,
            direction=[0.0, 1.0, 0.0],
            position=[0.0, 0.0, 0.0],
            speed=0.0,
            variation=0.25,
            mass=0.0,
            surfaceArea=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            speed=speed,
            variation=variation,
            mass=mass,
            surfaceArea=surfaceArea,
            **kwargs
        )
        self.angle = angle
        self.direction = direction
        self.position = position

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        if angle is None:
            angle = math.pi/4
        assertSFFloat(angle)
        assertValidGreaterThanEquals(angle, 0)
        assertValidLessThanEquals(angle, math.pi)
        self.__angle = angle

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 1.0, 0.0]
        assertSFVec3f(direction)
        self.__direction = direction

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position is None:
            position = [0.0, 0.0, 0.0]
        assertSFVec3f(position)
        self.__position = position

class PolylineEmitter(X3DParticleEmitterNode):
    """
    PolylineEmitter : X3DParticleEmitterNode { 
        MFInt32 [in]     set_coordIndex
        SFNode  [in,out] coord          NULL  [X3DCoordinateNode]
        SFVec3f [in,out] direction      0 1 0 [-1,1]
        SFNode  [in,out] metadata       NULL  [X3DMetadataObject]
        SFFloat [in,out] speed          0     [0,∞)
        SFFloat [in,out] variation      0.25  [0,∞)
        MFInt32 []       coordIndex     -1    [0,∞) or -1
        SFFloat []       mass           0     [0,∞)
        SFFloat []       surfaceArea    0     [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            angle=math.pi/4,
            coord=None,
            coordIndex=-1,
            direction=[0.0, 1.0, 0.0],
            speed=0.0,
            variation=0.25,
            mass=0.0,
            surfaceArea=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            speed=speed,
            variation=variation,
            mass=mass,
            surfaceArea=surfaceArea,
            **kwargs
        )
        self.angle = angle
        self.direction = direction
        self.coord = coord
        self.coordIndex = coordIndex

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        if angle is None:
            angle = math.pi/4
        assertSFFloat(angle)
        assertValidGreaterThanEquals(angle, 0)
        assertValidLessThanEquals(angle, math.pi)
        self.__angle = angle

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 1.0, 0.0]
        assertSFVec3f(direction)
        assertValidGreaterThanEquals(direction, -1)
        assertValidLessThanEquals(direction, 1)
        self.__direction = direction

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, coord):
        if coord is None:
            coord = None
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

    @property
    def coordIndex(self):
        return self.__coordIndex

    @coordIndex.setter
    def coordIndex(self, coordIndex):
        if coordIndex is None:
            coordIndex = [-1]
        assertMFInt32(coordIndex)
        assertValidGreaterThanEquals(coordIndex, -1)
        self.__coordIndex = coordIndex

class SurfaceEmitter(X3DParticleEmitterNode):
    """
    SurfaceEmitter : X3DParticleEmitterNode { 
        MFInt32 [in]     set_coordIndex
        SFNode  [in,out] metadata       NULL  [X3DMetadataObject]
        SFFloat [in,out] speed          0     [0,∞)
        SFFloat [in,out] variation      0.25  [0,∞)
        MFInt32 []       coordIndex     -1    [0,∞) or -1
        SFFloat []       mass           0     [0,∞)
        SFNode  []       surface        NULL  [X3DGeometryNode]
        SFFloat []       surfaceArea    0     [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            coordIndex=-1,
            speed=0.0,
            variation=0.25,
            mass=0.0,
            surface=None,
            surfaceArea=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            speed=speed,
            variation=variation,
            mass=mass,
            surfaceArea=surfaceArea,
            **kwargs
        )
        self.coordIndex = coordIndex
        self.surface = surface

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, coord):
        if coord is None:
            coord = None
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

    @property
    def coordIndex(self):
        return self.__coordIndex

    @coordIndex.setter
    def coordIndex(self, coordIndex):
        if coordIndex is None:
            coordIndex = [-1]
        assertMFInt32(coordIndex)
        assertValidGreaterThanEquals(coordIndex, -1)
        self.__coordIndex = coordIndex

    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, surface):
        if surface is None:
            surface = None
        assertSFNode(surface, X3DGeometryNode)
        self.__surface = surface

class VolumeEmitter(X3DParticleEmitterNode):
    """
    VolumeEmitter : X3DParticleEmitterNode { 
        MFInt32 [in]     set_coordIndex
        SFNode  [in,out] coord          NULL  [X3DCoordinateNode]
        SFVec3f [in,out] direction      0 1 0 [-1,1]
        SFNode  [in,out] metadata       NULL  [X3DMetadataObject]
        SFFloat [in,out] speed          0     [0,∞)
        SFFloat [in,out] variation      0.25  [0,∞)
        MFInt32 []       coordIndex     -1    [0,∞) or -1
        SFBool  []       internal       TRUE
        SFFloat []       mass           0     [0,∞)
        SFFloat []       surfaceArea    0     [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            coord=None,
            coordIndex=-1,
            direction=[0.0, 1.0, 0.0],
            speed=0.0,
            variation=0.25,
            internal=True,
            mass=0.0,
            surfaceArea=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            speed=speed,
            variation=variation,
            mass=mass,
            surfaceArea=surfaceArea,
            **kwargs
        )
        self.coord = coord
        self.coordIndex = coordIndex
        self.direction = direction
        self.internal = internal

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, coord):
        if coord is None:
            coord = None
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

    @property
    def coordIndex(self):
        return self.__coordIndex

    @coordIndex.setter
    def coordIndex(self, coordIndex):
        if coordIndex is None:
            coordIndex = [-1]
        assertMFInt32(coordIndex)
        assertValidGreaterThanEquals(coordIndex, -1)
        self.__coordIndex = coordIndex

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 1.0, 0.0]
        assertSFVec3f(direction)
        assertValidGreaterThanEquals(direction, -1)
        assertValidLessThanEquals(direction, -1)
        self.__direction = direction

    @property
    def internal(self):
        return self.__internal

    @internal.setter
    def internal(self, internal):
        if internal is None:
            internal = True
        assertSFBool(internal)
        self.__internal = internal

class BoundedPhysicsModel(X3DParticlePhysicsModelNode):
    """
    BoundedPhysicsModel : X3DParticlePhysicsModelNode { 
        SFBool [in,out] enabled  TRUE
        SFNode [in,out] geometry NULL [X3DGeometryNode]
        SFNode [in,out] metadata NULL [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            geometry=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.geometry = geometry

    @property
    def geometry(self):
        return self.__geometry

    @geometry.setter
    def geometry(self, geometry):
        if geometry is None:
            geometry = None
        assertSFNode(geometry. X3DGeometryNode)
        self.__geometry = geometry

class ForcePhysicsModel(X3DParticlePhysicsModelNode):
    """
    ForcePhysicsModel : X3DParticlePhysicsModelNode { 
        SFBool  [in,out] enabled  TRUE
        SFVec3f [in,out] force    0 -9.8 0 (∞,∞)
        SFNode  [in,out] metadata NULL     [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            force=[0.0, -9.8, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.force = force

    @property
    def force(self):
        return self.__force

    @force.setter
    def force(self, force):
        if force is None:
            force = [0.0, -9.8, 0.0]
        assertSFVec3f(force)
        self.__force = force

class WindPhysicsModel(X3DParticlePhysicsModelNode):
    """
    WindPhysicsModel : X3DParticlePhysicsModelNode { 
        SFVec3f [in,out] direction  0 0 0 (∞,∞)
        SFBool  [in,out] enabled    TRUE
        SFFloat [in,out] gustiness  0.1   [0,∞)
        SFNode  [in,out] metadata   NULL  [X3DMetadataObject]
        SFFloat [in,out] speed      0.1   [0,∞)
        SFFloat [in,out] turbulence 0     [0,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            direction=[0.0, 0.0, 0.0],
            enabled=True,
            gustiness=0.1,
            speed=0.1,
            turbulence=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.direction = direction
        self.gustiness = gustiness
        self.speed = speed
        self.turbulence = turbulence

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 0.0, 0.0]
        assertSFVec3f(direction)
        self.__direction = direction

    @property
    def gustiness(self):
        return self.__gustiness

    @gustiness.setter
    def gustiness(self, gustiness):
        if gustiness is None:
            gustiness = 0.1
        assertSFFloat(gustiness)
        assertValidGreaterThanEquals(gustiness, 0)
        self.__gustiness = gustiness

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if speed is None:
            speed = 0.1
        assertSFFloat(speed)
        assertValidGreaterThanEquals(speed, 0)
        self.__speed = speed

    @property
    def turbulence(self):
        return self.__turbulence

    @turbulence.setter
    def turbulence(self, turbulence):
        if turbulence is None:
            turbulence = 0.0
        assertSFFloat(turbulence)
        assertValidGreaterThanEquals(turbulence, 0)
        assertValidLessThanEquals(turbulence, 1)
        self.__turbulence = turbulence

class BallJoint(X3DRigidJointNode):
    """
    BallJoint : X3DRigidJointNode {
        SFVec3f  [in,out] anchorPoint      0 0 0
        SFNode   [in,out] body1            NULL   [RigidBody]
        SFNode   [in,out] body2            NULL   [RigidBody]
        MFString [in,out] forceOutput      "NONE" ["ALL","NONE",...]
        SFNode   [in,out] metadata         NULL   [X3DMetadataObject]
        SFVec3f  [out]    body1AnchorPoint
        SFVec3f  [out]    body2AnchorPoint
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            anchorPoint=[0.0, 0.0, 0.0],
            body1=None,
            body2=None,
            forceOutput=["NONE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            forceOutput=forceOutput,
            **kwargs
        )
        self.anchorPoint = anchorPoint
        self.body1 = body1
        self.body2 = body2

    @property
    def anchorPoint(self):
        return self.__anchorPoint

    @anchorPoint.setter
    def anchorPoint(self, anchorPoint):
        if anchorPoint is None:
            anchorPoint = [0.0, 0.0, 0.0]
        assertSFVec3f(anchorPoint)
        self.__anchorPoint = anchorPoint

    @property
    def body1(self):
        return self.__body1

    @body1.setter
    def body1(self, body1):
        if body1 is None:
            body1 = None
        assertSFNode(body1, RigidBody)
        self.__body1 = body1

    @property
    def body2(self):
        return self.__body2

    @body2.setter
    def body2(self, body2):
        if body2 is None:
            body2 = None
        assertSFNode(body2, RigidBody)
        self.__body2 = body2

class DoubleAxisHingeJoint(X3DRigidJointNode):
    """
    DoubleAxisHingeJoint : X3DRigidJointNode {
        SFVec3f  [in,out] anchorPoint               0 0 0
        SFVec3f  [in,out] axis1                     0 0 0
        SFVec3f  [in,out] axis2                     0 0 0
        SFNode   [in,out] body1                     NULL   [RigidBody]
        SFNode   [in,out] body2                     NULL   [RigidBody]
        SFFloat  [in,out] desiredAngularVelocity1   0      (-∞,∞)
        SFFloat  [in,out] desiredAngularVelocity2   0      (-∞,∞)
        MFString [in,out] forceOutput               "NONE" ["ALL","NONE",...]
        SFFloat  [in,out] maxAngle1                 π      [-π,π]
        SFFloat  [in,out] maxTorque1                0      (-∞,∞)
        SFFloat  [in,out] maxTorque2                0      (-∞,∞)
        SFNode   [in,out] metadata                  NULL   [X3DMetadataObject]
        SFFloat  [in,out] minAngle1                 -π     [-π,π]
        SFFloat  [in,out] stopBounce1               0      [0,1]
        SFFloat  [in,out] stopConstantForceMix1     0.001  [0,∞)
        SFFloat  [in,out] stopErrorCorrection1      0.8    [0,1]
        SFFloat  [in,out] suspensionErrorCorrection 0.8    [0,1]
        SFFloat  [in,out] suspensionForce           0      [0,∞)
        SFVec3f  [out]    body1AnchorPoint
        SFVec3f  [out]    body1Axis
        SFVec3f  [out]    body2AnchorPoint
        SFVec3f  [out]    body2Axis
        SFFloat  [out]    hinge1Angle
        SFFloat  [out]    hinge1AngleRate
        SFFloat  [out]    hinge2Angle
        SFFloat  [out]    hinge2AngleRate
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            anchorPoint=[0.0, 0.0, 0.0],
            axis1=[0.0, 0.0, 0.0],
            axis2=[0.0, 0.0, 0.0],
            body1=None,
            body2=None,
            desiredAngularVelocity1=0.0,
            desiredAngularVelocity2=0.0,
            forceOutput=["NONE"],
            maxAngle1=math.pi,
            maxTorque1=0.0,
            maxTorque2=0.0,
            minAngle1=-math.pi,
            stopBounce1=0.0,
            stopConstantForceMix1=0.001,
            stopErrorCorrection1=0.8,
            suspensionErrorCorrection=0.8,
            suspensionForce=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            forceOutput=forceOutput,
            **kwargs
        )
        self.anchorPoint = anchorPoint
        self.axis1 = axis1
        self.axis2 = axis2
        self.body1 = body1
        self.body2 = body2
        self.desiredAngularVelocity1 = desiredAngularVelocity1
        self.desiredAngularVelocity2 = desiredAngularVelocity2
        self.maxAngle1 = maxAngle1
        self.maxTorque1 = maxTorque1
        self.maxTorque2 = maxTorque2
        self.minAngle1 = minAngle1
        self.stopBounce1 = stopBounce1
        self.stopConstantForceMix1 = stopConstantForceMix1
        self.stopErrorCorrection1 = stopErrorCorrection1
        self.suspensionErrorCorrection = suspensionErrorCorrection
        self.suspensionForce = suspensionForce

    @property
    def anchorPoint(self):
        return self.__anchorPoint

    @anchorPoint.setter
    def anchorPoint(self, anchorPoint):
        if anchorPoint is None:
            anchorPoint = [0.0, 0.0, 0.0]
        assertSFVec3f(anchorPoint)
        self.__anchorPoint = anchorPoint

    @property
    def axis1(self):
        return self.__axis1

    @axis1.setter
    def axis1(self, axis1):
        if axis1 is None:
            axis1 = [0.0, 0.0, 0.0]
        assertSFVec3f(axis1)
        self.__axis1 = axis1

    @property
    def axis2(self):
        return self.__axis2

    @axis2.setter
    def axis2(self, axis2):
        if axis2 is None:
            axis2 = [0.0, 0.0, 0.0]
        assertSFVec3f(axis2)
        self.__axis2 = axis2

    @property
    def body1(self):
        return self.__body1

    @body1.setter
    def body1(self, body1):
        if body1 is None:
            body1 = None
        assertSFNode(body1, RigidBody)
        self.__body1 = body1

    @property
    def body2(self):
        return self.__body2

    @body2.setter
    def body2(self, body2):
        if body2 is None:
            body2 = None
        assertSFNode(body2, RigidBody)
        self.__body2 = body2

    @property
    def desiredAngularVelocity1(self):
        return self.__desiredAngularVelocity1

    @desiredAngularVelocity1.setter
    def desiredAngularVelocity1(self, desiredAngularVelocity1):
        if desiredAngularVelocity1 is None:
            desiredAngularVelocity1 = 0.0
        assertSFFloat(desiredAngularVelocity1)
        self.__desiredAngularVelocity1 = desiredAngularVelocity1

    @property
    def desiredAngularVelocity2(self):
        return self.__desiredAngularVelocity2

    @desiredAngularVelocity2.setter
    def desiredAngularVelocity2(self, desiredAngularVelocity2):
        if desiredAngularVelocity2 is None:
            desiredAngularVelocity2 = 0.0
        assertSFFloat(desiredAngularVelocity2)
        self.__desiredAngularVelocity2 = desiredAngularVelocity2

    @property
    def maxAngle1(self):
        return self.__maxAngle1

    @maxAngle1.setter
    def maxAngle1(self, maxAngle1):
        if maxAngle1 is None:
            maxAngle1 = math.pi
        assertSFFloat(maxAngle1)
        assertValidGreaterThanEquals(maxAngle1, -math.pi)
        assertValidLessThanEquals(maxAngle1, math.pi)
        self.__maxAngle1 = maxAngle1

    @property
    def maxTorque1(self):
        return self.__maxTorque1

    @maxTorque1.setter
    def maxTorque1(self, maxTorque1):
        if maxTorque1 is None:
            maxTorque1 = 0.0
        assertSFFloat(maxTorque1)
        self.__maxTorque1 = maxTorque1

    @property
    def maxTorque2(self):
        return self.__maxTorque2

    @maxTorque2.setter
    def maxTorque2(self, maxTorque2):
        if maxTorque2 is None:
            maxTorque2 = 0.0
        assertSFFloat(maxTorque2)
        self.__maxTorque2 = maxTorque2

    @property
    def minAngle1(self):
        return self.__minAngle1

    @minAngle1.setter
    def minAngle1(self, minAngle1):
        if minAngle1 is None:
            minAngle1 = -math.pi
        assertSFFloat(minAngle1)
        assertValidGreaterThanEquals(minAngle1, -math.pi)
        assertValidLessThanEquals(minAngle1, math.pi)
        self.__minAngle1 = minAngle1

    @property
    def stopBounce1(self):
        return self.__stopBounce1

    @stopBounce1.setter
    def stopBounce1(self, stopBounce1):
        if stopBounce1 is None:
            stopBounce1 = 0.0
        assertSFFloat(stopBounce1)
        assertValidGreaterThanEquals(stopBounce1, 0)
        assertValidLessThanEquals(stopBounce1, 1)
        self.__stopBounce1 = stopBounce1

    @property
    def stopConstantForceMix1(self):
        return self.__stopConstantForceMix1

    @stopConstantForceMix1.setter
    def stopConstantForceMix1(self, stopConstantForceMix1):
        if stopConstantForceMix1 is None:
            stopConstantForceMix1 = 0.001
        assertSFFloat(stopConstantForceMix1)
        assertValidGreaterThanEquals(stopConstantForceMix1, 0)
        self.__stopConstantForceMix1 = stopConstantForceMix1

    @property
    def stopErrorCorrection1(self):
        return self.__stopErrorCorrection1

    @stopErrorCorrection1.setter
    def stopErrorCorrection1(self, stopErrorCorrection1):
        if stopErrorCorrection1 is None:
            stopErrorCorrection1 = 0.8
        assertSFFloat(stopErrorCorrection1)
        assertValidGreaterThanEquals(stopErrorCorrection1, 0)
        assertValidLessThanEquals(stopErrorCorrection1, 1)
        self.__stopErrorCorrection1 = stopErrorCorrection1

    @property
    def suspensionErrorCorrection(self):
        return self.__suspensionErrorCorrection

    @suspensionErrorCorrection.setter
    def suspensionErrorCorrection(self, suspensionErrorCorrection):
        if suspensionErrorCorrection is None:
            suspensionErrorCorrection = 0.8
        assertSFFloat(suspensionErrorCorrection)
        assertValidGreaterThanEquals(suspensionErrorCorrection, 0)
        assertValidLessThanEquals(suspensionErrorCorrection, 1)
        self.__suspensionErrorCorrection = suspensionErrorCorrection

    @property
    def suspensionForce(self):
        return self.__suspensionForce

    @suspensionForce.setter
    def suspensionForce(self, suspensionForce):
        if suspensionForce is None:
            suspensionForce = 0.0
        assertSFFloat(suspensionForce)
        assertValidGreaterThanEquals(suspensionForce, 0)
        self.__suspensionForce = suspensionForce

class MotorJoint(X3DRigidJointNode):
    """
    MotorJoint : X3DRigidJointNode {
        SFFloat  [in,out] axis1Angle           0      [-π,π]
        SFFloat  [in,out] axis1Torque          0      (-∞,∞)
        SFFloat  [in,out] axis2Angle           0      [-π,π]
        SFFloat  [in,out] axis2Torque          0      (-∞,∞)
        SFFloat  [in,out] axis3Angle           0      [-π,π]
        SFFloat  [in,out] axis3Torque          0      (-∞,∞)
        SFNode   [in,out] body1                NULL   [RigidBody]
        SFNode   [in,out] body2                NULL   [RigidBody]
        SFInt32  [in,out] enabledAxes          1	[0,3]
        MFString [in,out] forceOutput          "NONE" ["ALL","NONE",...]
        SFNode   [in,out] metadata             NULL   [X3DMetadataObject]
        SFVec3f  [in,out] motor1Axis           0 0 0
        SFVec3f  [in,out] motor2Axis           0 0 0
        SFVec3f  [in,out] motor3Axis           0 0 0
        SFFloat  [in,out] stop1Bounce          0      [0,1]
        SFFloat  [in,out] stop1ErrorCorrection 0.8    [0,1]
        SFFloat  [in,out] stop2Bounce          0      [0,1]
        SFFloat  [in,out] stop2ErrorCorrection 0.8    [0,1]
        SFFloat  [in,out] stop3Bounce          0      [0,1]
        SFFloat  [in,out] stop3ErrorCorrection 0.8    [0,1]
        SFFloat  [out]    motor1Angle
        SFFloat  [out]    motor1AngleRate
        SFFloat  [out]    motor2Angle
        SFFloat  [out]    motor2AngleRate
        SFFloat  [out]    motor3Angle
        SFFloat  [out]    motor3AngleRate
        SFBool   []       autoCalc             FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            axis1Angle=0.0,
            axis1Torque=0.0,
            axis2Angle=0.0,
            axis2Torque=0.0,
            axis3Angle=0.0,
            axis3Torque=0.0,
            body1=None,
            body2=None,
            enabledAxes=1,
            forceOutput=["NONE"],
            motor1Axis=[0.0, 0.0, 0.0],
            motor2Axis=[0.0, 0.0, 0.0],
            motor3Axis=[0.0, 0.0, 0.0],
            stop1Bounce=0.0,
            stop1ErrorCorrection=0.8,
            stop2Bounce=0.0,
            stop2ErrorCorrection=0.8,
            stop3Bounce=0.0,
            stop3ErrorCorrection=0.8,
            autoCalc=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            forceOutput=forceOutput,
            **kwargs
        )
        self.axis1Angle = axis1Angle
        self.axis1Torque = axis1Torque
        self.axis2Angle = axis2Angle
        self.axis2Torque = axis2Torque
        self.axis3Angle = axis3Angle
        self.axis3Torque = axis3Torque
        self.body1 = body1
        self.body2 = body2
        self.enabledAxes = enabledAxes
        self.motor1Axis = motor1Axis
        self.motor2Axis = motor2Axis
        self.motor3Axis = motor3Axis
        self.stop1Bounce = stop1Bounce
        self.stop1ErrorCorrection = stop1ErrorCorrection
        self.stop2Bounce = stop2Bounce
        self.stop2ErrorCorrection = stop2ErrorCorrection
        self.stop3Bounce = stop3Bounce
        self.stop3ErrorCorrection = stop3ErrorCorrection
        self.autoCalc = autoCalc

    @property
    def axis1Angle(self):
        return self.__axis1Angle

    @axis1Angle.setter
    def axis1Angle(self, axis1Angle):
        if axis1Angle is None:
            axis1Angle = math.pi
        assertSFFloat(axis1Angle)
        assertValidGreaterThanEquals(axis1Angle, -math.pi)
        assertValidLessThanEquals(axis1Angle, math.pi)
        self.__axis1Angle = axis1Angle

    @property
    def axis1Torque(self):
        return self.__axis1Torque

    @axis1Torque.setter
    def axis1Torque(self, axis1Torque):
        if axis1Torque is None:
            axis1Torque = 0.0
        assertSFFloat(axis1Torque)
        self.__axis1Torque = axis1Torque

    @property
    def axis2Angle(self):
        return self.__axis2Angle

    @axis2Angle.setter
    def axis2Angle(self, axis2Angle):
        if axis2Angle is None:
            axis2Angle = math.pi
        assertSFFloat(axis2Angle)
        assertValidGreaterThanEquals(axis2Angle, -math.pi)
        assertValidLessThanEquals(axis2Angle, math.pi)
        self.__axis2Angle = axis2Angle

    @property
    def axis2Torque(self):
        return self.__axis2Torque

    @axis2Torque.setter
    def axis2Torque(self, axis2Torque):
        if axis2Torque is None:
            axis2Torque = 0.0
        assertSFFloat(axis2Torque)
        self.__axis2Torque = axis2Torque

    @property
    def axis3Angle(self):
        return self.__axis3Angle

    @axis3Angle.setter
    def axis3Angle(self, axis3Angle):
        if axis3Angle is None:
            axis3Angle = math.pi
        assertSFFloat(axis3Angle)
        assertValidGreaterThanEquals(axis3Angle, -math.pi)
        assertValidLessThanEquals(axis3Angle, math.pi)
        self.__axis3Angle = axis3Angle

    @property
    def axis3Torque(self):
        return self.__axis3Torque

    @axis3Torque.setter
    def axis3Torque(self, axis3Torque):
        if axis3Torque is None:
            axis3Torque = 0.0
        assertSFFloat(axis3Torque)
        self.__axis3Torque = axis3Torque

    @property
    def body1(self):
        return self.__body1

    @body1.setter
    def body1(self, body1):
        if body1 is None:
            body1 = None
        assertSFNode(body1, RigidBody)
        self.__body1 = body1

    @property
    def body2(self):
        return self.__body2

    @body2.setter
    def body2(self, body2):
        if body2 is None:
            body2 = None
        assertSFNode(body2, RigidBody)
        self.__body2 = body2

    @property
    def enabledAxes(self):
        return self.__enabledAxes

    @enabledAxes.setter
    def enabledAxes(self, enabledAxes):
        if enabledAxes is None:
            enabledAxes = 1
        assertSFInt32(enabledAxes)
        assertValidGreaterThanEquals(enabledAxes, 0)
        assertValidLessThanEquals(enabledAxes, 3)
        self.__enabledAxes = enabledAxes

    @property
    def motor1Axis(self):
        return self.__motor1Axis

    @motor1Axis.setter
    def motor1Axis(self, motor1Axis):
        if motor1Axis is None:
            motor1Axis = [0.0, 0.0, 0.0]
        assertSFVec3f(motor1Axis)
        self.__motor1Axis = motor1Axis

    @property
    def motor2Axis(self):
        return self.__motor2Axis

    @motor2Axis.setter
    def motor2Axis(self, motor2Axis):
        if motor2Axis is None:
            motor2Axis = [0.0, 0.0, 0.0]
        assertSFVec3f(motor2Axis)
        self.__motor2Axis = motor2Axis

    @property
    def motor3Axis(self):
        return self.__motor3Axis

    @motor3Axis.setter
    def motor3Axis(self, motor3Axis):
        if motor3Axis is None:
            motor3Axis = [0.0, 0.0, 0.0]
        assertSFVec3f(motor3Axis)
        self.__motor3Axis = motor3Axis

    @property
    def stop1Bounce(self):
        return self.__stop1Bounce

    @stop1Bounce.setter
    def stop1Bounce(self, stop1Bounce):
        if stop1Bounce is None:
            stop1Bounce = 0.0
        assertSFFloat(stop1Bounce)
        assertValidGreaterThanEquals(stop1Bounce, 0)
        assertValidLessThanEquals(stop1Bounce, 1)
        self.__stop1Bounce = stop1Bounce
    
    @property
    def stop1ErrorCorrection(self):
        return self.__stop1ErrorCorrection

    @stop1ErrorCorrection.setter
    def stop1ErrorCorrection(self, stop1ErrorCorrection):
        if stop1ErrorCorrection is None:
            stop1ErrorCorrection = 0.8
        assertSFFloat(stop1ErrorCorrection)
        assertValidGreaterThanEquals(stop1ErrorCorrection, 0)
        assertValidLessThanEquals(stop1ErrorCorrection, 1)
        self.__stop1ErrorCorrection = stop1ErrorCorrection

    @property
    def stop2Bounce(self):
        return self.__stop2Bounce

    @stop2Bounce.setter
    def stop2Bounce(self, stop2Bounce):
        if stop2Bounce is None:
            stop2Bounce = 0.0
        assertSFFloat(stop2Bounce)
        assertValidGreaterThanEquals(stop2Bounce, 0)
        assertValidLessThanEquals(stop2Bounce, 1)
        self.__stop2Bounce = stop2Bounce

    @property
    def stop2ErrorCorrection(self):
        return self.__stop2ErrorCorrection

    @stop2ErrorCorrection.setter
    def stop2ErrorCorrection(self, stop2ErrorCorrection):
        if stop2ErrorCorrection is None:
            stop2ErrorCorrection = 0.8
        assertSFFloat(stop2ErrorCorrection)
        assertValidGreaterThanEquals(stop2ErrorCorrection, 0)
        assertValidLessThanEquals(stop2ErrorCorrection, 1)
        self.__stop2ErrorCorrection = stop2ErrorCorrection

    @property
    def stop3Bounce(self):
        return self.__stop3Bounce

    @stop3Bounce.setter
    def stop3Bounce(self, stop3Bounce):
        if stop3Bounce is None:
            stop3Bounce = 0.0
        assertSFFloat(stop3Bounce)
        assertValidGreaterThanEquals(stop3Bounce, 0)
        assertValidLessThanEquals(stop3Bounce, 1)
        self.__stop3Bounce = stop3Bounce

    @property
    def stop3ErrorCorrection(self):
        return self.__stop3ErrorCorrection

    @stop3ErrorCorrection.setter
    def stop3ErrorCorrection(self, stop3ErrorCorrection):
        if stop3ErrorCorrection is None:
            stop3ErrorCorrection = 0.8
        assertSFFloat(stop3ErrorCorrection)
        assertValidGreaterThanEquals(stop3ErrorCorrection, 0)
        assertValidLessThanEquals(stop3ErrorCorrection, 1)
        self.__stop3ErrorCorrection = stop3ErrorCorrection

    @property
    def autoCalc(self):
        return self.__autoCalc

    @autoCalc.setter
    def autoCalc(self, autoCalc):
        if autoCalc is None:
            autoCalc = False
        assertSFBool(autoCalc)
        self.__autoCalc = autoCalc

class SingleAxisHingeJoint(X3DRigidJointNode):
    """
    SingleAxisHingeJoint : X3DRigidJointNode {
        SFVec3f  [in,out] anchorPoint         0 0 0
        SFVec3f  [in,out] axis                0 0 0
        SFNode   [in,out] body1               NULL   [RigidBody]
        SFNode   [in,out] body2               NULL   [RigidBody]
        MFString [in,out] forceOutput         "NONE" ["ALL","NONE",...]
        SFFloat  [in,out] maxAngle            π
        SFNode   [in,out] metadata            NULL   [X3DMetadataObject]
        SFFloat  [in,out] minAngle            -π
        SFFloat  [in,out] stopBounce          0      [0,1]
        SFFloat  [in,out] stopErrorCorrection 0.8    [0,1]
        SFFloat  [out]    angle
        SFFloat  [out]    angleRate
        SFVec3f  [out]    body1AnchorPoint
        SFVec3f  [out]    body2AnchorPoint
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            anchorPoint=[0.0, 0.0, 0.0],
            axis=[0.0, 0.0, 0.0],
            body1=None,
            body2=None,
            forceOutput=["NONE"],
            maxAngle=math.pi,
            minAngle=-math.pi,
            stopBounce=0.0,
            stopErrorCorrection=0.8,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            forceOutput=forceOutput,
            **kwargs
        )
        self.anchorPoint = anchorPoint
        self.axis = axis
        self.body1 = body1
        self.body2 = body2
        self.maxAngle = maxAngle
        self.minAngle = minAngle
        self.stopBounce = stopBounce
        self.stopErrorCorrection = stopErrorCorrection

    @property
    def anchorPoint(self):
        return self.__anchorPoint

    @anchorPoint.setter
    def anchorPoint(self, anchorPoint):
        if anchorPoint is None:
            anchorPoint = [0.0, 0.0, 0.0]
        assertSFVec3f(anchorPoint)
        self.__anchorPoint = anchorPoint

    @property
    def axis(self):
        return self.__axis

    @axis.setter
    def axis(self, axis):
        if axis is None:
            axis = [0.0, 0.0, 0.0]
        assertSFVec3f(axis)
        self.__axis = axis

    @property
    def body1(self):
        return self.__body1

    @body1.setter
    def body1(self, body1):
        if body1 is None:
            body1 = None
        assertSFNode(body1, RigidBody)
        self.__body1 = body1

    @property
    def body2(self):
        return self.__body2

    @body2.setter
    def body2(self, body2):
        if body2 is None:
            body2 = None
        assertSFNode(body2, RigidBody)
        self.__body2 = body2

    @property
    def maxAngle(self):
        return self.__maxAngle

    @maxAngle.setter
    def maxAngle(self, maxAngle):
        if maxAngle is None:
            maxAngle = math.pi
        assertSFFloat(maxAngle)
        self.__maxAngle = maxAngle

    @property
    def minAngle(self):
        return self.__minAngle

    @minAngle.setter
    def minAngle(self, minAngle):
        if minAngle is None:
            minAngle = -math.pi
        assertSFFloat(minAngle)
        self.__minAngle = minAngle

    @property
    def stopBounce(self):
        return self.__stopBounce

    @stopBounce.setter
    def stopBounce(self, stopBounce):
        if stopBounce is None:
            stopBounce = 0.0
        assertSFFloat(stopBounce)
        assertValidGreaterThanEquals(stopBounce, 0)
        assertValidLessThanEquals(stopBounce, 1)
        self.__stopBounce = stopBounce

    @property
    def stopErrorCorrection(self):
        return self.__stopErrorCorrection

    @stopErrorCorrection.setter
    def stopErrorCorrection(self, stopErrorCorrection):
        if stopErrorCorrection is None:
            stopErrorCorrection = 0.8
        assertSFFloat(stopErrorCorrection)
        assertValidGreaterThanEquals(stopErrorCorrection, 0)
        assertValidLessThanEquals(stopErrorCorrection, 1)
        self.__stopErrorCorrection = stopErrorCorrection

class SliderJoint(X3DRigidJointNode):
    """
    SliderJoint : X3DRigidJointNode {
        SFVec3f  [in,out] axis                0 1 0
        SFNode   [in,out] body1               NULL   [RigidBody]
        SFNode   [in,out] body2               NULL   [RigidBody]
        MFString [in,out] forceOutput         "NONE" ["ALL","NONE",...]
        SFFloat  [in,out] maxSeparation       1      [0,∞)
        SFNode   [in,out] metadata            NULL   [X3DMetadataObject]
        SFFloat  [in,out] minSeparation       0      [0,∞)
        SFFloat  [in,out] sliderForce         0      [-∞,∞)
        SFFloat  [in,out] stopBounce          0      [0,1]
        SFFloat  [in,out] stopErrorCorrection 1      [0,1]
        SFFloat  [out]    separation
        SFFloat  [out]    separationRate
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            axis=[0.0, 0.1, 0.0],
            body1=None,
            body2=None,
            forceOutput=["NONE"],
            maxSeparation=1.0,
            minSeparation=0.0,
            sliderForce=0.0,
            stopBounce=0.0,
            stopErrorCorrection=1.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            forceOutput=forceOutput,
            **kwargs
        )
        self.axis = axis
        self.body1 = body1
        self.body2 = body2
        self.maxSeparation = maxSeparation
        self.minSeparation = minSeparation
        self.sliderForce = sliderForce
        self.stopBounce = stopBounce
        self.stopErrorCorrection = stopErrorCorrection

    @property
    def axis(self):
        return self.__axis

    @axis.setter
    def axis(self, axis):
        if axis is None:
            axis = [0.0, 0.1, 0.0]
        assertSFVec3f(axis)
        self.__axis = axis

    @property
    def body1(self):
        return self.__body1

    @body1.setter
    def body1(self, body1):
        if body1 is None:
            body1 = None
        assertSFNode(body1, RigidBody)
        self.__body1 = body1

    @property
    def body2(self):
        return self.__body2

    @body2.setter
    def body2(self, body2):
        if body2 is None:
            body2 = None
        assertSFNode(body2, RigidBody)
        self.__body2 = body2

    @property
    def maxSeparation(self):
        return self.__maxSeparation

    @maxSeparation.setter
    def maxSeparation(self, maxSeparation):
        if maxSeparation is None:
            maxSeparation = 1.0
        assertSFFloat(maxSeparation)
        assertValidGreaterThanEquals(maxSeparation, 0.0)
        self.__maxSeparation = maxSeparation

    @property
    def minSeparation(self):
        return self.__minSeparation

    @minSeparation.setter
    def minSeparation(self, minSeparation):
        if minSeparation is None:
            minSeparation = 0.0
        assertSFFloat(minSeparation)
        assertValidGreaterThanEquals(minSeparation, 0.0)
        self.__minSeparation = minSeparation

    @property
    def sliderForce(self):
        return self.__sliderForce

    @sliderForce.setter
    def sliderForce(self, sliderForce):
        if sliderForce is None:
            sliderForce = 0.0
        assertSFFloat(sliderForce)
        self.__sliderForce = sliderForce

    @property
    def stopBounce(self):
        return self.__stopBounce

    @stopBounce.setter
    def stopBounce(self, stopBounce):
        if stopBounce is None:
            stopBounce = 0.0
        assertSFFloat(stopBounce)
        assertValidGreaterThanEquals(stopBounce, 0)
        assertValidLessThanEquals(stopBounce, 1)
        self.__stopBounce = stopBounce

    @property
    def stopErrorCorrection(self):
        return self.__stopErrorCorrection

    @stopErrorCorrection.setter
    def stopErrorCorrection(self, stopErrorCorrection):
        if stopErrorCorrection is None:
            stopErrorCorrection = 1.0
        assertSFFloat(stopErrorCorrection)
        assertValidGreaterThanEquals(stopErrorCorrection, 0)
        assertValidLessThanEquals(stopErrorCorrection, 1)
        self.__stopErrorCorrection 

class UniversalJoint(X3DRigidJointNode):
    """
    UniversalJoint : X3DRigidJointNode {
        SFVec3f  [in,out] anchorPoint          0 0 0
        SFVec3f  [in,out] axis1                0 0 0
        SFVec3f  [in,out] axis2                0 0 0
        SFNode   [in,out] body1                NULL   [RigidBody]
        SFNode   [in,out] body2                NULL   [RigidBody]
        SFNode   [in,out] metadata             NULL   [X3DMetadataObject]
        MFString [in,out] forceOutput          "NONE" ["ALL","NONE",...]
        SFFloat  [in,out] stopBounce1          0      [0,1]
        SFFloat  [in,out] stop1ErrorCorrection 0.8    [0,1]
        SFFloat  [in,out] stop2Bounce          0      [0,1]
        SFFloat  [in,out] stop2ErrorCorrection 0.8    [0,1]
        SFVec3f  [out]    body1AnchorPoint
        SFVec3f  [out]    body1Axis
        SFVec3f  [out]    body2AnchorPoint
        SFVec3f  [out]    body2Axis
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            anchorPoint=[0.0, 0.0, 0.0],
            axis1=[0.0, 0.0, 0.0],
            axis2=[0.0, 0.0, 0.0],
            body1=None,
            body2=None,
            forceOutput=["NONE"],
            stop1Bounce=0.0,
            stop1ErrorCorrection=0.8,
            stop2Bounce=0.0,
            stop2ErrorCorrection=0.8,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            forceOutput=forceOutput,
            **kwargs
        )
        self.anchorPoint = anchorPoint
        self.axis1 = axis1
        self.axis2 = axis2
        self.body1 = body1
        self.body2 = body2
        self.stop1Bounce = stop1Bounce
        self.stop1ErrorCorrection = stop1ErrorCorrection
        self.stop2Bounce = stop2Bounce
        self.stop2ErrorCorrection = stop2ErrorCorrection

    @property
    def anchorPoint(self):
        return self.__anchorPoint

    @anchorPoint.setter
    def anchorPoint(self, anchorPoint):
        if anchorPoint is None:
            anchorPoint = [0.0, 0.0, 0.0]
        assertSFVec3f(anchorPoint)
        self.__anchorPoint = anchorPoint

    @property
    def axis1(self):
        return self.__axis1

    @axis1.setter
    def axis1(self, axis1):
        if axis1 is None:
            axis1 = [0.0, 0.0, 0.0]
        assertSFVec3f(axis1)
        self.__axis1 = axis1

    @property
    def axis2(self):
        return self.__axis2

    @axis2.setter
    def axis2(self, axis2):
        if axis2 is None:
            axis2 = [0.0, 0.0, 0.0]
        assertSFVec3f(axis2)
        self.__axis2 = axis2
    
    @property
    def body1(self):
        return self.__body1

    @body1.setter
    def body1(self, body1):
        if body1 is None:
            body1 = None
        assertSFNode(body1, RigidBody)
        self.__body1 = body1

    @property
    def body2(self):
        return self.__body2

    @body2.setter
    def body2(self, body2):
        if body2 is None:
            body2 = None
        assertSFNode(body2, RigidBody)
        self.__body2 = body2
        
    @property
    def stop1Bounce(self):
        return self.__stop1Bounce

    @stop1Bounce.setter
    def stop1Bounce(self, stop1Bounce):
        if stop1Bounce is None:
            stop1Bounce = 0.0
        assertSFFloat(stop1Bounce)
        assertValidGreaterThanEquals(stop1Bounce, 0)
        assertValidLessThanEquals(stop1Bounce, 1)
        self.__stop1Bounce = stop1Bounce
    
    @property
    def stop1ErrorCorrection(self):
        return self.__stop1ErrorCorrection

    @stop1ErrorCorrection.setter
    def stop1ErrorCorrection(self, stop1ErrorCorrection):
        if stop1ErrorCorrection is None:
            stop1ErrorCorrection = 0.8
        assertSFFloat(stop1ErrorCorrection)
        assertValidGreaterThanEquals(stop1ErrorCorrection, 0)
        assertValidLessThanEquals(stop1ErrorCorrection, 1)
        self.__stop1ErrorCorrection = stop1ErrorCorrection

    @property
    def stop2Bounce(self):
        return self.__stop2Bounce

    @stop2Bounce.setter
    def stop2Bounce(self, stop2Bounce):
        if stop2Bounce is None:
            stop2Bounce = 0.0
        assertSFFloat(stop2Bounce)
        assertValidGreaterThanEquals(stop2Bounce, 0)
        assertValidLessThanEquals(stop2Bounce, 1)
        self.__stop2Bounce = stop2Bounce

    @property
    def stop2ErrorCorrection(self):
        return self.__stop2ErrorCorrection

    @stop2ErrorCorrection.setter
    def stop2ErrorCorrection(self, stop2ErrorCorrection):
        if stop2ErrorCorrection is None:
            stop2ErrorCorrection = 0.8
        assertSFFloat(stop2ErrorCorrection)
        assertValidGreaterThanEquals(stop2ErrorCorrection, 0)
        assertValidLessThanEquals(stop2ErrorCorrection, 1)
        self.__stop2ErrorCorrection = stop2ErrorCorrection

class BlendedVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    BlendedVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFBool   [in,out] enabled                 TRUE
        SFNode   [in,out] metadata                NULL       [X3DMetadataObject]
        SFNode   [in,out] renderStyle             NULL       [X3DComposableVolumeRenderStyleNode]
        SFNode   [in,out] voxels                  NULL       [X3DTexture3DNode]         
        SFFloat  [in,out] weightConstant1         0.5        [0,1]
        SFFloat  [in,out] weightConstant2         0.5        [0,1]
        SFString [in,out] weightFunction1         "CONSTANT" ["CONSTANT", "ALPHA0", "ALPHA1", "TABLE",
                                                                "ONE_MINUS_ALPHA0", "ONE_MINUS_ALPHA1" ] 
        SFString [in,out] weightFunction2         "CONSTANT" ["CONSTANT", "ALPHA0", "ALPHA1", "TABLE",
                                                                "ONE_MINUS_ALPHA0", "ONE_MINUS_ALPHA1" ] 
        SFNode   [in,out] weightTransferFunction1 NULL       [X3DTexture2DNode]
        SFNode   [in,out] weightTransferFunction2 NULL       [X3DTexture2DNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            renderStyle=None,
            voxels=None,
            weightConstant1=0.5,
            weightConstant2=0.5,
            weightFunction1="CONSTANT",
            weightFunction2="CONSTANT",
            weightTransferFunction1=None,
            weightTransferFunction2=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.renderStyle = renderStyle
        self.voxels = voxels
        self.weightConstant1 = weightConstant1
        self.weightConstant2 = weightConstant2
        self.weightFunction1 = weightFunction1
        self.weightFunction2 = weightFunction2
        self.weightTransferFunction1 = weightTransferFunction1
        self.weightTransferFunction2 = weightTransferFunction2

    @property
    def renderStyle(self):
        return self.__renderStyle

    @renderStyle.setter
    def renderStyle(self, renderStyle):
        if renderStyle is None:
            renderStyle = None
        assertSFNode(renderStyle, X3DComposableVolumeRenderStyle)
        self.__renderStyle = renderStyle

    @property
    def voxels(self):
        return self.__voxels

    @voxels.setter
    def voxels(self, voxels):
        if voxels is None:
            voxels = None
        assertSFNode(voxels, X3DTexture3DNode)
        self.__voxels = voxels

    @property
    def weightConstant1(self):
        return self.__weightConstant1

    @weightConstant1.setter
    def weightConstant1(self, weightConstant1):
        if weightConstant1 is None:
            weightConstant1 = 0.5
        assertSFFloat(weightConstant1)
        assertValidGreaterThanEquals(weightConstant1, 0)
        assertValidLessThanEquals(weightConstant1, 1)
        self.__weightConstant1 = weightConstant1

    @property
    def weightConstant2(self):
        return self.__weightConstant2

    @weightConstant2.setter
    def weightConstant2(self, weightConstant2):
        if weightConstant2 is None:
            weightConstant2 = 0.5
        assertSFFloat(weightConstant2)
        assertValidGreaterThanEquals(weightConstant2, 0)
        assertValidLessThanEquals(weightConstant2, 1)
        self.__weightConstant2 = weightConstant2

    @property
    def weightFunction1(self):
        return self.__weightFunction1

    @weightFunction1.setter
    def weightFunction1(self, weightFunction1):
        if weightFunction1 is None:
            weightFunction1 = "CONSTANT"
        assertValidWeightFunctionType(weightFunction1)
        self.__weightFunction1 = weightFunction1

    @property
    def weightFunction2(self):
        return self.__weightFunction2

    @weightFunction2.setter
    def weightFunction2(self, weightFunction2):
        if weightFunction2 is None:
            weightFunction2 = "CONSTANT"
        assertValidWeightFunctionType(weightFunction2)
        self.__weightFunction2 = weightFunction2

    @property
    def weightTransferFunction1(self):
        return self.__weightTransferFunction1

    @weightTransferFunction1.setter
    def weightTransferFunction1(self, weightTransferFunction1):
        if weightTransferFunction1 is None:
            weightTransferFunction1 = None
        assertSFNode(weightTransferFunction1, X3DTexture2DNode)
        self.__weightTransferFunction1 = weightTransferFunction1

    @property
    def weightTransferFunction2(self):
        return self.__weightTransferFunction2

    @weightTransferFunction2.setter
    def weightTransferFunction2(self, weightTransferFunction2):
        if weightTransferFunction2 is None:
            weightTransferFunction2 = None
        assertSFNode(weightTransferFunction2, X3DTexture2DNode)
        self.__weightTransferFunction2 = weightTransferFunction2

class BoundaryEnhancementVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    BoundaryEnhancementVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFFloat     [in,out] boundaryOpacity  0.9     [0,1]
        SFBool      [in,out] enabled          TRUE
        SFNode      [in,out] metadata         NULL    [X3DMetadataObject]
        SFFloat     [in,out] opacityFactor    2       [0,∞)
        SFFloat     [in,out] retainedOpacity  0.2     [0,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            boundaryOpacity=0.9,
            opacityFactor=2.0,
            retainedOpacity=0.2,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.boundaryOpacity = boundaryOpacity
        self.opacityFactor = opacityFactor
        self.retainedOpacity = retainedOpacity

    @property
    def boundaryOpacity(self):
        return self.__boundaryOpacity

    @boundaryOpacity.setter
    def boundaryOpacity(self, boundaryOpacity):
        if boundaryOpacity is None:
            boundaryOpacity = 0.9
        assertSFFloat(boundaryOpacity)
        assertValidGreaterThanEquals(boundaryOpacity, 0)
        assertValidLessThanEquals(boundaryOpacity, 1)
        self.__boundaryOpacity = boundaryOpacity

    @property
    def opacityFactor(self):
        return self.__opacityFactor

    @opacityFactor.setter
    def opacityFactor(self, opacityFactor):
        if opacityFactor is None:
            opacityFactor = 2.0
        assertSFFloat(opacityFactor)
        assertValidGreaterThanEquals(opacityFactor, 0)
        self.__opacityFactor = opacityFactor

    @property
    def retainedOpacity(self):
        return self.__retainedOpacity

    @retainedOpacity.setter
    def retainedOpacity(self, retainedOpacity):
        if retainedOpacity is None:
            retainedOpacity = 0.2
        assertSFFloat(retainedOpacity)
        assertValidGreaterThanEquals(retainedOpacity, 0)
        assertValidLessThanEquals(retainedOpacity, 1)
        self.__retainedOpacity = retainedOpacity

class CartoonVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    CartoonVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFInt32     [in,out] colorSteps       4       [1,64]
        SFBool      [in,out] enabled          TRUE
        SFNode      [in,out] metadata         NULL    [X3DMetadataObject]
        SFColorRGBA [in,out] orthogonalColor  1 1 1 1 [0,1]
        SFColorRGBA [in,out] parallelColor    0 0 0 1 [0,1]
        SFNode      [in,out] surfaceNormals   NULL    [X3DTexture3DNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            colorSteps=4,
            orthogonalColor=[1.0, 1.0, 1.0, 1.0],
            parallelColor=[0.0, 0.0, 0.0, 1.0],
            surfaceNormals=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.colorSteps = colorSteps
        self.orthogonalColor = orthogonalColor
        self.parallelColor = parallelColor
        self.surfaceNormals = surfaceNormals

    @property
    def colorSteps(self):
        return self.__colorSteps

    @colorSteps.setter
    def colorSteps(self, colorSteps):
        if colorSteps is None:
            colorSteps = 4
        assertSFInt32(colorSteps)
        assertValidGreaterThanEquals(colorSteps, 1)
        assertValidLessThanEquals(colorSteps, 64)
        self.__colorSteps = colorSteps

    @property
    def orthogonalColor(self):
        return self.__orthogonalColor

    @orthogonalColor.setter
    def orthogonalColor(self, orthogonalColor):
        if orthogonalColor is None:
            orthogonalColor = [1.0, 1.0, 1.0, 1.0]
        assertSFColorRGBA(orthogonalColor)
        assertValidGreaterThanEquals(orthogonalColor, 0)
        assertValidLessThanEquals(orthogonalColor, 1)
        self.__orthogonalColor = orthogonalColor

    @property
    def parallelColor(self):
        return self.__parallelColor

    @parallelColor.setter
    def parallelColor(self, parallelColor):
        if parallelColor is None:
            parallelColor = [0.0, 0.0, 0.0, 1.0]
        assertSFColorRGBA(parallelColor)
        assertValidGreaterThanEquals(parallelColor, 0)
        assertValidLessThanEquals(parallelColor, 1)
        self.__parallelColor = parallelColor

    @property
    def surfaceNormals(self):
        return self.__surfaceNormals

    @surfaceNormals.setter
    def surfaceNormals(self, surfaceNormals):
        if surfaceNormals is None:
            surfaceNormals = None
        assertSFNode(surfaceNormals, X3DTexture3DNode)
        self.__surfaceNormals = surfaceNormals

class ComposedVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    ComposedVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFBool [in,out] enabled     TRUE
        SFNode [in,out] metadata    NULL  [X3DMetadataObject]
        MFNode [in,out] renderStyle []    [X3DComposableVolumeRenderStyleNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            renderStyle=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            renderStyle=renderStyle,
            **kwargs
        )
        self.renderStyle = renderStyle

    @property
    def renderStyle(self):
        return self.__renderStyle

    @renderStyle.setter
    def renderStyle(self, renderStyle):
        if renderStyle is None:
            renderStyle = []
        assertMFNode(renderStyle, X3DComposableVolumeRenderStyle)
        self.__renderStyle = renderStyle

class EdgeEnhancementVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    EdgeEnhancementVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFColorRGBA [in,out] edgeColor         0 0 0 1 [0,1]
        SFBool      [in,out] enabled           TRUE
        SFFloat     [in,out] gradientThreshold 0.4     [0,π]
        SFNode      [in,out] metadata          NULL    [X3DMetadataObject]
        SFNode      [in,out] surfaceNormals    NULL    [X3DTexture3DNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            edgeColor=[0.0, 0.0, 0.0, 1.0],
            gradientThreshold=0.4,
            surfaceNormals=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.edgeColor = edgeColor
        self.gradientThreshold = gradientThreshold
        self.surfaceNormals = surfaceNormals

    @property
    def edgeColor(self):
        return self.__edgeColor

    @edgeColor.setter
    def edgeColor(self, edgeColor):
        if edgeColor is None:
            edgeColor = [0.0, 0.0, 0.0, 1.0]
        assertSFColorRGBA(edgeColor)
        assertValidGreaterThanEquals(edgeColor, 0)
        assertValidLessThanEquals(edgeColor, 1)
        self.__edgeColor = edgeColor

    @property
    def gradientThreshold(self):
        return self.__gradientThreshold

    @gradientThreshold.setter
    def gradientThreshold(self, gradientThreshold):
        if gradientThreshold is None:
            gradientThreshold = 0.4
        assertSFFloat(gradientThreshold)
        assertValidGreaterThanEquals(gradientThreshold, 0)
        assertValidLessThanEquals(gradientThreshold, math.pi)
        self.gradientThreshold = gradientThreshold

    @property
    def surfaceNormals(self):
        return self.__surfaceNormals

    @surfaceNormals.setter
    def surfaceNormals(self, surfaceNormals):
        if surfaceNormals is None:
            surfaceNormals = None
        assertSFNode(surfaceNormals, X3DTexture3DNode)
        self.__surfaceNormals = surfaceNormals

class OpacityMapVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    OpacityMapVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFBool [in,out] enabled          TRUE
        SFNode [in,out] metadata         NULL [X3DMetadataObject]
        SFNode [in,out] transferFunction NULL [X3DTexture2DNode,X3DTexture3DNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            transferFunction=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.transferFunction = transferFunction

    @property
    def transferFunction(self):
        return self.__transferFunction

    @transferFunction.setter
    def transferFunction(self, transferFunction):
        if transferFunction is None:
            transferFunction = None
        assertSFNode(transferFunction, X3DTexture2DNode, X3DTexture3DNode)
        self.transferFunction = transferFunction

class ProjectionVolumeStyle(X3DVolumeRenderStyleNode):
    """
    ProjectionVolumeStyle : X3DVolumeRenderStyleNode {
        SFBool   [in,out] enabled            TRUE
        SFNode   [in,out] metadata           NULL  [X3DMetadataObject]
        SFFloat  [in,out] intensityThreshold 0     [0,1]
        SFString [in,put] type               "MAX" ["MAX", "MIN", "AVERAGE"]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            intensityThreshold=0.0,
            type_="MAX",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.intensityThreshold = intensityThreshold
        self.type_ = type_

    @property
    def intensityThreshold(self):
        return self.__intensityThreshold

    @intensityThreshold.setter
    def intensityThreshold(self, intensityThreshold):
        if intensityThreshold is None:
            intensityThreshold = 0.0
        assertSFFloat(intensityThreshold)
        assertValidGreaterThanEquals(intensityThreshold, 0)
        assertValidLessThanEquals(intensityThreshold, 1)
        self.intensityThreshold = intensityThreshold

    @property
    def type_(self):
        return self.__type_

    @type_.setter
    def type_(self, type_):
        if type_ is None:
            type_ = "MAX"
        assertValidProjectionVolumeStypeType(type_)
        self.type_ = type_

class ShadedVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    ShadedVolumeStyle : X3DComposableVolumeRenderStyleNode {
        SFBool   [in,out] enabled        TRUE
        SFBool   [in,out] lighting       FALSE
        SFNode   [in,out] material       NULL                [X3DMaterialNode]
        SFNode   [in,out] metadata       NULL                [X3DMetadataObject]
        SFBool   [in,out] shadows        FALSE
        SFNode   [in,out] surfaceNormals NULL                [X3DTexture3DNode]
        SFString []       phaseFunction  "Henyey-Greenstein" ["Henyey-Greenstein","NONE",...]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            lighting=False,
            shadows=False,
            surfaceNormals=None,
            phaseFunction="Henyey-Greenstein",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.lighting = lighting
        self.shadows = shadows
        self.surfaceNormals = surfaceNormals
        self.phaseFunction = phaseFunction

    @property
    def lighting(self):
        return self.__lighting

    @lighting.setter
    def lighting(self, lighting):
        if lighting is None:
            lighting = False
        assertSFBool(lighting)
        self.__lighting = lighting

    @property
    def shadows(self):
        return self.__shadows

    @shadows.setter
    def shadows(self, shadows):
        if shadows is None:
            shadows = False
        assertSFBool(shadows)
        self.__shadows = shadows

    @property
    def surfaceNormals(self):
        return self.__surfaceNormals

    @surfaceNormals.setter
    def surfaceNormals(self, surfaceNormals):
        if surfaceNormals is None:
            surfaceNormals = None
        assertSFNode(surfaceNormals, X3DTexture3DNode)
        self.__surfaceNormals = surfaceNormals

    @property
    def phaseFunction(self):
        return self.__phaseFunction

    @phaseFunction.setter
    def phaseFunction(self, phaseFunction):
        if phaseFunction is None:
            phaseFunction = "Henyey-Greenstein"
        assertValidPhaseFunction(phaseFunction)
        self.__phaseFunction = phaseFunction

class SilhouetteEnhancementVolumeStyle(X3DComposableVolumeRenderStyleNode):
    """
    SilhouetteEnhancementVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFBool  [in,out] enabled                   TRUE
        SFNode  [in,out] metadata                  NULL [X3DMetadataObject]
        SFFloat [in,out] silhouetteBoundaryOpacity 0    [0,1]
        SFFloat [in,out] silhouetteRetainedOpacity 1    [0,1]
        SFFloat [in,out] silhouetteSharpness       0.5  [0,∞)
        SFNode  [in,out] surfaceNormals            NULL [X3DTexture3DNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            silhouetteBoundaryOpacity=0.0,
            silhouetteRetainedOpacity=1.0,
            silhouetteSharpness=0.5,
            surfaceNormals=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.silhouetteBoundaryOpacity = silhouetteBoundaryOpacity
        self.silhouetteRetainedOpacity = silhouetteRetainedOpacity
        self.silhouetteSharpness = silhouetteSharpness
        self.surfaceNormals = surfaceNormals

    @property
    def silhouetteBoundaryOpacity(self):
        return self.__silhouetteBoundaryOpacity

    @silhouetteBoundaryOpacity.setter
    def silhouetteBoundaryOpacity(self, silhouetteBoundaryOpacity):
        if silhouetteBoundaryOpacity is None:
            silhouetteBoundaryOpacity = 0.0
        assertSFNode(silhouetteBoundaryOpacity)
        assertValidGreaterThanEquals(silhouetteBoundaryOpacity, 0)
        assertValidLessThanEquals(silhouetteBoundaryOpacity, 1)
        self.__silhouetteBoundaryOpacity = silhouetteBoundaryOpacity

    @property
    def silhouetteRetainedOpacity(self):
        return self.__silhouetteRetainedOpacity

    @silhouetteRetainedOpacity.setter
    def silhouetteRetainedOpacity(self, silhouetteRetainedOpacity):
        if silhouetteRetainedOpacity is None:
            silhouetteRetainedOpacity = 1.0
        assertSFFloat(silhouetteRetainedOpacity)
        assertValidGreaterThanEquals(silhouetteRetainedOpacity, 0)
        assertValidLessThanEquals(silhouetteRetainedOpacity, 1)
        self.__silhouetteRetainedOpacity = silhouetteRetainedOpacity

    @property
    def silhouetteSharpness(self):
        return self.__silhouetteSharpness

    @silhouetteSharpness.setter
    def silhouetteSharpness(self, silhouetteSharpness):
        if silhouetteSharpness is None:
            silhouetteSharpness = 0.5
        assertSFFloat(silhouetteSharpness)
        assertValidGreaterThanEquals(silhouetteSharpness, 0)
        self.__silhouetteSharpness = silhouetteSharpness

    @property
    def surfaceNormals(self):
        return self.__surfaceNormals

    @surfaceNormals.setter
    def surfaceNormals(self, surfaceNormals):
        if surfaceNormals is None:
            surfaceNormals = None
        assertSFNode(surfaceNormals, X3DTexture3DNode)
        self.__surfaceNormals = surfaceNormals

class ToneMappedVolumeStyle(X3DComposableVolumeRenderStyleNode): 
    """
    ToneMappedVolumeStyle : X3DComposableVolumeRenderStyleNode { 
        SFColorRGBA [in,out] coolColor      0 0 1 0 [0,1]
        SFBool      [in,out] enabled        TRUE
        SFNode      [in,out] metadata       NULL    [X3DMetadataObject]
        SFNode      [in,out] surfaceNormals NULL    [X3DTexture3DNode]
        SFColorRGBA [in,out] warmColor      1 1 0 0 [0,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            coolColor=[0.0, 0.0, 1.0, 0.0],
            surfaceNormals=None,
            warmColor=[1.0, 1.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.coolColor = coolColor
        self.surfaceNormals = surfaceNormals
        self.warmColor = warmColor

    @property
    def coolColor(self):
        return self.__coolColor

    @coolColor.setter
    def coolColor(self, coolColor):
        if coolColor is None:
            coolColor = [0.0, 0.0, 1.0, 0.0]
        assertSFColorRGBA(coolColor)
        assertValidGreaterThanEquals(coolColor, 0)
        assertValidLessThanEquals(coolColor, 1)
        self.__coolColor = coolColor

    @property
    def surfaceNormals(self):
        return self.__surfaceNormals

    @surfaceNormals.setter
    def surfaceNormals(self, surfaceNormals):
        if surfaceNormals is None:
            surfaceNormals = None
        assertSFNode(surfaceNormals, X3DTexture3DNode)
        self.__surfaceNormals = surfaceNormals

    @property
    def warmColor(self):
        return self.__warmColor

    @warmColor.setter
    def warmColor(self, warmColor):
        if warmColor is None:
            warmColor = [1.0, 1.0, 0.0, 0.0]
        assertSFColorRGBA(warmColor)
        assertValidGreaterThanEquals(warmColor, 0)
        assertValidLessThanEquals(warmColor, 1)
        self.__warmColor = warmColor

class BooleanFilter(X3DChildNode):
    """
    BooleanFilter : X3DChildNode {
        SFBool [in]     set_boolean
        SFNode [in,out] metadata    NULL [X3DMetadataObject]
        SFBool [out]    inputFalse
        SFBool [out]    inputNegate
        SFBool [out]    inputTrue
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )

class BooleanToggle(X3DChildNode):
    """
    BooleanToggle : X3DChildNode {
        SFBool [in]     set_boolean
        SFNode [in,out] metadata    NULL  [X3DMetadataObject]
        SFBool [in,out] toggle      FALSE 
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            toggle=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.toggle = toggle

    @property
    def toggle(self):
        return self.__toggle

    @toggle.setter
    def toggle(self, toggle):
        if toggle is None:
            toggle = False
        assertSFBool(toggle)
        self.__toggle = toggle

class ClipPlane(X3DChildNode): 
    """
    ClipPlane : X3DChildNode { 
        SFBool  [in,out] enabled  TRUE
        SFNode  [in,out] metadata NULL    [X3DMetadataObject]
        SFVec4f [in,out] plane    0 1 0 0 [0,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            plane=[0, 1, 0, 0],
            **kwargs    
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.enabled = enabled
        self.plane = plane

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

    @property
    def plane(self):
        return self.__plane

    @plane.setter
    def plane(self, plane):
        if plane is None:
            plane = [0.0, 1.0, 0.0, 0.0]
        assertSFVec4f(plane)
        assertValidGreaterThanEquals(plane, 0)
        assertValidLessThanEquals(plane, 1)
        self.__plane = plane

class CollisionCollection(X3DChildNode):
    """
    CollisionCollection : X3DChildNode {
        MFString [in,out] appliedParameters        "BOUNCE"
        SFFloat  [in,out] bounce                   0        [0,1]
        MFNode   [in,out] collidables              NULL     [X3DNBodyCollisionSpaceNode,
                                                            X3DNBodyCollidableNode]
        SFBool   [in,out] enabled                  TRUE
        SFVec2f  [in,out] frictionCoefficients     0 0      [0,∞)
        SFNode   [in,out] metadata                 NULL     [X3DMetadataObject]
        SFFloat  [in,out] minBounceSpeed           0.1      [0,∞)
        SFVec2f  [in,out] slipFactors	             0 0      (-∞,∞)
        SFFloat  [in,out] softnessConstantForceMix 0.0001   [0,1]
        SFFloat  [in,out] softnessErrorCorrection  0.8      [0,1]
        SFVec2f  [in,out] surfaceSpeed             0 0      (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            appliedParameters=["BOUNCE"],
            bounce=0.0,
            collidables=[],
            enabled=True,
            frictionCoefficients=[0.0, 0.0],
            minBounceSpeed=0.1,
            slipFactors=[0.0, 0.0],
            softnessConstantForceMix=0.0001,
            softnessErrorCorrection=0.8,
            surfaceSpeed=[0.0, 0.0], 
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.appliedParameters = appliedParameters
        self.bounce = bounce
        self.collidables = collidables
        self.enabled = enabled
        self.frictionCoefficients = frictionCoefficients
        self.minBounceSpeed = minBounceSpeed
        self.slipFactors = slipFactors
        self.softnessConstantForceMix = softnessConstantForceMix
        self.softnessErrorCorrection = softnessErrorCorrection
        self.surfaceSpeed = surfaceSpeed

    @property
    def appliedParameters(self):
        return self.__appliedParameters

    @appliedParameters.setter
    def appliedParameters(self, appliedParameters):
        if appliedParameters is None:
            appliedParameters = ["BOUNCE"]
        assertValidCollisionAppliedParameters(appliedParameters)
        self.__appliedParameters = appliedParameters

    @property
    def bounce(self):
        return self.__bounce

    @bounce.setter
    def bounce(self, bounce):
        if bounce is None:
            bounce = 0.0
        assertSFFloat(bounce)
        assertValidGreaterThanEquals(bounce, 0)
        assertValidLessThanEquals(bounce, 1)
        self.__bounce = bounce

    @property
    def collidables(self):
        return self.__collidables

    @collidables.setter
    def collidables(self, collidables):
        if collidables is None:
            collidables = [None]
        assertSFNode(collidables, X3DNBodyCollisionSpaceNode, X3DNBodyCollidableNode)
        self.__collidables = collidables

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

    @property
    def frictionCoefficients(self):
        return self.__frictionCoefficients

    @frictionCoefficients.setter
    def frictionCoefficients(self, frictionCoefficients):
        if frictionCoefficients is None:
            frictionCoefficients = [0.0, 0.0]
        assertSFVec2f(frictionCoefficients)
        assertValidGreaterThanEquals(frictionCoefficients, 0)
        self.__frictionCoefficients = frictionCoefficients

    @property
    def minBounceSpeed(self):
        return self.__minBounceSpeed

    @minBounceSpeed.setter
    def minBounceSpeed(self, minBounceSpeed):
        if minBounceSpeed is None:
            minBounceSpeed = [0.0, 0.0]
        assertSFFloat(minBounceSpeed)
        assertValidGreaterThanEquals(minBounceSpeed, 0)
        self.__minBounceSpeed = minBounceSpeed

    @property
    def slipFactors(self):
        return self.__slipFactors

    @slipFactors.setter
    def slipFactors(self, slipFactors):
        if slipFactors is None:
            slipFactors = [0.0, 0.0]
        assertSFVec2f(slipFactors)
        self.__slipFactors = slipFactors
    
    @property
    def softnessConstantForceMix(self):
        return self.__softnessConstantForceMix

    @softnessConstantForceMix.setter
    def softnessConstantForceMix(self, softnessConstantForceMix):
        if softnessConstantForceMix is None:
            softnessConstantForceMix = 0.0001
        assertSFFloat(softnessConstantForceMix)
        assertValidGreaterThanEquals(softnessConstantForceMix, 0)
        assertValidLessThanEquals(softnessConstantForceMix, 1)
        self.__softnessConstantForceMix = softnessConstantForceMix

    @property
    def softnessErrorCorrection(self):
        return self.__softnessErrorCorrection

    @softnessErrorCorrection.setter
    def softnessErrorCorrection(self, softnessErrorCorrection):
        if softnessErrorCorrection is None:
            softnessErrorCorrection = 0.8
        assertSFFloat(softnessErrorCorrection)
        assertValidGreaterThanEquals(softnessErrorCorrection, 0)
        assertValidLessThanEquals(softnessErrorCorrection, 1)
        self.__softnessErrorCorrection = softnessErrorCorrection

    @property
    def surfaceSpeed(self):
        return self.__surfaceSpeed

    @surfaceSpeed.setter
    def surfaceSpeed(self, surfaceSpeed):
        if surfaceSpeed is None:
            surfaceSpeed = [0.0, 0.0]
        assertSFVec2f(surfaceSpeed)
        self.__surfaceSpeed = surfaceSpeed

class DISEntityManager(X3DChildNode):
    """
    DISEntityManager : X3DChildNode {
        SFString [in,out] address         "localhost"
        SFInt32  [in,out] applicationID   1           [0,65535]
        MFNode   [in,out] mapping         []          [DISEntityTypeMapping]
        SFNode   [in,out] metadata        NULL        [X3DMetadataObject]
        SFInt32  [in,out] port            0           [0,65535]
        SFInt32  [in,out] siteID          0           [0,65535]
        MFNode   [out]    addedEntities
        MFNode   [out]    removedEntities
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            address="localhost",
            applicationID=1,
            mapping=[],
            port=0,
            siteID=0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.address = address
        self.applicationID = applicationID
        self.mapping = mapping
        self.port = port
        self.siteID = siteID

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if address is None:
            address = "localhost"
        assertSFString(address)
        self.__address = address

    @property
    def applicationID(self):
        return self.__applicationID

    @applicationID.setter
    def applicationID(self, applicationID):
        if applicationID is None:
            applicationID = 1
        assertSFInt32(applicationID)
        assertValidGreaterThanEquals(applicationID, 0)
        assertValidLessThanEquals(applicationID, 65535)
        self.__applicationID = applicationID

    @property
    def mapping(self):
        return self.__mapping

    @mapping.setter
    def mapping(self, mapping):
        if mapping is None:
            mapping = []
        assertMFNode(mapping, DISEntityTypeMapping)
        self.__mapping = mapping

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if port is None:
            port = 0
        assertSFInt32(port)
        assertValidGreaterThanEquals(port, 0)
        assertValidLessThanEquals(port, 65535)
        self.__port = port

    @property
    def siteID(self):
        return self.__siteID

    @siteID.setter
    def siteID(self, siteID):
        if siteID is None:
            siteID = 0
        assertSFInt32(siteID)
        assertValidGreaterThanEquals(siteID, 0)
        assertValidLessThanEquals(siteID, 65535)
        self.__siteID = siteID

class GeoLOD(X3DChildNode, X3DBoundedObject):
    """
    GeoLOD : X3DChildNode, X3DBoundedObject {
        SFNode   [in,out] metadata       NULL        [X3DMetadataObject]
        MFNode   [out]    children                   [X3DChildNode]
        SFInt32  [out]    level_changed
        SFVec3d  []       center         0 0 0       (-∞,∞)
        MFString []       child1Url      []          [URI]
        MFString []       child2Url      []          [URI]
        MFString []       child3Url      []          [URI]
        MFString []       child4Url      []          [URI]
        SFNode   []       geoOrigin      NULL        [GeoOrigin] (deprecated)
        MFString []       geoSystem      ["GD","WE"] [see 25.2.3]
        SFFloat  []       range          10          [0,∞)
        MFString []       rootUrl        []          [URI]
        MFNode   []       rootNode       []          [X3DChildNode]
        SFVec3f  []       bboxCenter     0 0 0       (-∞,∞)
        SFVec3f  []       bboxSize       -1 -1 -1    [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            child1Url=[],
            child2Url=[],
            child3Url=[],
            child4Url=[],
            geoOrigin=None,
            geoSystem=["GD", "WE"],
            range_=10.0,
            rootUrl=[],
            rootNode=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.center = center
        self.child1Url = child1Url
        self.child2Url = child2Url
        self.child3Url = child3Url
        self.child4Url = child4Url
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem
        self.range_ = range_
        self.rootUrl = rootUrl
        self.rootNode = rootNode

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3d(center)
        self.__center = center

    @property
    def child1Url(self):
        return self.__child1Url

    @child1Url.setter
    def child1Url(self, child1Url):
        if child1Url is None:
            child1Url = []
        assertMFString(child1Url)
        self.__child1Url = child1Url

    @property
    def child2Url(self):
        return self.__child2Url

    @child2Url.setter
    def child2Url(self, child2Url):
        if child2Url is None:
            child2Url = []
        assertMFString(child2Url)
        self.__child2Url = child2Url

    @property
    def child3Url(self):
        return self.__child3Url

    @child3Url.setter
    def child3Url(self, child3Url):
        if child3Url is None:
            child3Url = []
        assertMFString(child3Url)
        self.__child3Url = child3Url

    @property
    def child4Url(self):
        return self.__child4Url

    @child4Url.setter
    def child4Url(self, child4Url):
        if child4Url is None:
            child4Url = []
        assertMFString(child4Url)
        self.__child4Url = child4Url

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

    @property
    def range_(self):
        return self.__range_

    @range_.setter
    def range_(self, range_):
        if range_ is None:
            range_ = 10.0
        assertSFFloat(range_)
        assertValidGreaterThanEquals(range_, 0)
        self.__range_ = range_

    @property
    def rootUrl(self):
        return self.__rootUrl

    @rootUrl.setter
    def rootUrl(self, rootUrl):
        if rootUrl is None:
            rootUrl = []
        assertMFString(rootUrl)
        self.__rootUrl = rootUrl

    @property
    def rootNode(self):
        return self.__rootNode

    @rootNode.setter
    def rootNode(self, rootNode):
        if rootNode is None:
            rootNode = []
        assertSFNode(rootNode, X3DChildNode)
        self.__rootNode = rootNode

class HAnimHumanoid(X3DChildNode, X3DBoundedObject): 
    """
    HAnimHumanoid : X3DChildNode, X3DBoundedObject {
        SFVec3f    [in,out] center           0 0 0    (-∞,∞)
        MFString   [in,out] info             []
        MFNode     [in,out] joints           []       [HAnimJoint]
        SFNode     [in,out] metadata         NULL     [X3DMetadataObject]
        SFString   [in,out] name             ""
        SFRotation [in,out] rotation         0 0 1 0  (-∞,∞)|[-1,1]
        SFVec3f    [in,out] scale            1 1 1    (0,∞)
        SFRotation [in,out] scaleOrientation 0 0 1 0  (-∞,∞)|[-1,1]
        MFNode     [in,out] segments         []       [HAnimSegment]
        MFNode     [in,out] sites            []       [HAnimSite]
        MFNode     [in,out] skeleton         []       [HAnimJoint, HAnimSite]
        MFNode     [in,out] skin             []       [X3DChildNode]
        SFNode     [in,out] skinCoord        NULL     [X3DCoordinateNode]
        SFNode     [in,out] skinNormal       NULL     [X3DNormalNode]
        SFVec3f    [in,out] translation      0 0 0    (-∞,∞)
        SFString   [in,out] version          ""
        MFNode     [in,out] viewpoints       []       [HAnimSite]
        SFVec3f    []       bboxCenter       0 0 0    (-∞,∞)
        SFVec3f    []       bboxSize         -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            info=[],
            joints=[],
            name="",
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            scaleOrientation=[0.0, 0.0, 1.0, 0.0],
            segments=[],
            sites=[],
            skeleton=[],
            skin=[],
            skinCoord=None,
            skinNormal=None,
            translation=[0.0, 0.0, 0.0],
            version="",
            viewpoints=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.center = center
        self.info = info
        self.joints = joints
        self.name = name
        self.rotation = rotation
        self.scale = scale
        self.scaleOrientation = scaleOrientation
        self.segments = segments
        self.sites = sites
        self.skeleton = skeleton
        self.skin = skin
        self.skinCoord = skinCoord
        self.skinNormal = skinNormal
        self.translation = translation
        self.version = version
        self.viewpoints = viewpoints

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0, 0, 0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        if info is None:
            info = []
        assertMFString(info)
        self.__info = info

    @property
    def joints(self):
        return self.__joints

    @joints.setter
    def joints(self, joints):
        if joints is None:
            joints = []
        assertMFNode(joints, HAnimJoint)
        self.__joints = joints

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            name = ""
        assertSFString(name)
        self.__name = name

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        assertSFVec3f(scale)
        assertValidGreaterThan(scale, 0)
        self.__scale = scale

    @property
    def scaleOrientation(self):
        return self.__scaleOrientation

    @scaleOrientation.setter
    def scaleOrientation(self, scaleOrientation):
        if scaleOrientation is None:
            scaleOrientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(scaleOrientation)
        self.__scaleOrientation = scaleOrientation

    @property
    def segments(self):
        return self.__segments

    @segments.setter
    def segments(self, segments):
        if segments is None:
            segments = []
        assertMFNode(segments, HAnimSegment)
        self.__segments = segments

    @property
    def sites(self):
        return self.__sites

    @sites.setter
    def sites(self, sites):
        if sites is None:
            sites = []
        assertMFNode(sites, HAnimSite)
        self.__sites = sites

    @property
    def skeleton(self):
        return self.__skeleton

    @skeleton.setter
    def skeleton(self, skeleton):
        if skeleton is None:
            skeleton = []
        assertMFNode(skeleton, HAnimJoint, HAnimSite)
        self.__skeleton = skeleton

    @property
    def skin(self):
        return self.__skin

    @skin.setter
    def skin(self, skin):
        if skin is None:
            skin = []
        assertMFNode(skin, X3DChildNode)
        self.__skin = skin

    @property
    def skinCoord(self):
        return self.__skinCoord

    @skinCoord.setter
    def skinCoord(self, skinCoord):
        if skinCoord is None:
            skinCoord = None
        assertSFNode(skinCoord, X3DCoordinateNode)
        self.__skinCoord = skinCoord

    @property
    def skinNormal(self):
        return self.__skinNormal

    @skinNormal.setter
    def skinNormal(self, skinNormal):
        if skinNormal is None:
            skinNormal = None
        assertSFNode(skinNormal, X3DNormalNode)
        self.__skinNormal = skinNormal

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version):
        if version is None:
            version = []
        assertSFString(version)
        self.__version = version

    @property
    def viewpoints(self):
        return self.__viewpoints

    @viewpoints.setter
    def viewpoints(self, viewpoints):
        if viewpoints is None:
            viewpoints = []
        assertMFNode(viewpoints, HAnimSite)
        self.__viewpoints = viewpoints

class Inline(X3DChildNode, X3DBoundedObject, X3DUrlObject):
    """
    Inline : X3DChildNode, X3DBoundedObject, X3DUrlObject {
        SFBool   [in,out] load       TRUE
        SFNode   [in,out] metadata   NULL     [X3DMetadataObject]
        MFString [in,out] url        []       [URI]
        SFVec3f  []       bboxCenter 0 0 0    (-∞,∞)
        SFVec3f  []       bboxSize   -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            load=True,
            url=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            url=url,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.load = load

    @property
    def load(self):
        return self.__load

    @load.setter
    def load(self, load):
        if load is None:
            load = True
        assertSFBool(load)
        self.__load = load

class LocalFog(X3DChildNode, X3DFogObject):
    """
    LocalFog : X3DChildNode, X3DFogObject {
        SFColor  [in,out] color           1 1 1    [0,1]
        SFBool   [in,out] enabled         TRUE
        SFString [in,out] fogType         "LINEAR" ["LINEAR"|"EXPONENTIAL"]
        SFNode   [in,out] metadata        NULL     [X3DMetadataObject]
        SFFloat  [in,out] visibilityRange 0        [0,-∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            color=[1.0, 1.0, 1.0],
            enabled=True,
            fogType="LINEAR",
            visibilityRange=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            color=color,
            fogType=fogType,
            visibilityRange=visibilityRange,
            **kwargs
        )
        self.enabled = enabled

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

class NurbsOrientationInterpolator(X3DChildNode):
    """
    NurbsOrientationInterpolator : X3DChildNode { 
        SFFloat    [in]     set_fraction       (-∞,∞)
        SFNode     [in,out] controlPoint  NULL [X3DCoordinateNode]
        MFDouble   [in,out] knot          []   (-∞,∞)  
        SFNode     [in,out] metadata      NULL [X3DMetadataObject]
        SFInt32    [in,out] order         3    (2,∞)
        MFDouble   [in,out] weight        []   (-∞,∞)
        SFRotation [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=None,
            knot=[],
            order=3,
            weight=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.controlPoint = controlPoint
        self.knot = knot
        self.order = order
        self.weight = weight

    @property
    def controlPoint(self):
        return self.__controlPoint

    @controlPoint.setter
    def controlPoint(self, controlPoint):
        if controlPoint is None:
            controlPoint = None
        assertSFNode(controlPoint, X3DCoordinateNode)
        self.__controlPoint = controlPoint

    @property
    def knot(self):
        return self.__knot

    @knot.setter
    def knot(self, knot):
        if knot is None:
            knot = []
        assertMFDouble(knot)
        self.__knot = knot

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if order is None:
            order = 3
        assertSFInt32(order)
        assertValidGreaterThan(order, 2)
        self.__order = order
        
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight is None:
            weight = []
        assertMFDouble(weight)
        self.__weight = weight

class NurbsPositionInterpolator(X3DChildNode):
    """
    NurbsPositionInterpolator : X3DChildNode { 
        SFFloat  [in]     set_fraction       (-∞,∞)
        SFNode   [in,out] controlPoint  NULL [X3DCoordinateNode]
        MFDouble [in,out] knot          []   (-∞,∞)  
        SFNode   [in,out] metadata      NULL [X3DMetadataObject]
        SFInt32  [in,out] order         3    (2,∞)
        MFDouble [in,out] weight        []   (-∞,∞)
        SFVec3f  [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=None,
            knot=[],
            order=3,
            weight=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.controlPoint = controlPoint
        self.knot = knot
        self.order = order
        self.weight = weight
    
    @property
    def controlPoint(self):
        return self.__controlPoint

    @controlPoint.setter
    def controlPoint(self, controlPoint):
        if controlPoint is None:
            controlPoint = None
        assertSFNode(controlPoint, X3DCoordinateNode)
        self.__controlPoint = controlPoint

    @property
    def knot(self):
        return self.__knot

    @knot.setter
    def knot(self, knot):
        if knot is None:
            knot = []
        assertMFDouble(knot)
        self.__knot = knot

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if order is None:
            order = 3
        assertSFInt32(order)
        assertValidGreaterThan(order, 2)
        self.__order = order

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight is None:
            weight = []
        assertMFDouble(weight)
        self.__weight = weight

class NurbsSet(X3DChildNode, X3DBoundedObject):
    """
    NurbsSet : X3DChildNode, X3DBoundedObject {
        MFNode  [in]     addGeometry                [X3DNurbsSurfaceGeometryNode]
        MFNode  [in]     removeGeometry             [X3DNurbsSurfaceGeometryNode]
        MFNode  [in,out] geometry          []       [X3DNurbsSurfaceGeometryNode]
        SFNode  [in,out] metadata          NULL     [X3DMetadataObject]
        SFFloat [in,out] tessellationScale 1.0      (0,∞)
        SFVec3f []       bboxCenter        0 0 0    (-∞,∞)
        SFVec3f []       bboxSize          -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            geometry=[],
            tessellationScale=1.0,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.geometry = geometry
        self.tessellationScale = tessellationScale

    @property
    def geometry(self):
        return self.__geometry

    @geometry.setter
    def geometry(self, geometry):
        if geometry is None:
            geometry = []
        assertMFNode(geometry, X3DNurbsSurfaceGeometryNode)
        self.__geometry = geometry
    
    @property
    def tessellationScale(self):
        return self.__tessellationScale

    @tessellationScale.setter
    def tessellationScale(self, tessellationScale):
        if tessellationScale is None:
            tessellationScale = 1.0
        assertSFFloat(tessellationScale)
        assertValidGreaterThan(tessellationScale, 0)
        self.__tessellationScale = tessellationScale

class NurbsSurfaceInterpolator(X3DChildNode): 
    """
    NurbsSurfaceInterpolator : X3DChildNode { 
        SFVec2f  [in]     set_fraction          (-∞,∞)
        SFNode   [in,out] controlPoint     NULL [X3DCoordinateNode]
        SFNode   [in,out] metadata         NULL [X3DMetadataObject]
        MFDouble [in,out] weight           []   (-∞,∞)
        SFVec3f  [out]    position_changed
        SFVec3f  [out]    normal_changed
        SFInt32  []       uDimension       0    [0,∞)
        MFDouble []       uKnot            []   (-∞,∞)
        SFInt32  []       uOrder           3    [2,∞)
        SFInt32  []       vDimension       0    [0,∞)
        MFDouble []       vKnot            []   (-∞,∞)
        SFInt32  []       vOrder           3    [2,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            controlPoint=None,
            weight=[],
            uDimension=0,
            uKnot=[],
            uOrder=3,
            vDimension=0,
            vKnot=[],
            vOrder=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.controlPoint = controlPoint
        self.weight = weight
        self.uDimension = uDimension
        self.uKnot = uKnot
        self.uOrder = uOrder
        self.vDimension = vDimension
        self.vKnot = vKnot
        self.vOrder = vOrder

    @property
    def controlPoint(self):
        return self.__controlPoint

    @controlPoint.setter
    def controlPoint(self, controlPoint):
        if controlPoint is None:
            controlPoint = None
        assertSFNode(controlPoint, X3DCoordinateNode)
        self.__controlPoint = controlPoint

    @property
    def uDimension(self):
        return self.__uDimension

    @uDimension.setter
    def uDimension(self, uDimension):
        if uDimension is None:
            uDimension = 0
        assertSFInt32(uDimension)
        assertValidGreaterThanEquals(uDimension, 0)
        self.__uDimension = uDimension

    @property
    def uKnot(self):
        return self.__uKnot

    @uKnot.setter
    def uKnot(self, uKnot):
        if uKnot is None:
            uKnot = []
        assertMFDouble(uKnot)
        self.__uKnot = uKnot

    @property
    def uOrder(self):
        return self.__uOrder

    @uOrder.setter
    def uOrder(self, uOrder):
        if uOrder is None:
            uOrder = 3
        assertSFInt32(uOrder)
        assertValidGreaterThanEquals(uOrder, 2)
        self.__uOrder = uOrder

    @property
    def vDimension(self):
        return self.__vDimension

    @vDimension.setter
    def vDimension(self, vDimension):
        if vDimension is None:
            vDimension = 0
        assertSFInt32(vDimension)
        assertValidGreaterThanEquals(vDimension, 0)
        self.__vDimension = vDimension

    @property
    def vKnot(self):
        return self.__vKnot

    @vKnot.setter
    def vKnot(self, vKnot):
        if vKnot is None:
            vKnot = []
        assertMFDouble(vKnot)
        self.__vKnot = vKnot

    @property
    def vOrder(self):
        return self.__vOrder

    @vOrder.setter
    def vOrder(self, vOrder):
        if vOrder is None:
            vOrder = 3
        assertSFInt32(vOrder)
        assertValidGreaterThanEquals(vOrder, 2)
        self.__vOrder = vOrder

class RigidBodyCollection(X3DChildNode):
    """
    RigidBodyCollection : X3DChildNode {
        MFNode  [in]     set_contacts                     [Contact] 
        SFBool  [in,out] autoDisable             FALSE
        MFNode  [in,out] bodies                  []       [RigidBody]
        SFFloat [in,out] constantForceMix        0.0001   [0,∞)
        SFFloat [in,out] contactSurfaceThickness 0        [0,∞)
        SFFloat [in,out] disableAngularSpeed     0        [0,∞)
        SFFloat [in,out] disableLinearSpeed      0        [0,∞)
        SFFloat [in,out] disableTime             0        [0,∞)
        SFBool  [in,out] enabled                 TRUE
        SFFloat [in,out] errorCorrection         0.8      [0,1]
        SFVec3f [in,out] gravity                 0 -9.8 0
        SFInt32 [in,out] iterations              10	    [0,∞)
        MFNode  [in,out] joints                  []       [X3DRigidJointNode]
        SFFloat [in,out] maxCorrectionSpeed      -1       [0,∞) or -1
        SFNode  [in,out] metadata                NULL     [X3DMetadataObject]
        SFBool  [in,out] preferAccuracy          FALSE
        SFNode  []       collider                NULL     [CollisionCollection]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            autoDisable=False,
            boides=[],
            constantForceMix=0.0001,
            contactSurfaceThickness=0.0,
            disableAngularSpeed=0.0,
            disableLinearSpeed=0.0,
            disableTime=0.0,
            enabled=True,
            errorCorrection=0.8,
            gravity=[0.0, -9.8, 0.0],
            iterations=10,
            joints=[],
            maxCorrectionSpeed=-1.0,
            preferAccuracy=False,
            collider=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.autoDisable = autoDisable
        self.boides = boides
        self.constantForceMix = constantForceMix
        self.contactSurfaceThickness = contactSurfaceThickness
        self.disableAngularSpeed = disableAngularSpeed
        self.disableLinearSpeed = disableLinearSpeed
        self.disableTime = disableTime
        self.enabled = enabled
        self.errorCorrection = errorCorrection
        self.gravity = gravity
        self.iterations = iterations
        self.joints = joints
        self.maxCorrectionSpeed = maxCorrectionSpeed
        self.preferAccuracy = preferAccuracy
        self.collider = collider

    @property
    def autoDisable(self):
        return self.__autoDisable

    @autoDisable.setter
    def autoDisable(self, autoDisable):
        if autoDisable is None:
            autoDisable = False
        assertSFBool(autoDisable)
        self.__autoDisable = autoDisable

    @property
    def boides(self):
        return self.__boides

    @boides.setter
    def boides(self, boides):
        if boides is None:
            boides = False
        assertMFNode(boides, RigidBody)
        self.__boides = boides

    @property
    def constantForceMix(self):
        return self.__constantForceMix

    @constantForceMix.setter
    def constantForceMix(self, constantForceMix):
        if constantForceMix is None:
            constantForceMix = 0.0001
        assertSFFloat(constantForceMix)
        assertValidGreaterThanEquals(constantForceMix, 0)
        self.__constantForceMix = constantForceMix

    @property
    def contactSurfaceThickness(self):
        return self.__contactSurfaceThickness

    @contactSurfaceThickness.setter
    def contactSurfaceThickness(self, contactSurfaceThickness):
        if contactSurfaceThickness is None:
            contactSurfaceThickness = 0.0
        assertSFFloat(contactSurfaceThickness)
        assertValidGreaterThanEquals(contactSurfaceThickness, 0)
        self.__contactSurfaceThickness = contactSurfaceThickness

    @property
    def disableAngularSpeed(self):
        return self.__disableAngularSpeed

    @disableAngularSpeed.setter
    def disableAngularSpeed(self, disableAngularSpeed):
        if disableAngularSpeed is None:
            disableAngularSpeed = 0.0
        assertSFFloat(disableAngularSpeed)
        assertValidGreaterThanEquals(disableAngularSpeed, 0)
        self.__disableAngularSpeed = disableAngularSpeed

    @property
    def disableLinearSpeed(self):
        return self.__disableLinearSpeed

    @disableLinearSpeed.setter
    def disableLinearSpeed(self, disableLinearSpeed):
        if disableLinearSpeed is None:
            disableLinearSpeed = 0.0
        assertSFFloat(disableLinearSpeed)
        assertValidGreaterThanEquals(disableLinearSpeed, 0)
        self.__disableLinearSpeed = disableLinearSpeed

    @property
    def disableTime(self):
        return self.__disableTime

    @disableTime.setter
    def disableTime(self, disableTime):
        if disableTime is None:
            disableTime = 0.0
        assertSFFloat(disableTime)
        assertValidGreaterThanEquals(disableTime, 0)
        self.__disableTime = disableTime

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

    @property
    def errorCorrection(self):
        return self.__errorCorrection

    @errorCorrection.setter
    def errorCorrection(self, errorCorrection):
        if errorCorrection is None:
            errorCorrection = 0.8
        assertSFFloat(errorCorrection)
        assertValidGreaterThanEquals(errorCorrection, 0)
        assertValidLessThanEquals(errorCorrection, 1)
        self.__errorCorrection = errorCorrection

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, gravity):
        if gravity is None:
            gravity = [0.0, -9.8, 0.0]
        assertSFFloat(gravity)
        self.__gravity = gravity

    @property
    def iterations(self):
        return self.__iterations

    @iterations.setter
    def iterations(self, iterations):
        if iterations is None:
            iterations = 10
        assertSFInt32(iterations)
        assertValidGreaterThanEquals(iterations, 0)
        self.__iterations = iterations

    @property
    def joints(self):
        return self.__joints

    @joints.setter
    def joints(self, joints):
        if joints is None:
            joints = 0.0
        assertMFNode(joints, X3DRigidJointNode)
        self.__joints = joints

    @property
    def maxCorrectionSpeed(self):
        return self.__maxCorrectionSpeed

    @maxCorrectionSpeed.setter
    def maxCorrectionSpeed(self, maxCorrectionSpeed):
        if maxCorrectionSpeed is None:
            maxCorrectionSpeed = -1.0
        assertValidMaxCorrectionSpeed(maxCorrectionSpeed)
        self.__maxCorrectionSpeed = maxCorrectionSpeed

    @property
    def preferAccuracy(self):
        return self.__preferAccuracy

    @preferAccuracy.setter
    def preferAccuracy(self, preferAccuracy):
        if preferAccuracy is None:
            preferAccuracy = False
        assertSFBool(preferAccuracy)
        self.__preferAccuracy = preferAccuracy

    @property
    def collider(self):
        return self.__collider

    @collider.setter
    def collider(self, collider):
        if collider is None:
            collider = None
        assertSFNode(collider, CollisionCollection)
        self.__collider = collider

class StaticGroup(X3DChildNode, X3DBoundedObject):
    """
    StaticGroup : X3DChildNode, X3DBoundedObject {
        SFNode  [in,out] metadata   NULL     [X3DMetadataObject]
        MFNode  []       children   []       [X3DChildNode]
        SFVec3f []       bboxCenter 0 0 0    (-∞,∞)
        SFVec3f []       bboxSize   -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )

class Fog(X3DBindableNode, X3DFogObject):
    """
    Fog : X3DBindableNode, X3DFogObject {
        SFBool   [in]     set_bind
        SFColor  [in,out] color           1 1 1    [0,1]
        SFString [in,out] fogType         "LINEAR" ["LINEAR"|"EXPONENTIAL"]
        SFNode   [in,out] metadata        NULL     [X3DMetadataObject]
        SFFloat  [in,out] visibilityRange 0        [0,∞)
        SFTime   [out]    bindTime
        SFBool   [out]    isBound
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            color=[1.0, 1.0, 1.0],
            fogType="LINEAR",
            visibilityRange=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            color=color,
            fogType=fogType,
            visibilityRange=visibilityRange,
            **kwargs
        )

class GeoViewpoint(X3DViewpointNode):
    """
    GeoViewpoint : X3DViewpointNode {
        SFBool     [in]     set_bind
        SFVec3d    [in,out] centerOfRotation  0 0 0             (-∞,∞)
        SFString   [in,out] description       ""
        SFFloat    [in,out] fieldOfView       π/4               (0,π)
        SFBool     [in,out] jump              TRUE
        SFNode     [in,out] metadata          NULL              [X3DMetadataObject]
        SFRotation [in,out] orientation       0 0 1 0           (-∞,∞) or -1 1
        SFVec3d    [in,out] position          0 0 100000        (-∞,∞)
        SFBool     [in,out] retainUserOffsets FALSE
        SFTime     [out]    bindTime
        SFBool     [out]    isBound
        SFNode     []       geoOrigin         NULL              [GeoOrigin] (deprecated)
        MFString   []       geoSystem         ["GD","WE"]       [see 25.2.3]
        SFFloat    []       speedFactor       1.0               [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            centerOfRotation=[0.0, 0.0, 0.0],
            description="",
            fieldOfView=math.pi/4,
            jump=True,
            orientation=[0.0, 0.0, 1.0, 0.0],
            position=[0.0, 0.0, 100000.0],
            retainUserOffsets=False,
            geoOrigin=[0.0, 0.0, 0.0],
            geoSystem=["GD", "WE"],
            speedFactor=1.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            centerOfRotation=centerOfRotation,
            description=description,
            jump=jump,
            orientation=orientation,
            position=position,
            retainUserOffsets=retainUserOffsets,
            **kwargs
        )
        self.fieldOfView = fieldOfView
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem
        self.speedFactor = speedFactor
    
    @property
    def fieldOfView(self):
        return self.__fieldOfView

    @fieldOfView.setter
    def fieldOfView(self, fieldOfView):
        if fieldOfView is None:
            fieldOfView = math.pi/4
        assertSFFloat(fieldOfView)
        assertValidGreaterThan(fieldOfView, 0)
        assertValidLessThan(fieldOfView, math.pi)
        self.__fieldOfView = fieldOfView

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

    @property
    def speedFactor(self):
        return self.__speedFactor

    @speedFactor.setter
    def speedFactor(self, speedFactor):
        if speedFactor is None:
            speedFactor = 1.0
        assertSFFloat(speedFactor)
        assertValidGreaterThanEquals(speedFactor, 0)
        self.__speedFactor = speedFactor

class NavigationInfo(X3DBindableNode):
    """
    NavigationInfo : X3DBindableNode {
    SFBool   [in]     set_bind
        MFFloat  [in,out] avatarSize      [0.25 1.6 0.75]   [0,∞)
        SFBool   [in,out] headlight       TRUE
        SFNode   [in,out] metadata        NULL              [X3DMetadataObject]
        SFFloat  [in,out] speed           1.0               [0,∞)
        SFTime   [in,out] transitionTime  1.0               [0, ∞)
        MFString [in,out] transitionType  ["LINEAR"]        ["TELEPORT","LINEAR",
                                                            "ANIMATE",...]
        MFString [in,out] type            ["EXAMINE" "ANY"] ["ANY","WALK","EXAMINE","FLY",
                                                            "LOOKAT","NONE","EXPLORE",...]
        SFFloat  [in,out] visibilityLimit 0.0               [0,∞)
        SFTime   [out]    bindTime
        SFBool   [out]    isBound
        SFBool   [out]    transitionComplete
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            avatarSize=[0.25, 1.6, 0.75],
            headlight=True,
            speed=1.0,
            transitionTime=1.0,
            transitionType=["LINEAR"],
            type_=["EXAMINE", "ANY"],
            visibilityLimit=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.avatarSize = avatarSize
        self.headlight = headlight
        self.speed = speed
        self.transitionTime = transitionTime
        self.transitionType = transitionType
        self.type_ = type_
        self.visibilityLimit = visibilityLimit

    @property
    def avatarSize(self):
        return self.__avatarSize

    @avatarSize.setter
    def avatarSize(self, avatarSize):
        if avatarSize is None:
            avatarSize = [0.25, 1.6, 0.75]
        assertMFFloat(avatarSize)
        assertValidGreaterThanEquals(avatarSize, 0)
        self.__avatarSize = avatarSize
    
    @property
    def headlight(self):
        return self.__headlight

    @headlight.setter
    def headlight(self, headlight):
        if headlight is None:
            headlight = True
        assertSFBool(headlight)
        self.__headlight = headlight
    
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if speed is None:
            speed = 1.0
        assertSFFloat(speed)
        assertValidGreaterThanEquals(speed, 0)
        self.__speed = speed

    @property
    def transitionTime(self):
        return self.__transitionTime

    @transitionTime.setter
    def transitionTime(self, transitionTime):
        if transitionTime is None:
            transitionTime = 1.0
        assertSFTime(transitionTime)
        assertValidGreaterThanEquals(transitionTime, 0)
        self.__transitionTime = transitionTime

    @property
    def transitionType(self):
        return self.__transitionType

    @transitionType.setter
    def transitionType(self, transitionType):
        if transitionType is None:
            transitionType = ["LINEAR"]
        assertValidNavigationInfoTransitionType(transitionType)
        self.__transitionType = transitionType

    @property
    def type_(self):
        return self.__type_

    @type_.setter
    def type_(self, type_):
        if type_ is None:
            type_ = ["EXAMINE", "ANY"]
        assertValidNavigationInfoType(type_)
        self.__type_ = type_

    @property
    def visibilityLimit(self):
        return self.__visibilityLimit

    @visibilityLimit.setter
    def visibilityLimit(self, visibilityLimit):
        if visibilityLimit is None:
            visibilityLimit = 0.0
        assertSFFloat(visibilityLimit)
        assertValidGreaterThanEquals(visibilityLimit, 0)
        self.__visibilityLimit = visibilityLimit

class Background(X3DBackgroundNode):
    """
    Background : X3DBackgroundNode {
        SFBool   [in]     set_bind
        MFFloat  [in,out] groundAngle  []    [0,π/2]
        MFColor  [in,out] groundColor  []    [0,1]
        MFString [in,out] backUrl      []    [URI]
        MFString [in,out] bottomUrl    []    [URI]
        MFString [in,out] frontUrl     []    [URI]
        MFString [in,out] leftUrl      []    [URI]
        SFNode   [in,out] metadata     NULL  [X3DMetadataObject]
        MFString [in,out] rightUrl     []    [URI]
        MFString [in,out] topUrl       []    [URI]
        MFFloat  [in,out] skyAngle     []    [0,π]
        MFColor  [in,out] skyColor     0 0 0 [0,1]
        SFFloat  [in,out] transparency 0     [0,1]
        SFTime   [out]    bindTime
        SFBool   [out]    isBound
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            groundAngle=[],
            groundColor=[],
            backUrl=[],
            bottomUrl=[],
            frontUrl=[],
            leftUrl=[],
            rightUrl=[],
            topUrl=[],
            skyAngle=[],
            skyColor=[[0.0, 0.0, 0.0]],
            transparency=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            groundAngle=groundAngle,
            groundColor=groundColor,
            skyAngle=skyAngle,
            skyColor=skyColor,
            transparency=transparency,
            **kwargs
        )
        self.backUrl = backUrl
        self.bottomUrl = bottomUrl
        self.frontUrl = frontUrl
        self.leftUrl = leftUrl
        self.rightUrl = rightUrl
        self.topUrl = topUrl

    @property
    def backUrl(self):
        return self.__backUrl

    @backUrl.setter
    def backUrl(self, backUrl):
        if backUrl is None:
            backUrl = []
        assertMFString(backUrl)
        self.__backUrl = backUrl

    @property
    def bottomUrl(self):
        return self.__bottomUrl

    @bottomUrl.setter
    def bottomUrl(self, bottomUrl):
        if bottomUrl is None:
            bottomUrl = []
        assertMFString(bottomUrl)
        self.__bottomUrl = bottomUrl

    @property
    def frontUrl(self):
        return self.__frontUrl

    @frontUrl.setter
    def frontUrl(self, frontUrl):
        if frontUrl is None:
            frontUrl = []
        assertMFString(frontUrl)
        self.__frontUrl = frontUrl

    @property
    def leftUrl(self):
        return self.__leftUrl

    @leftUrl.setter
    def leftUrl(self, leftUrl):
        if leftUrl is None:
            leftUrl = []
        assertMFString(leftUrl)
        self.__leftUrl = leftUrl

    @property
    def rightUrl(self):
        return self.__rightUrl

    @rightUrl.setter
    def rightUrl(self, rightUrl):
        if rightUrl is None:
            rightUrl = []
        assertMFString(rightUrl)
        self.__rightUrl = rightUrl

    @property
    def topUrl(self):
        return self.__topUrl

    @topUrl.setter
    def topUrl(self, topUrl):
        if topUrl is None:
            topUrl = []
        assertMFString(topUrl)
        self.__topUrl = topUrl

class TextureBackground(X3DBackgroundNode):
    """
    TextureBackground : X3DBackgroundNode {
        SFBool  [in]     set_bind
        MFFloat [in,out] groundAngle   []    [0,π/2]
        MFColor [in,out] groundColor   []    [0,1]
        SFNode  [in,out] backTexture   NULL  [X3DTexture2DNode,MultiTexture]
        SFNode  [in,out] bottomTexture NULL  [X3DTexture2DNode,MultiTexture]
        SFNode  [in,out] frontTexture  NULL  [X3DTexture2DNode,MultiTexture]
        SFNode  [in,out] leftTexture   NULL  [X3DTexture2DNode,MultiTexture]
        SFNode  [in,out] metadata      NULL  [X3DMetadataObject]
        SFNode  [in,out] rightTexture  NULL  [X3DTexture2DNode,MultiTexture]
        SFNode  [in,out] topTexture    NULL  [X3DTexture2DNode,MultiTexture]
        MFFloat [in,out] skyAngle      []    [0,π]
        MFColor [in,out] skyColor      0 0 0 [0,1]
        SFFloat [in,out] transparency  0     [0,1]
        SFTime  [out]    bindTime
        SFBool  [out]    isBound
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            groundAngle=[],
            groundColor=[],
            backTexture=None,
            bottomTexture=None,
            frontTexture=None,
            leftTexture=None,
            rightTexture=None,
            topTexture=None,
            skyAngle=[],
            skyColor=[[0.0, 0.0, 0.0]],
            transparency=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            groundAngle=groundAngle,
            groundColor=groundColor,
            skyAngle=skyAngle,
            skyColor=skyColor,
            transparency=transparency,
            **kwargs
        )
        self.backTexture = backTexture
        self.bottomTexture = bottomTexture
        self.frontTexture = frontTexture
        self.leftTexture = leftTexture
        self.rightTexture = rightTexture
        self.topTexture = topTexture

    @property
    def backTexture(self):
        return self.__backTexture

    @backTexture.setter
    def backTexture(self, backTexture):
        if backTexture is None:
            backTexture = None
        assertSFNode(backTexture, X3DTexture2DNode, MultiTexture)
        self.__backTexture = backTexture

    @property
    def bottomTexture(self):
        return self.__bottomTexture

    @bottomTexture.setter
    def bottomTexture(self, bottomTexture):
        if bottomTexture is None:
            bottomTexture = None
        assertSFNode(bottomTexture, X3DTexture2DNode, MultiTexture)
        self.__bottomTexture = bottomTexture

    @property
    def frontTexture(self):
        return self.__frontTexture

    @frontTexture.setter
    def frontTexture(self, frontTexture):
        if frontTexture is None:
            frontTexture = None
        assertSFNode(frontTexture, X3DTexture2DNode, MultiTexture)
        self.__frontTexture = frontTexture

    @property
    def leftTexture(self):
        return self.__leftTexture

    @backTexture.setter
    def leftTexture(self, leftTexture):
        if leftTexture is None:
            leftTexture = None
        assertSFNode(leftTexture, X3DTexture2DNode, MultiTexture)
        self.__leftTexture = leftTexture

    @property
    def rightTexture(self):
        return self.__rightTexture

    @rightTexture.setter
    def rightTexture(self, rightTexture):
        if rightTexture is None:
            rightTexture = None
        assertSFNode(rightTexture, X3DTexture2DNode, MultiTexture)
        self.__rightTexture = rightTexture

    @property
    def topTexture(self):
        return self.__topTexture

    @topTexture.setter
    def topTexture(self, topTexture):
        if topTexture is None:
            topTexture = None
        assertSFNode(topTexture, X3DTexture2DNode, MultiTexture)
        self.__topTexture = topTexture

class OrthoViewpoint(X3DViewpointNode): 
    """
    OrthoViewpoint : X3DViewpointNode { 
        SFBool     [in]     set_bind
        SFVec3f    [in,out] centerOfRotation  0 0 0         (-∞,∞)
        SFString   [in,out] description       ""
        MFFloat    [in,out] fieldOfView       -1, -1, 1, 1  (-∞,∞)
        SFBool     [in,out] jump              TRUE
        SFNode     [in,out] metadata          NULL          [X3DMetadataObject]
        SFRotation [in,out] orientation       0 0 1 0       [-1,1],(-∞,∞)
        SFVec3f    [in,out] position          0 0 10        (-∞,∞)
        SFBool     [in,out] retainUserOffsets FALSE
        SFTime     [out]    bindTime
        SFBool     [out]    isBound
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            centerOfRotation=[0.0, 0.0, 0.0],
            description="",
            jump=True,
            orientation=[0.0, 0.0, 1.0, 0.0],
            position=[0.0, 0.0, 10.0],
            retainUserOffsets=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            centerOfRotation=centerOfRotation,
            description=description,
            jump=jump,
            orientation=orientation,
            position=position,
            retainUserOffsets=retainUserOffsets
            **kwargs
        )

class Viewpoint(X3DViewpointNode): 
    """
    Viewpoint : X3DViewpointNode { 
        SFBool     [in]     set_bind
        SFVec3f    [in,out] centerOfRotation  0 0 0   (-∞,∞)
        SFString   [in,out] description       ""
        SFFloat    [in,out] fieldOfView       π/4     (0,π)
        SFBool     [in,out] jump              TRUE
        SFNode     [in,out] metadata          NULL    [X3DMetadataObject]
        SFRotation [in,out] orientation       0 0 1 0 [-1,1],(-∞,∞)
        SFVec3f    [in,out] position          0 0 10  (-∞,∞)
        SFBool     [in,out] retainUserOffsets FALSE
        SFTime     [out]    bindTime
        SFBool     [out]    isBound
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            centerOfRotation=[0.0, 0.0, 0.0],
            description="",
            fieldOfView=math.pi/4,
            jump=True,
            orientation=[0.0, 0.0, 1.0, 0.0],
            position=[0.0, 0.0, 10.0],
            retainUserOffsets=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            centerOfRotation=centerOfRotation,
            description=description,
            jump=jump,
            orientation=orientation,
            position=position,
            retainUserOffsets=retainUserOffsets,
            **kwargs
        )
        self.fieldOfView = fieldOfView
    
    @property
    def fieldOfView(self):
        return self.__fieldOfView

    @fieldOfView.setter
    def fieldOfView(self, fieldOfView):
        if fieldOfView is None:
            fieldOfView = math.pi/4
        assertSFFloat(fieldOfView)
        assertValidGreaterThan(fieldOfView, 0)
        assertValidLessThan(fieldOfView, math.pi)
        self.__fieldOfView = fieldOfView

class ViewpointGroup(X3DChildNode):
    """
    ViewpointGroup : X3DChildNode { 
        SFVec3f  [in,out] center            0 0 0 (-∞,∞)
        MFNode   [in,out] children          NULL  [X3DViewpointNode | ViewpointGroup]
        SFString [in,out] description       ""
        SFBool   [in,out] displayed         TRUE
        SFNode   [in,out] metadata          NULL  [X3DMetadataObject]
        SFBool   [in,out] retainUserOffsets FALSE
        SFVec3f  [in,out] size              0 0 0 (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            description="",
            displayed=True,
            retainUserOffsets=False,
            size=[0.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            **kwargs
        )
        self.center = center
        self.description = description
        self.displayed = displayed
        self.retainUserOffsets = retainUserOffsets
        self.size = size
    
    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def description(self, description):
        return self.__description

    @description.setter
    def description(self, description):
        if description is None:
            description = ""
        assertSFString(description)
        self.__description = description

    @property
    def displayed(self):
        return self.__displayed

    @displayed.setter
    def displayed(self, displayed):
        if displayed is None:
            displayed = True
        assertSFBool(displayed)
        self.__displayed = displayed

    @property
    def retainUserOffsets(self):
        return self.__retainUserOffsets

    @retainUserOffsets.setter
    def retainUserOffsets(self, retainUserOffsets):
        if retainUserOffsets is None:
            retainUserOffsets = False
        assertSFBool(retainUserOffsets)
        self.__retainUserOffsets = retainUserOffsets

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size is None:
            size = [0.0, 0.0, 0.0]
        assertSFVec3f(size)
        self.__size = size

class ColorChaser(X3DChaserNode):
    """
    ColorChaser: X3DChaserNode {
        SFColor [in]     set_destination
        SFColor [in]     set_value
        SFNode  [in,out] metadata           NULL        [X3DMetadataObject]
        SFBool  [out]    isActive
        SFColor [out]    value_changed
        SFTime  []       duration           1           [0,∞)
        SFColor []       initialDestination 0.8 0.8 0.8 [0,1]
        SFColor []       initialValue       0.8 0.8 0.8 [0,1]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            initialDestination=[0.8, 0.8, 0.8],
            initialValue=[0.8, 0.8, 0.8],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            duration=duration,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.8, 0.8, 0.8]
        assertSFColor(initialDestination)
        assertValidGreaterThanEquals(initialDestination, 0)
        assertValidLessThanEquals(initialDestination, 1)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.8, 0.8, 0.8]
        assertSFColor(initialValue)
        assertValidGreaterThanEquals(initialValue, 0)
        assertValidLessThanEquals(initialValue, 1)
        self.__initialValue = initialValue

class CoordinateChaser(X3DChaserNode):
    """
    CoordinateChaser: X3DChaserNode {
        MFVec3f [in]     set_destination
        MFVec3f [in]     set_value
        SFNode  [in,out] metadata           NULL  [X3DMetadataObject]
        SFBool  [out]    isActive
        MFVec3f [out]    value_changed
        SFTime  []       duration           1     [0,∞)
        MFVec3f []       initialDestination 0 0 0
        MFVec3f []       initialValue       0 0 0
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            initialDestination=[[0.0, 0.0, 0.0]],
            initialValue=[[0.0, 0.0, 0.0]],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            duration=duration,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [[0.0, 0.0, 0.0]]
        assertMFVec3f(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [[0.0, 0.0, 0.0]]
        assertMFVec3f(initialValue)
        self.__initialValue = initialValue

class OrientationChaser(X3DChaserNode):
    """
    OrientationChaser : X3DChaserNode {
        SFRotation [in]     set_destination
        SFRotation [in]     set_value
        SFNode     [in,out] metadata           NULL    [X3DMetadataObject]
        SFBool     [out]    isActive
        SFRotation [out]    value_changed
        SFTime     []       duration           1       [0,∞)
        SFRotation []       initialDestination 0 1 0 0
        SFRotation []       initialValue       0 1 0 0
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            initialDestination=[0.0, 1.0, 0.0, 0.0],
            initialValue=[0.0, 1.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            duration=duration,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.0, 1.0, 0.0, 0.0]
        assertSFRotation(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.0, 1.0, 0.0, 0.0]
        assertSFRotation(initialValue)
        self.__initialValue = initialValue

class PositionChaser(X3DChaserNode):
    """
    PositionChaser : X3DChaserNode {
        SFVec3f [in]     set_destination
        SFVec3f [in]     set_value
        SFNode  [in,out] metadata           NULL  [X3DMetadataObject]
        SFBool  [out]    isActive
        SFVec3f [out]    value_changed
        SFTime  []       duration           1     [0,∞)
        SFVec3f []       initialDestination 0 0 0
        SFVec3f []       initialValue       0 0 0
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            initialDestination=[0.0, 0.0, 0.0],
            initialValue=[0.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            duration=duration,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.0, 0.0, 0.0]
        assertSFVec3f(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.0, 0.0, 0.0]
        assertSFVec3f(initialValue)
        self.__initialValue = initialValue

class PositionChaser2D(X3DChaserNode):
    """
    PositionChaser2D : X3DChaserNode {
        SFVec2f [in]     set_destination
        SFVec2f [in]     set_value
        SFNode  [in,out] metadata           NULL  [X3DMetadataObject]
        SFBool  [out]    isActive
        SFVec2f [out]    value_changed
        SFTime  []       duration           1     [0,∞)
        SFVec2f []       initialDestination 0 0
        SFVec2f []       initialValue       0 0
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            initialDestination=[0.0, 0.0],
            initialValue=[0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            duration=duration,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.0, 0.0]
        assertSFVec2f(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.0, 0.0]
        assertSFVec2f(initialValue)
        self.__initialValue = initialValue

class ScalerChaser(X3DChaserNode):
    """
    ScalarChaser : X3DChaserNode {
        SFFloat [in]     set_destination
        SFFloat [in]     set_value
        SFNode  [in,out] metadata           NULL [X3DMetadataObject]
        SFBool  [out]    isActive
        SFFloat [out]    value_changed
        SFTime  []       duration           1    [0,∞)
        SFFloat []       initialDestination 0
        SFFloat []       initialValue       0
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            initialDestination=0.0,
            initialValue=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            duration=duration,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = 0.0
        assertSFFloat(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = 0.0
        assertSFFloat(initialValue)
        self.__initialValue = initialValue

class TexCoordChaser2D(X3DChaserNode):
    """
    TexCoordChaser2D: X3DChaserNode {
        MFVec2f [in]     set_destination
        MFVec2f [in]     set_value
        SFNode  [in,out] metadata           NULL [X3DMetadataObject]
        SFBool  [out]    isActive
        MFVec2f [out]    value_changed
        SFTime  []       duration           1    [0,∞)
        MFVec2f []       initialDestination []
        MFVec2f []       initialValue       []
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            initialDestination=[],
            initialValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            duration=duration,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = []
        assertMFVec2f(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = []
        assertMFVec2f(initialValue)
        self.__initialValue = initialValue

class ColorDamper(X3DDamperNode):
    """
    ColorDamper : X3DDamperNode {
        SFColor [in]     set_destination
        SFColor [in]     set_value
        SFNode  [in,out] metadata           NULL        [X3DMetadataObject]
        SFTime  [in,out] tau                0.3         [0,∞)
        SFFloat [in,out] tolerance          -1          -1 or [0,∞)
        SFBool  [out]    isActive
        SFColor [out]    value_changed
        SFColor []       initialDestination 0.8 0.8 0.8 [0,1]
        SFColor []       initialValue       0.8 0.8 0.8 [0,1]
        SFInt32 []       order              3           [0..5]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            tau=0.3,
            tolerance=-1.0,
            initialDestination=[0.8, 0.8, 0.8],
            initialValue=[0.8, 0.8, 0.8],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            tau=tau,
            tolerance=tolerance,
            order=order,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.8, 0.8, 0.8]
        assertSFColor(initialDestination)
        assertValidGreaterThanEquals(initialDestination, 0)
        assertValidLessThanEquals(initialDestination, 1)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.8, 0.8, 0.8]
        assertSFColor(initialValue)
        assertValidGreaterThanEquals(initialValue, 0)
        assertValidLessThanEquals(initialValue, 1)
        self.__initialValue = initialValue

class CoordinateDamper(X3DDamperNode):
    """
    CoordinateDamper : X3DDamperNode {
        MFVec3f [in]     set_destination
        MFVec3f [in]     set_value
        SFNode  [in,out] metadata           NULL  [X3DMetadataObject]
        SFTime  [in,out] tau                0.3   [0,∞)
        SFFloat [in,out] tolerance          -1    -1 or [0,∞)
        SFBool  [out]    isActive
        MFVec3f [out]    value_changed
        MFVec3f []       initialDestination 0 0 0
        MFVec3f []       initialValue       0 0 0
        SFInt32 []       order              3     [0..5]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            tau=0.3,
            tolerance=-1.0,
            initialDestination=[0.8, 0.8, 0.8],
            initialValue=[0.8, 0.8, 0.8],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            tau=tau,
            tolerance=tolerance,
            order=order,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.8, 0.8, 0.8]
        assertSFColor(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.8, 0.8, 0.8]
        assertSFColor(initialValue)
        self.__initialValue = initialValue

class OrientationDamper(X3DDamperNode):
    """
    OrientationDamper : X3DDamperNode {
        SFRotation [in]     set_destination
        SFRotation [in]     set_value
        SFNode     [in,out] metadata           NULL    [X3DMetadataObject]
        SFTime     [in,out] tau                0.3     [0,∞)
        SFFloat    [in,out] tolerance          -1      -1 or [0..∞]
        SFBool     [out]    isActive
        SFRotation [out]    value_changed
        SFRotation []       initialDestination 0 1 0 0
        SFRotation []       initialValue       0 1 0 0
        SFInt32    []       order              3       [0..5]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            tau=0.3,
            tolerance=-1.0,
            initialDestination=[0.0, 0.1, 0.0, 0.0],
            initialValue=[0.0, 0.1, 0.0, 0.0],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            tau=tau,
            tolerance=tolerance,
            order=order,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.0, 0.1, 0.0, 0.0]
        assertSFRotation(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.0, 0.1, 0.0, 0.0]
        assertSFRotation(initialValue)
        self.__initialValue = initialValue

class PositionDamper(X3DDamperNode):
    """
    PositionDamper : X3DDamperNode {
        SFVec3f [in]     set_destination
        SFVec3f [in]     set_value
        SFNode  [in,out] metadata           NULL  [X3DMetadataObject]
        SFTime  [in,out] tau                0.3   [0,∞)
        SFFloat [in,out] tolerance          -1    -1 or [0,∞)
        SFBool  [out]    isActive
        SFVec3f [out]    value_changed
        SFVec3f []       initialDestination 0 0 0
        SFVec3f []       initialValue       0 0 0
        SFInt32 []       order              3     [0..5]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            tau=0.3,
            tolerance=-1.0,
            initialDestination=[0.0, 0.0, 0.0],
            initialValue=[0.0, 0.0, 0.0],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            tau=tau,
            tolerance=tolerance,
            order=order,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.0, 0.0, 0.0]
        assertSFVec3f(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.0, 0.0, 0.0]
        assertSFVec3f(initialValue)
        self.__initialValue = initialValue

class PositionDamper2D(X3DDamperNode):
    """
    PositionDamper2D : X3DDamperNode {
        SFVec2f [in]     set_destination
        SFVec2f [in]     set_value
        SFNode  [in,out] metadata           NULL [X3DMetadataObject]
        SFTime  [in,out] tau                0.3  [0,∞)
        SFFloat [in,out] tolerance          -1   -1 or [0..∞]
        SFBool  [out]    isActive
        SFVec2f [out]    value_changed
        SFVec2f []       initialDestination 0 0
        SFVec2f []       initialValue       0 0
        SFInt32 []       order              3    [0..5]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            tau=0.3,
            tolerance=-1.0,
            initialDestination=[0.0, 0.0],
            initialValue=[0.0, 0.0],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            tau=tau,
            tolerance=tolerance,
            order=order,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = [0.0, 0.0]
        assertSFVec2f(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = [0.0, 0.0]
        assertSFVec2f(initialValue)
        self.__initialValue = initialValue

class ScalarDamper(X3DDamperNode):
    """
    ScalarDamper: X3DDamperNode {
        SFFloat [in]     set_destination
        SFFloat [in]     set_value
        SFNode  [in,out] metadata           NULL  [X3DMetadataObject]
        SFTime  [in,out] tau                0.3   [0,∞)
        SFFloat [in,out] tolerance          -1    -1 or [0,∞)
        SFBool  [out]    isActive
        SFFloat [out]    value_changed
        SFFloat []       initialDestination 0
        SFFloat []       initialValue       0
        SFInt32 []       order              3     [0..5]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            tau=0.3,
            tolerance=-1.0,
            initialDestination=0.0,
            initialValue=0.0,
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            tau=tau,
            tolerance=tolerance,
            order=order,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = 0.0
        assertSFFloat(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = 0.0
        assertSFFloat(initialValue)
        self.__initialValue = initialValue

class TexCoordDamper2D(X3DDamperNode):
    """
    TexCoordDamper2D : X3DDamperNode {
        MFVec2f [in]     set_destination
        MFVec2f [in]     set_value
        SFNode  [in,out] metadata           NULL [X3DMetadataObject]
        SFTime  [in,out] tau                0.3  [0,∞)
        SFFloat [in,out] tolerance          -1   -1 or [0..∞]
        SFBool  [out]    isActive
        MFVec2f [out]    value_changed
        MFVec2f []       initialDestination []
        MFVec2f []       initialValue       []
        SFInt32 []       order              3    [0..5]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            tau=0.3,
            tolerance=-1.0,
            initialDestination=[],
            initialValue=[],
            order=3,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            tau=tau,
            tolerance=tolerance,
            order=order,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    @property
    def initialDestination(self):
        return self.__initialDestination

    @initialDestination.setter
    def initialDestination(self, initialDestination):
        if initialDestination is None:
            initialDestination = []
        assertMFVec2f(initialDestination)
        self.__initialDestination = initialDestination

    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        if initialValue is None:
            initialValue = []
        assertMFVec2f(initialValue)
        self.__initialValue = initialValue

class Anchor(X3DGroupingNode, X3DUrlObject):
    """
    Anchor : X3DGroupingNode,X3DUrlObject { 
        MFNode   [in]     addChildren
        MFNode   [in]     removeChildren
        MFNode   [in,out] children       []       [X3DChildNode]
        SFString [in,out] description    ""
        SFNode   [in,out] metadata       NULL     [X3DMetadataObject]
        MFString [in,out] parameter      []
        MFString [in,out] url            []       [URI]
        SFVec3f  []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f  []       bboxSize       -1 -1 -1 [0,∞) or −1 −1 −1 
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            children=[],
            description="",
            parameter=[],
            url=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            url=url,
            **kwargs
        )
        self.description = description
        self.parameter = parameter

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if description is None:
            description = ""
        assertSFString(description)
        self.__description = description
        
    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter):
        if parameter is None:
            parameter = []
        assertMFString(parameter)
        self.__parameter = parameter

class Billboard(X3DGroupingNode):
    """
    Billboard : X3DGroupingNode {
        MFNode  [in]     addChildren             [X3DChildNode]
        MFNode  [in]     removeChildren          [X3DChildNode]
        SFVec3f [in,out] axisOfRotation 0 1 0    (-∞,∞)
        MFNode  [in,out] children       []       [X3DChildNode]
        SFNode  [in,out] metadata       NULL     [X3DMetadataObject]
        SFVec3f []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f []       bboxSize       -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            axisOfRotation=[0.0, 1.0, 0.0],
            children=[],
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.axisOfRotation = axisOfRotation

    @property
    def axisOfRotation(self):
        return self.__axisOfRotation

    @axisOfRotation.setter
    def axisOfRotation(self, axisOfRotation):
        if axisOfRotation is None:
            axisOfRotation = [0.0, 1.0, 0.0]
        assertSFVec3f(axisOfRotation)
        self.__axisOfRotation = axisOfRotation

class CADAssembly(X3DGroupingNode, X3DProductStructureChildNode):
    """
    CADAssembly : X3DGroupingNode, X3DProductStructureChildNode {
        MFNode   [in]     addChildren
        MFNode   [in]     removeChildren
        MFNode   [in,out] children       []       [X3DProductStructureChildNode, X3DGroupingNode]
        SFNode   [in,out] metadata       NULL     [X3DMetadataObject]
        SFString [in,out] name           ""
        SFVec3f  []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f  []       bboxSize       -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            children=[],
            name="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            name=name,
            **kwargs
        )

class CADFace(X3DProductStructureChildNode, X3DBoundedObject):
    """
    CADFace : X3DProductStructureChildNode, X3DBoundedObject {
        SFNode   [in,out] metadata   NULL     [X3DMetadataObject]
        SFString [in,out] name       ""
        SFNode   [in,out] shape      NULL     [X3DShapeNode, LOD, Transform]
        SFVec3f  []       bboxCenter 0 0 0    (-∞, ∞)
        SFVec3f  []       bboxSize   -1 -1 -1 [0, ∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            children=[],
            name="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            name=name,
            **kwargs
        )
        self.shape = shape

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape):
        if shape is None:
            shape = None
        assertSFNode(shape, X3DShapeNode, LOD, Transform)
        self.__shape = shape

class CADLayer(X3DGroupingNode):
    """
    CADLayer : X3DGroupingNode {
        MFNode   [in]     addChildren
        MFNode   [in]     removeChildren
        MFNode   [in,out] children       []       [X3DChildNode]
        SFNode   [in,out] metadata       NULL     [X3DMetadataObject]
        SFString [in,out] name           ""
        MFBool   [in,out] visible        []
        SFVec3f  []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f  []       bboxSize       -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            children=[],
            visible=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            **kwargs
        )
        self.visible = visible

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible):
        if visible is None:
            visible = []
        assertMFBool(visible)
        self.__visible = visible

class CADPart(X3DGroupingNode, X3DProductStructureChildNode):
    """
    CADPart : X3DGroupingNode, X3DProductStructureChildNode {
        MFNode     [in]     addChildren
        MFNode     [in]     removeChildren
        SFVec3f    [in,out] center           0 0 0    (-∞,∞)
        MFNode     [in,out] children         []       [CADFace]
        SFNode     [in,out] metadata         NULL     [X3DMetadataObject]
        SFString   [in,out] name             ""
        SFRotation [in,out] rotation         0 0 1 0  [-1,1] or (-∞,∞)
        SFVec3f    [in,out] scale            1 1 1    (0,∞)
        SFRotation [in,out] scaleOrientation 0 0 1 0  [-1,1] or (-∞,∞)
        SFVec3f    [in,out] translation      0 0 0    (-∞,∞)
        SFVec3f    []       bboxCenter       0 0 0    (-∞,∞)
        SFVec3f    []       bboxSize         -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            children=[],
            name="",
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            scaleOrientation=[0.0, 0.0, 1.0, 0.0],
            translation=[0.0, 0.0, 0.0],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            name=name,
            **kwargs
        )
        self.center = center
        self.rotation = rotation
        self.scale = scale
        self.scaleOrientation = scaleOrientation
        self.translation = translation

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        assertSFVec3f(scale)
        assertValidGreaterThan(scale, 0)
        self.__scale = scale

    @property
    def scaleOrientation(self):
        return self.__scaleOrientation

    @scaleOrientation.setter
    def scaleOrientation(self, scaleOrientation):
        if scaleOrientation is None:
            scaleOrientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(scaleOrientation)
        self.__scaleOrientation = scaleOrientation

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

class Collision(X3DGroupingNode, X3DSensorNode):
    """
    Collision : X3DGroupingNode, X3DSensorNode {
        MFNode  [in]     addChildren             [X3DChildNode]
        MFNode  [in]     removeChildren          [X3DChildNode]
        MFNode  [in,out] children       []       [X3DChildNode]
        SFBool  [in,out] enabled        TRUE
        SFNode  [in,out] metadata       NULL     [X3DMetadataObject]
        SFTime  [out]    collideTime
        SFBool  [out]    isActive
        SFVec3f []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f []       bboxSize       -1 -1 -1 [0,∞) or −1 −1 −1
        SFNode  []       proxy          NULL     [X3DChildNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            enabled=True,
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            proxy=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            enabled=enabled,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.proxy = proxy

    @property
    def proxy(self):
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy):
        if proxy is None:
            proxy = None
        assertSFNode(proxy, X3DChildNode)
        self.__proxy = proxy

class EspduTransform(X3DGroupingNode, X3DSensorNode):
    """
    EspduTransform : X3DGroupingNode, X3DSensorNode { 
        MFNode     [in]     addChildren
        MFNode     [in]     removeChildren
        SFFloat    [in]     set_articulationParameterValue0                         (-∞,∞)
        SFFloat    [in]     set_articulationParameterValue1                         (-∞,∞)
        SFFloat    [in]     set_articulationParameterValue2                         (-∞,∞)
        SFFloat    [in]     set_articulationParameterValue3                         (-∞,∞)
        SFFloat    [in]     set_articulationParameterValue4                         (-∞,∞)
        SFFloat    [in]     set_articulationParameterValue5                         (-∞,∞)
        SFFloat    [in]     set_articulationParameterValue6                         (-∞,∞)
        SFFloat    [in]     set_articulationParameterValue7                         (-∞,∞)
        SFString   [in,out] address                                    "localhost"
        SFInt32    [in,out] applicationID                              1            [0,65535]
        SFInt32    [in,out] articulationParameterCount                 0            [0,78]
        MFInt32    [in,out] articulationParameterDesignatorArray       []           [0,255]
        MFInt32    [in,out] articulationParameterChangeIndicatorArray  []           [0,255]
        MFInt32    [in,out] articulationParameterIdPartAttachedToArray []           [0,65535]
        MFInt32    [in,out] articulationParameterTypeArray             []     
        MFFloat    [in,out] articulationParameterArray                 []           (-∞,∞)
        SFVec3f    [in,out] center                                     0 0 0        (-∞,∞)
        MFNode     [in,out] children                                   []
        SFInt32    [in,out] collisionType                              0            [0,255]
        SFInt32    [in,out] deadReckoning                              0            [0,255]
        SFVec3f    [in,out] detonationLocation                         0 0 0        (-∞,∞)
        SFVec3f    [in,out] detonationRelativeLocation                 0 0 0        (-∞,∞)
        SFInt32    [in,out] detonationResult                           0            [0,255]
        SFBool     [in,out] enabled                                    TRUE
        SFInt32    [in,out] entityCategory                             0            [0,255]
        SFInt32    [in,out] entityCountry                              0            [0,65535]
        SFInt32    [in,out] entityDomain                               0            [0,255]
        SFInt32    [in,out] entityExtra                                0            [0,255]
        SFInt32    [in,out] entityID                                   0            [0,65535]
        SFInt32    [in,out] entityKind                                 0            [0,255]
        SFInt32    [in,out] entitySpecific                             0            [0,255]
        SFInt32    [in,out] entitySubCategory                          0            [0,255]
        SFInt32    [in,out] eventApplicationID                         1            [0,65535]
        SFInt32    [in,out] eventEntityID                              0            [0,65535]
        SFInt32    [in,out] eventNumber                                0            [0,65355]
        SFInt32    [in,out] eventSiteID                                0            [0,65535]
        SFBool     [in,out] fired1                                     FALSE
        SFBool     [in,out] fired2                                     FALSE
        SFInt32    [in,out] fireMissionIndex                           0            [0,65535]
        SFFloat    [in,out] firingRange                                0.0          (0,∞)
        SFInt32    [in,out] firingRate                                 0            [0,65535]
        SFInt32    [in,out] forceID                                    0            [0,255]
        SFInt32    [in,out] fuse                                       0            [0,65535]
        SFVec3d    [in,out] geoCoords                                  0 0 0        (-∞,∞)
        SFVec3f    [in,out] linearVelocity                             0 0 0        (-∞,∞)
        SFVec3f    [in,out] linearAcceleration                         0 0 0        (-∞,∞)
        SFString   [in,out] marking                                    ""
        SFNode     [in,out] metadata                                   NULL         [X3DMetadataObject]
        SFString   [in,out] multicastRelayHost                         ""
        SFInt32    [in,out] multicastRelayPort                         0             
        SFInt32    [in,out] munitionApplicationID                      1            [0,65535]
        SFVec3f    [in,out] munitionEndPoint                           0 0 0        (-∞,∞)
        SFInt32    [in,out] munitionEntityID                           0            [0,65535]
        SFInt32    [in,out] munitionQuantity                           0            [0,65535]
        SFInt32    [in,out] munitionSiteID                             0            [0,65535]
        SFVec3f    [in,out] munitionStartPoint                         0 0 0        (-∞,∞)
        SFString   [in,out] networkMode                                "standAlone" ["standAlone"|
                                                                                    "networkReader"|
                                                                                    "networkWriter"]
        SFInt32    [in,out] port                                       0            [0,65535]
        SFTime     [in,out] readInterval                               0.1          [0,∞)
        SFRotation [in,out] rotation                                   0 0 1 0      (-∞,∞)|[-1,1]
        SFVec3f    [in,out] scale                                      1 1 1        (-∞,∞)
        SFRotation [in,out] scaleOrientation                           0 0 1 0      (-∞,∞)|[-1,1]
        SFInt32    [in,out] siteID                                     0            [0,65535]
        SFVec3f    [in,out] translation                                0 0 0        (-∞,∞)
        SFInt32    [in,out] warhead                                    0            [0,65535]
        SFTime     [in,out] writeInterval                              1.0          [0,∞)
        SFFloat    [out]    articulationParameterValue0_changed        0.0          (-∞,∞)
        SFFloat    [out]    articulationParameterValue1_changed        0.0          (-∞,∞)
        SFFloat    [out]    articulationParameterValue2_changed        0.0          (-∞,∞)
        SFFloat    [out]    articulationParameterValue3_changed        0.0          (-∞,∞)
        SFFloat    [out]    articulationParameterValue4_changed        0.0          (-∞,∞)
        SFFloat    [out]    articulationParameterValue5_changed        0.0          (-∞,∞)
        SFFloat    [out]    articulationParameterValue6_changed        0.0          (-∞,∞)
        SFFloat    [out]    articulationParameterValue7_changed        0.0          (-∞,∞)
        SFTime     [out]    collideTime                                0            [0,∞)
        SFTime     [out]    detonateTime                               0            [0,∞)
        SFTime     [out]    firedTime                                  0            [0,∞)
        SFBool     [out]    isActive                                   FALSE
        SFBool     [out]    isCollided                                 FALSE                     
        SFBool     [out]    isDetonated                                FALSE                    
        SFBool     [out]    isNetworkReader                            FALSE
        SFBool     [out]    isNetworkWriter                            FALSE
        SFBool     [out]    isRtpHeaderHeard                           FALSE
        SFBool     [out]    isStandAlone                               FALSE
        SFTime     [out]    timestamp                                  0            [0,∞)
        SFVec3f    []       bboxCenter                                 0 0 0        (-∞,∞)
        SFVec3f    []       bboxSize                                   -1 -1 -1     [0,∞) or −1 −1 −1
        MFString   []       geoSystem                                  ["GD","WE"]  [see 25.2.3]
        SFBool     []       rtpHeaderExpected                          FALSE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            address="localhost",
            applicationId=1,
            articulationParameterCount=0,
            articulationParameterDesignatorArray=[],
            articulationParameterChangeIndicatorArray=[],
            articulationParameterIdPartAttachedToArray=[],
            articulationParameterTypeArray=[],
            articulationParameterArray=[],
            center=[0.0, 0.0, 0.0],
            children=[],
            collisionType=0,
            deadReckoning=0,
            detonationLocation=[0.0, 0.0, 0.0],
            detonationRelativeLocation=[0.0, 0.0, 0.0],
            detonationResult=0,
            enabled=True,
            entityCategory=0,
            entityCountry=0,
            entityDomain=0,
            entityExtra=0,
            entityID=0,
            entityKind=0,
            entitySpecific=0,
            entitySubCategory=0,
            eventApplicationID=1,
            eventEntityID=0,
            eventNumber=0,
            eventSiteID=0,
            fired1=False,
            fired2=False,
            fireMissionIndex=0,
            firingRange=0.0,
            firingRate=0,
            forceID=0,
            fuse=0,
            geoCoords=[0.0, 0.0, 0.0],
            linearVelocity=[0.0, 0.0, 0.0],
            linearAcceleration=[0.0, 0.0, 0.0],
            marking="",
            multicastRelayHost="",
            multicastRelayPort=0,
            munitionApplicationID=1,
            munitionEndPoint=[0.0, 0.0, 0.0],
            munitionEntityID=0,
            munitionQuantity=0,
            munitionSiteID=0,
            munitionStartPoint=[0.0, 0.0, 0.0],
            networkMode="standAlone",
            port=0,
            readInterval=0.1,
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            scaleOrientation=[0.0, 0.0, 1.0, 0.0],
            siteID=0,
            translation=[0.0, 0.0, 0.0],
            warhead=0,
            writeInterval=1.0,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            geoSystem=["GD", "WE"],
            rtpHeaderExpected=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children
            **kwargs
        )
        self.address = address
        self.applicationId = applicationId
        self.articulationParameterCount = articulationParameterCount
        self.articulationParameterDesignatorArray = articulationParameterDesignatorArray
        self.articulationParameterChangeIndicatorArray = articulationParameterChangeIndicatorArray
        self.articulationParameterIdPartAttachedToArray = articulationParameterIdPartAttachedToArray
        self.articulationParameterTypeArray = articulationParameterTypeArray
        self.articulationParameterArray = articulationParameterArray
        self.center = center
        self.collisionType = collisionType
        self.deadReckoning = deadReckoning
        self.detonationLocation = detonationLocation
        self.detonationRelativeLocation = detonationRelativeLocation
        self.detonationResult = detonationResult
        self.entityCategory = entityCategory
        self.entityCountry = entityCountry
        self.entityDomain = entityDomain
        self.entityExtra = entityExtra
        self.entityID = entityID
        self.entityKind = entityKind
        self.entitySpecific = entitySpecific
        self.entitySubCategory = entitySubCategory
        self.eventApplicationID = eventApplicationID
        self.eventEntityID = eventEntityID
        self.eventNumber = eventNumber
        self.eventSiteID = eventSiteID
        self.fired1 = fired1
        self.fired2 = fired2
        self.fireMissionIndex = fireMissionIndex
        self.firingRange = firingRange
        self.firingRate = firingRate
        self.forceID = forceID
        self.fuse = fuse
        self.geoCoords = geoCoords
        self.linearVelocity = linearVelocity
        self.linearAcceleration = linearAcceleration
        self.marking = marking
        self.multicastRelayHost = multicastRelayHost
        self.multicastRelayPort = multicastRelayPort
        self.munitionApplicationID = munitionApplicationID
        self.munitionEndPoint = munitionEndPoint
        self.munitionEntityID = munitionEntityID
        self.munitionQuantity = munitionQuantity
        self.munitionSiteID = munitionSiteID
        self.munitionStartPoint = munitionStartPoint
        self.networkMode = networkMode
        self.port = port
        self.readInterval = readInterval
        self.rotation = rotation
        self.scale = scale
        self.scaleOrientation = scaleOrientation
        self.siteID = siteID
        self.translation = translation
        self.warhead = warhead
        self.writeInterval = writeInterval
        self.geoSystem = geoSystem
        self.rtpHeaderExpected = rtpHeaderExpected

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if address is None:
            address = "localhost"
        assertSFString(address)
        self.__address = address

    @property
    def applicationID(self):
        return self.__applicationID

    @applicationID.setter
    def applicationID(self, applicationID):
        if applicationID is None:
            applicationID = 1
        assertSFInt32(applicationID)
        assertValidGreaterThanEquals(applicationID, 0)
        assertValidLessThanEquals(applicationID, 65535)
        self.__applicationID = applicationID

    @property
    def articulationParameterCount(self):
        return self.__articulationParameterCount

    @articulationParameterCount.setter
    def articulationParameterCount(self, articulationParameterCount):
        if articulationParameterCount is None:
            articulationParameterCount = 0
        assertSFInt32(articulationParameterCount)
        assertValidGreaterThanEquals(articulationParameterCount, 0)
        assertValidLessThanEquals(articulationParameterCount, 78)
        self.__articulationParameterCount = articulationParameterCount

    @property
    def articulationParameterDesignatorArray(self):
        return self.__articulationParameterDesignatorArray

    @articulationParameterDesignatorArray.setter
    def articulationParameterDesignatorArray(self, articulationParameterDesignatorArray):
        if articulationParameterDesignatorArray is None:
            articulationParameterDesignatorArray = []
        assertMFInt32(articulationParameterDesignatorArray)
        assertValidGreaterThanEquals(articulationParameterDesignatorArray, 0)
        assertValidLessThanEquals(articulationParameterDesignatorArray, 255)
        self.__articulationParameterDesignatorArray = articulationParameterDesignatorArray

    @property
    def articulationParameterChangeIndicatorArray(self):
        return self.__articulationParameterChangeIndicatorArray

    @articulationParameterChangeIndicatorArray.setter
    def articulationParameterChangeIndicatorArray(self, articulationParameterChangeIndicatorArray):
        if articulationParameterChangeIndicatorArray is None:
            articulationParameterChangeIndicatorArray = []
        assertMFInt32(articulationParameterChangeIndicatorArray)
        assertValidGreaterThanEquals(articulationParameterChangeIndicatorArray, 0)
        assertValidLessThanEquals(articulationParameterChangeIndicatorArray, 255)
        self.__articulationParameterChangeIndicatorArray = articulationParameterChangeIndicatorArray

    @property
    def articulationParameterIdPartAttachedToArray(self):
        return self.__articulationParameterIdPartAttachedToArray

    @articulationParameterIdPartAttachedToArray.setter
    def articulationParameterIdPartAttachedToArray(self, articulationParameterIdPartAttachedToArray):
        if articulationParameterIdPartAttachedToArray is None:
            articulationParameterIdPartAttachedToArray = []
        assertMFInt32(articulationParameterIdPartAttachedToArray)
        assertValidGreaterThanEquals(articulationParameterIdPartAttachedToArray, 0)
        assertValidLessThanEquals(articulationParameterIdPartAttachedToArray, 65535)
        self.__articulationParameterIdPartAttachedToArray = articulationParameterIdPartAttachedToArray

    @property
    def articulationParameterTypeArray(self):
        return self.__articulationParameterTypeArray

    @articulationParameterTypeArray.setter
    def articulationParameterTypeArray(self, articulationParameterTypeArray):
        if articulationParameterTypeArray is None:
            articulationParameterTypeArray = []
        assertMFInt32(articulationParameterTypeArray)
        self.__articulationParameterTypeArray = articulationParameterTypeArray

    @property
    def articulationParameterArray(self):
        return self.__articulationParameterArray

    @articulationParameterArray.setter
    def articulationParameterArray(self, articulationParameterArray):
        if articulationParameterArray is None:
            articulationParameterArray = []
        assertMFFloat(articulationParameterArray)
        self.__articulationParameterArray = articulationParameterArray

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def collisionType(self):
        return self.__collisionType

    @collisionType.setter
    def collisionType(self, collisionType):
        if collisionType is None:
            collisionType = True
        assertSFInt32(collisionType)
        assertValidGreaterThanEquals(collisionType, 0)
        assertValidLessThanEquals(collisionType, 255)
        self.__collisionType = collisionType

    @property
    def deadReckoning(self):
        return self.__deadReckoning

    @deadReckoning.setter
    def deadReckoning(self, deadReckoning):
        if deadReckoning is None:
            deadReckoning = True
        assertSFInt32(deadReckoning)
        assertValidGreaterThanEquals(deadReckoning, 0)
        assertValidLessThanEquals(deadReckoning, 255)
        self.__deadReckoning = deadReckoning

    @property
    def detonationLocation(self):
        return self.__detonationLocation

    @detonationLocation.setter
    def detonationLocation(self, detonationLocation):
        if detonationLocation is None:
            detonationLocation = [0.0, 0.0, 0.0]
        assertSFVec3f(detonationLocation)
        self.__detonationLocation = detonationLocation

    @property
    def detonationRelativeLocation(self):
        return self.__detonationRelativeLocation

    @detonationRelativeLocation.setter
    def detonationRelativeLocation(self, detonationRelativeLocation):
        if detonationRelativeLocation is None:
            detonationRelativeLocation = [0.0, 0.0, 0.0]
        assertSFVec3f(detonationRelativeLocation)
        self.__detonationRelativeLocation = detonationRelativeLocation

    @property
    def detonationResult(self):
        return self.__detonationResult

    @detonationResult.setter
    def detonationResult(self, detonationResult):
        if detonationResult is None:
            detonationResult = 0
        assertSFInt32(detonationResult)
        assertValidGreaterThanEquals(detonationResult, 0)
        assertValidLessThanEquals(detonationResult, 255)
        self.__detonationResult = detonationResult

    @property
    def entityCategory(self):
        return self.__entityCategory

    @entityCategory.setter
    def entityCategory(self, entityCategory):
        if entityCategory is None:
            entityCategory = 0
        assertSFInt32(entityCategory)
        assertValidGreaterThanEquals(entityCategory, 0)
        assertValidLessThanEquals(entityCategory, 255)
        self.__entityCategory = entityCategory

    @property
    def entityCountry(self):
        return self.__entityCountry

    @entityCountry.setter
    def entityCountry(self, entityCountry):
        if entityCountry is None:
            entityCountry = 0
        assertSFInt32(entityCountry)
        assertValidGreaterThanEquals(entityCountry, 0)
        assertValidLessThanEquals(entityCountry, 65535)
        self.__entityCountry = entityCountry

    @property
    def entityDomain(self):
        return self.__entityDomain

    @entityDomain.setter
    def entityDomain(self, entityDomain):
        if entityDomain is None:
            entityDomain = 0
        assertSFInt32(entityDomain)
        assertValidGreaterThanEquals(entityDomain, 0)
        assertValidLessThanEquals(entityDomain, 255)
        self.__entityDomain = entityDomain

    @property
    def entityExtra(self):
        return self.__entityExtra

    @entityExtra.setter
    def entityExtra(self, entityExtra):
        if entityExtra is None:
            entityExtra = 0
        assertSFInt32(entityExtra)
        assertValidGreaterThanEquals(entityExtra, 0)
        assertValidLessThanEquals(entityExtra, 255)
        self.__entityExtra = entityExtra

    @property
    def entityID(self):
        return self.__entityID

    @entityID.setter
    def entityID(self, entityID):
        if entityID is None:
            entityID = 0
        assertSFInt32(entityID)
        assertValidGreaterThanEquals(entityID, 0)
        assertValidLessThanEquals(entityID, 65535)
        self.__entityID = entityID

    @property
    def entityKind(self):
        return self.__entityKind

    @entityKind.setter
    def entityKind(self, entityKind):
        if entityKind is None:
            entityKind = 0
        assertSFInt32(entityKind)
        assertValidGreaterThanEquals(entityKind, 0)
        assertValidLessThanEquals(entityKind, 255)
        self.__entityKind = entityKind

    @property
    def entitySpecific(self):
        return self.__entitySpecific

    @entitySpecific.setter
    def entitySpecific(self, entitySpecific):
        if entitySpecific is None:
            entitySpecific = 0
        assertSFInt32(entitySpecific)
        assertValidGreaterThanEquals(entitySpecific, 0)
        assertValidLessThanEquals(entitySpecific, 255)
        self.__entitySpecific = entitySpecific

    @property
    def entitySubCategory(self):
        return self.__entitySubCategory

    @entitySubCategory.setter
    def entitySubCategory(self, entitySubCategory):
        if entitySubCategory is None:
            entitySubCategory = 0
        assertSFInt32(entitySubCategory)
        assertValidGreaterThanEquals(entitySubCategory, 0)
        assertValidLessThanEquals(entitySubCategory, 255)
        self.__entitySubCategory = entitySubCategory

    @property
    def eventApplicationID(self):
        return self.__eventApplicationID

    @eventApplicationID.setter
    def eventApplicationID(self, eventApplicationID):
        if eventApplicationID is None:
            eventApplicationID = 0
        assertSFInt32(eventApplicationID)
        assertValidGreaterThanEquals(eventApplicationID, 0)
        assertValidLessThanEquals(eventApplicationID, 65535)
        self.__eventApplicationID = eventApplicationID

    @property
    def eventEntityID(self):
        return self.__eventEntityID

    @eventEntityID.setter
    def eventEntityID(self, eventEntityID):
        if eventEntityID is None:
            eventEntityID = 0
        assertSFInt32(eventEntityID)
        assertValidGreaterThanEquals(eventEntityID, 0)
        assertValidLessThanEquals(eventEntityID, 65535)
        self.__eventEntityID = eventEntityID

    @property
    def eventNumber(self):
        return self.__eventNumber

    @eventNumber.setter
    def eventNumber(self, eventNumber):
        if eventNumber is None:
            eventNumber = 0
        assertSFInt32(eventNumber)
        assertValidGreaterThanEquals(eventNumber, 0)
        assertValidLessThanEquals(eventNumber, 65535)
        self.__eventNumber = eventNumber

    @property
    def eventSiteID(self):
        return self.__eventSiteID

    @eventSiteID.setter
    def eventSiteID(self, eventSiteID):
        if eventSiteID is None:
            eventSiteID = 0
        assertSFInt32(eventSiteID)
        assertValidGreaterThanEquals(eventSiteID, 0)
        assertValidLessThanEquals(eventSiteID, 65535)
        self.__eventSiteID = eventSiteID

    @property
    def fired1(self):
        return self.__fired1

    @fired1.setter
    def fired1(self, fired1):
        if fired1 is None:
            fired1 = False
        assertSFBool(fired1)
        self.__fired1 = fired1

    @property
    def fired2(self):
        return self.__fired2

    @fired2.setter
    def fired2(self, fired2):
        if fired2 is None:
            fired2 = False
        assertSFBool(fired2)
        self.__fired2 = fired2

    @property
    def fireMissionIndex(self):
        return self.__fireMissionIndex

    @fireMissionIndex.setter
    def fireMissionIndex(self, fireMissionIndex):
        if fireMissionIndex is None:
            fireMissionIndex = 0
        assertSFInt32(fireMissionIndex)
        assertValidGreaterThanEquals(fireMissionIndex, 0)
        assertValidLessThanEquals(fireMissionIndex, 65535)
        self.__fireMissionIndex = fireMissionIndex

    @property
    def firingRange(self):
        return self.__firingRange

    @firingRange.setter
    def firingRange(self, firingRange):
        if firingRange is None:
            firingRange = 0.0
        assertSFFloat(firingRange)
        assertValidGreaterThan(firingRange, 0)
        self.__firingRange = firingRange

    @property
    def firingRate(self):
        return self.__firingRate

    @firingRate.setter
    def firingRate(self, firingRate):
        if firingRate is None:
            firingRate = 0
        assertSFInt32(firingRate)
        assertValidGreaterThanEquals(firingRate, 0)
        assertValidLessThanEquals(firingRate, 65535)
        self.__firingRate = firingRate

    @property
    def forceID(self):
        return self.__forceID

    @forceID.setter
    def forceID(self, forceID):
        if forceID is None:
            forceID = 0
        assertSFInt32(forceID)
        assertValidGreaterThanEquals(forceID, 0)
        assertValidLessThanEquals(forceID, 255)
        self.__forceID = forceID

    @property
    def fuse(self):
        return self.__fuse

    @fuse.setter
    def fuse(self, fuse):
        if fuse is None:
            fuse = 0
        assertSFInt32(fuse)
        assertValidGreaterThanEquals(fuse, 0)
        assertValidLessThanEquals(fuse, 65535)
        self.__fuse = fuse

    @property
    def geoCoords(self):
        return self.__geoCoords

    @geoCoords.setter
    def geoCoords(self, geoCoords):
        if geoCoords is None:
            geoCoords = [0.0, 0.0, 0.0]
        assertSFVec3d(geoCoords)
        self.__geoCoords = geoCoords

    @property
    def linearVelocity(self):
        return self.__linearVelocity

    @linearVelocity.setter
    def linearVelocity(self, linearVelocity):
        if linearVelocity is None:
            linearVelocity = [0.0, 0.0, 0.0]
        assertSFVec3f(linearVelocity)
        self.__linearVelocity = linearVelocity

    @property
    def linearAcceleration(self):
        return self.__linearAcceleration

    @linearAcceleration.setter
    def linearAcceleration(self, linearAcceleration):
        if linearAcceleration is None:
            linearAcceleration = [0.0, 0.0, 0.0]
        assertSFVec3f(linearAcceleration)
        self.__linearAcceleration = linearAcceleration

    @property
    def marking(self):
        return self.__marking

    @marking.setter
    def marking(self, marking):
        if marking is None:
            marking = ""
        assertSFString(marking)
        self.__marking = marking

    @property
    def multicastRelayHost(self):
        return self.__multicastRelayHost

    @multicastRelayHost.setter
    def multicastRelayHost(self, multicastRelayHost):
        if multicastRelayHost is None:
            multicastRelayHost = ""
        assertSFString(multicastRelayHost)
        self.__multicastRelayHost = multicastRelayHost

    @property
    def multicastRelayPort(self):
        return self.__multicastRelayPort

    @multicastRelayPort.setter
    def multicastRelayPort(self, multicastRelayPort):
        if multicastRelayPort is None:
            multicastRelayPort = 0
        assertSFInt32(multicastRelayPort)
        self.__multicastRelayPort = multicastRelayPort

    @property
    def munitionApplicationID(self):
        return self.__munitionApplicationID

    @munitionApplicationID.setter
    def munitionApplicationID(self, munitionApplicationID):
        if munitionApplicationID is None:
            munitionApplicationID = 1
        assertSFInt32(munitionApplicationID)
        assertValidGreaterThanEquals(munitionApplicationID, 0)
        assertValidLessThanEquals(munitionApplicationID, 65535)
        self.__munitionApplicationID = munitionApplicationID

    @property
    def munitionEndPoint(self):
        return self.__munitionEndPoint

    @munitionEndPoint.setter
    def munitionEndPoint(self, munitionEndPoint):
        if munitionEndPoint is None:
            munitionEndPoint = [0.0, 0.0, 0.0]
        assertSFVec3f(munitionEndPoint)
        self.__munitionEndPoint = munitionEndPoint

    @property
    def munitionEntityID(self):
        return self.__munitionEntityID

    @munitionEntityID.setter
    def munitionEntityID(self, munitionEntityID):
        if munitionEntityID is None:
            munitionEntityID = 0
        assertSFInt32(munitionEntityID)
        assertValidGreaterThanEquals(munitionEntityID, 0)
        assertValidLessThanEquals(munitionEntityID, 65535)
        self.__munitionEntityID = munitionEntityID

    @property
    def munitionQuantity(self):
        return self.__munitionQuantity

    @munitionQuantity.setter
    def munitionQuantity(self, munitionQuantity):
        if munitionQuantity is None:
            munitionQuantity = 0
        assertSFInt32(munitionQuantity)
        assertValidGreaterThanEquals(munitionQuantity, 0)
        assertValidLessThanEquals(munitionQuantity, 65535)
        self.__munitionQuantity = munitionQuantity

    @property
    def munitionSiteID(self):
        return self.__munitionSiteID

    @munitionSiteID.setter
    def munitionSiteID(self, munitionSiteID):
        if munitionSiteID is None:
            munitionSiteID = 0
        assertSFInt32(munitionSiteID)
        assertValidGreaterThanEquals(munitionSiteID, 0)
        assertValidLessThanEquals(munitionSiteID, 65535)
        self.__munitionSiteID = munitionSiteID

    @property
    def munitionStartPoint(self):
        return self.__munitionStartPoint

    @munitionStartPoint.setter
    def munitionStartPoint(self, munitionStartPoint):
        if munitionStartPoint is None:
            munitionStartPoint = [0.0, 0.0, 0.0]
        assertSFVec3f(munitionStartPoint)
        self.__munitionStartPoint = munitionStartPoint

    @property
    def networkMode(self):
        return self.__networkMode

    @networkMode.setter
    def networkMode(self, networkMode):
        if networkMode is None:
            networkMode = "standAlone"
        assertValidNetworkMode(networkMode)
        self.__networkMode = networkMode

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if port is None:
            port = 0
        assertSFInt32(port)
        assertValidGreaterThanEquals(port, 0)
        assertValidLessThanEquals(port, 65535)
        self.__port = port

    @property
    def readInterval(self):
        return self.__readInterval

    @readInterval.setter
    def readInterval(self, readInterval):
        if readInterval is None:
            readInterval = 0.1
        assertSFTime(readInterval)
        assertValidGreaterThanEquals(readInterval, 0)
        self.__readInterval = readInterval

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        assertSFVec3f(scale)
        self.__scale = scale

    @property
    def scaleOrientation(self):
        return self.__scaleOrientation

    @scaleOrientation.setter
    def scaleOrientation(self, scaleOrientation):
        if scaleOrientation is None:
            scaleOrientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(scaleOrientation)
        self.__scaleOrientation = scaleOrientation

    @property
    def siteID(self):
        return self.__siteID

    @siteID.setter
    def siteID(self, siteID):
        if siteID is None:
            siteID = 0
        assertSFInt32(siteID)
        assertValidGreaterThanEquals(siteID, 0)
        assertValidLessThanEquals(siteID, 65535)
        self.__siteID = siteID

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

    @property
    def warhead(self):
        return self.__warhead

    @warhead.setter
    def warhead(self, warhead):
        if warhead is None:
            warhead = 0
        assertSFInt32(warhead)
        assertValidGreaterThanEquals(warhead, 0)
        assertValidLessThanEquals(warhead, 65535)
        self.__warhead = warhead

    @property
    def writeInterval(self):
        return self.__writeInterval

    @writeInterval.setter
    def writeInterval(self, writeInterval):
        if writeInterval is None:
            writeInterval = 0.1
        assertSFTime(writeInterval)
        assertValidGreaterThanEquals(writeInterval, 0)
        self.__writeInterval = writeInterval

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

    @property
    def rtpHeaderExpected(self):
        return self.__rtpHeaderExpected

    @rtpHeaderExpected.setter
    def rtpHeaderExpected(self, rtpHeaderExpected):
        if rtpHeaderExpected is None:
            rtpHeaderExpected = False
        assertSFBool(rtpHeaderExpected)
        self.__rtpHeaderExpected = rtpHeaderExpected

class GeoLocation(X3DGroupingNode):
    """
    GeoLocation : X3DGroupingNode {
        MFNode   [in]     addChildren                [X3DChildNode]
        MFNode   [in]     removeChildren             [X3DChildNode]
        MFNode   [in,out] children       []          [X3DChildNode]
        SFVec3d  [in,out] geoCoords      0 0 0       (-∞,∞)
        SFNode   [in,out] metadata       NULL        [X3DMetadataObject]
        SFNode   []       geoOrigin      NULL        [GeoOrigin] (deprecated)
        MFString []       geoSystem      ["GD","WE"] [see 25.2.3]
        SFVec3f  []       bboxCenter     0 0 0       (-∞,∞)
        SFVec3f  []       bboxSize       -1 -1 -1    [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            geoCoords=[0.0, 0.0, 0.0],
            geoOrigin=None,
            geoSystem=["GD", "WE"],
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.geoCoords = geoCoords
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem

    @property
    def geoCoords(self):
        return self.__geoCoords

    @geoCoords.setter
    def geoCoords(self, geoCoords):
        if geoCoords is None:
            geoCoords = [0.0, 0.0, 0.0]
        assertSFVec3d(geoCoords)
        self.__geoCoords = geoCoords

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class GeoTransform(X3DGroupingNode): 
    """
    GeoTransform : X3DGroupingNode {
        MFNode     [in]     addChildren                  [X3DChildNode]
        MFNode     [in]     removeChildren               [X3DChildNode]
        MFNode     [in,out] children         []          [X3DChildNode]
        SFVec3d    [in,out] geoCenter        0 0 0       (-∞,∞)
        SFNode     [in,out] metadata         NULL        [X3DMetadataObject]
        SFRotation [in,out] rotation         0 0 1 0     [-1,1] or (-∞,∞)
        SFVec3f    [in,out] scale            1 1 1       (0,∞)
        SFRotation [in,out] scaleOrientation 0 0 1 0     [-1,1] or (-∞,∞)
        SFVec3f    [in,out] translation      0 0 0       (-∞,∞)
        SFVec3f    []       bboxCenter       0 0 0       (-∞,∞)
        SFVec3f    []       bboxSize         -1 -1 -1    [0,∞) or −1 −1 −1
        SFNode     []       geoOrigin        NULL        [GeoOrigin] (deprecated)
        MFString   []       geoSystem        ["GD","WE"] [see 25.2.3]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            geoCenter=[0.0, 0.0, 0.0],
            children=[],
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            scaleOrientation=[0.0, 0.0, 1.0, 0.0],
            translation=[0.0, 0.0, 0.0],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            geoOrigin=None,
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.geoCenter = geoCenter
        self.rotation = rotation
        self.scale = scale
        self.scaleOrientation = scaleOrientation
        self.translation = translation
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0, 0, 0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0, 0, 1, 0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1, 1, 1]
        assertSFVec3f(scale)
        assertValidGreaterThan(scale, 0)
        self.__scale = scale

    @property
    def scaleOrientation(self):
        return self.__scaleOrientation

    @scaleOrientation.setter
    def scaleOrientation(self, scaleOrientation):
        if scaleOrientation is None:
            scaleOrientation = [0, 0, 1, 0]
        assertSFRotation(scaleOrientation)
        self.__scaleOrientation = scaleOrientation

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0, 0, 0]
        assertSFVec3f(translation)
        self.__translation = translation

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class Group(X3DGroupingNode):
    """
    Group : X3DGroupingNode {
        MFNode  [in]     addChildren             [X3DChildNode]
        MFNode  [in]     removeChildren          [X3DChildNode]
        MFNode  [in,out] children       []       [X3DChildNode]
        SFNode  [in,out] metadata       NULL     [X3DMetadataObject]
        SFVec3f []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f []       bboxSize       -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs

    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )

class HAnimJoint(X3DGroupingNode):
    """
    HAnimJoint : X3DGroupingNode {
        MFNode     [in]     addChildren               [HAnimJoint,HAnimSegment,HAnimSite]
        MFNode     [in]     removeChildren            [HAnimJoint,HAnimSegment,HAnimSite]
        SFVec3f    [in,out] center           0 0 0    (-∞,∞)
        MFNode     [in,out] children         []       [HAnimJoint,HAnimSegment,HAnimSite]
        MFNode     [in,out] displacers       []       [HAnimDisplacer]
        SFRotation [in,out] limitOrientation 0 0 1 0  (-∞,∞)|[-1,1]
        MFFloat    [in,out] llimit           []       (-∞,∞)
        SFNode     [in,out] metadata         NULL     [X3DMetadataObject]
        SFString   [in,out] name             ""
        SFRotation [in,out] rotation         0 0 1 0  (-∞,∞)|[-1,1]
        SFVec3f    [in,out] scale            1 1 1    (0,∞)
        SFRotation [in,out] scaleOrientation 0 0 1 0  (-∞,∞)|[-1,1]
        MFInt32    [in,out] skinCoordIndex   []
        MFFloat    [in,out] skinCoordWeight  []
        MFFloat    [in,out] stiffness        [0 0 0]  [0,1]
        SFVec3f    [in,out] translation      0 0 0    (-∞,∞)
        MFFloat    [in,out] ulimit           []       (-∞,∞)
        SFVec3f    []       bboxCenter       0 0 0    (-∞,∞)
        SFVec3f    []       bboxSize         -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            center=[0.0, 0.0, 0.0],
            displacers=[],
            limitOrientation=[0.0, 0.0, 1.0, 0.0],
            limit=[],
            name="",
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            scaleOrientation=[0.0, 0.0, 1.0, 0.0],
            skinCoordIndex=[],
            skinCoordWeight=[],
            stiffness=[[0.0, 0.0, 0.0]],
            translation=[0.0, 0.0, 0.0],
            ulimit=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            **kwargs
        )
        self.center = center
        self.name = name
        self.displacers = displacers
        self.limitOrientation = limitOrientation
        self.limit = limit
        self.rotation = rotation
        self.scale = scale
        self.scaleOrientation = scaleOrientation
        self.skinCoordIndex = skinCoordIndex
        self.skinCoordWeight = skinCoordWeight
        self.stiffness = stiffness
        self.translation = translation
        self.ulimit = ulimit
        
    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def displacers(self):
        return self.__displacers

    @displacers.setter
    def displacers(self, displacers):
        if displacers is None:
            displacers = []
        assertMFNode(displacers, HAnimDisplacer)
        self.__displacers = displacers

    @property
    def limitOrientation(self):
        return self.__limitOrientation

    @limitOrientation.setter
    def limitOrientation(self, limitOrientation):
        if limitOrientation is None:
            limitOrientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(limitOrientation)
        self.__limitOrientation = limitOrientation

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        if limit is None:
            limit = []
        assertMFFloat(limit)
        self.__limit = limit

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            name = ""
        assertSFString(name)
        self.__name = name

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        assertSFVec3f(scale)
        assertValidGreaterThan(scale, 0)
        self.__scale = scale

    @property
    def scaleOrientation(self):
        return self.__scaleOrientation

    @scaleOrientation.setter
    def scaleOrientation(self, scaleOrientation):
        if scaleOrientation is None:
            scaleOrientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(scaleOrientation)
        self.__scaleOrientation = scaleOrientation

    @property
    def skinCoordIndex(self):
        return self.__skinCoordIndex

    @skinCoordIndex.setter
    def skinCoordIndex(self, skinCoordIndex):
        if skinCoordIndex is None:
            skinCoordIndex = []
        assertMFInt32(skinCoordIndex)
        self.__skinCoordIndex = skinCoordIndex

    @property
    def skinCoordWeight(self):
        return self.__skinCoordWeight

    @skinCoordWeight.setter
    def skinCoordWeight(self, skinCoordWeight):
        if skinCoordWeight is None:
            skinCoordWeight = []
        assertMFFloat(skinCoordWeight)
        self.__skinCoordWeight = skinCoordWeight

    @property
    def stiffness(self):
        return self.__stiffness

    @stiffness.setter
    def stiffness(self, stiffness):
        if stiffness is None:
            stiffness = [0.0, 0.0, 0.0]
        assertMFFloat(stiffness)
        assertValidGreaterThanEquals(stiffness, 0)
        assertValidLessThanEquals(stiffness, 1)
        self.__stiffness = stiffness

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

    @property
    def ulimit(self):
        return self.__ulimit

    @ulimit.setter
    def ulimit(self, ulimit):
        if ulimit is None:
            ulimit = []
        assertMFFloat(ulimit)
        self.__ulimit = ulimit

class HAnimSegment(X3DGroupingNode): 
    """
    HAnimSegment : X3DGroupingNode {
        MFNode   [in]     addChildren                          [X3DChildNode]
        MFNode   [in]     removeChildren                       [X3DChildNode]
        SFVec3f  [in,out] centerOfMass     0 0 0               (-∞,∞)
        MFNode   [in,out] children         []                  [X3DChildNode]
        SFNode   [in,out] coord            NULL                [X3DCoordinateNode]
        MFNode   [in,out] displacers       []                  [HAnimDisplacer]
        SFFloat  [in,out] mass             0                   [0,∞)
        SFNode   [in,out] metadata         NULL                [X3DMetadataObject]
        MFFloat  [in,out] momentsOfInertia [0 0 0 0 0 0 0 0 0] [0,∞)
        SFString [in,out] name             ""
        SFVec3f  []       bboxCenter       0 0 0               (-∞,∞)
        SFVec3f  []       bboxSize         -1 -1 -1            [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            centerOfMass=[0.0, 0.0, 0.0],
            children=[],
            coord=None,
            displacers=[],
            mass=0.0,
            momentsOfInertia=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            name="",
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            **kwargs
        )
        self.centerOfMass = centerOfMass
        self.coord = coord
        self.displacers = displacers
        self.mass = mass
        self.momentsOfInertia = momentsOfInertia
        self.name = name

    @property
    def centerOfMass(self):
        return self.__centerOfMass

    @centerOfMass.setter
    def centerOfMass(self, centerOfMass):
        if centerOfMass is None:
            centerOfMass = [0.0, 0.0, 0.0]
        assertMFVec3f(centerOfMass)
        self.__centerOfMass = centerOfMass

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, coord):
        if coord is None:
            coord = None
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

    @property
    def displacers(self):
        return self.__displacers

    @displacers.setter
    def displacers(self, displacers):
        if displacers is None:
            displacers = []
        assertMFNode(displacers, HAnimDisplacer)
        self.__displacers = displacers

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        if mass is None:
            mass = 0.0
        assertSFFloat(mass)
        assertValidGreaterThanEquals(mass, 0)
        self.__mass = mass

    @property
    def momentsOfInertia(self):
        return self.__momentsOfInertia

    @momentsOfInertia.setter
    def momentsOfInertia(self, momentsOfInertia):
        if momentsOfInertia is None:
            momentsOfInertia = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        assertMFFloat(momentsOfInertia)
        assertValidGreaterThanEquals(momentsOfInertia, 0)
        self.__momentsOfInertia = momentsOfInertia

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            name = ""
        assertSFString(name)
        self.__name = name

class HAnimSite(X3DGroupingNode): 
    """
    HAnimSite : X3DGroupingNode {
        MFNode     [in]     addChildren               [X3DChildNode]
        MFNode     [in]     removeChildren            [X3DChildNode]
        SFVec3f    [in,out] center           0 0 0    (-∞,∞)
        MFNode     [in,out] children         []       [X3DChildNode]
        SFNode     [in,out] metadata         NULL     [X3DMetadataObject]
        SFString   [in,out] name             ""
        SFRotation [in,out] rotation         0 0 1 0  (-∞,∞)|[-1,1]
        SFVec3f    [in,out] scale            1 1 1    (0,∞)
        SFRotation [in,out] scaleOrientation 0 0 1 0  (-∞,∞)|[-1,1]
        SFVec3f    [in,out] translation      0 0 0    (-∞,∞)|[-1,1]
        SFVec3f    []       bboxCenter       0 0 0    (-∞,∞)
        SFVec3f    []       bboxSize         -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            children=[],
            name="",
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            scaleOrientation=[0.0, 0.0, 1.0, 0.0],
            translation=[0.0, 0.0, 0.0],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            **kwargs
        )
        self.center = center
        self.name = name
        self.rotation = rotation
        self.scale = scale
        self.scaleOrientation = scaleOrientation
        self.translation = translation

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            name = ""
        assertSFString(name)
        self.__name = name

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        assertSFVec3f(scale)
        assertValidGreaterThan(scale, 0)
        self.__scale = scale

    @property
    def scaleOrientation(self):
        return self.__scaleOrientation

    @scaleOrientation.setter
    def scaleOrientation(self, scaleOrientation):
        if scaleOrientation is None:
            scaleOrientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(scaleOrientation)
        self.__scaleOrientation = scaleOrientation

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

class LayoutGroup(X3DGroupingNode):
    """
    LayoutGroup : X3DGroupingNode {
        MFNode  [in]     addChildren          [X3DChildNode]
        MFNode  [in]     removeChildren       [X3DChildNode]
        MFNode  [in,out] children       []    [X3DChildNode]
        SFNode  [in,out] layout         NULL  [X3DLayoutNode]
        SFNode  [in,out] metadata       NULL  [X3DMetadataObject]
        SFNode  [in,out] viewport       NULL  [X3DViewportNode]
        SFVec3f []       bboxCenter     0 0 0 (-∞,∞)
        SFVec3f []       bboxSize       0 0 0 (-∞,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            layout=None,
            viewport=None,
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.layout = layout
        self.viewport = viewport

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout):
        if layout is None:
            layout = None
        assertSFNode(layout, X3DLayoutNode)
        self.__layout = layout

    @property
    def viewport(self):
        return self.__viewport

    @viewport.setter
    def viewport(self, viewport):
        if viewport is None:
            viewport = None
        assertSFNode(viewport, X3DViewportNode)
        self.__viewport = viewport

class LOD(X3DGroupingNode):
    """
    LOD : X3DGroupingNode {
        MFNode  [in]     addChildren               [X3DChildNode]
        MFNode  [in]     removeChildren            [X3DChildNode]
        MFNode  [in,out] children         []       [X3DChildNode]
        SFNode  [in,out] metadata         NULL     [X3DMetadataObject]
        SFInt32 [out]    level_changed
        SFVec3f []       bboxCenter       0 0 0    (-∞,∞)
        SFVec3f []       bboxSize         -1 -1 -1 [0,∞) or −1 −1 −1
        SFVec3f []       center           0 0 0    (-∞,∞)
        SFBool  []       forceTransitions FALSE
        MFFloat []       range            []       [0,∞) or -1 
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            center=[0.0, 0.0, 0.0],
            forceTransitions=False,
            range_=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.center = center
        self.forceTransitions = forceTransitions
        self.range_ = range_

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = None
        assertSFVec3f(center)
        self.__center = center
    
    @property
    def forceTransitions(self):
        return self.__forceTransitions

    @forceTransitions.setter
    def forceTransitions(self, forceTransitions):
        if forceTransitions is None:
            forceTransitions = False
        assertSFBool(forceTransitions)
        self.__forceTransitions = forceTransitions
    
    @property
    def range_(self):
        return self.__range_

    @range_.setter
    def range_(self, range_):
        if range_ is None:
            range_ = []
        assertValidLODRange(range_)
        self.__range_ = range_

class PickableGroup(X3DGroupingNode, X3DPickableObject):
    """
    PickableGroup : X3DGroupingNode, X3DPickableObject {
        MFNode   [in]     addChildren
        MFNode   [in]     removeChildren
        MFNode   [in,out] children       []       [X3DChildNode]
        SFNode   [in,out] metadata       NULL     [X3DMetadataObject]
        MFString [in,out] objectType     "ALL"    ["ALL","NONE","TERRAIN",...]
        SFBool   [in,out] pickable       TRUE
        SFVec3f  []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f  []       bboxSize       -1 -1 -1 [0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            objectType=["ALL"],
            pickable=True,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            children=[],
            **kwargs
    ):
        super().__init__(
            objectTye=objectType,
            pickable=pickable,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            children=children,
            **kwargs
        )

class ScreenGroup(X3DGroupingNode):
    """
    ScreenGroup : X3DGroupingNode {
        MFNode  [in]     addChildren             [X3DChildNode]
        MFNode  [in]     removeChildren          [X3DChildNode]
        MFNode  [in,out] children       []       [X3DChildNode]
        SFNode  [in,out] metadata       NULL     [X3DMetadataObject]
        SFVec3f []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f []       bboxSize       -1 -1 -1 (0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )

class Switch(X3DGroupingNode):
    """
    Switch : X3DGroupingNode {
        MFNode  [in]     addChildren             [X3DChildNode]
        MFNode  [in]     removeChildren          [X3DChildNode]
        MFNode  [in,out] children       []       [X3DChildNode]
        SFNode  [in,out] metadata       NULL     [X3DMetadataObject]
        SFInt32 [in,out] whichChoice    -1       [-1,∞)
        SFVec3f []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f []       bboxSize       -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            whichChoice=-1,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.whichChoice = whichChoice

    @property
    def whichChoice(self):
        return self.__whichChoice

    @whichChoice.setter
    def whichChoice(self, whichChoice):
        if whichChoice is None:
            whichChoice = -1
        assertSFInt32(whichChoice)
        assertValidGreaterThanEquals(whichChoice, -1)
        self.__whichChoice = whichChoice

class Transform(X3DGroupingNode):
    """
    Transform : X3DGroupingNode {
        MFNode     [in]     addChildren               [X3DChildNode]
        MFNode     [in]     removeChildren            [X3DChildNode]
        SFVec3f    [in,out] center           0 0 0    (-∞,∞)
        MFNode     [in,out] children         []       [X3DChildNode]
        SFNode     [in,out] metadata         NULL     [X3DMetadataObject]
        SFRotation [in,out] rotation         0 0 1 0  [-1,1] or (-∞,∞)
        SFVec3f    [in,out] scale            1 1 1    (-∞, ∞)
        SFRotation [in,out] scaleOrientation 0 0 1 0  [-1,1] or (-∞,∞)
        SFVec3f    [in,out] translation      0 0 0    (-∞,∞)
        SFVec3f    []       bboxCenter       0 0 0    (-∞,∞)
        SFVec3f    []       bboxSize         -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            children=[],
            rotation=[0.0, 0.0, 1.0, 0.0],
            scale=[1.0, 1.0, 1.0],
            scaleOrientation=[0.0, 0.0, 1.0, 0.0],
            translation=[0.0, 0.0, 0.0],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.center = center
        self.rotation = rotation
        self.scale = scale
        self.scaleOrientation = scaleOrientation
        self.translation = translation

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if center is None:
            center = [0.0, 0.0, 0.0]
        assertSFVec3f(center)
        self.__center = center

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        assertSFVec3f(scale)
        self.__scale = scale

    @property
    def scaleOrientation(self):
        return self.__scaleOrientation

    @scaleOrientation.setter
    def scaleOrientation(self, scaleOrientation):
        if scaleOrientation is None:
            scaleOrientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(scaleOrientation)
        self.__scaleOrientation = scaleOrientation

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

class Viewport(X3DViewportNode, X3DBoundedObject):
    """
    Viewport : X3DViewportNode, X3DBoundedObject {
        MFNode  [in]     addChildren             [X3DChildNode]
        MFNode  [in]     removeChildren          [X3DChildNode]
        MFNode  [in,out] children       []       [X3DChildNode]
        MFFloat [in,out] clipBoundary   0 1 0 1  [0,1]
        SFNode  [in,out] metadata       NULL     [X3DMetadataObject]
        SFVec3f []       bboxCenter     0 0 0    (-∞,∞)
        SFVec3f []       bboxSize       -1 -1 -1 (0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            children=[],
            clipBoundary=[0.0, 1.0, 0.0, 1.0],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            children=children,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.clipBoundary = clipBoundary

    @property
    def clipBoundary(self):
        return self.__clipBoundary

    @clipBoundary.setter
    def clipBoundary(self, clipBoundary):
        if clipBoundary is None:
            clipBoundary = [0.0, 1.0, 0.0, 1.0]
        assertMFFloat(clipBoundary)
        assertValidGreaterThanEquals(clipBoundary, 0)
        assertValidLessThanEquals(clipBoundary, 1)
        self.__clipBoundary = clipBoundary

class DISEntityTypeMapping(X3DInfoNode,X3DUrlObject):
    """
    DISEntityTypeMapping : X3DInfoNode,X3DUrlObject {
        SFNode   [in,out] metadata    NULL [X3DMetadataObject]
        MFString [in,out] url         []   [URI]
        SFInt32  []       category    0    [0,255]
        SFInt32  []       country     0    [0,65535]
        SFInt32  []       domain      0    [0,255]
        SFInt32  []       extra       0    [0,255]
        SFInt32  []       kind        0    [0,255]
        SFInt32  []       specific    0    [0,255]
        SFInt32  []       subcategory 0    [0,255]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
            category=0,
            country=0,
            domain=0,
            extra=0,
            kind=0,
            specific=0,
            subcategory=0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            url=url,
            **kwargs
        )
        self.category = category
        self.country = country
        self.domain = domain
        self.extra = extra
        self.kind = kind
        self.specific = specific
        self.subcategory = subcategory

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        if category is None:
            category = 0
        assertSFInt32(category)
        assertValidGreaterThanEquals(category, 0)
        assertValidLessThanEquals(category, 255)
        self.__category = category

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        if country is None:
            country = 0
        assertSFInt32(country)
        assertValidGreaterThanEquals(country, 0)
        assertValidLessThanEquals(country, 65535)
        self.__country = country

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain):
        if domain is None:
            domain = 0
        assertSFInt32(domain)
        assertValidGreaterThanEquals(domain, 0)
        assertValidLessThanEquals(domain, 255)
        self.__domain = domain

    @property
    def extra(self):
        return self.__extra

    @extra.setter
    def extra(self, extra):
        if extra is None:
            extra = 0
        assertSFInt32(extra)
        assertValidGreaterThanEquals(extra, 0)
        assertValidLessThanEquals(extra, 255)
        self.__extra = extra

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        if kind is None:
            kind = 0
        assertSFInt32(kind)
        assertValidGreaterThanEquals(kind, 0)
        assertValidLessThanEquals(kind, 255)
        self.__kind = kind

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, specific):
        if specific is None:
            specific = 0
        assertSFInt32(specific)
        assertValidGreaterThanEquals(specific, 0)
        assertValidLessThanEquals(specific, 255)
        self.__specific = specific

    @property
    def subcategory(self):
        return self.__subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        if subcategory is None:
            subcategory = 0
        assertSFInt32(subcategory)
        assertValidGreaterThanEquals(subcategory, 0)
        assertValidLessThanEquals(subcategory, 255)
        self.__subcategory = subcategory

class GeoMetadata(X3DInfoNode):
    """
    GeoMetadata : X3DInfoNode {
        MFNode   [in,out] data     []
        SFNode   [in,out] metadata NULL [X3DMetadataObject]
        MFString [in,out] summary  []
        MFString [in,out] url      []   [URI]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            data=[],
            summary=[],
            url=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            **kwargs
        )
        self.data = data
        self.summary = summary
        self.url = url

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if data is None:
            data = []
        assertMFNode(data)
        self.__data = data

    @property
    def summary(self):
        return self.__summary

    @summary.setter
    def summary(self, summary):
        if summary is None:
            summary = []
        assertMFString(summary)
        self.__summary = summary

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        if url is None:
            url = []
        assertMFString(url)
        self.__url = url
    
class WorldInfo(X3DInfoNode):
    """
    WorldInfo : X3DInfoNode {
      SFNode   [in,out] metadata NULL [X3DMetadataObject]
      MFString []       info     []
      SFString []       title    ""
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            info=[],
            title="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.info = info
        self.title = title

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        if info is None:
            info = []
        assertMFString(info)
        self.__info = info

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title is None:
            title = ""
        assertSFString(title)
        self.__title = title

class ColorInterpolator(X3DInterpolatorNode):
    """
    ColorInterpolator : X3DInterpolatorNode {
        SFFloat [in]     set_fraction       (-∞,∞)
        MFFloat [in,out] key           []   (-∞,∞)
        MFColor [in,out] keyValue      []   [0,1]
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        SFColor [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFColor(keyValue)
        assertValidGreaterThanEquals(keyValue, 0)
        assertValidLessThanEquals(keyValue, 1)
        self.__keyValue = keyValue

class CoordinateInterpolator(X3DInterpolatorNode):
    """
    CoordinateInterpolator : X3DInterpolatorNode {
        SFFloat [in]     set_fraction       (-∞,∞)
        MFFloat [in,out] key           []   (-∞,∞)
        MFVec3f [in,out] keyValue      []   (-∞,∞)
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        MFVec3f [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec3f(keyValue)
        self.__keyValue = keyValue

class CoordinateInterpolator2D(X3DInterpolatorNode):
    """
    CoordinateInterpolator2D : X3DInterpolatorNode {
        SFFloat [in]     set_fraction       (-∞,∞)
        MFFloat [in,out] key           []   (-∞,∞)
        MFVec2f [in,out] keyValue      []   (-∞,∞)
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        MFVec2f [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec2f(keyValue)
        self.__keyValue = keyValue

class GeoPositionInterpolator(X3DInterpolatorNode):
    """
    GeoPositionInterpolator : X3DInterpolatorNode {
        SFFloat  [in]     set_fraction                 (-∞,∞)
        MFFloat  [in,out] key              []          (-∞,∞)
        MFVec3d  [in,out] keyValue         []
        SFNode   [in,out] metadata         NULL        [X3DMetadataObject]
        SFVec3d  [out]    geovalue_changed
        SFVec3f  [out]    value_changed
        SFNode   []       geoOrigin        NULL        [GeoOrigin] (deprecated)
        MFString []       geoSystem        ["GD","WE"] [see 25.2.3]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            geoOrigin=[0.0, 0.0, 0.0],
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec3d(keyValue)
        self.__keyValue = keyValue

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem
class NormalInterpolator(X3DInterpolatorNode):
    """
    NormalInterpolator : X3DInterpolatorNode {
        SFFloat [in]     set_fraction       (-∞,∞)
        MFFloat [in,out] key           []   (-∞,∞)
        MFVec3f [in,out] keyValue      []   (-∞,∞)
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        MFVec3f [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec3f(keyValue)
        self.__keyValue = keyValue

class OrientationInterpolator(X3DInterpolatorNode):
    """
    OrientationInterpolator : X3DInterpolatorNode {
        SFFloat    [in]     set_fraction       (-∞,∞)
        MFFloat    [in,out] key           []   (-∞,∞)
        MFRotation [in,out] keyValue      []   [-1,1] or (-∞,∞)
        SFNode     [in,out] metadata      NULL [X3DMetadataObject]
        SFRotation [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFRotation(keyValue)
        self.__keyValue = keyValue

class PositionInterpolator(X3DInterpolatorNode):
    """
    PositionInterpolator : X3DInterpolatorNode {
        SFFloat [in]     set_fraction       (-∞,∞)
        MFFloat [in,out] key           []   (-∞,∞)
        MFVec3f [in,out] keyValue      []   (-∞,∞)
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        SFVec3f [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec3f(keyValue)
        self.__keyValue = keyValue
    
class PositionInterpolator2D(X3DInterpolatorNode):
    """
    PositionInterpolator2D : X3DInterpolatorNode {
        SFFloat [in]     set_fraction       (-∞,∞)
        MFFloat [in,out] key           []   (-∞,∞)
        MFVec2f [in,out] keyValue      []   (-∞,∞)
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        SFVec2f [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec2f(keyValue)
        self.__keyValue = keyValue

class ScalarInterpolator(X3DInterpolatorNode):
    """
    ScalarInterpolator : X3DInterpolatorNode {
        SFFloat [in]     set_fraction       (-∞,∞)
        MFFloat [in,out] key           []   (-∞,∞)
        MFFloat [in,out] keyValue      []   (-∞,∞)
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        SFFloat [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFFloat(keyValue)
        self.__keyValue = keyValue

class SplinePositionInterpolator(X3DInterpolatorNode):
    """
    SplinePositionInterpolator : X3DInterpolatorNode {
        SFFloat [in]     set_fraction            (-∞,∞)
        SFBool  [in,out] closed            FALSE
        MFFloat [in,out] key               []    (-∞,∞)
        MFVec3f [in,out] keyValue          []    (-∞,∞)
        MFVec3f [in,out] keyVelocity       []    (-∞,∞)
        SFNode  [in,out] metadata          NULL  [X3DMetadataObject]
        SFBool  [in,out] normalizeVelocity FALSE
        SFVec3f [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            closed=False,
            key=[],
            keyValue=[],
            keyVelocity=[],
            normalizeVelocity=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.closed = closed
        self.keyValue = keyValue
        self.keyVelocity = keyVelocity
        self.normalizeVelocity = normalizeVelocity

    @property
    def closed(self):
        return self.__closed
    
    @closed.setter
    def closed(self, closed):
        if closed is None:
            closed = False
        assertSFBool(closed)
        self.__closed = closed

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec3f(keyValue)
        self.__keyValue = keyValue
    
    @property
    def keyVelocity(self):
        return self.__keyVelocity
    
    @keyVelocity.setter
    def keyVelocity(self, keyVelocity):
        if keyVelocity is None:
            keyVelocity = []
        assertMFVec3f(keyVelocity)
        self.__keyVelocity = keyVelocity

    @property
    def normalizeVelocity(self):
        return self.__normalizeVelocity
    
    @normalizeVelocity.setter
    def normalizeVelocity(self, normalizeVelocity):
        if normalizeVelocity is None:
            normalizeVelocity = False
        assertSFBool(normalizeVelocity)
        self.__normalizeVelocity = normalizeVelocity

class SplinePositionInterpolator2D(X3DInterpolatorNode):
    """
    SplinePositionInterpolator2D : X3DInterpolatorNode {
        SFFloat [in]     set_fraction            (-∞,∞)
        SFBool  [in,out] closed            FALSE
        MFFloat [in,out] key               []    (-∞,∞)
        MFVec2f [in,out] keyValue          []    (-∞,∞)
        MFVec2f [in,out] keyVelocity       []    (-∞,∞)
        SFNode  [in,out] metadata          NULL  [X3DMetadataObject]
        SFBool  [in,out] normalizeVelocity FALSE
        SFVec2f [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            closed=False,
            key=[],
            keyValue=[],
            keyVelocity=[],
            normalizeVelocity=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.closed = closed
        self.keyValue = keyValue
        self.keyVelocity = keyVelocity
        self.normalizeVelocity = normalizeVelocity

    @property
    def closed(self):
        return self.__closed
    
    @closed.setter
    def closed(self, closed):
        if closed is None:
            closed = False
        assertSFBool(closed)
        self.__closed = closed

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFVec2f(keyValue)
        self.__keyValue = keyValue
    
    @property
    def keyVelocity(self):
        return self.__keyVelocity
    
    @keyVelocity.setter
    def keyVelocity(self, keyVelocity):
        if keyVelocity is None:
            keyVelocity = []
        assertMFVec2f(keyVelocity)
        self.__keyVelocity = keyVelocity

    @property
    def normalizeVelocity(self):
        return self.__normalizeVelocity
    
    @normalizeVelocity.setter
    def normalizeVelocity(self, normalizeVelocity):
        if normalizeVelocity is None:
            normalizeVelocity = False
        assertSFBool(normalizeVelocity)
        self.__normalizeVelocity = normalizeVelocity

class SplineScalarInterpolator(X3DInterpolatorNode):
    """
    SplineScalarInterpolator : X3DInterpolatorNode {
        SFFloat [in]     set_fraction            (-∞,∞)
        SFBool  [in,out] closed            FALSE
        MFFloat [in,out] key               []    (-∞,∞)
        MFFloat [in,out] keyValue          []    (-∞,∞)
        MFFloat [in,out] keyVelocity       []    (-∞,∞)
        SFNode  [in,out] metadata          NULL  [X3DMetadataObject]
        SFBool  [in,out] normalizeVelocity FALSE
        SFFloat [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            closed=False,
            key=[],
            keyValue=[],
            keyVelocity=[],
            normalizeVelocity=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.closed = closed
        self.keyValue = keyValue
        self.keyVelocity = keyVelocity
        self.normalizeVelocity = normalizeVelocity

    @property
    def closed(self):
        return self.__closed
    
    @closed.setter
    def closed(self, closed):
        if closed is None:
            closed = False
        assertSFBool(closed)
        self.__closed = closed

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFFloat(keyValue)
        self.__keyValue = keyValue
    
    @property
    def keyVelocity(self):
        return self.__keyVelocity
    
    @keyVelocity.setter
    def keyVelocity(self, keyVelocity):
        if keyVelocity is None:
            keyVelocity = []
        assertMFFloat(keyVelocity)
        self.__keyVelocity = keyVelocity

    @property
    def normalizeVelocity(self):
        return self.__normalizeVelocity
    
    @normalizeVelocity.setter
    def normalizeVelocity(self, normalizeVelocity):
        if normalizeVelocity is None:
            normalizeVelocity = False
        assertSFBool(normalizeVelocity)
        self.__normalizeVelocity = normalizeVelocity

class SquadOrientationInterpolator(X3DInterpolatorNode):
    """
    SquadOrientationInterpolator : X3DInterpolatorNode {
        SFFloat    [in]     set_fraction            (-∞,∞)
        MFFloat    [in,out] key               []    (-∞,∞)
        MFRotation [in,out] keyValue          []    (-∞,∞)
        SFNode     [in,out] metadata          NULL  [X3DMetadataObject]
        SFBool     [in,out] normalizeVelocity FALSE
        SFRotation [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            normalizeVelocity=False,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue
        self.normalizeVelocity = normalizeVelocity

    @property
    def keyValue(self):
        return self.__keyValue
    
    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFRotation(keyValue)
        self.__keyValue = keyValue

    @property
    def normalizeVelocity(self):
        return self.__normalizeVelocity

    @normalizeVelocity.setter
    def normalizeVelocity(self, normalizeVelocity):
        if normalizeVelocity is None:
            normalizeVelocity = False
        assertSFBool(normalizeVelocity)
        self.__normalizeVelocity = normalizeVelocity

class Layout(X3DLayoutNode):
    """
    Layout : X3DLayoutNode { 
        MFString [in,out] align       ["CENTER","CENTER"] ["LEFT"|"CENTER"|"RIGHT"&
                                                            "BOTTOM"|"CENTER"|"TOP"]
        SFNode   [in,out] metadata    NULL                [X3DMetadataObject]
        MFFloat  [in,out] offset      [0,0]               (-∞,∞)
        MFString [in,out] offsetUnits ["WORLD","WORLD"]   ["WORLD","FRACTION","PIXEL"]
        MFString [in,out] scaleMode   ["NONE","NONE"]     ["NONE","FRACTION","STRETCH","PIXEL"]
        MFFloat  [in,out] size        [1,1]               (0,∞)
        MFString [in,out] sizeUnits   ["WORLD","WORLD"]   ["WORLD","FRACTION","PIXEL"]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            align=["CENTER","CENTER"],
            offset=[0.0, 0.0],
            offsetUnits=["WORLD","WORLD"],
            scaleMode=["NONE","NONE"],
            size=[1.0, 1.0],
            sizeUnits=["WORLD","WORLD"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            **kwargs
        )
        self.align = align
        self.offset = offset
        self.offsetUnits = offsetUnits
        self.scaleMode = scaleMode
        self.size = size
        self.sizeUnits = sizeUnits

    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align):
        if align is None:
            align = ["CENTER","CENTER"]
        assertValidLayoutAlign(align)
        self.__align = align

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        if offset is None:
            offset = [0.0, 0.0]
        assertMFFloat(offset)
        self.__offset = offset

    @property
    def offsetUnits(self):
        return self.__offsetUnits

    @offsetUnits.setter
    def scaleMode(self, offsetUnits):
        if offsetUnits is None:
            offsetUnits = ["WORLD","WORLD"]
        assertValidLayoutOffsetUnits(offsetUnits)
        self.__offsetUnits = offsetUnits

    @property
    def scaleMode(self):
        return self.__scaleMode

    @scaleMode.setter
    def scaleMode(self, scaleMode):
        if scaleMode is None:
            scaleMode = ["NONE","NONE"]
        assertValidLayoutScaleMode(scaleMode)
        self.__scaleMode = scaleMode

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size is None:
            size = [1.0, 1.0]
        assertMFFloat(size)
        assertValidGreaterThan(size, 0)
        self.__size = size

    @property
    def sizeUnits(self):
        return self.__sizeUnits

    @sizeUnits.setter
    def sizeUnits(self, sizeUnits):
        if sizeUnits is None:
            sizeUnits = ["WORLD","WORLD"]
        assertValidLayoutSizeUnits(sizeUnits)
        self.__sizeUnits = sizeUnits

class DirectionalLight(X3DLightNode):
    """
    DirectionalLight : X3DLightNode {
        SFFloat [in,out] ambientIntensity 0      [0,1]
        SFColor [in,out] color            1 1 1  [0,1]
        SFVec3f [in,out] direction        0 0 -1 (-∞,∞)
        SFBool  [in,out] global           FALSE
        SFFloat [in,out] intensity        1      [0,1]
        SFNode  [in,out] metadata         NULL   [X3DMetadataObject]
        SFBool  [in,out] on               TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            ambientIntensity=0.0,
            color=[1.0, 1.0, 1.0],
            direction=[0.0, 0.0, -1.0],
            global_=False,
            intensity=1.0,
            on=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            ambientIntensity=ambientIntensity,
            color=color,
            global_=global_,
            intensity=intensity,
            on=on,
            **kwargs
        )
        self.direction = direction

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 0.0, -1.0]
        assertSFVec3f(direction)
        self.__direction = direction

class PointLight(X3DLightNode):
    """
    PointLight : X3DLightNode {
        SFFloat [in,out] ambientIntensity 0     [0,1]
        SFVec3f [in,out] attenuation      1 0 0 [0,∞)
        SFColor [in,out] color            1 1 1 [0,1]
        SFBool  [in,out] global           TRUE
        SFFloat [in,out] intensity        1     [0,1]
        SFVec3f [in,out] location         0 0 0 (-∞,∞)
        SFNode  [in,out] metadata         NULL  [X3DMetadataObject]
        SFBool  [in,out] on               TRUE
        SFFloat [in,out] radius           100   [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            ambientIntensity=0.0,
            attenuation=[1.0, 0.0, 0.0],
            color=[1.0, 1.0, 1.0],
            global_=True,
            intensity=1.0,
            location=[0.0, 0.0, 0.0],
            on=True,
            radius=100.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            ambientIntensity=ambientIntensity,
            color=color,
            global_=global_,
            intensity=intensity,
            on=on,
            **kwargs
        )
        self.attenuation = attenuation
        self.location = location
        self.radius = radius

    @property
    def attenuation(self):
        return self.__attenuation

    @attenuation.setter
    def attenuation(self, attenuation):
        if attenuation is None:
            attenuation = [1.0, 0.0, 0.0]
        assertSFVec3f(attenuation)
        assertValidGreaterThanEquals(attenuation, 0)
        self.__attenuation = attenuation

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        if location is None:
            location = [1.0, 0.0, 0.0]
        assertSFVec3f(location)
        self.__location = location

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 100.0
        assertValidFontFamily(radius)
        assertValidGreaterThanEquals(radius, 0)
        self.__radius = radius

class SpotLight(X3DLightNode):
    """
    SpotLight : X3DLightNode {
        SFFloat [in,out] ambientIntensity 0        [0,1]
        SFVec3f [in,out] attenuation      1 0 0    [0,∞)
        SFFloat [in,out] beamWidth        π/4      (0,π/2]
        SFColor [in,out] color            1 1 1    [0,1]
        SFFloat [in,out] cutOffAngle      π/2      (0,π/2]
        SFVec3f [in,out] direction        0 0 -1   (-∞,∞)
        SFBool  [in,out] global           TRUE
        SFFloat [in,out] intensity        1        [0,1]
        SFVec3f [in,out] location         0 0 0    (-∞,∞)
        SFNode  [in,out] metadata         NULL     [X3DMetadataObject]
        SFBool  [in,out] on               TRUE
        SFFloat [in,out] radius           100      [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            ambientIntensity=0.0,
            attenuation=[1.0, 0.0, 0.0],
            beamWidth=math.pi/4,
            color=[1.0, 1.0, 1.0],
            cutOffAngle=math.pi/2,
            direction=[0.0, 0.0, -1.0],
            global_=True,
            intensity=1.0,
            location=[0.0, 0.0, 0.0],
            on=True,
            radius=100.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            ambientIntensity=ambientIntensity,
            color=color,
            global_=global_,
            intensity=intensity,
            on=on,
            **kwargs
        )
        self.attenuation = attenuation
        self.beamWidth = beamWidth
        self.cutOffAngle = cutOffAngle
        self.direction = direction
        self.location = location
        self.radius = radius

    @property
    def attenuation(self):
        return self.__attenuation

    @attenuation.setter
    def attenuation(self, attenuation):
        if attenuation is None:
            attenuation = [1.0, 0.0, 0.0]
        assertSFVec3f(attenuation)
        assertValidGreaterThanEquals(attenuation, 0)
        self.__attenuation = attenuation

    @property
    def beamWidth(self):
        return self.__beamWidth

    @beamWidth.setter
    def beamWidth(self, beamWidth):
        if beamWidth is None:
            beamWidth = math.pi/4
        assertSFFloat(beamWidth)
        assertValidGreaterThan(beamWidth, 0)
        assertValidLessThanEquals(beamWidth, math.pi/2)
        self.__beamWidth = beamWidth

    @property
    def cutOffAngle(self):
        return self.__cutOffAngle

    @cutOffAngle.setter
    def cutOffAngle(self, cutOffAngle):
        if cutOffAngle is None:
            cutOffAngle = math.pi/2
        assertSFFloat(cutOffAngle)
        assertValidGreaterThan(cutOffAngle, 0)
        assertValidLessThanEquals(cutOffAngle, math.pi/2)
        self.__cutOffAngle = cutOffAngle

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 0.0, -1.0]
        assertSFVec3f(direction)
        self.__direction = direction

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        if location is None:
            location = [1.0, 0.0, 0.0]
        assertSFVec3f(location)
        self.__location = location

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius is None:
            radius = 100.0
        assertValidFontFamily(radius)
        assertValidGreaterThanEquals(radius, 0)
        self.__radius = radius

class CollidableOffset(X3DNBodyCollidableNode):
    """
    CollidableOffset : X3DNBodyCollidableNode {
        SFBool     [in,out] enabled     TRUE
        SFNode     [in,out] metadata    NULL     [X3DMetadataObject]
        SFRotation [in,out] rotation    0 0 1 0  [0,1]
        SFVec3f    [in,out] translation 0 0 0    (-∞,∞)
        SFVec3f    []       bboxCenter  0 0 0    (-∞,∞)
        SFVec3f    []       bboxSize    -1 -1 -1 [0,∞) or -1 -1 -1
        SFNode     []       collidable  NULL     [X3DNBodyCollidableNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            rotation=[0.0, 0.0, 1.0, 0.0],
            translation=[0.0, 0.0, 0.0],
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            collidable=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            rotation=rotation,
            translation=translation,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.collidable = collidable

    @property
    def collidable(self):
        return self.__collidable

    @collidable.setter
    def collidable(self, collidable):
        if collidable is None:
            collidable = None
        assertSFNode(collidable, X3DNBodyCollidableNode)
        self.__collidable = collidable

class CollidableShape(X3DNBodyCollidableNode):
    """
    CollidableShape : X3DNBodyCollidableNode  {
        SFBool     [in,out] enabled     TRUE
        SFNode     [in,out] metadata    NULL     [X3DMetadataObject]
        SFRotation [in,out] rotation    0 0 1 0  [0,1]
        SFVec3f    [in,out] translation 0 0 0    (-∞,∞)
        SFVec3f    []       bboxCenter  0 0 0    (-∞,∞)
        SFVec3f    []       bboxSize    -1 -1 -1 [0,∞) or -1 -1 -1
        SFNode     []       shape       NULL     [Shape]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            rotation=[0.0, 0.0, 1.0, 0.0],
            translation=[0.0, 0.0, 0.0],
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
            shape=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            rotation=rotation,
            translation=translation,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.shape = shape

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape):
        if shape is None:
            shape = None
        assertSFNode(shape, Shape)
        self.__shape = shape

class Script(X3DScriptNode):
    """
    Script : X3DScriptNode {
        SFNode    [in,out] metadata     NULL  [X3DMetadataObject]
        MFString  [in,out] url          []    [URI]
        SFBool    []       directOutput FALSE
        SFBool    []       mustEvaluate FALSE
        # And any number of:
        fieldType [in]     fieldName
        fieldType [in,out] fieldName    initialValue
        fieldType [out]    fieldName
        fieldType []       fieldName    initialValue
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
            directOuput=False,
            mustEvaluate=False,
            fieldType=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            url=url,
            **kwargs
        )
        self.directOuput = directOuput
        self.mustEvaluate = mustEvaluate
        self.fieldType = fieldType

    @property
    def directOuput(self):
        return self.__directOuput

    @directOuput.setter
    def directOuput(self, directOuput):
        if directOuput is None:
            directOuput = False
        assertSFBool(directOuput)
        self.__directOuput = directOuput

    @property
    def mustEvaluate(self):
        return self.__mustEvaluate

    @mustEvaluate.setter
    def mustEvaluate(self, mustEvaluate):
        if mustEvaluate is None:
            mustEvaluate = False
        assertSFBool(mustEvaluate)
        self.__mustEvaluate = mustEvaluate

    @property
    def fieldType(self):
        return self.__fieldType

    @fieldType.setter
    def fieldType(self, fieldType):
        self.__fieldType = fieldType

class CollisionSensor(X3DSensorNode):
    """
    CollisionSensor : X3DSensorNode {
        SFNode [in,out] collider      NULL [CollisionCollection]
        SFBool [in,out] enabled       TRUE
        SFNode [in,out] metadata      NULL [X3DMetadataObject]
        MFNode [out]    intersections	     [X3DNBodyCollidableNode]
        MFNode [out]    contacts           [Contact]
        SFBool [out]    isActive
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            collider=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.collider = collider

    @property
    def collider(self):
        return self.__collider

    @collider.setter
    def collider(self, collider):
        if collider is None:
            collider = None
        assertSFNode(collider, CollisionCollection)
        self.__collider = collider

class ReceiverPdu(X3DNetworkSensorNode, X3DBoundedObject):
    """
    ReceiverPdu : X3DNetworkSensorNode, X3DBoundedObject {
        SFString [in,out] address                  "localhost"
        SFInt32  [in,out] applicationID            1            [0,65535]
        SFBool   [in,out] enabled                  TRUE
        SFInt32  [in,out] entityID                 0            [0,65535]
        SFVec3d  [in,out] geoCoords                0 0 0        (-∞,∞)
        SFNode   [in,out] metadata                 NULL         [X3DMetadataObject]
        SFString [in,out] multicastRelayHost       ""
        SFInt32  [in,out] multicastRelayPort       0     
        SFString [in,out] networkMode              "standAlone" ["standAlone"|
                                                                "networkReader"|
                                                                "networkWriter"]
        SFInt32  [in,out] port                     0            [0,65535]
        SFInt32  [in,out] radioID                  0            [0,65535]
        SFFloat  [in,out] readInterval             0.1          [0,∞)
        SFFloat  [in,out] receivedPower            0.0          [0,∞)
        SFInt32  [in,out] receiverState            0            [0,65535]
        SFBool   [in,out] rtpHeaderExpected        FALSE
        SFInt32  [in,out] siteID                   0            [0,65535]
        SFInt32  [in,out] transmitterApplicationID 1            [0,65535]
        SFInt32  [in,out] transmitterEntityID      0            [0,65535]
        SFInt32  [in,out] transmitterRadioID       0            [0,65535]
        SFInt32  [in,out] transmitterSiteID        0            [0,65535]           
        SFInt32  [in,out] whichGeometry            1            [-1,∞)
        SFFloat  [in,out] writeInterval            1.0          [0,∞)
        SFBool   [out]    isActive                 FALSE
        SFBool   [out]    isNetworkReader          FALSE
        SFBool   [out]    isNetworkWriter          FALSE
        SFBool   [out]    isRtpHeaderHeard         FALSE
        SFBool   [out]    isStandAlone             FALSE
        SFTime   [out]    timestamp                0
        SFVec3f  []       bboxCenter               0 0 0        (-∞,∞)
        SFVec3f  []       bboxSize                 -1 -1 -1     [0,∞) [0,∞) [0,∞) or −1 −1 −1
        MFString []       geoSystem                ["GD","WE"]  [see 25.2.3]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            address="localhost",
            applicationId=1,
            enabled=True,
            entityID=0,
            geoCoords=[0.0, 0.0, 0.0],
            multicastRelayHost="",
            multicastRelayPort=0,
            networkMode="standAlone",
            port=0,
            radioID=0,
            readInterval=0.1,
            receivedPower=0.0,
            receiverState=0,
            rtpHeaderExpected=False,
            siteID=0,
            transmitterApplicationID=1,
            transmitterEntityID=0,
            transmitterRadioID=0,
            transmitterSiteID=0,
            whichGeometry=1,
            writeInterval=1.0,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.address = address
        self.applicationId = applicationId
        self.entityID = entityID
        self.geoCoords = geoCoords
        self.multicastRelayHost = multicastRelayHost
        self.multicastRelayPort = multicastRelayPort
        self.networkMode = networkMode
        self.port = port
        self.radioID = radioID
        self.readInterval = readInterval
        self.receivedPower = receivedPower
        self.receiverState = receiverState
        self.rtpHeaderExpected = rtpHeaderExpected
        self.siteID = siteID
        self.transmitterApplicationID = transmitterApplicationID
        self.transmitterEntityID = transmitterEntityID
        self.transmitterRadioID = transmitterRadioID
        self.transmitterSiteID = transmitterSiteID
        self.whichGeometry = whichGeometry
        self.writeInterval = writeInterval
        self.geoSystem = geoSystem
        
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if address is None:
            address = "localhost"
        assertSFString(address)
        self.__address = address

    @property
    def applicationID(self):
        return self.__applicationID

    @applicationID.setter
    def applicationID(self, applicationID):
        if applicationID is None:
            applicationID = 1
        assertSFInt32(applicationID)
        assertValidGreaterThanEquals(applicationID, 0)
        assertValidLessThanEquals(applicationID, 65535)
        self.__applicationID = applicationID

    @property
    def entityID(self):
        return self.__entityID

    @entityID.setter
    def entityID(self, entityID):
        if entityID is None:
            entityID = 0
        assertSFInt32(entityID)
        assertValidGreaterThanEquals(entityID, 0)
        assertValidLessThanEquals(entityID, 65535)
        self.__entityID = entityID

    @property
    def geoCoords(self):
        return self.__geoCoords

    @geoCoords.setter
    def geoCoords(self, geoCoords):
        if geoCoords is None:
            geoCoords = [0.0, 0.0, 0.0]
        assertSFVec3d(geoCoords)
        self.__geoCoords = geoCoords

    @property
    def multicastRelayHost(self):
        return self.__multicastRelayHost

    @multicastRelayHost.setter
    def multicastRelayHost(self, multicastRelayHost):
        if multicastRelayHost is None:
            multicastRelayHost = ""
        assertSFString(multicastRelayHost)
        self.__multicastRelayHost = multicastRelayHost

    @property
    def multicastRelayPort(self):
        return self.__multicastRelayPort

    @multicastRelayPort.setter
    def multicastRelayPort(self, multicastRelayPort):
        if multicastRelayPort is None:
            multicastRelayPort = 0
        assertSFInt32(multicastRelayPort)
        self.__multicastRelayPort = multicastRelayPort

    @property
    def networkMode(self):
        return self.__networkMode

    @networkMode.setter
    def networkMode(self, networkMode):
        if networkMode is None:
            networkMode = "standAlone"
        assertValidNetworkMode(networkMode)
        self.__networkMode = networkMode

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if port is None:
            port = 0
        assertSFInt32(port)
        assertValidGreaterThanEquals(port, 0)
        assertValidLessThanEquals(port, 65535)
        self.__port = port

    @property
    def radioID(self):
        return self.__radioID

    @radioID.setter
    def radioID(self, radioID):
        if radioID is None:
            radioID = 0
        assertSFInt32(radioID)
        assertValidGreaterThanEquals(radioID, 0)
        assertValidLessThanEquals(radioID, 65535)
        self.__radioID = radioID

    @property
    def readInterval(self):
        return self.__readInterval

    @readInterval.setter
    def readInterval(self, readInterval):
        if readInterval is None:
            readInterval = 0.1
        assertSFFloat(readInterval)
        assertValidGreaterThanEquals(readInterval, 0)
        self.__readInterval = readInterval

    @property
    def receivedPower(self):
        return self.__receivedPower

    @receivedPower.setter
    def receivedPower(self, receivedPower):
        if receivedPower is None:
            receivedPower = 0.0
        assertSFFloat(receivedPower)
        assertValidGreaterThanEquals(receivedPower, 0)
        self.__receivedPower = receivedPower

    @property
    def receiverState(self):
        return self.__receiverState

    @receiverState.setter
    def receiverState(self, receiverState):
        if receiverState is None:
            receiverState = 0
        assertSFFloat(receiverState)
        assertValidGreaterThanEquals(receiverState, 0)
        assertValidLessThanEquals(receiverState, 65535)
        self.__receiverState = receiverState

    @property
    def rtpHeaderExpected(self):
        return self.__rtpHeaderExpected

    @rtpHeaderExpected.setter
    def rtpHeaderExpected(self, rtpHeaderExpected):
        if rtpHeaderExpected is None:
            rtpHeaderExpected = False
        assertSFBool(rtpHeaderExpected)
        self.__rtpHeaderExpected = rtpHeaderExpected

    @property
    def siteID(self):
        return self.__siteID

    @siteID.setter
    def siteID(self, siteID):
        if siteID is None:
            siteID = 0
        assertSFInt32(siteID)
        assertValidGreaterThanEquals(siteID, 0)
        assertValidLessThanEquals(siteID, 65535)
        self.__siteID = siteID

    @property
    def transmitterApplicationID(self):
        return self.__transmitterApplicationID

    @transmitterApplicationID.setter
    def transmitterApplicationID(self, transmitterApplicationID):
        if transmitterApplicationID is None:
            transmitterApplicationID = 1
        assertSFInt32(transmitterApplicationID)
        assertValidGreaterThanEquals(transmitterApplicationID, 0)
        assertValidLessThanEquals(transmitterApplicationID, 65535)
        self.__transmitterApplicationID = transmitterApplicationID

    @property
    def transmitterEntityID(self):
        return self.__transmitterEntityID

    @transmitterEntityID.setter
    def transmitterEntityID(self, transmitterEntityID):
        if transmitterEntityID is None:
            transmitterEntityID = 0
        assertSFInt32(transmitterEntityID)
        assertValidGreaterThanEquals(transmitterEntityID, 0)
        assertValidLessThanEquals(transmitterEntityID, 65535)
        self.__transmitterEntityID = transmitterEntityID

    @property
    def transmitterRadioID(self):
        return self.__transmitterRadioID

    @transmitterRadioID.setter
    def transmitterRadioID(self, transmitterRadioID):
        if transmitterRadioID is None:
            transmitterRadioID = 0
        assertSFInt32(transmitterRadioID)
        assertValidGreaterThanEquals(transmitterRadioID, 0)
        assertValidLessThanEquals(transmitterRadioID, 65535)
        self.__transmitterRadioID = transmitterRadioID

    @property
    def transmitterSiteID(self):
        return self.__transmitterSiteID

    @transmitterSiteID.setter
    def transmitterSiteID(self, transmitterSiteID):
        if transmitterSiteID is None:
            transmitterSiteID = 0
        assertSFInt32(transmitterSiteID)
        assertValidGreaterThanEquals(transmitterSiteID, 0)
        assertValidLessThanEquals(transmitterSiteID, 65535)
        self.__transmitterSiteID = transmitterSiteID

    @property
    def whichGeometry(self):
        return self.__whichGeometry

    @whichGeometry.setter
    def whichGeometry(self, whichGeometry):
        if whichGeometry is None:
            whichGeometry = 1
        assertSFInt32(whichGeometry)
        assertValidGreaterThanEquals(whichGeometry, -1)
        self.__whichGeometry = whichGeometry
    
    @property
    def writeInterval(self):
        return self.__writeInterval

    @writeInterval.setter
    def writeInterval(self, writeInterval):
        if writeInterval is None:
            writeInterval = 1.0
        assertSFFloat(writeInterval)
        assertValidGreaterThanEquals(writeInterval, 0)
        self.__writeInterval = writeInterval

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class SignalPdu(X3DNetworkSensorNode, X3DBoundedObject):
    """
    SignalPdu : X3DNetworkSensorNode, X3DBoundedObject {
        SFString [in,out] address            "localhost"
        SFInt32  [in,out] applicationID      1            [0,65535]
        MFInt32  [in,out] data               []           [0,255]                  
        SFInt32  [in,out] dataLength         0            [0,65535]
        SFBool   [in,out] enabled            TRUE
        SFInt32  [in,out] encodingScheme     0            [0,65535]
        SFInt32  [in,out] entityID           0            [0,65535]
        SFVec3d  [in,out] geoCoords          0 0 0        (-∞,∞)
        SFNode   [in,out] metadata           NULL         [X3DMetadataObject]
        SFString [in,out] multicastRelayHost ""
        SFInt32  [in,out] multicastRelayPort 0           
        SFString [in,out] networkMode        "standAlone" ["standAlone"|
                                                            "networkReader"|
                                                            "networkWriter"]
        SFInt32  [in,out] port               0            [0,65535]
        SFInt32  [in,out] radioID            0            [0,65535]
        SFFloat  [in,out] readInterval       0.1          [0,∞)
        SFBool   [in,out] rtpHeaderExpected  FALSE
        SFInt32  [in,out] sampleRate         0            [0,65535]
        SFInt32  [in,out] samples            0            [0,65535]
        SFInt32  [in,out] siteID             0            [0,65535]
        SFInt32  [in,out] tdlType            0            [0,65535]
        SFInt32  [in,out] whichGeometry      1            [-1,∞)
        SFFloat  [in,out] writeInterval      1.0          [0,∞)
        SFBool   [out]    isActive
        SFBool   [out]    isNetworkReader
        SFBool   [out]    isNetworkWriter
        SFBool   [out]    isRtpHeaderHeard
        SFBool   [out]    isStandAlone
        SFTime   [out]    timestamp
        SFVec3f  []       bboxCenter         0 0 0        (-∞,∞)
        SFVec3f  []       bboxSize           -1 -1 -1     [0,∞) or −1 −1 −1
        MFString []       geoSystem          ["GD","WE"]  [see 25.2.3]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            address="localhost",
            applicationId=1,
            data=[],
            dataLength=0,
            enabled=True,
            encodingScheme=0,
            entityID=0,
            geoCoords=[0.0, 0.0, 0.0],
            multicastRelayHost="",
            multicastRelayPort=0,
            networkMode="standAlone",
            port=0,
            radioID=0,
            readInterval=0.1,
            rtpHeaderExpected=False,
            sampleRate=0,
            samples=0,
            siteID=0,
            tdlType=0,
            whichGeometry=1,
            writeInterval=1.0,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.address = address
        self.applicationId = applicationId
        self.data = data
        self.dataLength = dataLength
        self.entityID = entityID
        self.encodingScheme = encodingScheme
        self.geoCoords = geoCoords
        self.multicastRelayHost = multicastRelayHost
        self.multicastRelayPort = multicastRelayPort
        self.networkMode = networkMode
        self.port = port
        self.radioID = radioID
        self.readInterval = readInterval
        self.sampleRate = sampleRate
        self.samples = samples
        self.siteID = siteID
        self.tdlType = tdlType
        self.whichGeometry = whichGeometry
        self.writeInterval = writeInterval
        self.geoSystem = geoSystem
        self.rtpHeaderExpected = rtpHeaderExpected

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if address is None:
            address = "localhost"
        assertSFString(address)
        self.__address = address

    @property
    def applicationID(self):
        return self.__applicationID

    @applicationID.setter
    def applicationID(self, applicationID):
        if applicationID is None:
            applicationID = 1
        assertSFInt32(applicationID)
        assertValidGreaterThanEquals(applicationID, 0)
        assertValidLessThanEquals(applicationID, 65535)
        self.__applicationID = applicationID

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if data is None:
            data = []
        assertMFInt32(data)
        assertValidGreaterThanEquals(data, 0)
        assertValidLessThanEquals(data, 255)
        self.__data = data

    @property
    def dataLength(self):
        return self.__dataLength

    @dataLength.setter
    def dataLength(self, dataLength):
        if dataLength is None:
            dataLength = 0
        assertSFInt32(dataLength)
        assertValidGreaterThanEquals(dataLength, 0)
        assertValidLessThanEquals(dataLength, 65535)
        self.__dataLength = dataLength

    @property
    def encodingScheme(self):
        return self.__encodingScheme

    @encodingScheme.setter
    def encodingScheme(self, encodingScheme):
        if encodingScheme is None:
            encodingScheme = 0
        assertSFInt32(encodingScheme)
        assertValidGreaterThanEquals(encodingScheme, 0)
        assertValidLessThanEquals(encodingScheme, 65535)
        self.__encodingScheme = encodingScheme

    @property
    def entityID(self):
        return self.__entityID

    @entityID.setter
    def entityID(self, entityID):
        if entityID is None:
            entityID = 0
        assertSFInt32(entityID)
        assertValidGreaterThanEquals(entityID, 0)
        assertValidLessThanEquals(entityID, 65535)
        self.__entityID = entityID

    @property
    def geoCoords(self):
        return self.__geoCoords

    @geoCoords.setter
    def geoCoords(self, geoCoords):
        if geoCoords is None:
            geoCoords = [0.0, 0.0, 0.0]
        assertSFVec3d(geoCoords)
        self.__geoCoords = geoCoords

    @property
    def multicastRelayHost(self):
        return self.__multicastRelayHost

    @multicastRelayHost.setter
    def multicastRelayHost(self, multicastRelayHost):
        if multicastRelayHost is None:
            multicastRelayHost = ""
        assertSFString(multicastRelayHost)
        self.__multicastRelayHost = multicastRelayHost

    @property
    def multicastRelayPort(self):
        return self.__multicastRelayPort

    @multicastRelayPort.setter
    def multicastRelayPort(self, multicastRelayPort):
        if multicastRelayPort is None:
            multicastRelayPort = 0
        assertSFInt32(multicastRelayPort)
        self.__multicastRelayPort = multicastRelayPort

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if port is None:
            port = 0
        assertSFInt32(port)
        assertValidGreaterThanEquals(port, 0)
        assertValidLessThanEquals(port, 65535)
        self.__port = port

    @property
    def radioID(self):
        return self.__radioID

    @radioID.setter
    def radioID(self, radioID):
        if radioID is None:
            radioID = 0
        assertSFInt32(radioID)
        assertValidGreaterThanEquals(radioID, 0)
        assertValidLessThanEquals(radioID, 65535)
        self.__radioID = radioID

    @property
    def readInterval(self):
        return self.__readInterval

    @readInterval.setter
    def readInterval(self, readInterval):
        if readInterval is None:
            readInterval = 0.1
        assertSFTime(readInterval)
        assertValidGreaterThanEquals(readInterval, 0)
        self.__readInterval = readInterval

    @property
    def rtpHeaderExpected(self):
        return self.__rtpHeaderExpected

    @rtpHeaderExpected.setter
    def rtpHeaderExpected(self, rtpHeaderExpected):
        if rtpHeaderExpected is None:
            rtpHeaderExpected = False
        assertSFBool(rtpHeaderExpected)
        self.__rtpHeaderExpected = rtpHeaderExpected

    @property
    def sampleRate(self):
        return self.__sampleRate

    @sampleRate.setter
    def sampleRate(self, sampleRate):
        if sampleRate is None:
            sampleRate = 0
        assertSFInt32(sampleRate)
        assertValidGreaterThanEquals(sampleRate, 0)
        assertValidLessThanEquals(sampleRate, 65535)
        self.__sampleRate = sampleRate

    @property
    def samples(self):
        return self.__samples

    @samples.setter
    def samples(self, samples):
        if samples is None:
            samples = 0
        assertSFInt32(samples)
        assertValidGreaterThanEquals(samples, 0)
        assertValidLessThanEquals(samples, 65535)
        self.__samples = samples

    @property
    def siteID(self):
        return self.__siteID

    @siteID.setter
    def siteID(self, siteID):
        if siteID is None:
            siteID = 0
        assertSFInt32(siteID)
        assertValidGreaterThanEquals(siteID, 0)
        assertValidLessThanEquals(siteID, 65535)
        self.__siteID = siteID

    @property
    def tdlType(self):
        return self.__tdlType

    @tdlType.setter
    def tdlType(self, tdlType):
        if tdlType is None:
            tdlType = 0
        assertSFInt32(tdlType)
        assertValidGreaterThanEquals(tdlType, 0)
        assertValidLessThanEquals(tdlType, 65535)
        self.__tdlType = tdlType

    @property
    def whichGeometry(self):
        return self.__whichGeometry

    @whichGeometry.setter
    def whichGeometry(self, whichGeometry):
        if whichGeometry is None:
            whichGeometry = 1
        assertSFInt32(whichGeometry)
        assertValidGreaterThanEquals(whichGeometry, -1)
        self.__whichGeometry = whichGeometry

    @property
    def writeInterval(self):
        return self.__writeInterval

    @writeInterval.setter
    def writeInterval(self, writeInterval):
        if writeInterval is None:
            writeInterval = 1.0
        assertSFFloat(writeInterval)
        assertValidGreaterThanEquals(writeInterval, 0)
        self.__writeInterval = writeInterval

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class TimeSensor(X3DTimeDependentNode, X3DSensorNode): 
    """
    TimeSensor : X3DTimeDependentNode, X3DSensorNode {
        SFTime  [in,out] cycleInterval    1     (0,∞)
        SFBool  [in,out] enabled          TRUE
        SFBool  [in,out] loop             FALSE
        SFNode  [in,out] metadata         NULL  [X3DMetadataObject]
        SFTime  [in,out] pauseTime        0     (-∞,∞)
        SFTime  [in,out] resumeTime       0
        SFTime  [in,out] startTime        0     (-∞,∞)
        SFTime  [in,out] stopTime         0     (-∞,∞)
        SFTime  [out]    cycleTime
        SFTime  [out]    elapsedTime
        SFFloat [out]    fraction_changed
        SFBool  [out]    isActive
        SFBool  [out]    isPaused
        SFTime  [out]    time
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            cycleInterval=1.0,
            enabled=True,
            loop=False,
            pauseTime=0.0,
            resumeTime=0.0,
            startTime=0.0,
            stopTime=0.0,
            **kwargs
            
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            loop=loop,
            pauseTime=pauseTime,
            resumeTime=resumeTime,
            startTime=startTime,
            stopTime=stopTime,
            enabled=enabled,
            **kwargs
        )
        self.cycleInterval = cycleInterval

    @property
    def cycleInterval(self):
        return self.__cycleInterval

    @cycleInterval.setter
    def cycleInterval(self, cycleInterval):
        if cycleInterval is None:
            cycleInterval = 1.0
        assertSFTime(cycleInterval)
        assertValidGreaterThan(cycleInterval, 0)
        self.__cycleInterval = cycleInterval
    
class TransmitterPdu(X3DNetworkSensorNode, X3DBoundedObject):
    """
    TransmitterPdu : X3DNetworkSensorNode, X3DBoundedObject { 
        SFString [in,out] address                            "localhost"
        SFVec3f  [in,out] antennaLocation                    0 0 0        (-∞,∞)
        SFInt32  [in,out] antennaPatternLength               0            [0,65535]
        SFInt32  [in,out] antennaPatternType                 0            [0,65535]
        SFInt32  [in,out] applicationID                      1            [0,65535]
        SFInt32  [in,out] cryptoKeyID                        0            [0,65535]           
        SFInt32  [in,out] cryptoSystem                       0            [0,65535]
        SFBool   [in,out] enabled                            TRUE
        SFInt32  [in,out] entityID                           0            [0,65535]
        SFInt32  [in,out] frequency                          0      
        SFVec3d  [in,out] geoCoords                          0 0 0        (-∞,∞)
        SFInt32  [in,out] inputSource                        0            [0,255]
        SFInt32  [in,out] lengthOfModulationParameters       0            [0,255]
        SFNode   [in,out] metadata                           NULL         [X3DMetadataObject]
        SFInt32  [in,out] modulationTypeDetail               0            [0,65535]
        SFInt32  [in,out] modulationTypeMajor                0            [0,65535]
        SFInt32  [in,out] modulationTypeSpreadSpectrum       0            [0,65535]
        SFInt32  [in,out] modulationTypeSystem               0            [0,65535]
        SFString [in,out] multicastRelayHost                 ""
        SFInt32  [in,out] multicastRelayPort                 0           
        SFString [in,out] networkMode                        "standAlone" ["standAlone"|
                                                                            "networkReader"|
                                                                            "networkWriter"]
        SFInt32  [in,out] port                               0            [0,65535]
        SFFloat  [in,out] power                              0.0          [0,∞)
        SFInt32  [in,out] radioEntityTypeCategory            0            [0,255]
        SFInt32  [in,out] radioEntityTypeCountry             0            [0,65535]
        SFInt32  [in,out] radioEntityTypeDomain              0            [0,255]
        SFInt32  [in,out] radioEntityTypeKind                0            [0,255]
        SFInt32  [in,out] radioEntityTypeNomenclature        0            [0,255]
        SFInt32  [in,out] radioEntityTypeNomenclatureVersion 0            [0,65535]
        SFInt32  [in,out] radioID                            0            [0,255]
        SFFloat  [in,out] readInterval                       0.1          [0,∞)
        SFVec3f  [in,out] relativeAntennaLocation            0 0 0        (-∞,∞)
        SFBool   [in,out] rtpHeaderExpected                  FALSE
        SFInt32  [in,out] siteID                             0            [0,65535]
        SFFloat  [in,out] transmitFrequencyBandwidth         0.0          (-∞,∞)
        SFInt32  [in,out] transmitState                      0            [0,255]
        SFInt32  [in,out] whichGeometry                      1            [-1,∞)
        SFFloat  [in,out] writeInterval                      1.0          [0,∞)
        SFBool   [out]    isActive                           FALSE
        SFBool   [out]    isNetworkReader                    FALSE
        SFBool   [out]    isNetworkWriter                    FALSE
        SFBool   [out]    isRtpHeaderHeard                   FALSE
        SFBool   [out]    isStandAlone                       FALSE
        SFTime   [out]    timestamp                          0
        SFVec3f  []       bboxCenter                         0 0 0        (-∞,∞)
        SFVec3f  []       bboxSize                           -1 -1 -1     [0,∞) [0,∞) [0,∞) or −1 −1 −1
        MFString []       geoSystem                          ["GD","WE"]  [see 25.2.3]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            address="localhost",
            antennaLocation=[0.0, 0.0, 0.0],
            antennaPatternLength=0,
            antennaPatternType=0,
            applicationID=1,
            cryptoKeyID=0,
            cryptoSystem=0,
            enabled=True,
            entityID=0,
            frequency=0,
            geoCoords=[0.0, 0.0, 0.0],
            inputSource=0,
            lengthOfModulationParameters=0,
            modulationTypeDetail=0,
            modulationTypeMajor=0,
            modulationTypeSpreadSpectrum=0,
            modulationTypeSystem=0,
            multicastRelayHost="",
            multicastRelayPort=0,
            networkMode="standAlone",
            port=0,
            power=0.0,
            radioEntityTypeCategory=0.0,
            radioEntityTypeCountry=0,
            radioEntityTypeDomain=0,
            radioEntityTypeKind=0,
            radioEntityTypeNomenclature=0,
            radioEntityTypeNomenclatureVersion=0,
            radioID=0,
            readInterval=0.1,
            relativeAntennaLocation=0,
            rtpHeaderExpected=False,
            siteID=0,
            transmitFrequencyBandwidth=0.0,
            transmitState=0,
            whichGeometry=1,
            writeInterval=1.0,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.address = address
        self.antennaLocation = antennaLocation
        self.antennaPatternLength = antennaPatternLength
        self.antennaPatternType = antennaPatternType
        self.applicationID = applicationID
        self.cryptoKeyID = cryptoKeyID
        self.cryptoSystem = cryptoSystem
        self.entityID = entityID
        self.frequency = frequency
        self.geoCoords = geoCoords
        self.inputSource = inputSource
        self.lengthOfModulationParameters = lengthOfModulationParameters
        self.modulationTypeDetail = modulationTypeDetail
        self.modulationTypeMajor = modulationTypeMajor
        self.modulationTypeSpreadSpectrum = modulationTypeSpreadSpectrum
        self.modulationTypeSystem = modulationTypeSystem
        self.multicastRelayHost = multicastRelayHost
        self.multicastRelayPort = multicastRelayPort
        self.networkMode = networkMode
        self.port = port
        self.power = power
        self.radioEntityTypeCategory = radioEntityTypeCategory
        self.radioEntityTypeCountry = radioEntityTypeCountry
        self.radioEntityTypeDomain = radioEntityTypeDomain
        self.radioEntityTypeKind = radioEntityTypeKind
        self.radioEntityTypeNomenclature = radioEntityTypeNomenclature
        self.radioEntityTypeNomenclatureVersion = radioEntityTypeNomenclatureVersion
        self.radioID = radioID
        self.readInterval = readInterval
        self.relativeAntennaLocation = relativeAntennaLocation
        self.rtpHeaderExpected = rtpHeaderExpected
        self.siteID = siteID
        self.transmitFrequencyBandwidth = transmitFrequencyBandwidth
        self.transmitState = transmitState
        self.whichGeometry = whichGeometry
        self.writeInterval = writeInterval
        self.geoSystem = geoSystem

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if address is None:
            address = "localhost"
        assertSFString(address)
        self.__address = address

    @property
    def antennaLocation(self):
        return self.__antennaLocation

    @antennaLocation.setter
    def antennaLocation(self, antennaLocation):
        if antennaLocation is None:
            antennaLocation = [0.0, 0.0, 0.0]
        assertSFVec3f(antennaLocation)
        self.__antennaLocation = antennaLocation

    @property
    def antennaPatternLength(self):
        return self.__antennaPatternLength

    @antennaPatternLength.setter
    def antennaPatternLength(self, antennaPatternLength):
        if antennaPatternLength is None:
            antennaPatternLength = 0
        assertSFInt32(antennaPatternLength)
        assertValidGreaterThanEquals(antennaPatternLength, 0)
        assertValidLessThanEquals(antennaPatternLength, 65535)
        self.__antennaPatternLength = antennaPatternLength

    @property
    def antennaPatternType(self):
        return self.__antennaPatternType

    @antennaPatternType.setter
    def antennaPatternType(self, antennaPatternType):
        if antennaPatternType is None:
            antennaPatternType = 0
        assertSFInt32(antennaPatternType)
        assertValidGreaterThanEquals(antennaPatternType, 0)
        assertValidLessThanEquals(antennaPatternType, 65535)
        self.__antennaPatternType = antennaPatternType

    @property
    def applicationID(self):
        return self.__applicationID

    @applicationID.setter
    def applicationID(self, applicationID):
        if applicationID is None:
            applicationID = 1
        assertSFInt32(applicationID)
        assertValidGreaterThanEquals(applicationID, 0)
        assertValidLessThanEquals(applicationID, 65535)
        self.__applicationID = applicationID

    @property
    def cryptoKeyID(self):
        return self.__cryptoKeyID

    @cryptoKeyID.setter
    def cryptoKeyID(self, cryptoKeyID):
        if cryptoKeyID is None:
            cryptoKeyID = 0
        assertSFInt32(cryptoKeyID)
        assertValidGreaterThanEquals(cryptoKeyID, 0)
        assertValidLessThanEquals(cryptoKeyID, 65535)
        self.__cryptoKeyID = cryptoKeyID

    @property
    def cryptoSystem(self):
        return self.__cryptoSystem

    @cryptoSystem.setter
    def cryptoSystem(self, cryptoSystem):
        if cryptoSystem is None:
            cryptoSystem = 0
        assertSFInt32(cryptoSystem)
        assertValidGreaterThanEquals(cryptoSystem, 0)
        assertValidLessThanEquals(cryptoSystem, 65535)
        self.__cryptoSystem = cryptoSystem

    @property
    def entityID(self):
        return self.__entityID

    @entityID.setter
    def entityID(self, entityID):
        if entityID is None:
            entityID = 0
        assertSFInt32(entityID)
        assertValidGreaterThanEquals(entityID, 0)
        assertValidLessThanEquals(entityID, 65535)
        self.__entityID = entityID

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency):
        if frequency is None:
            frequency = 0
        assertSFInt32(frequency)
        self.__frequency = frequency

    @property
    def geoCoords(self):
        return self.__geoCoords

    @geoCoords.setter
    def geoCoords(self, geoCoords):
        if geoCoords is None:
            geoCoords = [0.0, 0.0, 0.0]
        assertSFVec3d(geoCoords)
        self.__geoCoords = geoCoords

    @property
    def inputSource(self):
        return self.__inputSource

    @inputSource.setter
    def inputSource(self, inputSource):
        if inputSource is None:
            inputSource = 0
        assertSFInt32(inputSource)
        assertValidGreaterThanEquals(inputSource, 0)
        assertValidLessThanEquals(inputSource, 255)
        self.__inputSource = inputSource

    @property
    def lengthOfModulationParameters(self):
        return self.__lengthOfModulationParameters

    @lengthOfModulationParameters.setter
    def lengthOfModulationParameters(self, lengthOfModulationParameters):
        if lengthOfModulationParameters is None:
            lengthOfModulationParameters = 0
        assertSFInt32(lengthOfModulationParameters)
        assertValidGreaterThanEquals(lengthOfModulationParameters, 0)
        assertValidLessThanEquals(lengthOfModulationParameters, 255)
        self.__lengthOfModulationParameters = lengthOfModulationParameters

    @property
    def modulationTypeDetail(self):
        return self.__modulationTypeDetail

    @modulationTypeDetail.setter
    def modulationTypeDetail(self, modulationTypeDetail):
        if modulationTypeDetail is None:
            modulationTypeDetail = 0
        assertSFInt32(modulationTypeDetail)
        assertValidGreaterThanEquals(modulationTypeDetail, 0)
        assertValidLessThanEquals(modulationTypeDetail, 65535)
        self.__modulationTypeDetail = modulationTypeDetail

    @property
    def modulationTypeMajor(self):
        return self.__modulationTypeMajor

    @modulationTypeMajor.setter
    def modulationTypeMajor(self, modulationTypeMajor):
        if modulationTypeMajor is None:
            modulationTypeMajor = 0
        assertSFInt32(modulationTypeMajor)
        assertValidGreaterThanEquals(modulationTypeMajor, 0)
        assertValidLessThanEquals(modulationTypeMajor, 65535)
        self.__modulationTypeMajor = modulationTypeMajor

    @property
    def modulationTypeSpreadSpectrum(self):
        return self.__modulationTypeSpreadSpectrum

    @modulationTypeSpreadSpectrum.setter
    def modulationTypeSpreadSpectrum(self, modulationTypeSpreadSpectrum):
        if modulationTypeSpreadSpectrum is None:
            modulationTypeSpreadSpectrum = 0
        assertSFInt32(modulationTypeSpreadSpectrum)
        assertValidGreaterThanEquals(modulationTypeSpreadSpectrum, 0)
        assertValidLessThanEquals(modulationTypeSpreadSpectrum, 65535)
        self.__modulationTypeSpreadSpectrum = modulationTypeSpreadSpectrum

    @property
    def modulationTypeSystem(self):
        return self.__modulationTypeSystem

    @modulationTypeSystem.setter
    def modulationTypeSystem(self, modulationTypeSystem):
        if modulationTypeSystem is None:
            modulationTypeSystem = 0
        assertSFInt32(modulationTypeSystem)
        assertValidGreaterThanEquals(modulationTypeSystem, 0)
        assertValidLessThanEquals(modulationTypeSystem, 65535)
        self.__modulationTypeSystem = modulationTypeSystem

    @property
    def multicastRelayHost(self):
        return self.__multicastRelayHost

    @multicastRelayHost.setter
    def multicastRelayHost(self, multicastRelayHost):
        if multicastRelayHost is None:
            multicastRelayHost = ""
        assertSFString(multicastRelayHost)
        self.__multicastRelayHost = multicastRelayHost

    @property
    def multicastRelayPort(self):
        return self.__multicastRelayPort

    @multicastRelayPort.setter
    def multicastRelayPort(self, multicastRelayPort):
        if multicastRelayPort is None:
            multicastRelayPort = 0
        assertSFInt32(multicastRelayPort)
        self.__multicastRelayPort = multicastRelayPort

    @property
    def networkMode(self):
        return self.__networkMode

    @networkMode.setter
    def networkMode(self, networkMode):
        if networkMode is None:
            networkMode = "standAlone"
        assertValidNetworkMode(networkMode)
        self.__networkMode = networkMode

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if port is None:
            port = 0
        assertSFInt32(port)
        assertValidGreaterThanEquals(port, 0)
        assertValidLessThanEquals(port, 65535)
        self.__port = port

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        if power is None:
            power = 0.0
        assertSFFloat(power)
        assertValidGreaterThanEquals(power, 0)
        self.__power = power

    @property
    def radioEntityTypeCategory(self):
        return self.__radioEntityTypeCategory

    @radioEntityTypeCategory.setter
    def radioEntityTypeCategory(self, radioEntityTypeCategory):
        if radioEntityTypeCategory is None:
            radioEntityTypeCategory = 0
        assertSFInt32(radioEntityTypeCategory)
        assertValidGreaterThanEquals(radioEntityTypeCategory, 0)
        assertValidLessThanEquals(radioEntityTypeCategory, 255)
        self.__radioEntityTypeCategory = radioEntityTypeCategory

    @property
    def radioEntityTypeCountry(self):
        return self.__radioEntityTypeCountry

    @radioEntityTypeCountry.setter
    def radioEntityTypeCountry(self, radioEntityTypeCountry):
        if radioEntityTypeCountry is None:
            radioEntityTypeCountry = 0
        assertSFInt32(radioEntityTypeCountry)
        assertValidGreaterThanEquals(radioEntityTypeCountry, 0)
        assertValidLessThanEquals(radioEntityTypeCountry, 65535)
        self.__radioEntityTypeCountry = radioEntityTypeCountry

    @property
    def radioEntityTypeDomain(self):
        return self.__radioEntityTypeDomain

    @radioEntityTypeDomain.setter
    def radioEntityTypeDomain(self, radioEntityTypeDomain):
        if radioEntityTypeDomain is None:
            radioEntityTypeDomain = 0
        assertSFInt32(radioEntityTypeDomain)
        assertValidGreaterThanEquals(radioEntityTypeDomain, 0)
        assertValidLessThanEquals(radioEntityTypeDomain, 255)
        self.__radioEntityTypeDomain = radioEntityTypeDomain

    @property
    def radioEntityTypeKind(self):
        return self.__radioEntityTypeKind

    @radioEntityTypeKind.setter
    def radioEntityTypeKind(self, radioEntityTypeKind):
        if radioEntityTypeKind is None:
            radioEntityTypeKind = 0
        assertSFInt32(radioEntityTypeKind)
        assertValidGreaterThanEquals(radioEntityTypeKind, 0)
        assertValidLessThanEquals(radioEntityTypeKind, 255)
        self.__radioEntityTypeKind = radioEntityTypeKind

    @property
    def radioEntityTypeNomenclature(self):
        return self.__radioEntityTypeNomenclature

    @radioEntityTypeNomenclature.setter
    def radioEntityTypeNomenclature(self, radioEntityTypeNomenclature):
        if radioEntityTypeNomenclature is None:
            radioEntityTypeNomenclature = 0
        assertSFInt32(radioEntityTypeNomenclature)
        assertValidGreaterThanEquals(radioEntityTypeNomenclature, 0)
        assertValidLessThanEquals(radioEntityTypeNomenclature, 255)
        self.__radioEntityTypeNomenclature = radioEntityTypeNomenclature

    @property
    def radioEntityTypeNomenclatureVersion(self):
        return self.__radioEntityTypeNomenclatureVersion

    @radioEntityTypeNomenclatureVersion.setter
    def radioEntityTypeNomenclatureVersion(self, radioEntityTypeNomenclatureVersion):
        if radioEntityTypeNomenclatureVersion is None:
            radioEntityTypeNomenclatureVersion = 0
        assertSFInt32(radioEntityTypeNomenclatureVersion)
        assertValidGreaterThanEquals(radioEntityTypeNomenclatureVersion, 0)
        assertValidLessThanEquals(radioEntityTypeNomenclatureVersion, 65535)
        self.__radioEntityTypeNomenclatureVersion = radioEntityTypeNomenclatureVersion

    @property
    def radioID(self):
        return self.__radioID

    @radioID.setter
    def radioID(self, radioID):
        if radioID is None:
            radioID = 0
        assertSFInt32(radioID)
        assertValidGreaterThanEquals(radioID, 0)
        assertValidLessThanEquals(radioID, 65535)
        self.__radioID = radioID

    @property
    def readInterval(self):
        return self.__readInterval

    @readInterval.setter
    def readInterval(self, readInterval):
        if readInterval is None:
            readInterval = 0.1
        assertSFTime(readInterval)
        assertValidGreaterThanEquals(readInterval, 0)
        self.__readInterval = readInterval

    @property
    def relativeAntennaLocation(self):
        return self.__relativeAntennaLocation

    @relativeAntennaLocation.setter
    def relativeAntennaLocation(self, relativeAntennaLocation):
        if relativeAntennaLocation is None:
            relativeAntennaLocation = [0.0, 0.0, 0.0]
        assertSFVec3f(relativeAntennaLocation)
        self.__relativeAntennaLocation = relativeAntennaLocation

    @property
    def rtpHeaderExpected(self):
        return self.__rtpHeaderExpected

    @rtpHeaderExpected.setter
    def rtpHeaderExpected(self, rtpHeaderExpected):
        if rtpHeaderExpected is None:
            rtpHeaderExpected = False
        assertSFBool(rtpHeaderExpected)
        self.__rtpHeaderExpected = rtpHeaderExpected

    @property
    def siteID(self):
        return self.__siteID

    @siteID.setter
    def siteID(self, siteID):
        if siteID is None:
            siteID = 0
        assertSFInt32(siteID)
        assertValidGreaterThanEquals(siteID, 0)
        assertValidLessThanEquals(siteID, 65535)
        self.__siteID = siteID

    @property
    def transmitFrequencyBandwidth(self):
        return self.__transmitFrequencyBandwidth

    @transmitFrequencyBandwidth.setter
    def transmitFrequencyBandwidth(self, transmitFrequencyBandwidth):
        if transmitFrequencyBandwidth is None:
            transmitFrequencyBandwidth = 0.0
        assertSFFloat(transmitFrequencyBandwidth)
        self.__transmitFrequencyBandwidth = transmitFrequencyBandwidth

    @property
    def transmitState(self):
        return self.__transmitState

    @transmitState.setter
    def transmitState(self, transmitState):
        if transmitState is None:
            transmitState = 0
        assertSFInt32(transmitState)
        assertValidGreaterThanEquals(transmitState, 0)
        assertValidLessThanEquals(transmitState, 255)
        self.__transmitState = transmitState

    @property
    def whichGeometry(self):
        return self.__whichGeometry

    @whichGeometry.setter
    def whichGeometry(self, whichGeometry):
        if whichGeometry is None:
            whichGeometry = 1
        assertSFInt32(whichGeometry)
        assertValidGreaterThanEquals(whichGeometry, -1)
        self.__whichGeometry = whichGeometry
    
    @property
    def writeInterval(self):
        return self.__writeInterval

    @writeInterval.setter
    def writeInterval(self, writeInterval):
        if writeInterval is None:
            writeInterval = 1.0
        assertSFFloat(writeInterval)
        assertValidGreaterThanEquals(writeInterval, 0)
        self.__writeInterval = writeInterval

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class GeoProximitySensor(X3DEnvironmentalSensorNode):
    """
    GeoProximitySensor : X3DEnvironmentalSensorNode {
        SFBool     [in,out] enabled                  TRUE
        SFVec3d    [in,out] geoCenter                0 0 0       (-∞,∞) (deprecated as of vs. 3.3)
        SFVec3d    [in,out] center                   0 0 0       (-∞,∞) (starting with vs. 3.3)
        SFNode     [in,out] metadata                 NULL        [X3DMetadataObject]
        SFVec3f    [in,out] size                     0 0 0       [0,∞)
        SFVec3f    [out]    centerOfRotation_changed
        SFTime     [out]    enterTime
        SFTime     [out]    exitTime
        SFVec3d    [out]    geoCoord_changed
        SFBool     [out]    isActive
        SFRotation [out]    orientation_changed
        SFVec3f    [out]    position_changed
        SFNode     []       geoOrigin                NULL        [GeoOrigin] (deprecated)
        MFString   []       geoSystem                ["GD","WE"] [see 25.2.3]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            geoCenter=[0.0, 0.0, 0.0],
            center=[0.0, 0.0, 0.0],
            size=[0.0, 0.0, 0.0],
            geoOrigin=None,
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            center=center,
            enabled=enabled,
            size=size,
            **kwargs
        )
        self.geoCenter = geoCenter
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem

    @property
    def geoCenter(self):
        return self.__geoCenter

    @geoCenter.setter
    def geoCenter(self, geoCenter):
        if geoCenter is None:
            geoCenter = [0.0, 0.0, 0.0]
        assertSFVec3d(geoCenter)
        self.__geoCenter = geoCenter

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class ProximitySensor(X3DEnvironmentalSensorNode):
    """
    ProximitySensor : X3DEnvironmentalSensorNode {
        SFVec3f    [in,out] center                   0 0 0 (-∞,∞)
        SFBool     [in,out] enabled                  TRUE
        SFNode     [in,out] metadata                 NULL  [X3DMetadataObject]
        SFVec3f    [in,out] size                     0 0 0 [0,∞)
        SFTime     [out]    enterTime
        SFTime     [out]    exitTime
        SFVec3f    [out]    centerOfRotation_changed
        SFBool     [out]    isActive
        SFRotation [out]    orientation_changed
        SFVec3f    [out]    position_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            enabled=True,
            size=[0.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            center=center,
            enabled=enabled,
            size=size,
            **kwargs
        )

class TransformSensor(X3DEnvironmentalSensorNode): 
    """
    TransformSensor : X3DEnvironmentalSensorNode {
        SFVec3f    [in,out] center              0 0 0 (-∞,∞)
        SFBool     [in,out] enabled             TRUE
        SFNode     [in,out] metadata            NULL  [X3DMetadataObject]
        SFVec3f    [in,out] size                0 0 0 [0,∞)
        SFNode     [in,out] targetObject        NULL  [X3DGroupingNode|X3DShapeNode]
        SFTime     [out]    enterTime
        SFTime     [out]    exitTime
        SFBool     [out]    isActive
        SFRotation [out]    orientation_changed
        SFVec3f    [out]    position_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            enabled=True,
            size=[0.0, 0.0, 0.0],
            targetObject=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            center=center,
            enabled=enabled,
            size=size,
            **kwargs
        )
        self.targetObject = targetObject
    
    @property
    def targetObject(self):
        return self.__targetObject

    @targetObject.setter
    def targetObject(self, targetObject):
        if targetObject is None:
            targetObject = None
        assertSFNode(targetObject, X3DGroupingNode, X3DShapeNode)
        self.__targetObject = targetObject
        
class VisibilitySensor(X3DEnvironmentalSensorNode):
    """
    VisibilitySensor : X3DEnvironmentalSensorNode {
        SFVec3f [in,out] center    0 0 0 (-∞,∞)
        SFBool  [in,out] enabled   TRUE
        SFNode  [in,out] metadata  NULL  [X3DMetadataObject]
        SFVec3f [in,out] size      0 0 0 [0,∞)
        SFTime  [out]    enterTime
        SFTime  [out]    exitTime
        SFBool  [out]    isActive
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            center=[0.0, 0.0, 0.0],
            enabled=True,
            size=[0.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            center=center,
            enabled=enabled,
            size=size,
            **kwargs
        )

class KeySensor(X3DKeyDeviceSensorNode):
    """
    KeySensor : X3DKeyDeviceSensorNode {
        SFBool   [in,out] enabled          TRUE
        SFNode   [in,out] metadata         NULL [X3DMetadataObject]
        SFInt32  [out]    actionKeyPress   
        SFInt32  [out]    actionKeyRelease 
        SFBool   [out]    altKey           
        SFBool   [out]    controlKey       
        SFBool   [out]    isActive         
        SFString [out]    keyPress         
        SFString [out]    keyRelease       
        SFBool   [out]    shiftKey         
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )

class StringSensor(X3DKeyDeviceSensorNode):
    """
    StringSensor  : X3DKeyDeviceSensorNode {
        SFBool   [in,out] deletionAllowed TRUE
        SFBool   [in,out] enabled         TRUE
        SFNode   [in,out] metadata        NULL [X3DMetadataObject]
        SFString [out]    enteredText       
        SFString [out]    finalText         
        SFBool   [out]    isActive          
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            deletionAllowed=True,
            enabled=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.deletionAllowed = deletionAllowed

    @property
    def deletionAllowed(self):
        return self.__deletionAllowed

    @deletionAllowed.setter
    def deletionAllowed(self, deletionAllowed):
        if deletionAllowed is None:
            deletionAllowed = True
        assertSFBool(deletionAllowed)
        self.__deletionAllowed = deletionAllowed

class LoadSensor(X3DNetworkSensorNode):
    """
        LoadSensor : X3DNetworkSensorNode {
        SFBool  [in,out] enabled   TRUE
        SFNode  [in,out] metadata  NULL [X3DMetadataObject]
        SFTime  [in,out] timeOut   0
        MFNode  [in,out] watchList []   [X3DUrlObject]
        SFBool  [out]    isActive
        SFBool  [out]    isLoaded
        SFTime  [out]    loadTime
        SFFloat [out]    progress
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            timeout=0.0,
            watchList=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            **kwargs
        )
        self.timeout = timeout
        self.watchList = watchList

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout):
        if timeout is None:
            timeout = 0.0
        assertSFTime(timeout)
        self.__timeout = timeout

    @property
    def watchList(self):
        return self.__watchList

    @watchList.setter
    def watchList(self, watchList):
        if watchList is None:
            watchList = []
        assertMFNode(watchList, X3DUrlObject)
        self.__watchList = watchList

class LinePickSensor(X3DPickSensorNode):
    """
    LinePickSensor : X3DPickSensorNode {
        SFBool   [in,out] enabled                 TRUE
        SFNode   [in,out] metadata                NULL      [X3DMetadataObject]
        MFString [in,out] objectType              "ALL"     ["ALL","NONE","TERRAIN",...]
        SFNode   [in,out] pickingGeometry         NULL      [IndexedLineSet|LineSet]
        MFNode   [in,out] pickTarget              []        [X3DGroupingNode|X3DShapeNode|Inline]
        SFBool   [out]    isActive
        MFNode   [out]    pickedGeometry
        MFVec3f  [out]    pickedNormal
        MFVec3f  [out]    pickedPoint
        MFVec3f  [out]    pickedTextureCoordinate
        SFString []       intersectionType        "BOUNDS"  ["GEOMETRY"|"BOUNDS"|...]
        SFString []       sortOrder               "CLOSEST" ["ANY"|"CLOSEST"|"ALL"|"ALL_SORTED"]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            objectType=["ALL"],
            pickingGeometry=None,
            pickTarget=[],
            intersectionType="BOUNDS",
            sortOrder="CLOSEST",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            objectType=objectType,
            pickTarget=pickTarget,
            intersectionType=intersectionType,
            sortOrder=sortOrder,
            **kwargs
        )
        self.pickingGeometry = pickingGeometry

    @property
    def pickingGeometry(self):
        return self.__pickingGeometry

    @pickingGeometry.setter
    def pickingGeometry(self, pickingGeometry):
        if pickingGeometry is None:
            pickingGeometry = None
        assertSFNode(pickingGeometry, IndexedLineSet, LineSet)
        self.__pickingGeometry = pickingGeometry

class PointPickSensor(X3DPickSensorNode):
    """
    PointPickSensor : X3DPickSensorNode {
        SFBool   [in,out] enabled          TRUE
        SFNode   [in,out] metadata         NULL      [X3DMetadataObject]
        MFString [in,out] objectType       "ALL"     ["ALL","NONE","TERRAIN",...]
        SFNode   [in,out] pickingGeometry  NULL      [PointSet]
        MFNode   [in,out] pickTarget       []        [X3DGroupingNode|X3DShapeNode|Inline]
        SFBool   [out]    isActive
        MFNode   [out]    pickedGeometry
        MFVec3f  [out]    pickedPoint
        SFString []       intersectionType "BOUNDS"  ["GEOMETRY"|"BOUNDS"|...]
        SFString []       sortOrder        "CLOSEST" ["CLOSEST"|"ALL"|"ALL_SORTED"]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            objectType=["ALL"],
            pickingGeometry=None,
            pickTarget=[],
            intersectionType="BOUNDS",
            sortOrder="CLOSEST",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            objectType=objectType,
            pickTarget=pickTarget,
            intersectionType=intersectionType,
            sortOrder=sortOrder,
            **kwargs
        )
        self.pickingGeometry = pickingGeometry

    @property
    def pickingGeometry(self):
        return self.__pickingGeometry

    @pickingGeometry.setter
    def pickingGeometry(self, pickingGeometry):
        if pickingGeometry is None:
            pickingGeometry = None
        assertSFNode(pickingGeometry, PointSet)
        self.__pickingGeometry = pickingGeometry

class PrimitivePickSensor(X3DPickSensorNode):
    """
    PrimitivePickSensor : X3DPickSensorNode {
        SFBool   [in,out] enabled          TRUE
        SFNode   [in,out] metadata         NULL      [X3DMetadataObject]
        MFString [in,out] objectType       "ALL"     ["ALL","NONE","TERRAIN",...]
        SFNode   [in,out] pickingGeometry  NULL      [Cone|Cylinder|Sphere|Box]
        MFNode   [in,out] pickTarget       []        [X3DGroupingNode|X3DShapeNode|Inline]
        SFBool   [out]    isActive
        MFNode   [out]    pickedGeometry
        SFString []       intersectionType "BOUNDS"  ["GEOMETRY"|"BOUNDS"|...]
        SFString []       sortOrder        "CLOSEST" ["ANY"|"CLOSEST"|"ALL"|"ALL_SORTED"]
    }   
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            objectType=["ALL"],
            pickingGeometry=None,
            pickTarget=[],
            intersectionType="BOUNDS",
            sortOrder="CLOSEST",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            objectType=objectType,
            pickTarget=pickTarget,
            intersectionType=intersectionType,
            sortOrder=sortOrder,
            **kwargs
        )
        self.pickingGeometry = pickingGeometry

    @property
    def pickingGeometry(self):
        return self.__pickingGeometry

    @pickingGeometry.setter
    def pickingGeometry(self, pickingGeometry):
        if pickingGeometry is None:
            pickingGeometry = None
        assertSFNode(pickingGeometry, Cone, Cylinder, Sphere, Box)
        self.__pickingGeometry = pickingGeometry

class VolumePickSensor(X3DPickSensorNode):
    """
    VolumePickSensor : X3DPickSensorNode {
        SFBool   [in,out] enabled          TRUE
        SFNode   [in,out] metadata         NULL      [X3DMetadataObject]
        MFString [in,out] objectType       "ALL"     ["ALL","NONE","TERRAIN",...]
        SFNode   [in,out] pickingGeometry  NULL      [X3DGeometryNode]
        MFNode   [in,out] pickTarget       []        [X3DGroupingNode|X3DShapeNode|Inline]
        SFBool   [out]    isActive
        MFNode   [out]    pickedGeometry
        SFString []       intersectionType "BOUNDS"  ["GEOMETRY"|"BOUNDS"|...]
        SFString []       sortOrder        "CLOSEST" ["ANY"|"CLOSEST"|"ALL"|"ALL_SORTED"]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            objectType=["ALL"],
            pickingGeometry=None,
            pickTarget=[],
            intersectionType="BOUNDS",
            sortOrder="CLOSEST",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            objectType=objectType,
            pickingGeometry=pickingGeometry,
            pickTarget=pickTarget,
            intersectionType=intersectionType,
            sortOrder=sortOrder,
            **kwargs
        )

class CylinderSensor(X3DDragSensorNode): 
    """
    CylinderSensor : X3DDragSensorNode { 
        SFBool     [in,out] autoOffset         TRUE
        SFRotation [in,out] axisRotation       0 1 0 0
        SFString   [in,out] description        ""
        SFFloat    [in,out] diskAngle          π/12    [0,π/2]
        SFBool     [in,out] enabled            TRUE
        SFFloat    [in,out] maxAngle           -1      [-2π,2π]
        SFNode     [in,out] metadata           NULL    [X3DMetadataObject]
        SFFloat    [in,out] minAngle           0       [-2π,2π]
        SFFloat    [in,out] offset             0       (-∞,∞)
        SFBool     [out]    isActive
        SFBool     [out]    isOver
        SFRotation [out]    rotation_changed
        SFVec3f    [out]    trackPoint_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            autoOffset=True,
            axisRotation=[0.0, 1.0, 0.0, 0.0],
            diskAngle=math.pi/12,
            description="",
            enabled=True,
            maxAngle=-1.0,
            minAngle=0.0,
            offset=0.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            autoOffset=autoOffset,
            description=description,
            enabled=enabled,
            **kwargs
        )
        self.axisRotation = axisRotation
        self.diskAngle = diskAngle
        self.maxAngle = maxAngle
        self.minAngle = minAngle
        self.offset = offset

    @property
    def axisRotation(self):
        return self.__axisRotation

    @axisRotation.setter
    def axisRotation(self, axisRotation):
        if axisRotation is None:
            axisRotation = [0.0, 1.0, 0.0, 0.0]
        assertSFRotation(axisRotation)
        self.__axisRotation = axisRotation

    @property
    def diskAngle(self):
        return self.__diskAngle

    @diskAngle.setter
    def diskAngle(self, diskAngle):
        if diskAngle is None:
            diskAngle = math.pi/12
        assertSFFloat(diskAngle)
        assertValidGreaterThanEquals(diskAngle, 0)
        assertValidLessThanEquals(diskAngle, math.pi/2)
        self.__diskAngle = diskAngle

    @property
    def maxAngle(self):
        return self.__maxAngle

    @maxAngle.setter
    def maxAngle(self, maxAngle):
        if maxAngle is None:
            maxAngle = -1.0
        assertSFFloat(maxAngle)
        assertValidGreaterThanEquals(maxAngle, math.pi * -2)
        assertValidLessThanEquals(maxAngle, math.pi * 2)
        self.__maxAngle = maxAngle

    @property
    def minAngle(self):
        return self.__minAngle

    @minAngle.setter
    def minAngle(self, minAngle):
        if minAngle is None:
            minAngle = 0.0
        assertSFFloat(minAngle)
        assertValidGreaterThanEquals(minAngle, math.pi * -2)
        assertValidLessThanEquals(minAngle, math.pi * 2)
        self.__minAngle = minAngle

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        if offset is None:
            offset = 0.0
        assertSFFloat(offset)
        self.__offset = offset

class PlaneSensor(X3DDragSensorNode):
    """
    PlaneSensor : X3DDragSensorNode { 
        SFBool     [in,out] autoOffset          TRUE
        SFRotation [in,out] axisRotation        0 0 1 0
        SFString   [in,out] description         ""
        SFBool     [in,out] enabled             TRUE
        SFVec2f    [in,out] maxPosition         -1 -1 (-∞,∞)
        SFNode     [in,out] metadata            NULL  [X3DMetadataObject]
        SFVec2f    [in,out] minPosition         0 0   (-∞,∞)
        SFVec3f    [in,out] offset              0 0 0 (-∞,∞)
        SFBool     [out]    isActive
        SFBool     [out]    isOver
        SFVec3f    [out]    trackPoint_changed
        SFVec3f    [out]    translation_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            autoOffset=True,
            axisRotation=[0.0, 0.0, 1.0, 0.0],
            description="",
            enabled=True,
            maxPosition=[-1.0, -1.0],
            minPosition=[0.0, 0.0],
            offset=[0.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            autoOffset=autoOffset,
            description=description,
            enabled=enabled,
            **kwargs
        )
        self.axisRotation = axisRotation
        self.maxPosition = maxPosition
        self.minPosition = minPosition
        self.offset = offset

    @property
    def axisRotation(self):
        return self.__axisRotation

    @axisRotation.setter
    def axisRotation(self, axisRotation):
        if axisRotation is None:
            axisRotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(axisRotation)
        self.__axisRotation = axisRotation

    @property
    def maxPosition(self):
        return self.__maxPosition

    @maxPosition.setter
    def maxPosition(self, maxPosition):
        if maxPosition is None:
            maxPosition = [-1.0, -1.0]
        assertSFVec2f(maxPosition)
        self.__maxPosition = maxPosition

    @property
    def minPosition(self):
        return self.__minPosition

    @minPosition.setter
    def minPosition(self, minPosition):
        if minPosition is None:
            minPosition = [0.0, 0.0]
        assertSFVec2f(minPosition)
        self.__minPosition = minPosition

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        if offset is None:
            offset = [0.0, 0.0, 0.0]
        assertSFVec3f(offset)
        self.__offset = offset

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        if offset is None:
            offset = 0.0
        assertSFFloat(offset)
        self.__offset = offset

class SphereSensor(X3DDragSensorNode):
    """
    SphereSensor : X3DDragSensorNode { 
        SFBool     [in,out] autoOffset         TRUE
        SFString   [in,out] description        ""
        SFBool     [in,out] enabled            TRUE
        SFNode     [in,out] metadata           NULL    [X3DMetadataObject]
        SFRotation [in,out] offset             0 1 0 0 [-1,1],(-∞,∞)
        SFBool     [out]    isActive
        SFBool     [out]    isOver
        SFRotation [out]    rotation_changed
        SFVec3f    [out]    trackPoint_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            autoOffset=True,
            description="",
            enabled=True,
            offset=[0.0, 1.0, 0.0, 0.0],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            autoOffset=autoOffset,
            description=description,
            enabled=enabled,
            **kwargs
        )
        self.offset = offset

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        if offset is None:
            offset = [0.0, 1.0, 0.0, 0.0]
        assertSFRotation(offset)
        self.__offset = offset

class GeoTouchSensor(X3DTouchSensorNode): 
    """
    GeoTouchSensor : X3DTouchSensorNode {
        SFString [in,out] description         ""
        SFBool   [in,out] enabled             TRUE
        SFNode   [in,out] metadata            NULL        [X3DMetadataObject]
        SFVec3f  [out]    hitNormal_changed
        SFVec3f  [out]    hitPoint_changed
        SFVec2f  [out]    hitTexCoord_changed
        SFVec3d  [out]    hitGeoCoord_changed
        SFBool   [out]    isActive
        SFBool   [out]    isOver
        SFTime   [out]    touchTime
        SFNode   []       geoOrigin           NULL        [GeoOrigin] (deprecated)
        MFString []       geoSystem           ["GD","WE"] [see 25.2.3]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            description="",
            geoOrigin=None,
            geoSystem=["GD", "WE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            enabled=enabled,
            description=description,
            **kwargs
        )
        self.geoOrigin = geoOrigin
        self.geoSystem = geoSystem

    @property
    def geoOrigin(self):
        return self.__geoOrigin

    @geoOrigin.setter
    def geoOrigin(self, geoOrigin):
        if geoOrigin is None:
            geoOrigin = None
        assertSFNode(geoOrigin, GeoOrigin)
        self.__geoOrigin = geoOrigin

    @property
    def geoSystem(self):
        return self.__geoSystem

    @geoSystem.setter
    def geoSystem(self, geoSystem):
        if geoSystem is None:
            geoSystem = ["GD", "WE"]
        assertValidGeoSystem(geoSystem)
        self.__geoSystem = geoSystem

class TouchSensor(X3DTouchSensorNode):
    """
    TouchSensor : X3DTouchSensorNode { 
        SFString [in,out] description         ""
        SFBool   [in,out] enabled             TRUE
        SFNode   [in,out] metadata            NULL [X3DMetadataObject]
        SFVec3f  [out]    hitNormal_changed
        SFVec3f  [out]    hitPoint_changed
        SFVec2f  [out]    hitTexCoord_changed
        SFBool   [out]    isActive
        SFBool   [out]    isOver
        SFTime   [out]    touchTime
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            description="",
            enabled=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            description=description,
            enabled=enabled,
            **kwargs
        )

class BooleanSequencer(X3DSequencerNode):
    """
    BooleanSequencer : X3DSequencerNode {
        SFBool  [in]     next
        SFBool  [in]     previous
        SFFloat [in]     set_fraction
        MFFloat [in,out] key           []   (-∞,∞) 
        MFBool  [in,out] keyValue 	 [] 
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        SFBool  [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue

    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFBool(keyValue)
        self.__keyValue = keyValue

class IntegerSequencer(X3DSequencerNode):
    """
    IntegerSequencer : X3DSequencerNode {
        SFBool  [in]     next
        SFBool  [in]     previous
        SFFloat [in]     set_fraction
        MFFloat [in,out] key           []   (-∞,∞) 
        MFInt32 [in,out] keyValue      []   (-∞,∞)
        SFNode  [in,out] metadata      NULL [X3DMetadataObject]
        SFInt32 [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            keyValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            key=key,
            **kwargs
        )
        self.keyValue = keyValue

    @property
    def keyValue(self):
        return self.__keyValue

    @keyValue.setter
    def keyValue(self, keyValue):
        if keyValue is None:
            keyValue = []
        assertMFInt32(keyValue)
        self.__keyValue = keyValue

class ParticleSystem(X3DShapeNode):
    """
    ParticleSystem : X3DShapeNode { 
        SFNode   [in,out] appearance        NULL      [X3DAppearanceNode]
        SFBool   [in,out] createParticles   TRUE
        SFNode   [in,out] geometry          NULL      [X3DGeometryNode]
        SFBool   [in,out] enabled           TRUE
        SFFloat  [in,out] lifetimeVariation 0.25      [0,1]
        SFInt32  [in,out] maxParticles      200       [0,∞)
        SFNode   [in,out] metadata          NULL      [X3DMetadataObject]
        SFFloat  [in,out] particleLifetime  5         [0,∞)
        SFVec2f  [in,out] particleSize      0.02 0.02 [0,∞)
        SFBool   [out]    isActive
        SFVec3f  []       bboxCenter        0 0 0
        SFVec3f  []       bboxSize          -1 -1 -1  (0,∞) or -1 -1 -1
        SFNode   []       colorRamp         NULL      [X3DColorNode]
        MFFloat  []       colorKey          []        [0,∞)
        SFNode   []       emitter           NULL      [X3DParticleEmitterNode]
        SFString []       geometryType      "QUAD"    ["LINE"|"POINT"|"QUAD"|"SPRITE"|"TRIANGLE"|"GEOMETRY"|...]
        MFNode   []       physics           []        [X3DParticlePhysicsModelNode]
        SFNode   []       texCoordRamp      NULL      [TextureCoordinate]
        MFFloat  []       texCoordKey       []        [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            appearance=None,
            createParticles=True,
            geometry=None,
            enabled=True,
            lifetimeVariation=0.25,
            maxParticles=200,
            particleLifetime=5.0,
            particleSize=[0.02, 0.02],
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            colorRamp=None,
            colorKey=[],
            emitter=None,
            geometryType="QUAD",
            physics=[],
            texCoordRamp=None,
            texCoordKey=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            appearance=appearance,
            geometry=geometry,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.createParticles = createParticles
        self.enabled = enabled
        self.lifetimeVariation = lifetimeVariation
        self.maxParticles = maxParticles
        self.particleLifetime = particleLifetime
        self.particleSize = particleSize
        self.colorRamp = colorRamp
        self.colorKey = colorKey
        self.emitter = emitter
        self.geometryType = geometryType
        self.physics = physics
        self.texCoordRamp = texCoordRamp
        self.texCoordKey = texCoordKey

    @property
    def createParticles(self):
        return self.__createParticles

    @createParticles.setter
    def createParticles(self, createParticles):
        if createParticles is None:
            createParticles = True
        assertSFBool(createParticles)
        self.__createParticles = createParticles

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

    @property
    def lifetimeVariation(self):
        return self.__lifetimeVariation

    @lifetimeVariation.setter
    def lifetimeVariation(self, lifetimeVariation):
        if lifetimeVariation is None:
            lifetimeVariation = 0.25
        assertSFFloat(lifetimeVariation)
        assertValidGreaterThanEquals(lifetimeVariation, 0)
        assertValidLessThanEquals(lifetimeVariation, 1)
        self.__lifetimeVariation = lifetimeVariation

    @property
    def maxParticles(self):
        return self.__maxParticles

    @maxParticles.setter
    def maxParticles(self, maxParticles):
        if maxParticles is None:
            maxParticles = 200
        assertSFInt32(maxParticles)
        assertValidGreaterThanEquals(maxParticles, 0)
        self.__maxParticles = maxParticles

    @property
    def particleLifetime(self):
        return self.__particleLifetime

    @particleLifetime.setter
    def particleLifetime(self, particleLifetime):
        if particleLifetime is None:
            particleLifetime = 5
        assertSFFloat(particleLifetime)
        assertValidGreaterThanEquals(particleLifetime, 0.0)
        self.__particleLifetime = particleLifetime

    @property
    def particleSize(self):
        return self.__particleSize

    @particleSize.setter
    def particleSize(self, particleSize):
        if particleSize is None:
            particleSize = [0.02, 0.02]
        assertSFVec2f(particleSize)
        assertValidGreaterThanEquals(particleSize, 0)
        self.__particleSize = particleSize

    @property
    def colorRamp(self):
        return self.__colorRamp

    @colorRamp.setter
    def colorRamp(self, colorRamp):
        if colorRamp is None:
            colorRamp = None
        assertSFNode(colorRamp, X3DColorNode)
        self.__colorRamp = colorRamp

    @property
    def colorKey(self):
        return self.__colorKey

    @colorKey.setter
    def colorKey(self, colorKey):
        if colorKey is None:
            colorKey = []
        assertMFFloat(colorKey)
        assertValidGreaterThanEquals(colorKey, 0)
        self.__colorKey = colorKey

    @property
    def emitter(self):
        return self.__emitter

    @emitter.setter
    def emitter(self, emitter):
        if emitter is None:
            emitter = None
        assertSFNode(emitter, X3DParticleEmitterNode)
        self.__emitter = emitter

    @property
    def geometryType(self):
        return self.__geometryType

    @geometryType.setter
    def geometryType(self, geometryType):
        if geometryType is None:
            geometryType = "QUAD"
        assertValidGeometryType(geometryType)
        self.__geometryType = geometryType

    @property
    def pysics(self):
        return self.__pysics

    @pysics.setter
    def pysics(self, pysics):
        if pysics is None:
            pysics = []
        assertMFNode(pysics, X3DParticlePhysicsModelNode)
        self.__pysics = pysics

    @property
    def texCoordRamp(self):
        return self.__texCoordRamp

    @texCoordRamp.setter
    def texCoordRamp(self, texCoordRamp):
        if texCoordRamp is None:
            texCoordRamp = None
        assertSFNode(texCoordRamp, TextureCoordinate)
        self.__texCoordRamp = texCoordRamp

    @property
    def texCoordKey(self):
        return self.__texCoordKey

    @texCoordKey.setter
    def texCoordKey(self, texCoordKey):
        if texCoordKey is None:
            texCoordKey = True
        assertMFFloat(texCoordKey)
        assertValidGreaterThanEquals(texCoordKey, 0)
        self.__texCoordKey = texCoordKey

class Shape(X3DShapeNode): 
    """
    Shape : X3DShapeNode {
        SFNode  [in,out] appearance NULL     [X3DAppearanceNode]
        SFNode  [in,out] geometry   NULL     [X3DGeometryNode]
        SFNode  [in,out] metadata   NULL     [X3DMetadataObject]
        SFVec3f []       bboxCenter 0 0 0    (-∞,∞)
        SFVec3f []       bboxSize   -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            appearance=None,
            geometry=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadta=metadata,
            appearance=appearance,
            geometry=geometry,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )

class Sound(X3DSoundNode): 
    """
    Sound : X3DSoundNode {
        SFVec3f [in,out] direction  0 0 1 (-∞,∞)
        SFFloat [in,out] intensity  1     [0,1]
        SFVec3f [in,out] location   0 0 0 (-∞,∞)
        SFFloat [in,out] maxBack    10    [0,∞)
        SFFloat [in,out] maxFront   10    [0,∞)
        SFNode  [in,out] metadata   NULL  [X3DMetadataObject]
        SFFloat [in,out] minBack    1     [0,∞)
        SFFloat [in,out] minFront   1     [0,∞)
        SFFloat [in,out] priority   0     [0,1]
        SFNode  [in,out] source     NULL  [X3DSoundSourceNode]
        SFBool  []       spatialize TRUE
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            direction=[0.0, 0.0, 1.0],
            intensity=1.0,
            location=[0.0, 0.0, 0.0],
            maxBack=10.0,
            maxFront=10.0,
            minBack=1.0,
            minFront=1.0,
            priority=0.0,
            source=None,
            spatialize=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.direction = direction
        self.intensity = intensity
        self.location = location
        self.maxBack = maxBack
        self.maxFront = maxFront
        self.minBack = minBack
        self.minFront = minFront
        self.priority = priority
        self.source = source
        self.spatialize = spatialize

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if direction is None:
            direction = [0.0, 0.0, 1.0]
        assertSFVec3f(direction)
        self.__direction = direction

    @property
    def intensity(self):
        return self.__intensity

    @intensity.setter
    def intensity(self, intensity):
        if intensity is None:
            intensity = 1.0
        assertSFFloat(intensity)
        assertValidGreaterThanEquals(intensity, 0)
        assertValidLessThanEquals(intensity, 1)
        self.__intensity = intensity

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        if location is None:
            location = [0.0, 0.0, 0.0]
        assertSFVec3f(location)
        self.__location = location

    @property
    def maxBack(self):
        return self.__maxBack

    @maxBack.setter
    def maxBack(self, maxBack):
        if maxBack is None:
            maxBack = 10.0
        assertSFFloat(maxBack)
        assertValidGreaterThanEquals(maxBack, 0)
        self.__maxBack = maxBack

    @property
    def maxFront(self):
        return self.__maxFront

    @maxFront.setter
    def maxFront(self, maxFront):
        if maxFront is None:
            maxFront = 10.0
        assertSFFloat(maxFront)
        assertValidGreaterThanEquals(maxFront, 0)
        self.__maxFront = maxFront

    @property
    def minBack(self):
        return self.__minBack

    @minBack.setter
    def minBack(self, minBack):
        if minBack is None:
            minBack = 1.0
        assertSFFloat(minBack)
        assertValidGreaterThanEquals(minBack, 0)
        self.__minBack = minBack

    @property
    def minFront(self):
        return self.__minFront

    @minFront.setter
    def minFront(self, minFront):
        if minFront is None:
            minFront = 1.0
        assertSFFloat(minFront)
        assertValidGreaterThanEquals(minFront, 0)
        self.__minFront = minFront

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority):
        if priority is None:
            priority = 0.0
        assertSFFloat(priority)
        assertValidGreaterThanEquals(priority, 0)
        assertValidLessThanEquals(priority, 1)
        self.__priority = priority

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        if source is None:
            source = None
        assertSFNode(source, X3DSoundSourceNode)
        self.__source = source

    @property
    def spatialize(self):
        return self.__spatialize

    @spatialize.setter
    def spatialize(self, spatialize):
        if spatialize is None:
            spatialize = True
        assertSFBool(spatialize)
        self.__spatialize = spatialize

class AudioClip(X3DSoundSourceNode, X3DUrlObject):
    """
    AudioClip : X3DSoundSourceNode, X3DUrlObject {
        SFString [in,out] description      ""
        SFBool   [in,out] loop             FALSE
        SFNode   [in,out] metadata         NULL  [X3DMetadataObject]
        SFTime   [in,out] pauseTime        0     (-∞,∞)
        SFFloat  [in,out] pitch            1.0   (0,∞)
        SFTime   [in,out] resumeTime       0     (-∞,∞)
        SFTime   [in,out] startTime        0     (-∞,∞)
        SFTime   [in,out] stopTime         0     (-∞,∞)
        MFString [in,out] url              []    [URI]
        SFTime   [out]    duration_changed
        SFTime   [out]    elapsedTime
        SFBool   [out]    isActive
        SFBool   [out]    isPaused
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            description="",
            loop=False,
            pauseTime=0.0,
            pitch=1.0,
            resumeTime=0.0,
            startTime=0.0,
            stopTime=0.0,
            url=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            description=description,
            loop=loop,
            pauseTime=pauseTime,
            pitch=pitch,
            resumeTime=resumeTime,
            startTime=startTime,
            stopTime=stopTime,
            url=url,
            **kwargs
        )

class BooleanTrigger(X3DTriggerNode):
    """
    BooleanTrigger : X3DTriggerNode {
        SFTime [in]     set_triggerTime
        SFNode [in,out] metadata        NULL [X3DMetadataObject]
        SFBool [out]    triggerTrue 
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )

class IntegerTrigger(X3DTriggerNode):
    """
    IntegerTrigger : X3DTriggerNode {
        SFBool  [in]     set_boolean
        SFInt32 [in,out] integerKey   -1   (-∞,∞)
        SFNode  [in,out] metadata     NULL [X3DMetadataObject]
        SFInt32 [out]    triggerValue  
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            integerKey=-1,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.integerKey = integerKey

    @property
    def integerKey(self):
        return self.__integerKey

    @integerKey.setter
    def integerKey(self, integerKey):
        if integerKey is None:
            integerKey = -1
        assertSFInt32(integerKey)
        self.__integerKey = integerKey

class TimeTrigger(X3DTriggerNode):
    """
    TimeTrigger : X3DTriggerNode {
        SFBool [in]     set_boolean
        SFNode [in,out] metadata    NULL [X3DMetadataObject]
        SFTime [ot]    triggerTime
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )

class IsoSurfaceVolumeData(X3DVolumeDataNode):
    """
    IsoSurfaceVolumeData : X3DVolumeDataNode {
        SFFloat [in,out] contourStepSize  0        (-∞,∞)
        SFVec3f [in,out] dimensions       1 1 1    (0,∞)
        SFNode  [in,out] gradients        NULL     [X3DTexture3DNode]
        SFNode  [in,out] metadata         NULL     [X3DMetadataObject]
        MFNode  [in,out] renderStyle      []       [X3DVolumeRenderStyleNode]
        SFFloat [in,out] surfaceTolerance 0        [0,∞)
        MFFloat [in,out] surfaceValues    []       (-∞,∞)
        SFNode  [in,out] voxels           NULL     [X3DTexture3DNode]
        SFVec3f []       bboxCenter       0 0 0    (-∞,∞)
        SFVec3f []       bboxSize         -1 -1 -1 [0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            contourStepsize=0.0,
            dimensions=[1.0, 1.0, 1.0],
            gradients=None,
            renderStyle=[],
            surfaceTolerance=0.0,
            surfaceValues=[],
            voxels=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            dimensions=dimensions,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.contourStepsize = contourStepsize
        self.gradients = gradients
        self.renderStyle = renderStyle
        self.surfaceTolerance = surfaceTolerance
        self.surfaceValues = surfaceValues
        self.voxels = voxels

    @property
    def contourStepsize(self):
        return self.__contourStepsize

    @contourStepsize.setter
    def contourStepsize(self, contourStepsize):
        if contourStepsize is None:
            contourStepsize = 0.0
        assertSFFloat(contourStepsize)
        self.__contourStepsize = contourStepsize

    @property
    def gradients(self):
        return self.__gradients

    @gradients.setter
    def gradients(self, gradients):
        if gradients is None:
            gradients = None
        assertSFNode(gradients, X3DTexture3DNode)
        self.__gradients = gradients

    @property
    def renderStyle(self):
        return self.__renderStyle

    @renderStyle.setter
    def renderStyle(self, renderStyle):
        if renderStyle is None:
            renderStyle = []
        assertMFNode(renderStyle, X3DVolumeRenderStyleNode)
        self.__renderStyle = renderStyle

    @property
    def surfaceTolerance(self):
        return self.__surfaceTolerance

    @surfaceTolerance.setter
    def surfaceTolerance(self, surfaceTolerance):
        if surfaceTolerance is None:
            surfaceTolerance = 0.0
        assertSFFloat(surfaceTolerance)
        assertValidGreaterThan(surfaceTolerance, 0)
        self.__surfaceTolerance = surfaceTolerance

    @property
    def surfaceValues(self):
        return self.__surfaceValues

    @surfaceValues.setter
    def surfaceValues(self, surfaceValues):
        if surfaceValues is None:
            surfaceValues = []
        assertMFFloat(surfaceValues)
        self.__surfaceValues = surfaceValues

    @property
    def voxels(self):
        return self.__voxels

    @voxels.setter
    def voxels(self, voxels):
        if voxels is None:
            voxels = None
        assertSFNode(voxels, X3DTexture3DNode)
        self.__voxels = voxels

class SegmentedVolumeData(X3DVolumeDataNode):
    """
    SegmentedVolumeData : X3DVolumeDataNode { 
        SFVec3f [in,out] dimensions         1 1 1    (0,∞)
        SFNode  [in,out] metadata           NULL     [X3DMetadataObject]
        MFNode  [in,out] renderStyle        []       [X3DVolumeRenderStyleNode]
        MFBool  [in,out] segmentEnabled     []
        SFNode  [in,out] segmentIdentifiers NULL     [X3DTexture3DNode]
        SFNode  [in,out] voxels             NULL     [X3DTexture3DNode]
        SFVec3f []       bboxCenter         0 0 0    (-∞,∞)
        SFVec3f []       bboxSize           -1 -1 -1 [0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            dimensions=[1.0, 1.0, 1.0],
            renderStyle=[],
            segmentEnabled=[],
            segmentIdentifiers=None,
            voxels=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            dimensions=dimensions,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.renderStyle = renderStyle
        self.segmentEnabled = segmentEnabled
        self.segmentIdentifiers = segmentIdentifiers
        self.voxels = voxels

    @property
    def renderStyle(self):
        return self.__renderStyle

    @renderStyle.setter
    def renderStyle(self, renderStyle):
        if renderStyle is None:
            renderStyle = []
        assertMFNode(renderStyle, X3DVolumeRenderStyleNode)
        self.__renderStyle = renderStyle

    @property
    def segmentEnabled(self):
        return self.__segmentEnabled

    @segmentEnabled.setter
    def segmentEnabled(self, segmentEnabled):
        if segmentEnabled is None:
            segmentEnabled = []
        assertMFBool(segmentEnabled)
        self.__segmentEnabled = segmentEnabled

    @property
    def segmentIdentifiers(self):
        return self.__segmentIdentifiers

    @segmentIdentifiers.setter
    def segmentIdentifiers(self, segmentIdentifiers):
        if segmentIdentifiers is None:
            segmentIdentifiers = None
        assertSFNode(segmentIdentifiers, X3DTexture3DNode)
        self.__segmentIdentifiers = segmentIdentifiers

    @property
    def voxels(self):
        return self.__voxels

    @voxels.setter
    def voxels(self, voxels):
        if voxels is None:
            voxels = None
        assertSFNode(voxels, X3DTexture3DNode)
        self.__voxels = voxels

class VolumeData(X3DVolumeDataNode):
    """
    VolumeData : X3DVolumeDataNode { 
        SFVec3f [in,out] dimensions      1 1 1    (0,∞)
        SFNode  [in,out] metadata        NULL     [X3DMetadataObject]
        SFNode  [in,out] renderStyle     NULL     [X3DVolumeRenderStyleNode]
        SFNode  [in,out] voxels          NULL     [X3DTexture3DNode]
        SFVec3f []       bboxCenter      0 0 0    (-∞,∞)
        SFVec3f []       bboxSize        -1 -1 -1 [0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            dimensions=[1.0, 1.0, 1.0],
            renderStyle=[],
            voxels=None,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            dimensions=dimensions,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.renderStyle = renderStyle
        self.voxels = voxels

    @property
    def renderStyle(self):
        return self.__renderStyle

    @renderStyle.setter
    def renderStyle(self, renderStyle):
        if renderStyle is None:
            renderStyle = []
        assertMFNode(renderStyle, X3DVolumeRenderStyleNode)
        self.__renderStyle = renderStyle

    @property
    def voxels(self):
        return self.__voxels

    @voxels.setter
    def voxels(self, voxels):
        if voxels is None:
            voxels = None
        assertSFNode(voxels, X3DTexture3DNode)
        self.__voxels = voxels

class Head(X3DNode): pass
class Meta(X3DNode): pass
class Scene(X3DNode): pass
