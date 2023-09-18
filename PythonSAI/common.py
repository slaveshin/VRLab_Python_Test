import math

FOGTYPE = (
    "LINEAR",
    "EXPONENTIAL"
)

SHADERLANGUAGE = (
    "",
    "Cg",
    "GLSL",
    "HLSL"
)

MATCHCRITERION = (
    "MATCH_ANY",
    "MATCH_EVERY",
    "MATCH_ONLY_ONE"
)

INTERSECTIONTYPE = (
    "BOUNDS",
    "GEOMETRY"
)

SORTORDER = (
    "ANY",
    "CLOSEST",
    "ALL",
    "ALL_SORTED"
)

OBJECTTYPE = (
    "ALL",
    "NONE",
    "TERRAIN"
)

FORCEOUTPUT = (
    "ALL",
    "NONE"
)

FONTJUSTIFY = (
    "BEGIN",
    "END",
    "FIRST",
    "MIDDLE"
)

FONTSTYLE = (
    "PLAIN",
    "BOLD",
    "ITALIC",
    "BOLDITALIC"
)

FONTFAMILY = (
    "SANS",
    "SERIF",
    "TYPEWRITER"
)

MULTITEXTUREMODES = (
    "MODULATE",
    "REPLACE",
    "MODULATE2X",
    "MODULATE4X",
    "ADD",
    "ADDSIGNED",
    "ADDSIGNED2X",
    "SUBTRACT",
    "ADDSMOOTH",
    "BLENDDIFFUSEALPHA",
    "BLENDTEXTUREALPHA",
    "BLENDFACTORALPHA",
    "BLENDCURRENTALPHA",
    "MODULATEALPHA_ADDCOLOR",
    "MODULATEINVALPHA_ADDCOLOR",
    "MODULATEINVCOLOR_ADDALPHA",
    "OFF",
    "SELECTARG1",
    "SELECTARG2",
    "DOTPRODUCT3"
)

MULTITEXTURESOURCE = (
    "",
    "DIFFUSE",
    "SPECULAR",
    "FACTOR"
)

MULTITEXTUREFUNCTION = (
    "",
    "COMPLEMENT",
    "ALPHAREPLICATE"
)

TEXTURECOORDINATEGENRATIONMODES = (
    "SPHERE",
    "CAMERASPACENORMAL",
    "CAMERASPACEPOSITION",
    "CAMERASPACEREFLECTIONVECTOR",
    "SPHERE-LOCAL",
    "COORD",
    "COORD-EYE",
    "NOISE",
    "NOISE-EYE",
    "SPHERE-REFLECT",
    "SPHERE-REFLECT-LOCAL"
)

TEXTUREBOUNDARYMODES = (
    "CLAMP",
    "CLAMP_TO_EDGE",
    "CLAMP_TO_BOUNDARY",
    "MIRRORED_REPEAT",
    "REPEAT"
)

TEXTUREMAGNIFICATIONMODES = (
    "AVG_PIXEL",
    "DEFAULT",
    "FASTEST",
    "NEAREST_PIXEL",
    "NICEST"
)

TEXTUREMINIFICATIONMODES = (
    "AVG_PIXEL",
    "AVG_PIXEL_AVG_MIPMAP",
    "AVG_PIXEL_NEAREST_MIPMAP",
    "DEFAULT",
    "FASTEST",
    "NEAREST_PIXEL",
    "NEAREST_PIXEL_AVG_MIPMAP",
    "NEAREST_PIXEL_NEAREST_MIPMAP",
    "NICEST"
)

TEXTURECOMPRESSIONMODES = (
    "DEFAULT",
    "FASTEST",
    "HIGH",
    "LOW",
    "MEDIUM",
    "NICEST"
)

NAVIGATIONINFOTRANSITIONTYPE = (
    "TELEPORT",
    "LINEAR",
    "ANIMATE"
)

NAVIGATIONINFOTYPE = (
    "ANY",
    "WALK",
    "EXAMINE",
    "FLY",
    "LOOKAT",
    "NONE",
    "EXPLORE"
)

GEOSYSTEM = (
    "GD",
    "WE",
    "UTM"
)

NETWORKMODE = (
    "standAlone",
    "networkReader",
    "networkWriter"
)

SHADERTYPE = (
    "VERTEX",
    "FRAGMENT"
)

GENERATECUBEMAPTEXTUREUPDATE = (
    "NONE",
    "NEXT_FRAME_ONLY",
    "ALWAYS"
)

LAYOUTALIGN = (
    "LEFT",
    "CENTER",
    "RIGHT",
    "BOTTOM",
    "CENTER",
    "TOP"
)

LAYOUTOFFSETUNITS = (
    "WORLD",
    "FRACTION",
    "PIXEL"
)

LAYOUTSCALEMODE = (
    "NONE",
    "FRACTION",
    "STRETCH",
    "PIXEL"
)

LAYOUTSIZEUNITS = (
    "WORLD",
    "FRACTION",
    "PIXEL"
)

COLLISIONAPPLIEDPARAMETERS = (
    "BOUNCE",
    "USER_FRICTION",
    "FRICTION_COEFFICIENT-2",
    "ERROR_REDUCTION",
    "CONSTANT_FORCE",
    "SPEED-1",
    "SPEED-2",
    "SLIP-1",
    "SLIP-2"
)

GEOMETRYTYPE = (
    "LINE",
    "POINT",
    "QUAD",
    "SPRITE",
    "TRIANGLE",
    "GEOMETRY"
)

WEIGHTFUNCTIONTYPE = (
    "CONSTANT",
    "ALPHA1",
    "ALPHA2",
    "ONE_MINUS_ALPHA1",
    "ONE_MINUS_ALPHA2",
    "TABLE"
)

PROJECTIONVOLUMESTYLETYPE = (
    "MAX",
    "MIN",
    "AVERAGE"
)

PHASEFUNCTION = (
    "Henvey-Greenstein",
    "NONE"
)

X3DFIELDTYPE = (
    "SFBool",
    "MFBool",
    "SFColor",
    "MFColor",
    "SFColorRGBA",
    "MFColorRGBA",
    "SFDouble",
    "MFDouble",
    "SFFloat",
    "MFFloat",
    "SFImage",
    "MFImage",
    "SFInt32",
    "MFInt32",
    "SFNode",
    "MFNode",
    "SFRotation",
    "MFRotation",
    "SFString",
    "MFString",
    "SFTime",
    "MFTime",
    "SFVec2d",
    "MFVec2d",
    "SFVec2f",
    "MFVec2f",
    "SFVec3d",
    "MFVec3d",
    "SFVec3f",
    "MFVec3f",
    "SFVec4d",
    "MFVec4d",
    "SFVec4f",
    "MFVec4f",
    "SFMatrix3d",
    "MFMatrix3d",
    "SFMatrix3f",
    "MFMatrix3f",
    "SFMatrix4d",
    "MFMatrix4d",
    "SFMatrix4f",
    "MFMatrix4f",
)

X3DNODE = (
    "X3DBoundedObject",
    "X3DFogObject",
    "X3DPickableObject",
    "X3DProgrammableShaderObject",
    "X3DMetadataObject",
    "X3DUrlObject",
    "X3DNode",
    "Contact",
    "Contour2D",
    "EaseInEaseOut",
    "GeoOrigin",
    "LayerSet",
    "MetadataBoolean",
    "MetadataDouble",
    "MetadataFloat",
    "MetadataInteger",
    "MetadataSet",
    "MetadataString",
    "NurbsTextureCoordinate",
    "RigidBody",
    "ShaderPart",
    "ShaderProgram",
    "TextureProperties",
    "Appearance",
    "X3DAppearanceChildNode",
    "FillProperties",
    "LineProperties",
    "X3DMaterialNode",
    "Material",
    "TwoSidedMaterial",
    "X3DShaderNode",
    "ComposedShader",
    "PackagedShader",
    "ProgramShader",
    "X3DTextureNode",
    "MultiTexture",
    "X3DEnvironmentTextureNode",
    "ComposedCubeMapTexture",
    "GeneratedCubeMapTexture",
    "ImageCubeMapTexture",
    "X3DTexture2DNode",
    "ImageTexture",
    "MovieTexture",
    "PixelTexture",
    "X3DTexture3DNode",
    "ComposedTexture3D",
    "ImageTexture3D",
    "PixelTexture3D",
    "X3DTextureTransformNode",
    "MultiTextureTransform",
    "TextureTransform",
    "TextureTransformMatrix3D",
    "TextureTransform3D",
    "X3DFontStyleNode",
    "FontStyle",
    "ScreenFontStyle",
    "X3DGeometryNode",
    "Arc2D",
    "ArcClose2D",
    "Box",
    "Circle2D",
    "Cone",
    "Cylinder",
    "Disk2D",
    "ElevationGrid",
    "Extrusion",
    "GeoElevationGrid",
    "IndexedLineSet",
    "LineSet",
    "PointSet",
    "Polyline2D",
    "Polypoint2D",
    "Rectangle2D",
    "Sphere",
    "Text",
    "TriangleSet2D",
    "X3DComposedGeometryNode",
    "IndexedFaceSet",
    "IndexedTriangleFanSet",
    "IndexedTriangleSet",
    "IndexedTriangleStripSet",
    "IndexedQuadSet",
    "QuadSet",
    "TriangleFanSet",
    "TriangleSet",
    "TriangleStripSet",
    "X3DParametricGeometryNode",
    "NurbsCurve",
    "NurbsSweptSurface",
    "NurbsSwungSurface",
    "X3DNurbsSurfaceGeometryNode",
    "NurbsPatchSurface",
    "NurbsTrimmedSurface",
    "X3DGeometricPropertyNode",
    "FogCoordinate",
    "HAnimDisplacer",
    "X3DColorNode",
    "Color",
    "ColorRGBA",
    "X3DCoordinateNode",
    "Coordinate",
    "CoordinateDouble",
    "GeoCoordinate",
    "X3DNormalNode",
    "Normal",
    "X3DTextureCoordinateNode",
    "MultiTextureCoordinate",
    "TextureCoordinate",
    "TextureCoordinate3D",
    "TextureCoordinate4D",
    "TextureCoordinateGenerator",
    "X3DVertexAttributeNode",
    "FloatVertexAttribute",
    "Matrix3VertexAttribute",
    "Matrix4VertexAttribute",
    "X3DLayerNode",
    "Layer",
    "LayoutLayer",
    "X3DNBodyCollisionSpaceNode",
    "CollisionSpace",
    "X3DNurbsControlCurveNode",
    "ContourPolyline2D",
    "NurbsCurve2D",
    "X3DParticleEmitterNode",
    "ConeEmitter",
    "ExplosionEmitter",
    "PointEmitter",
    "PolylineEmitter",
    "SurfaceEmitter",
    "VolumeEmitter",
    "X3DParticlePhysicsModelNode",
    "BoundedPhysicsModel",
    "ForcePhysicsModel",
    "WindPhysicsModel",
    "X3DProtoInstance",
    "X3DRigidJointNode",
    "BallJoint",
    "DoubleAxisHingeJoint",
    "MotorJoint",
    "SingleAxisHingeJoint",
    "SliderJoint",
    "UniversalJoint",
    "X3DVolumeRenderStyleNode",
    "ProjectionVolumeStyle",
    "X3DComposableVolumeRenderStyle",
    "BlendedVolumeStyle",
    "BoundaryEnhancementVolumeStyle",
    "CartoonVolumeStyle",
    "ComposedVolumeStyle",
    "EdgeEnhancementVolumeStyle",
    "OpacityMapVolumeStyle",
    "ProjectionVolumeStyle",
    "ShadedVolumeStyle",
    "SilhouetteEnhancementVolumeStyle",
    "ToneMappedVolumeStyle",
    "X3DChildNode",
    "BooleanFilter",
    "BooleanToggle",
    "ClipPlane",
    "CollisionCollection",
    "DISEntityManager",
    "GeoLOD",
    "HAnimHumanoid",
    "Inline",
    "LocalFog",
    "NurbsOrientationInterpolator",
    "NurbsPositionInterpolator",
    "NurbsSet",
    "NurbsSurfaceInterpolator",
    "RigidBodyCollection",
    "StaticGroup",
    "X3DBindableNode",
    "Fog",
    "GeoViewpoint",
    "NavigationInfo",
    "X3DBackgroundNode",
    "Background",
    "TextureBackground",
    "X3DViewpointNode",
    "OrthoViewpoint",
    "Viewpoint",
    "ViewpointGroup",
    "X3DFollowerNode",
    "ColorChaser",
    "CoordinateChaser",
    "OrientationChaser",
    "PositionChaser",
    "PositionChaser2D",
    "ScalerChaser",
    "TexCoordChaser2D",
    "X3DDamperNode",
    "ColorDamper",
    "CoordinateDamper",
    "OrientationDamper",
    "PositionDamper",
    "PositionDamper2D",
    "ScalarDamper",
    "TexCoordDamper",
    "X3DGroupingNode",
    "Anchor",
    "Billboard",
    "CADAssembly",
    "CADLayer",
    "CADPart",
    "Collision",
    "EspduTransform",
    "GeoLocation",
    "GeoTransform",
    "Group",
    "HAnimJoint",
    "HAnimSegment",
    "HAnimSite",
    "LayoutGroup",
    "LOD",
    "PickableGroup",
    "ScreenGroup",
    "Switch",
    "Transform",
    "X3DViewportNode",
    "Viewport",
    "X3DInfoNode",
    "DISEntityTypeMapping",
    "GeoMetadata",
    "WorldInfo",
    "X3DInterpolatorNode",
    "ColorInterpolator",
    "CoordinateInterpolator",
    "CoordinateInterpolator2D",
    "GeoPositionInterpolator",
    "NormalInterpolator",
    "OrientationInterpolator",
    "PositionInterpolator",
    "PositionInterpolator2D",
    "ScalarInterpolator",
    "SplinePositionInterpolator",
    "SplinePositionInterpolator2D",
    "SplineScalarInterpolator",
    "SquadOrientationInterpolator",
    "X3DLayoutNode",
    "Layout",
    "X3DLightNode",
    "DirectionalLight",
    "PointLight",
    "SpotLight",
    "X3DNBodyCollidableNode",
    "CollidableOffset",
    "CollidableShape",
    "X3DProductStructureChildNode",
    "CADAssembly",
    "CADFace",
    "CADPart",
    "X3DScriptNode",
    "Script",
    "X3DSensorNode",
    "Collision",
    "CollisionSensor",
    "EspduTransform",
    "ReceiverPdu",
    "SignalPdu",
    "TimeSensor",
    "TransmitterPdu",
    "X3DEnvironmentalSensorNode",
    "GeoProximitySensor",
    "ProximitySensor",
    "TransformSensor",
    "VisibilitySensor",
    "X3DKeyDeviceSensorNode",
    "KeySensor",
    "StringSensor",
    "X3DNetworkSensorNode",
    "LoadSensor",
    "X3DPickSensorNode",
    "LinePickSensor",
    "PointPickSensor",
    "PrimitivePickSensor",
    "VolumePickSensor",
    "X3DPointingDeviceSensorNode",
    "X3DDragSensorNode",
    "CylinderSensor",
    "PlaneSensor",
    "SphereSensor",
    "X3DTouchSensorNode",
    "GeoTouchSensor",
    "TouchSensor",
    "X3DSequencerNode",
    "BooleanSequencer",
    "IntegerSequencer",
    "X3DShapeNode",
    "ParticleSystem",
    "Shape",
    "X3DSoundNode",
    "Sound",
    "X3DTimeDependentNode",
    "TimeSensor",
    "X3DSoundSourceNode",
    "AudioClip",
    "MovieTexture",
    "X3DTriggerNode",
    "BooleanTrigger",
    "IntegerTrigger",
    "TimeTrigger",
    "X3DVolumeDataNode",
    "IsoSurfaceVolumeData",
    "SegmentedVolumeData",
    "VolumeData"
)

X3D_CONSTANT = {
    "PI" : math.pi
}

class setter:
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc or func.__doc__

    def __set__(self, obj, value):
        obj.__dict__[self.func.__name__] = self.func(obj, value)
