"""
Texture and material system for Turtle3D
"""
import math
import random

class Texture:
    """Base texture class"""
    
    def __init__(self):
        self.width = 64
        self.height = 64
    
    def get_color_at(self, u, v):
        """Get color at UV coordinates (0-1 range). Override in subclasses."""
        return (255, 255, 255)  # White default

class SolidTexture(Texture):
    """Solid color texture"""
    
    def __init__(self, color):
        super().__init__()
        if isinstance(color, tuple):
            self.color = color
        elif isinstance(color, str):
            # Convert hex to RGB
            if color.startswith('#'):
                color = color[1:]
            self.color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        else:
            self.color = (255, 255, 255)
    
    def get_color_at(self, u, v):
        return self.color

class CheckerboardTexture(Texture):
    """Checkerboard pattern texture"""
    
    def __init__(self, color1=(255, 255, 255), color2=(0, 0, 0), size=8):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.size = size
    
    def get_color_at(self, u, v):
        # Wrap coordinates
        u = u % 1.0
        v = v % 1.0
        
        # Calculate checker pattern
        checker_u = int(u * self.size) % 2
        checker_v = int(v * self.size) % 2
        
        if (checker_u + checker_v) % 2 == 0:
            return self.color1
        else:
            return self.color2

class GradientTexture(Texture):
    """Gradient texture between two colors"""
    
    def __init__(self, color1=(255, 0, 0), color2=(0, 0, 255), direction='horizontal'):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.direction = direction  # 'horizontal', 'vertical', 'radial'
    
    def get_color_at(self, u, v):
        u = u % 1.0
        v = v % 1.0
        
        if self.direction == 'horizontal':
            t = u
        elif self.direction == 'vertical':
            t = v
        elif self.direction == 'radial':
            # Distance from center
            center_u, center_v = 0.5, 0.5
            t = math.sqrt((u - center_u)**2 + (v - center_v)**2) * 2
            t = min(t, 1.0)
        else:
            t = u
        
        # Linear interpolation between colors
        r = int(self.color1[0] * (1 - t) + self.color2[0] * t)
        g = int(self.color1[1] * (1 - t) + self.color2[1] * t)
        b = int(self.color1[2] * (1 - t) + self.color2[2] * t)
        
        return (r, g, b)

class NoiseTexture(Texture):
    """Random noise texture"""
    
    def __init__(self, base_color=(128, 128, 128), variation=50, seed=None):
        super().__init__()
        self.base_color = base_color
        self.variation = variation
        if seed:
            random.seed(seed)
    
    def get_color_at(self, u, v):
        # Simple noise based on UV coordinates
        noise_val = (math.sin(u * 50) * math.cos(v * 50) + 1) / 2
        noise_val += (math.sin(u * 100 + 1.5) * math.cos(v * 100 + 1.5) + 1) / 4
        noise_val += (math.sin(u * 200 + 3) * math.cos(v * 200 + 3) + 1) / 8
        noise_val /= 1.875  # Normalize
        
        # Apply to base color
        variation = int(self.variation * (noise_val - 0.5))
        r = max(0, min(255, self.base_color[0] + variation))
        g = max(0, min(255, self.base_color[1] + variation))
        b = max(0, min(255, self.base_color[2] + variation))
        
        return (r, g, b)

class BrickTexture(Texture):
    """Brick pattern texture"""
    
    def __init__(self, brick_color=(150, 50, 50), mortar_color=(200, 200, 200), 
                 brick_width=8, brick_height=4):
        super().__init__()
        self.brick_color = brick_color
        self.mortar_color = mortar_color
        self.brick_width = brick_width
        self.brick_height = brick_height
    
    def get_color_at(self, u, v):
        u = u % 1.0
        v = v % 1.0
        
        # Calculate brick grid position
        brick_u = u * self.brick_width
        brick_v = v * self.brick_height
        
        # Offset every other row
        if int(brick_v) % 2 == 1:
            brick_u += 0.5
        
        # Check if we're in mortar (edges)
        mortar_thickness = 0.1
        u_in_brick = brick_u % 1.0
        v_in_brick = brick_v % 1.0
        
        if (u_in_brick < mortar_thickness or u_in_brick > 1.0 - mortar_thickness or
            v_in_brick < mortar_thickness or v_in_brick > 1.0 - mortar_thickness):
            return self.mortar_color
        else:
            return self.brick_color

class Material:
    """Material class that combines texture with rendering properties"""
    
    def __init__(self, texture=None, color=(255, 255, 255), shininess=0.0, transparency=1.0):
        self.texture = texture if texture else SolidTexture(color)
        self.color = color
        self.shininess = shininess  # 0.0 to 1.0
        self.transparency = transparency  # 0.0 (transparent) to 1.0 (opaque)
    
    def get_color_at(self, u, v):
        """Get the final color at UV coordinates"""
        tex_color = self.texture.get_color_at(u, v)
        
        # Apply material tint
        r = int((tex_color[0] / 255.0) * (self.color[0] / 255.0) * 255)
        g = int((tex_color[1] / 255.0) * (self.color[1] / 255.0) * 255)
        b = int((tex_color[2] / 255.0) * (self.color[2] / 255.0) * 255)
        
        return (r, g, b)

# Utility functions for common colors and materials
def rgb(r, g, b):
    """Create RGB color tuple, handling 0-1 or 0-255 ranges"""
    if all(c <= 1.0 for c in [r, g, b]):
        return (int(r * 255), int(g * 255), int(b * 255))
    return (int(r), int(g), int(b))

def hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple"""
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Predefined materials
class Materials:
    """Collection of common materials"""
    
    RED = Material(color=rgb(255, 0, 0))
    GREEN = Material(color=rgb(0, 255, 0))
    BLUE = Material(color=rgb(0, 0, 255))
    WHITE = Material(color=rgb(255, 255, 255))
    BLACK = Material(color=rgb(0, 0, 0))
    YELLOW = Material(color=rgb(255, 255, 0))
    CYAN = Material(color=rgb(0, 255, 255))
    MAGENTA = Material(color=rgb(255, 0, 255))
    
    # Textured materials
    CHECKERBOARD = Material(texture=CheckerboardTexture())
    RED_BRICK = Material(texture=BrickTexture())
    GRASS = Material(texture=NoiseTexture(rgb(50, 150, 50), 30))
    STONE = Material(texture=NoiseTexture(rgb(100, 100, 100), 40))
    SKY = Material(texture=GradientTexture(rgb(135, 206, 235), rgb(255, 255, 255), 'vertical'))
    
    @staticmethod
    def gradient(color1, color2, direction='horizontal'):
        """Create a gradient material"""
        return Material(texture=GradientTexture(color1, color2, direction))
    
    @staticmethod
    def solid(color):
        """Create a solid color material"""
        return Material(color=color)