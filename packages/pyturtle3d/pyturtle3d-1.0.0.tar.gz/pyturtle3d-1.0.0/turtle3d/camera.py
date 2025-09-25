"""
3D Camera system with physics
"""
import math
from .vector import Vector3
from .collision import BoundingBox

class Camera:
    """3D Camera with physics simulation"""
    
    def __init__(self, position=None, rotation=None):
        self.position = position if position else Vector3(0, 0, 0)
        self.rotation = rotation if rotation else Vector3(0, 0, 0)
        self.focal_length = 400
        
        # Physics properties
        self.collision_box = BoundingBox(self.position, 10)
        self.velocity = Vector3(0, 0, 0)
        self.on_ground = False
        self.has_gravity = True
        
        # Movement properties
        self.jump_strength = 200
        self.can_jump = True
        self.move_speed = 150
    
    def get_forward_vector(self):
        """Get camera's forward direction based on Y rotation"""
        return Vector3(
            math.sin(self.rotation.y),
            0,
            math.cos(self.rotation.y)
        )
    
    def get_right_vector(self):
        """Get camera's right direction based on Y rotation"""
        return Vector3(
            math.cos(self.rotation.y),
            0,
            -math.sin(self.rotation.y)
        )
    
    def move_relative(self, direction):
        """Move camera relative to its current rotation"""
        forward = self.get_forward_vector()
        right = self.get_right_vector()
        
        movement = Vector3(0, 0, 0)
        movement = movement + forward * direction.z  # Forward/backward
        movement = movement + right * direction.x    # Left/right
        movement = movement + Vector3(0, direction.y, 0)  # Up/down (world space)
        
        self.position = self.position + movement
        self.collision_box.update_position(self.position)
    
    def jump(self):
        """Make camera jump"""
        if self.on_ground and self.can_jump:
            self.velocity.y = self.jump_strength
            self.on_ground = False
            self.can_jump = False
    
    def update(self, dt, gravity_strength):
        """Update camera physics"""
        # Apply gravity
        if self.has_gravity and not self.on_ground:
            self.velocity.y += gravity_strength * dt
        
        # Update position based on velocity
        self.position = self.position + self.velocity * dt
        self.collision_box.update_position(self.position)
    
    def rotate_point(self, point):
        """Transform a world point to camera space"""
        # Translate relative to camera
        translated = point - self.position
        
        # Apply rotations (Y then X)
        cos_y, sin_y = math.cos(-self.rotation.y), math.sin(-self.rotation.y)
        cos_x, sin_x = math.cos(-self.rotation.x), math.sin(-self.rotation.x)
        
        # Y rotation (yaw)
        x = translated.x * cos_y + translated.z * sin_y
        z = -translated.x * sin_y + translated.z * cos_y
        translated.x, translated.z = x, z
        
        # X rotation (pitch)
        y = translated.y * cos_x - translated.z * sin_x
        z = translated.y * sin_x + translated.z * cos_x
        translated.y, translated.z = y, z
        
        return translated
    
    def project_to_2d(self, point):
        """Project a 3D world point to 2D screen coordinates"""
        camera_space = self.rotate_point(point)
        
        # Avoid points behind the camera
        if camera_space.z <= 0:
            camera_space.z = 0.1
        
        # Perspective projection
        factor = self.focal_length / camera_space.z
        screen_x = camera_space.x * factor
        screen_y = camera_space.y * factor
        
        return (screen_x, screen_y)