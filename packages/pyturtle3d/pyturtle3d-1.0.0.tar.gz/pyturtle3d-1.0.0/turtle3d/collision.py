"""
Collision detection system
"""
from .vector import Vector3

class BoundingBox:
    """Axis-Aligned Bounding Box for collision detection"""
    
    def __init__(self, center, size):
        self.center = center.copy()
        self.size = size  # Half-extents from center
        self.update_bounds()
    
    def update_bounds(self):
        """Update min/max points based on center and size"""
        self.min_point = Vector3(
            self.center.x - self.size, 
            self.center.y - self.size, 
            self.center.z - self.size
        )
        self.max_point = Vector3(
            self.center.x + self.size, 
            self.center.y + self.size, 
            self.center.z + self.size
        )
    
    def update_position(self, new_center):
        """Update the bounding box position"""
        self.center = new_center.copy()
        self.update_bounds()
    
    def intersects(self, other):
        """Check if this bounding box intersects with another"""
        return (self.min_point.x <= other.max_point.x and self.max_point.x >= other.min_point.x and
                self.min_point.y <= other.max_point.y and self.max_point.y >= other.min_point.y and
                self.min_point.z <= other.max_point.z and self.max_point.z >= other.min_point.z)
    
    def contains_point(self, point):
        """Check if a point is inside this bounding box"""
        return (self.min_point.x <= point.x <= self.max_point.x and
                self.min_point.y <= point.y <= self.max_point.y and
                self.min_point.z <= point.z <= self.max_point.z)