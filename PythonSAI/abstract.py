# -*- coding: utf-8 -*-
from abc import *
from .concrete import *
from .common import *
from .field import *
import math

class X3DNode(metaclass=ABCMeta):
    """
    X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
    }
    """
    def __init__(self, DEF="", USE="", class_="", metadata=None, **kwargs):
        self.DEF = DEF
        self.USE = USE
        self.class_ = class_
        self.metadata = metadata

    def NODE_NAME(self):
        return self.__class__.__name__

    """
    def NODE_SPECIFICATION_URL(self):
        return "https://www.web3d.org/wiki/index.php/" + self.__class__.__name__
    """

    @property
    def DEF(self):
        return self.__DEF

    @DEF.setter
    def DEF(self, DEF):
        self.__DEF = str(DEF)
        if self.__DEF:
            self.__USE = None

    @property
    def USE(self):
        return self.__USE

    @USE.setter
    def USE(self, USE):
        self.__USE = str(USE)
        if self.__USE:
            self.__DEF = None

    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_):
        self.__class_ = class_

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata):
        if metadata is None:
            metadata = None
        assertSFNode(metadata, X3DMetadataObject)
        self.__metadata = metadata

class X3DBoundedObject(metaclass=ABCMeta):
    """
    X3DBoundedObject {
      SFVec3f [] bboxCenter 0 0 0    (-∞,∞)
      SFVec3f [] bboxSize   -1 -1 -1 [0,∞) or −1 −1 −1
    }
    """
    def __init__(
            self,
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            **kwargs
    ):
        self.bboxCenter = bboxCenter
        self.bboxSize = bboxSize

    @property
    def bboxCenter(self):
        return self.__bboxCenter

    @bboxCenter.setter
    def bboxCenter(self, bboxCenter):
        if bboxCenter is None:
            bboxCenter = [0, 0, 0]
        assertSFVec3f(bboxCenter)
        self.__bboxCenter = bboxCenter

    @property
    def bboxSize(self):
        return self.__bboxSize

    @bboxSize.setter
    def bboxSize(self, bboxSize):
        if bboxSize is None:
            bboxSize = [-1, -1, -1]
        assertSFVec3f(bboxSize)
        assertValidBboxSize(bboxSize)
        self.__bboxSize = bboxSize

class X3DFogObject(metaclass=ABCMeta):
    """
    X3DFogObject {
      SFColor  [in,out] color           1 1 1    [0,1]
      SFString [in,out] fogType         "LINEAR" ["LINEAR"|"EXPONENTIAL"]
      SFFloat  [in,out] visibilityRange 0        [0,-∞)
    }
    """
    def __init__(
            self,
            color=[1, 1, 1],
            fogType="LINEAR",
            visibilityRange=0.0,
            **kwargs
    ):
        self.color = color
        self.fogType = fogType
        self.visibilityRange = visibilityRange

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = [1, 1, 1]
        assertSFColor(color)
        self.__color = color

    @property
    def fogType(self):
        return self.__fogType

    @fogType.setter
    def fogType(self, fogType):
        if fogType is None:
            fogType = "LINEAR"
        assertSFString(fogType)
        assertValidFogType(fogType)
        self.__fogType = fogType

    @property
    def visibilityRange(self):
        return self.__visibilityRange

    @visibilityRange.setter
    def visibilityRange(self, visibilityRange):
        if visibilityRange is None:
            visibilityRange = 0.0
        assertSFFloat(visibilityRange)
        assertValidLessThanEquals(visibilityRange, 0.0)
        self.__visibilityRange = visibilityRange

class X3DPickableObject(metaclass=ABCMeta):
    """
    X3DPickableObject {
      MFString [in,out] objectType "ALL" ["ALL","NONE","TERRAIN",...]
      SFBool   [in,out] pickable   TRUE
    }
    """
    def __init__(
            self,
            objectType=["ALL"],
            pickable=True,
            **kwargs
    ):
        self.objectType = objectType
        self.pickable = pickable

    @property
    def objectType(self):
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType):
        if objectType is None:
            objectType = ["ALL"]
        assertMFString(objectType)
        assertValidObjectType(objectType)
        self.__objectType = objectType

    @property
    def pickable(self):
        return self.__pickable

    @pickable.setter
    def pickable(self, pickable):
        if pickable is None:
            pickable = [0, 0, 0]
        assertSFBool(pickable)
        self.__pickable = pickable

class X3DProgrammableShaderObject(metaclass=ABCMeta):
    """
    X3DProgrammableShaderObject {
    }
    """
    def __init__(self, **kwargs):
        pass

class X3DMetadataObject(metaclass=ABCMeta):
    """
    X3DMetadataObject {
      SFString [in,out] name      ""  (Required)
      SFString [in,out] reference ""
    }
    """
    def __init__(
            self,
            name="",
            reference="",
            **kwargs
    ):
        self.name = name
        self.reference = reference

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
    def reference(self):
        return self.__reference

    @reference.setter
    def reference(self, reference):
        if reference is None:
            reference = ""
        assertSFString(reference)
        self.__reference = reference

class X3DUrlObject(metaclass=ABCMeta):
    """
    X3DUrlObject {
      MFString [in,out] url [] [URI]
    }
    """
    def __init__(
            self,
            url=[],
            **kwargs
    ):
        self.url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        if url is None:
            url = []
        assertMFString(url)
        self.__url = url

class X3DAppearanceNode(X3DNode, metaclass=ABCMeta):
    """
    X3DAppearanceNode : X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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
            meatadata=metadata,
            **kwargs
        )

class X3DAppearanceChildNode(X3DNode, metaclass=ABCMeta):
    """
    X3DAppearanceChildNode : X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DMaterialNode(X3DAppearanceChildNode, metaclass=ABCMeta):
    """
    X3DMaterialNode : X3DAppearanceChildNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DShaderNode(X3DAppearanceChildNode, metaclass=ABCMeta):
    """
    X3DShaderNode : X3DAppearanceChildNode {
      SFBool   [in]     activate
      SFNode   [in,out] metadata   NULL [X3DMetadataObject]
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
            language="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language is None:
            language = ""
        assertValidShaderLanguage(language)
        self.__language = language

class X3DTextureNode(X3DAppearanceChildNode, metaclass=ABCMeta):
    """
    X3DTextureNode : X3DAppearanceChildNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DEnvironmentTextureNode(X3DTextureNode, metaclass=ABCMeta):
    """
    X3DEnvironmentTextureNode : X3DTextureNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DTexture2DNode(X3DTextureNode, metaclass=ABCMeta):
    """
    X3DTexture2DNode : X3DTextureNode {
      SFNode [in,out] metadata          NULL [X3DMetadataObject]
      SFBool []       repeatS           TRUE
      SFBool []       repeatT           TRUE
      SFNode []       textureProperties NULL [TextureProperties]
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
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.repeatS = repeatS
        self.repeatT = repeatT

    @property
    def repeatS(self):
        return self.__repeatS

    @repeatS.setter
    def repeatS(self, repeatS):
        if repeatS is None:
            repeatS = True
        assertSFBool(repeatS)
        self.__repeatS = repeatS

    @property
    def repeatT(self):
        return self.__repeatT

    @repeatT.setter
    def repeatT(self, repeatT):
        if repeatT is None:
            repeatT = True
        assertSFBool(repeatT)
        self.__repeatT = repeatT
class X3DTexture3DNode(X3DTextureNode, metaclass=ABCMeta):
    """
    X3DTexture3DNode : X3DTextureNode {
      SFNode [in,out] metadata          NULL  [X3DMetadataObject]
      SFBool []       repeatS           FALSE
      SFBool []       repeatT           FALSE
      SFBool []       repeatR           FALSE
      SFNode []       textureProperties NULL  [TextureProperties]
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
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.repeatS = repeatS
        self.repeatT = repeatT
        self.repeatR = repeatR

    @property
    def repeatS(self):
        return self.__repeatS

    @repeatS.setter
    def repeatS(self, repeatS):
        if repeatS is None:
            repeatS = True
        assertSFBool(repeatS)
        self.__repeatS = repeatS

    @property
    def repeatT(self):
        return self.__repeatT

    @repeatT.setter
    def repeatT(self, repeatT):
        if repeatT is None:
            repeatT = True
        assertSFBool(repeatT)
        self.__repeatT = repeatT

    @property
    def repeatR(self):
        return self.__repeatR

    @repeatR.setter
    def repeatR(self, repeatR):
        if repeatR is None:
            repeatR = True
        assertSFBool(repeatR)
        self.__repeatR = repeatR

class X3DTextureTransformNode(X3DAppearanceChildNode, metaclass=ABCMeta):
    """
    X3DTextureTransformNode : X3DAppearanceChildNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DFontStyleNode(X3DNode, metaclass=ABCMeta):
    """
    X3DFontStyleNode : X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DGeometryNode(X3DNode, metaclass=ABCMeta):
    """
    X3DGeometryNode : X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DComposedGeometryNode(X3DGeometryNode, metaclass=ABCMeta):
    """
    X3DComposedGeometryNode : X3DGeometryNode {
      MFNode [in,out] attrib          []   [X3DVertexAttributeNode]
      SFNode [in,out] color           NULL [X3DColorNode]
      SFNode [in,out] coord           NULL [X3DCoordinateNode]
      SFNode [in,out] fogCoord        NULL [FogCoordinate]
      SFNode [in,out] metadata        NULL [X3DMetadataObject]
      SFNode [in,out] normal          NULL [X3DNormalNode]
      SFNode [in,out] texCoord        NULL [X3DTextureCoordinateNode]
      SFBool []       ccw             TRUE
      SFBool []       colorPerVertex  TRUE
      SFBool []       normalPerVertex TRUE
      SFBool []       solid           TRUE
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
            **kwargs
        )
        self.attrib = attrib
        self.color = color
        self.coord = coord
        self.normal = normal
        self.texCoord = texCoord
        self.ccw = ccw
        self.colorPerVertex = colorPerVertex
        self.normalPerVertex = normalPerVertex
        self.solid = solid

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
            coord = []
        assertSFNode(coord, X3DCoordinateNode)
        self.__coord = coord

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

class X3DParametricGeometryNode(X3DGeometryNode, metaclass=ABCMeta):
    """
    X3DParametricGeometryNode : X3DGeometryNode {
      SFNode [in,out] metadata NULL  [X3DMetadataObject]
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

class X3DNurbsSurfaceGeometryNode(X3DParametricGeometryNode, metaclass=ABCMeta):
    """
    X3DNurbsSurfaceGeometryNode : X3DParametricGeometryNode {
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
            **kwargs
        )
        self.controlPoint = controlPoint
        self.texCoord = texCoord
        self.uTessellation = uTessellation
        self.vTessellation = vTessellation
        self.weight = weight
        self.solid = solid
        self.uClosed = uClosed
        self.uDimension = uDimension
        self.uKnot = uKnot
        self.uOrder = uOrder
        self.vClosed = vClosed
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
    def texCoord(self):
        return self.__texCoord

    @texCoord.setter
    def texCoord(self, texCoord):
        if texCoord is None:
            texCoord = True
        assertSFNode(texCoord, X3DTextureCoordinateNode, NurbsTextureCoordinate)
        self.__texCoord = texCoord

    @property
    def uTessellation(self):
        return self.__uTessellation

    @uTessellation.setter
    def uTessellation(self, uTessellation):
        if uTessellation is None:
            uTessellation = 0
        assertSFInt32(uTessellation)
        self.__uTessellation = uTessellation

    @property
    def vTessellation(self):
        return self.__vTessellation

    @vTessellation.setter
    def vTessellation(self, vTessellation):
        if vTessellation is None:
            vTessellation = 0
        assertSFInt32(vTessellation)
        self.__vTessellation = vTessellation

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
    def solid(self):
        return self.__solid

    @solid.setter
    def solid(self, solid):
        if solid is None:
            solid = []
        assertSFBool(solid)
        self.__solid = solid

    @property
    def uClosed(self):
        return self.__uClosed

    @uClosed.setter
    def uClosed(self, uClosed):
        if uClosed is None:
            uClosed = False
        assertSFBool(uClosed)
        self.__uClosed = uClosed

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
    def vClosed(self):
        return self.__vClosed

    @vClosed.setter
    def vClosed(self, vClosed):
        if vClosed is None:
            vClosed = False
        assertSFBool(vClosed)
        self.__vClosed = vClosed

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

class X3DGeometricPropertyNode(X3DNode, metaclass=ABCMeta):
    """
    X3DGeometricPropertyNode : X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            **kwargs
        )

class X3DColorNode(X3DGeometricPropertyNode, metaclass=ABCMeta):
    """
    X3DColorNode : X3DGeometricPropertyNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DCoordinateNode(X3DGeometricPropertyNode, metaclass=ABCMeta):
    """
    X3DCoordinateNode : X3DGeometricPropertyNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DNormalNode(X3DGeometricPropertyNode, metaclass=ABCMeta):
    """
    X3DNormalNode : X3DGeometricPropertyNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DTextureCoordinateNode(X3DGeometricPropertyNode, metaclass=ABCMeta):
    """
    X3DTextureCoordinateNode : X3DGeometricPropertyNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DVertexAttributeNode(X3DGeometricPropertyNode, metaclass=ABCMeta):
    """
    X3DVertexAttributeNode : X3DGeometricPropertyNode {
      SFNode   [in,out] metadata NULL [X3DMetadataObject]
      SFString []       name     ""
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            name="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            name = ""
        assertSFString(name)
        self.__name = name

class X3DLayerNode(X3DNode, metaclass=ABCMeta):
    """
    X3DLayerNode : X3DNode {
      SFBool [in,out] isPickable TRUE
      SFNode [in,out] metadata NULL [X3DMetadataObject]
      SFNode [in,out] viewport NULL [X3DViewportNode]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            isPickable=True,
            viewport=None,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.isPickable = isPickable
        self.viewport = viewport

    @property
    def isPickable(self):
        return self.__isPickable

    @isPickable.setter
    def isPickable(self, isPickable):
        if isPickable is None:
            isPickable = True
        assertSFBool(isPickable)
        self.__isPickable = isPickable

    @property
    def viewport(self):
        return self.__viewport

    @viewport.setter
    def viewport(self, viewport):
        if viewport is None:
            viewport = True
        assertSFNode(X3DViewportNode)
        self.__viewport = viewport

class X3DNBodyCollisionSpaceNode(X3DNode, X3DBoundedObject, metaclass=ABCMeta):
    """
    X3DNBodyCollisionSpaceNode : X3DNode, X3DBoundedObject {
      SFBool  [in,out] enabled    TRUE
      SFNode  [in,out] metadata   NULL     [X3DMetadataObject]
      SFVec3f []       bboxCenter 0 0 0    (-∞,∞)
      SFVec3f []       bboxSize   -1 -1 -1 [0,∞) or -1 -1 -1
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            bboxCenter=[0.0, 0.0, 0.0],
            bboxSize=[-1.0, -1.0, -1.0],
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

class X3DNurbsControlCurveNode(X3DNode, metaclass=ABCMeta):
    """
    X3DNurbsControlCurveNode : X3DNode {
      MFVec2d  [in,out] controlPoint []   (-∞,∞)
      SFNode   [in,out] metadata     NULL [X3DMetadataObject]
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
            **kwargs
        )
        self.controlPoint = controlPoint

    @property
    def controlPoint(self):
        return self.__controlPoint

    @controlPoint.setter
    def controlPoint(self, controlPoint):
        if controlPoint is None:
            controlPoint = []
        assertMFVec2d(controlPoint)
        self.__controlPoint = controlPoint

class X3DParticleEmitterNode(X3DNode, metaclass=ABCMeta):
    """
    X3DParticleEmitterNode : X3DNode {
      SFNode  [in,out] metadata    NULL [X3DMetadataObject]
      SFFloat [in,out] speed       0    [0,∞)
      SFFloat [in,out] variation   0.25 [0,∞)
      SFFloat []       mass        0    [0,∞)
      SFFloat []       surfaceArea 0    [0,∞)
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
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
            **kwargs
        )
        self.speed = speed
        self.variation = variation
        self.mass = mass
        self.surfaceArea = surfaceArea

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if speed is None:
            speed = 0.0
        assertSFFloat(speed)
        assertValidGreaterThanEquals(speed, 0)
        self.__speed = speed

    @property
    def variation(self):
        return self.__variation

    @variation.setter
    def variation(self, variation):
        if variation is None:
            variation = 0.25
        assertSFFloat(variation)
        assertValidGreaterThanEquals(variation, 0)
        self.__variation = variation

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
    def surfaceArea(self):
        return self.__surfaceArea

    @surfaceArea.setter
    def surfaceArea(self, surfaceArea):
        if surfaceArea is None:
            surfaceArea = 0.0
        assertSFFloat(surfaceArea)
        assertValidGreaterThanEquals(surfaceArea, 0)
        self.__surfaceArea = surfaceArea

class X3DParticlePhysicsModelNode(X3DNode, metaclass=ABCMeta):
    """
    X3DParticlePhysicsModelNode : X3DNode {
      SFBool [in,out] enabled  TRUE
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
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.enabled= enabled

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

class X3DPrototypeInstance(X3DNode, metaclass=ABCMeta):
    """
    X3DPrototypeInstance : X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DRigidJointNode(X3DNode, metaclass=ABCMeta):
    """
    X3DRigidJointNode : X3DNode {
      SFNode   [in,out] body1       NULL   [RigidBody]
      SFNode   [in,out] body2       NULL   [RigidBody]
      MFString [in,out] forceOutput "NONE" ["ALL","NONE",...]
      SFNode   [in,out] metadata    NULL   [X3DMetadataObject]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            forceOutput=["NONE"],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.forceOutput = forceOutput

    @property
    def forceOutput(self):
        return self.__forceOutput

    @forceOutput.setter
    def forceOutput(self, forceOutput):
        if forceOutput is None:
            forceOutput = ["None"]
        assertValidForceOutput(forceOutput)
        self.__forceOutput = forceOutput

class X3DVolumeRenderStyleNode(X3DNode, metaclass=ABCMeta):
    """
    X3DVolumeRenderStyleNode : X3DNode {
      SFBool   [in,out] enabled  TRUE
      SFNode   [in,out] metadata NULL [X3DMetadataObject]
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
            **kwargs
        )
        self.enabled= enabled

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

class X3DComposableVolumeRenderStyleNode(X3DVolumeRenderStyleNode, metaclass=ABCMeta):
    """
    X3DComposableVolumeRenderStyleNode : X3DVolumeRenderStyleNode {
      SFBool   [in,out] enabled  TRUE
      SFNode   [in,out] metadata NULL [X3DMetadataObject]
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

class X3DChildNode(X3DNode, metaclass=ABCMeta):
    """
    X3DChildNode : X3DNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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


class X3DBindableNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DBindableNode : X3DChildNode {
      SFBool [in]     set_bind
      SFNode [in,out] metadata NULL [X3DMetadataObject]
      SFTime [out]    bindTime
      SFBool [out]    isBound
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

class X3DBackgroundNode(X3DBindableNode, metaclass=ABCMeta):
    """
    X3DBackgroundNode : X3DBindableNode {
      SFBool  [in]     set_bind
      MFFloat [in,out] groundAngle   []      [0,π/2]
      MFColor [in,out] groundColor   []      [0,1]
      SFNode  [in,out] metadata      NULL    [X3DMetadataObject]
      MFFloat [in,out] skyAngle      []      [0,π]
      MFColor [in,out] skyColor      0 0 0   [0,1]
      SFFloat [in,out] transparency  0       [0,1]
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
            **kwargs
        )
        self.groundAngle = groundAngle
        self.groundColor = groundColor
        self.skyAngle = skyAngle
        self.skyColor = skyColor
        self.transparency = transparency

    @property
    def groundAngle(self):
        return self.__groundAngle

    @groundAngle.setter
    def groundAngle(self, groundAngle):
        if groundAngle is None:
            groundAngle = []
        assertMFFloat(groundAngle)
        assertValidGreaterThanEquals(groundAngle, 0)
        assertValidLessThanEquals(groundAngle, math.pi / 2)
        self.__groundAngle = groundAngle

    @property
    def groundColor(self):
        return self.__groundColor

    @groundColor.setter
    def groundColor(self, groundColor):
        if groundColor is None:
            groundColor = [[]]
        assertMFColor(groundColor)
        self.__groundColor = groundColor

    @property
    def skyAngle(self):
        return self.__skyAngle

    @skyAngle.setter
    def skyAngle(self, skyAngle):
        if skyAngle is None:
            skyAngle = []
        assertMFFloat(skyAngle)
        assertValidGreaterThanEquals(skyAngle, 0)
        assertValidLessThanEquals(skyAngle, math.pi)
        self.__skyAngle = skyAngle

    @property
    def skyColor(self):
        return self.__skyColor

    @skyColor.setter
    def skyColor(self, skyColor):
        if skyColor is None:
            skyColor = [[0.0, 0.0, 0.0]]
        assertMFColor(skyColor)
        self.__skyColor = skyColor

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

class X3DViewpointNode(X3DBindableNode, metaclass=ABCMeta):
    """
    X3DViewpointNode : X3DBindableNode {
      SFBool     [in]     set_bind
      SFVec3f/d  [in,out] centerOfRotation  0 0 0     (-∞,∞)
      SFString   [in,out] description       ""
      SFBool     [in,out] jump              TRUE
      SFNode     [in,out] metadata          NULL      [X3DMetadataObject]
      SFRotation [in,out] orientation       0 0 1 0   (-∞,∞)
      SFVec3f/d  [in,out] position          0 0 10    (-∞,∞)
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
            metadata=metadata,
            **kwargs
        )
        self.centerOfRotation = centerOfRotation
        self.description = description
        self.jump = jump
        self.orientation = orientation
        self.position = position
        self.retainUserOffsets = retainUserOffsets

    @property
    def centerOfRotation(self):
        return self.__centerOfRotation

    @centerOfRotation.setter
    def centerOfRotation(self, centerOfRotation):
        if centerOfRotation is None:
            centerOfRotation = [0.0, 0.0, 0.0]
        assertSFVec3f(centerOfRotation)
        self.__centerOfRotation = centerOfRotation

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
    def jump(self):
        return self.__jump

    @jump.setter
    def jump(self, jump):
        if jump is None:
            jump = True
        assertSFBool(jump)
        self.__jump = jump

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        if orientation is None:
            orientation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(orientation)
        self.__orientation = orientation

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if position is None:
            position = [0.0, 0.0, 10.0]
        assertSFVec3f(position)
        self.__position = position

    @property
    def retainUserOffsets(self):
        return self.__retainUserOffsets

    @retainUserOffsets.setter
    def retainUserOffsets(self, retainUserOffsets):
        if retainUserOffsets is None:
            retainUserOffsets = False
        assertSFBool(retainUserOffsets)
        self.__retainUserOffsets = retainUserOffsets

class X3DFollowerNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DFollowerNode : X3DChildNode {
      [S|M]F<type> [in]     set_destination
      [S|M]F<type> [in]     set_value
      SFNode       [in,out] metadata           NULL [X3DMetadataObject]
      SFBool       [out]    isActive
      [S|M]F<type> [out]    value_changed
      [S|M]F<type> []       initialDestination
      [S|M]F<type> []       initialValue
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            initialDestination=[],
            initialValue=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.initialDestination = initialDestination
        self.initialValue = initialValue

    # @property
    # def initialDestination(self):
    #     return self.__initialDestination
    #
    # @initialDestination.setter
    # def initialDestination(self, initialDestination):
    #     if initialDestination is None:
    #         initialDestination = []
    #     assertSFNode(initialDestination)
    #     self.__initialDestination = initialDestination
    #
    # @property
    # def initialValue(self):
    #     return self.__initialValue
    #
    # @initialValue.setter
    # def initialValue(self, initialValue):
    #     if initialValue is None:
    #         initialValue = []
    #     assertSFNode(initialValue)
    #     self.__initialValue = initialValue

class X3DChaserNode(X3DFollowerNode, metaclass=ABCMeta):
    """
    X3DChaserNode : X3DFollowerNode {
      [S|M]F<type> [in]     set_destination
      [S|M]F<type> [in]     set_value
      SFNode       [in,out] metadata           NULL  [X3DMetadataObject]
      SFBool       [out]    isActive
      [S|M]F<type> [out]    value_changed
      SFTime       []       duration           1     [0,∞)
      [S|M]F<type> []       initialDestination
      [S|M]F<type> []       initialValue
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            duration=1.0,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if duration is None:
            duration = 1.0
        assertSFTime(duration)
        assertValidGreaterThanEquals(duration, 0)
        self.__duration = duration

class X3DDamperNode(X3DFollowerNode, metaclass=ABCMeta):
    """
    X3DDamperNode : X3DFollowerNode {
      [S|M]F<type> [in]     set_destination
      [S|M]F<type> [in]     set_value
      SFNode       [in,out] metadata           NULL   [X3DMetadataObject]
      SFTime       [in,out] tau                0.3    [0,∞)
      SFFloat      [in,out] tolerance          -1     -1 or [0,∞)
      SFBool       [out]    isActive
      [S|M]F<type> [out]    value_changed
      [S|M]F<type> []       initialDestination
      [S|M]F<type> []       initialValue
      SFInt32      []       order              3     [0..5]
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
        self.tau = tau
        self.tolerance = tolerance
        self.order = order

    @property
    def tau(self):
        return self.__tau

    @tau.setter
    def tau(self, tau):
        if tau is None:
            tau = 0.3
        assertSFTime(tau)
        assertValidGreaterThanEquals(tau, 0)
        self.__tau = tau

    @property
    def tolerance(self):
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        if tolerance is None:
            tolerance = 1.0
        assertSFFloat(tolerance)
        assertValidTolerance(tolerance)
        self.__tolerance = tolerance

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if order is None:
            order = 3
        assertSFInt32(order)
        assertValidGreaterThanEquals(order, 0)
        assertValidLessThanEquals(order, 5)
        self.__order = order

class X3DGroupingNode(X3DChildNode, X3DBoundedObject, metaclass=ABCMeta):
    """
    X3DGroupingNode : X3DChildNode, X3DBoundedObject {
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
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            children=[],
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
        self.children = children

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        if children is None:
            children = []
        assertSFNode(children, X3DChildNode)
        self.__children = children

class X3DViewportNode(X3DGroupingNode, metaclass=ABCMeta):
    """
    X3DViewportNode : X3DGroupingNode {
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
            bboxCenter=[0, 0, 0],
            bboxSize=[-1, -1, -1],
            children=[],
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

class X3DInfoNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DInfoNode : X3DChildNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DInterpolatorNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DInterpolatorNode : X3DChildNode {
      SFFloat      [in]     set_fraction       (-∞,∞)
      MFFloat      [in,out] key           []   (-∞,∞)
      MF<type>     [in,out] keyValue      []
      SFNode       [in,out] metadata      NULL [X3DMetadataObject]
      [S|M]F<type> [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.key = key

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        if key is None:
            key = []
        assertMFFloat(key)
        self.__key = key

class X3DLayoutNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DLayoutNode : X3DChildNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DLightNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DLightNode : X3DChildNode {
      SFFloat [in,out] ambientIntensity 0     [0,1]
      SFColor [in,out] color            1 1 1 [0,1]
      SFBool  [in,out] global           FALSE
      SFFloat [in,out] intensity        1     [0,1]
      SFNode  [in,out] metadata         NULL  [X3DMetadataObject]
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
            **kwargs
        )

        self.ambientIntensity = ambientIntensity
        self.color = color
        self.global_ = global_
        self.intensity = intensity
        self.on = on

    @property
    def ambientIntensity(self):
        return self.__ambientIntensity

    @ambientIntensity.setter
    def ambientIntensity(self, ambientIntensity):
        if ambientIntensity is None:
            ambientIntensity = 0.0
        assertSFFloat(ambientIntensity)
        assertValidGreaterThanEquals(ambientIntensity, 0)
        assertValidLessThanEquals(ambientIntensity, 1)
        self.__ambientIntensity = ambientIntensity

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color is None:
            color = [1.0, 1.0, 1.0]
        assertSFColor(color)
        self.__color = color

    @property
    def global_(self):
        return self.__global_

    @global_.setter
    def global_(self, global_):
        if global_ is None:
            global_ = True
        assertSFBool(global_)
        self.__global_ = global_

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
    def on(self):
        return self.__on

    @on.setter
    def on(self, on):
        if on is None:
            on = True
        assertSFBool(on)
        self.__on = on

class X3DNBodyCollidableNode(X3DChildNode, X3DBoundedObject, metaclass=ABCMeta):
    """
      SFBool     [in,out] enabled     TRUE
      SFNode     [in,out] metadata    NULL     [X3DMetadataObject]
      SFRotation [in,out] rotation    0 0 1 0  [0,1]
      SFVec3f    [in,out] translation 0 0 0    (-∞,∞)
      SFVec3f    []       bboxCenter  0 0 0    (-∞,∞)
      SFVec3f    []       bboxSize    -1 -1 -1 [0,∞) or -1 -1 -1
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
        self.rotation = rotation
        self.translation = translation

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        if rotation is None:
            rotation = [0.0, 0.0, 1.0, 0.0]
        assertSFRotation(rotation)
        assertValidGreaterThanEquals(rotation, 0.0)
        assertValidLessThanEquals(rotation, 1.0)
        self.__rotation = rotation

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation):
        if translation is None:
            translation = [0.0, 0.0, 0.0]
        assertSFVec3f(translation)
        self.__translation = translation

class X3DProductStructureChildNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DProductStructureChildNode : X3DChildNode {
      SFNode   [in,out] metadata NULL [X3DMetadataObject]
      SFString [in,out] name     ""
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            name="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            name = ""
        assertSFString(name)
        self.__name = name

class X3DScriptNode(X3DChildNode, X3DUrlObject, metaclass=ABCMeta):
    """
    X3DScriptNode : X3DChildNode,X3DURLObject {
      SFNode   [in,out] metadata NULL [X3DMetadataObject]
      MFString [in,out] url      []   [URI]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            url=[],
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

class X3DSensorNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DSensorNode  : X3DChildNode {
      SFBool [in,out] enabled  TRUE
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled):
        if enabled is None:
            enabled = True
        assertSFBool(enabled)
        self.__enabled = enabled

class X3DEnvironmentalSensorNode(X3DSensorNode, metaclass=ABCMeta):
    """
    X3DEnvironmentalSensorNode : X3DSensorNode {
      SFVec3f/d [in,out] center    0 0 0 (-∞,∞)
      SFBool    [in,out] enabled   TRUE
      SFNode    [in,out] metadata  NULL  [X3DMetadataObject]
      SFVec3f   [in,out] size      0 0 0 (-∞,∞)
      SFTime    [out]    enterTime
      SFTime    [out]    exitTime
      SFBool    [out]    isActive
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            center=[0.0, 0.0, 0.0],
            size=[0.0, 0.0, 0.0],
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
        self.center = center
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
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size is None:
            size = [0.0, 0.0, 0.0]
        assertSFVec3f(size)
        self.__size = size

class X3DKeyDeviceSensorNode(X3DSensorNode, metaclass=ABCMeta):
    """
    X3DKeyDeviceSensorNode : X3DSensorNode {
      SFBool   [in,out] enabled  TRUE
      SFNode   [in,out] metadata NULL [X3DMetadataObject]
      SFBool   [out]    isActive
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

class X3DNetworkSensorNode(X3DSensorNode, metaclass=ABCMeta):
    """
    X3DNetworkSensorNode : X3DSensorNode {
      SFBool [in,out] enabled  TRUE
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DPickSensorNode(X3DSensorNode, metaclass=ABCMeta):
    """
    X3DPickSensorNode : X3DSensorNode {
      SFBool   [in,out] enabled          TRUE
      SFNode   [in,out] metadata         NULL        [X3DMetadataObject]
      SFString [in,out] matchCriterion   "MATCH_ANY" ["MATCH_ANY"|"MATCH_EVERY"|
                                                      "MATCH_ONLY_ONE"]
      MFString [in,out] objectType       "ALL"       ["ALL","NONE","TERRAIN",...]
      SFNode   [in,out] pickingGeometry  NULL        [X3DGeometryNode]
      MFNode   [in,out] pickTarget       []          [X3DGroupingNode|X3DShapeNode|Inline]
      MFNode   [out]    pickedGeometry
      SFBool   [out]    isActive
      SFString []       intersectionType "BOUNDS"    ["GEOMETRY"|"BOUNDS"|...]
      SFString []       sortOrder        "CLOSEST"   ["ANY"|"CLOSEST"|"ALL"|"ALL_SORTED"]
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            enabled=True,
            matchCriterion="MATCH_ANY",
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
            metadata=metadata,
            enabled=enabled,
            **kwargs
        )
        self.matchCriterion = matchCriterion
        self.objectType = objectType
        self.pickingGeometry = pickingGeometry
        self.pickTarget = pickTarget
        self.intersectionType = intersectionType
        self.sortOrder = sortOrder

    @property
    def matchCriterion(self):
        return self.__matchCriterion

    @matchCriterion.setter
    def matchCriterion(self, matchCriterion):
        if matchCriterion is None:
            matchCriterion = "MATCH_ANY"
        assertValidMatchCriterion(matchCriterion)
        self.__matchCriterion = matchCriterion

    @property
    def objectType(self):
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType):
        if objectType is None:
            objectType = ["ALL"]
        assertValidObjectType(objectType)
        self.__objectType = objectType

    @property
    def pickingGeometry(self):
        return self.__pickingGeometry

    @pickingGeometry.setter
    def pickingGeometry(self, pickingGeometry):
        if pickingGeometry is None:
            pickingGeometry = None
        assertSFNode(pickingGeometry, X3DGeometryNode)
        self.__pickingGeometry = pickingGeometry

    @property
    def pickTarget(self):
        return self.__pickTarget

    @pickTarget.setter
    def pickTarget(self, pickTarget):
        if pickTarget is None:
            pickTarget = []
        assertMFNode(pickTarget, X3DGroupingNode, X3DShapeNode, Inline)
        self.__pickTarget = pickTarget

    @property
    def intersectionType(self):
        return self.__intersectionType

    @intersectionType.setter
    def intersectionType(self, intersectionType):
        if intersectionType is None:
            intersectionType = "BOUNDS"
        assertValidIntersectionType(intersectionType)
        self.__intersectionType = intersectionType

    @property
    def sortOrder(self):
        return self.__sortOrder

    @sortOrder.setter
    def sortOrder(self, sortOrder):
        if sortOrder is None:
            sortOrder = "CLOSEST"
        assertValidSortOrder(sortOrder)
        self.__sortOrder = sortOrder

class X3DPointingDeviceSensorNode(X3DSensorNode, metaclass=ABCMeta):
    """
    X3DPointingDeviceSensorNode : X3DSensorNode {
      SFString [in,out] description ""
      SFBool   [in,out] enabled     TRUE
      SFNode   [in,out] metadata    NULL [X3DMetadataObject]
      SFBool   [out]    isActive
      SFBool   [out]    isOver
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
        self.description = description

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if description is None:
            description = ""
        assertSFString(description)
        self.__description = description

class X3DDragSensorNode(X3DPointingDeviceSensorNode, metaclass=ABCMeta):
    """
    X3DDragSensorNode : X3DPointingDeviceSensorNode {
      SFBool   [in,out] autoOffset         TRUE
      SFString [in,out] description        ""
      SFBool   [in,out] enabled            TRUE
      SFNode   [in,out] metadata           NULL [X3DMetadataObject]
      SFBool   [out]    isActive
      SFBool   [out]    isOver
      SFVec3f  [out]    trackPoint_changed
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
            autoOffset=True,
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            description=description,
            **kwargs
        )
        self.autoOffset = autoOffset

    @property
    def autoOffset(self):
        return self.__autoOffset

    @autoOffset.setter
    def autoOffset(self, autoOffset):
        if autoOffset is None:
            autoOffset = True
        assertSFString(autoOffset)
        self.__autoOffset = autoOffset

class X3DTouchSensorNode(X3DPointingDeviceSensorNode, metaclass=ABCMeta):
    """
    X3DTouchSensorNode : X3DPointingDeviceSensorNode {
      SFString [in,out] description ""
      SFBool   [in,out] enabled     TRUE
      SFNode   [in,out] metadata    NULL [X3DMetadataObject]
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
            enabled=True,
            description="",
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            enabled=enabled,
            description=description,
            **kwargs
        )

class X3DSequencerNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DSequencerNode : X3DChildNode {
      SFBool       [in]     next
      SFBool       [in]     previous
      SFFloat      [in]     set_fraction       (-∞,∞)
      MFFloat      [in,out] key           []   (-∞,∞)
      MF<type>     [in,out] keyValue      []
      SFNode       [in,out] metadata      NULL [X3DMetadataObject]
      [S|M]F<type> [out]    value_changed
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
            key=[],
            **kwargs
    ):
        super().__init__(
            DEF=DEF,
            USE=USE,
            class_=class_,
            metadata=metadata,
            **kwargs
        )
        self.key = key

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        if key is None:
            key = []
        assertMFFloat(key)
        self.__key = key


class X3DShapeNode(X3DChildNode, X3DBoundedObject, metaclass=ABCMeta):
    """
    X3DShapeNode : X3DChildNode, X3DBoundedObject {
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
            metadata=metadata,
            bboxCenter=bboxCenter,
            bboxSize=bboxSize,
            **kwargs
        )
        self.appearance = appearance
        self.geometry = geometry

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        if appearance is None:
            appearance = None
        assertSFNode(appearance, X3DAppearanceNode)
        self.__appearance = appearance

    @property
    def geometry(self):
        return self.__geometry

    @geometry.setter
    def geometry(self, geometry):
        if geometry is None:
            geometry = None
        assertSFNode(geometry, X3DGeometryNode)
        self.__geometry = geometry

class X3DSoundNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DSoundNode : X3DChildNode {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DTimeDependentNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DTimeDependentNode : X3DChildNode {
      SFBool  [in,out] loop         FALSE
      SFNode  [in,out] metadata     NULL  [X3DMetadataObject]
      SFTime  [in,out] pauseTime    0     (-∞,∞)
      SFTime  [in,out] resumeTime   0     (-∞,∞)
      SFTime  [in,out] startTime    0     (-∞,∞)
      SFTime  [in,out] stopTime     0     (-∞,∞)
      SFTime  [out]    elapsedTime
      SFBool  [out]    isActive
      SFBool  [out]    isPaused
    }
    """
    def __init__(
            self,
            DEF="",
            USE="",
            class_="",
            metadata=None,
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
            **kwargs
        )
        self.loop = loop
        self.pauseTime = pauseTime
        self.resumeTime = resumeTime
        self.startTime = startTime
        self.stopTime = stopTime

    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, loop):
        if loop is None:
            loop = False
        assertSFBool(loop)
        self.__loop = loop

    @property
    def pauseTime(self):
        return self.__pauseTime

    @pauseTime.setter
    def pauseTime(self, pauseTime):
        if pauseTime is None:
            pauseTime = 0.0
        assertSFTime(pauseTime)
        self.__pauseTime = pauseTime

    @property
    def resumeTime(self):
        return self.__resumeTime

    @resumeTime.setter
    def resumeTime(self, resumeTime):
        if resumeTime is None:
            resumeTime = 0.0
        assertSFTime(resumeTime)
        self.__resumeTime = resumeTime

    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime):
        if startTime is None:
            startTime = 0.0
        assertSFTime(startTime)
        self.__startTime = startTime

    @property
    def stopTime(self):
        return self.__stopTime

    @stopTime.setter
    def stopTime(self, stopTime):
        if stopTime is None:
            stopTime = 0.0
        assertSFTime(stopTime)
        self.__stopTime = stopTime

class X3DSoundSourceNode(X3DTimeDependentNode, metaclass=ABCMeta):
    """
    X3DSoundSourceNode : X3DTimeDependentNode {
      SFString [in,out] description      ""
      SFBool   [in,out] loop             FALSE
      SFNode   [in,out] metadata         NULL [X3DMetadataObject]
      SFTime   [in,out] pauseTime        0    (-∞,∞)
      SFFloat  [in,out] pitch            1.0  (0,∞)
      SFTime   [in,out] resumeTime       0    (-∞,∞)
      SFTime   [in,out] startTime        0    (-∞,∞)
      SFTime   [in,out] stopTime         0    (-∞,∞)
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
            **kwargs
        )
        self.description = description
        self.pitch = pitch

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
    def pitch(self):
        return self.__pitch

    @pitch.setter
    def pitch(self, pitch):
        if pitch is None:
            pitch = 1.0
        assertSFFloat(pitch)
        assertValidGreaterThan(pitch, 0)
        self.__pitch = pitch

class X3DTriggerNode(X3DChildNode, metaclass=ABCMeta):
    """
    X3DTriggerNode : X3DChildNode  {
      SFNode [in,out] metadata NULL [X3DMetadataObject]
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

class X3DVolumeDataNode(X3DChildNode, X3DBoundedObject, metaclass=ABCMeta):
    """
    X3DVolumeDataNode : X3DChildNode, X3DBoundedObject {
      SFVec3f [in,out] dimensions  1 1 1    (0,∞)
      SFNode  [in,out] metadata    NULL     [X3DMetadataObject]
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
            dimensions=[1.0, 1.0, 1.0],
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
        self.dimensions = dimensions

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if dimensions is None:
            dimensions = [1.0, 1.0, 1.0]
        assertSFVec3f(dimensions)
        assertValidGreaterThan(dimensions, 0)
        self.__dimensions = dimensions