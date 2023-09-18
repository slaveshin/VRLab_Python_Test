# X3D_LB_Python

## Introduction

This site defines a common data structure including classes and functions to access X3D files with a standardized scheme using the Python prgramming language, It describes the implementation of a Python language binding viewer, which is an X3D VR viewer for rendering standard X3D data files based on the language binding interface, The VR viewer includes Python based 3D scene libraries and a data structure for creating, modification, exchange, and transfer of X3D objects, In addition, the viewer displays X3D objects and processes events using the libraries and data structure.

### File Architecture

* **Documentation** : X3D Standard Specification
* **OpenGLSB3E** : Python OpenGL Example
* **PythonSAI** : Implments of Python ISO/IEC 19777-6 Standard
* **X3D for Web Authors (X3D4WA) Examples Archive** : Web3d python Example
* **X3DViewer** : Python X3D Viewer

```
X3D_LB_Python
├── Documentation
│   ├── abstract_node_specification
│   └── concrete_node_specification
├── LICENSE
├── OpenGLSB3E
│   ├── Chapter 2
│   ├── Chapter 3
│   ├── Chapter 4
│   ├── Chapter 5
│   ├── Chapter 6
│   ├── Chapter 7
│   ├── Chapter 8
│   └── Common
├── PythonSAI
│   ├── abstract.py
│   ├── common.py
│   ├── concrete.py
│   ├── exception.py
│   ├── field.py
│   └── x3d.py
├── X3D for Web Authors (X3D4WA) Examples Archive
│   ├── Chapter 01 Technical Overview
│   ├── Chapter 02 Geometry Primitives
│   ├── Chapter 03 Grouping
│   ├── Chapter 04 Viewing Navigation
│   ├── Chapter 05 Appearance Material Textures
│   ├── Chapter 06 Geometry Points Lines Polygons
│   ├── Chapter 07 Event Animation Interpolation
│   ├── Chapter 08 User Interactivity
│   ├── Chapter 09 Event Utilities Scripting
│   ├── Chapter 10 Geometry 2D
│   ├── Chapter 11 Lighting Environmental Effects
│   ├── Chapter 12 Environment Sensor Sound
│   ├── Chapter 13 Geometry Triangles Quadrilaterals
│   ├── Chapter 14 Prototypes
│   ├── Chapter 15 Metadata
│   ├── ConformanceNist X3D Examples Archive
│   └── Kelp Forest Exhibit
└── X3DViewer
```

### Get Started

#### Running OpenGLSB3E Examples

```
$ python Bounce.py
```

#### Running X3D for Web Authors (X3D4WA) Examples Archive Examples

```
$python HelloWorld.py
```

#### Running X3DViewer

```
$ python main.py
```