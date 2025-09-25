# Turtle3D - Pure Python 3D Engine

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pyturtle3d.svg)](https://badge.fury.io/py/pyturtle3d)

A lightweight, educational 3D engine built entirely with Python's built-in turtle graphics library. No external dependencies required!

## Features

- **Pure Python**: No external dependencies - uses only Python's standard library
- **3D Camera System**: First-person camera with gravity, physics, and collision detection
- **Real-time Rendering**: 3D to 2D projection with perspective rendering
- **Advanced Graphics**: Wireframe, filled polygons, textures, and materials
- **Physics Simulation**: Gravity, collision detection with bounding boxes
- **Input System**: WASD movement, mouse look, and customizable controls
- **Educational**: Perfect for learning 3D graphics, game development, and Python

## Installation

```bash
pip install pyturtle3d
```

## Quick Start

```python
import turtle3d
from turtle3d import Engine3D, Vector3

# Create a 3D engine
engine = Engine3D(title="My 3D Scene")

# Create a simple rotating cube
class Cube:
    def __init__(self, position):
        self.position = position
        self.rotation = 0
    
    def update(self, dt, gravity):
        self.rotation += dt
    
    def get_vertices(self):
        # Define cube vertices with rotation
        import math
        cos_r, sin_r = math.cos(self.rotation), math.sin(self.rotation)
        size = 50
        
        vertices = []
        for x in [-size, size]:
            for y in [-size, size]:
                for z in [-size, size]:
                    # Apply rotation
                    rx = x * cos_r - z * sin_r
                    rz = x * sin_r + z * cos_r
                    vertices.append(Vector3(rx, y, rz) + self.position)
        
        return vertices
    
    def get_edges(self):
        return [
            (0, 1), (2, 3), (4, 5), (6, 7),  # Edges along X
            (0, 2), (1, 3), (4, 6), (5, 7),  # Edges along Y  
            (0, 4), (1, 5), (2, 6), (3, 7)   # Edges along Z
        ]

# Add cube to scene
cube = Cube(Vector3(0, 0, 200))
engine.add_object(cube)

# Start the engine
engine.run()
```

## Advanced Example - Textured Objects

```python
from turtle3d import Engine3D, Vector3, Materials, Material, rgb

class TexturedCube:
    def __init__(self, position, materials=None):
        self.position = position
        self.rotation = Vector3(0, 0, 0)
        self.render_mode = 'filled'  # Enable filled rendering
        
        # Different material for each face
        self.materials = materials or {
            'front': Materials.RED_BRICK,
            'back': Materials.GRASS,
            'left': Materials.gradient(rgb(0, 100, 255), rgb(0, 255, 255)),
            'right': Materials.CHECKERBOARD,
            'top': Materials.SKY,
            'bottom': Materials.STONE
        }
    
    def get_faces(self):
        """Define faces with materials for filled rendering"""
        vertices = self.get_vertices()
        return [
            {
                'indices': [4, 5, 6, 7],  # Front face
                'color': self.materials['front'].get_color_at(0.5, 0.5),
                'texture': self.materials['front'].texture,
                'outline': 'white'
            },
            # ... more faces
        ]
    
    # ... rest of implementation

engine = Engine3D()
textured_cube = TexturedCube(Vector3(0, 0, 200))
engine.add_object(textured_cube)
engine.run()
```

## Controls

- **WASD**: Move forward/backward/left/right
- **Q/E**: Move up/down
- **Arrow Keys**: Look around (camera rotation)
- **Space**: Jump (when gravity is enabled)
- **Mouse**: Additional look controls (if implemented)

## Core Components

### Engine3D
The main engine class that handles rendering, input, and the game loop.

```python
engine = Engine3D(width=800, height=600, title="My 3D App")
engine.add_object(my_object)
engine.run()
```

### Vector3
3D vector class with mathematical operations.

```python
pos = Vector3(10, 20, 30)
vel = Vector3(1, 0, 0)
new_pos = pos + vel * delta_time
```

### Camera
3D camera with physics and collision detection.

```python
engine.camera.position = Vector3(0, 0, 0)
engine.camera.has_gravity = True
engine.camera.move_speed = 150
```

### Materials and Textures
Rich material system for realistic rendering.

```python
from turtle3d import Materials, Material, rgb

# Predefined materials
red_material = Materials.RED
brick_material = Materials.RED_BRICK
checker_material = Materials.CHECKERBOARD

# Custom materials
custom_material = Material(color=rgb(255, 128, 0))
gradient_material = Materials.gradient(rgb(255, 0, 0), rgb(0, 0, 255))
```

## Creating Objects

Objects in Turtle3D need to implement these methods:

### Required Methods

```python
class MyObject:
    def get_vertices(self):
        """Return list of Vector3 vertices in world space"""
        return [Vector3(0, 0, 0), Vector3(100, 0, 0), ...]
    
    def get_edges(self):
        """Return list of (vertex_index1, vertex_index2) tuples"""
        return [(0, 1), (1, 2), (2, 0)]
```

### Optional Methods

```python
    def update(self, dt, gravity):
        """Update object state each frame"""
        self.rotation += dt * 0.5
    
    def get_faces(self):
        """Return face definitions for filled rendering"""
        return [{
            'indices': [0, 1, 2, 3],  # Vertex indices
            'color': (255, 0, 0),     # RGB color
            'outline': 'white'        # Outline color
        }]
    
    # Set render mode
    render_mode = 'filled'  # 'wireframe', 'filled', or 'textured'
```

## Built-in Materials

- **Colors**: `RED`, `GREEN`, `BLUE`, `WHITE`, `BLACK`, `YELLOW`, `CYAN`, `MAGENTA`
- **Textures**: `CHECKERBOARD`, `RED_BRICK`, `GRASS`, `STONE`, `SKY`
- **Custom**: Create gradients, solid colors, and procedural textures

## Examples

The package includes several examples:

- **Basic Shapes**: Cubes, pyramids, and simple objects
- **Textured Objects**: Materials and texture mapping
- **Physics Demo**: Gravity, collision, and movement
- **Game Template**: Starting point for 3D games

## Performance Tips

- Keep vertex counts reasonable (< 1000 vertices for smooth performance)
- Use `render_mode = 'wireframe'` for complex objects
- Implement frustum culling for large scenes
- Consider level-of-detail (LOD) for distant objects

## Educational Use

Turtle3D is perfect for:
- Learning 3D graphics programming
- Understanding projection and rendering
- Teaching game development concepts
- Prototyping 3D ideas quickly
- Computer graphics coursework

## Limitations

- Performance is limited by turtle graphics
- No hardware acceleration
- Simple lighting model
- Best for educational use and prototypes

## Contributing

Contributions welcome! Areas for improvement:
- Lighting and shading
- More texture types  
- Animation system
- Scene management
- Documentation

## License

MIT License - see LICENSE file for details.

## Requirements

- Python 3.6 or higher
- No external dependencies (uses built-in `turtle` module)

*Built with ❤️ using Python's turtle graphics*