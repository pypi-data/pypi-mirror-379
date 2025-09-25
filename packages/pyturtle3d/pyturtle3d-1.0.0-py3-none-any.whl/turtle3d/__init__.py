"""
Turtle3D - A 3D engine built with Python's turtle graphics
=========================================================

A lightweight 3D engine featuring:
- 3D camera system with gravity and physics
- Collision detection with bounding boxes
- Real-time 3D rendering and projection
- Input handling and controls
- Pure Python - no external dependencies

Basic Usage:
    from turtle3d import Engine3D, Vector3, Camera, BoundingBox
    
    # Create engine
    engine = Engine3D()
    
    # Create a simple cube
    cube_vertices = [
        Vector3(-50, -50, -50), Vector3(50, -50, -50),
        Vector3(50, 50, -50), Vector3(-50, 50, -50),
        Vector3(-50, -50, 50), Vector3(50, -50, 50),
        Vector3(50, 50, 50), Vector3(-50, 50, 50),
    ]
    
    # Main loop
    try:
        while True:
            engine.update()
    except:
        pass

Advanced Usage:
    - Create your own GameObject classes
    - Implement custom collision detection
    - Add enemies, platforms, and game mechanics
    - Build 3D games and simulations
"""

__version__ = "1.0.0"
__author__ = "Turtle3D Team"
__license__ = "MIT"

from .engine import Engine3D
from .vector import Vector3
from .camera import Camera
from .collision import BoundingBox
from .texture import (
    Texture, SolidTexture, CheckerboardTexture, GradientTexture, 
    NoiseTexture, BrickTexture, Material, Materials, rgb, hex_to_rgb
)

__all__ = [
    'Engine3D', 'Vector3', 'Camera', 'BoundingBox',
    'Texture', 'SolidTexture', 'CheckerboardTexture', 'GradientTexture',
    'NoiseTexture', 'BrickTexture', 'Material', 'Materials', 'rgb', 'hex_to_rgb'
]