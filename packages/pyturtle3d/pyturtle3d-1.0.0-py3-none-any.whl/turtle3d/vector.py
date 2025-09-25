"""
3D Vector mathematics
"""
import math

class Vector3:
    """3D Vector class with mathematical operations"""
    
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar):
        return self * scalar
    
    def __truediv__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __str__(self):
        return f"Vector3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
    
    def __repr__(self):
        return self.__str__()
    
    def magnitude(self):
        """Calculate the magnitude (length) of the vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        """Return a normalized (unit) vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x/mag, self.y/mag, self.z/mag)
    
    def dot(self, other):
        """Calculate dot product with another vector"""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        """Calculate cross product with another vector"""
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def distance_to(self, other):
        """Calculate distance to another vector"""
        return (self - other).magnitude()
    
    def copy(self):
        """Return a copy of this vector"""
        return Vector3(self.x, self.y, self.z)