"""
Main 3D Engine
"""
import turtle
import time
from .vector import Vector3
from .camera import Camera

class Engine3D:
    """Main 3D engine class"""
    
    def __init__(self, width=800, height=600, title="Turtle3D Engine"):
        # Setup screen
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor('black')
        self.screen.title(title)
        self.screen.tracer(0)  # Disable animation for performance
        
        # Setup drawing turtle
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.pen.pensize(1)
        
        # Engine components
        self.camera = Camera()
        self.objects = []  # List of objects with get_vertices() and get_edges() methods
        
        # Physics
        self.gravity = -800
        self.dt = 1/60  # 60 FPS target
        
        # Input system
        self.keys_pressed = set()
        self.setup_default_controls()
        
        # Performance tracking
        self.frame_count = 0
        self.last_fps_time = time.time()
        self.current_fps = 0
        
        # State
        self.running = False
    
    def setup_default_controls(self):
        """Setup default WASD + arrow key controls"""
        self.screen.listen()
        
        keys = ['w', 's', 'a', 'd', 'q', 'e', 'space', 'Up', 'Down', 'Left', 'Right']
        
        for key in keys:
            self.screen.onkeypress(self._make_key_press(key), key)
            self.screen.onkeyrelease(self._make_key_release(key), key)
    
    def _make_key_press(self, key):
        """Create key press handler"""
        return lambda: self.keys_pressed.add(key)
    
    def _make_key_release(self, key):
        """Create key release handler"""
        return lambda: self.keys_pressed.discard(key)
    
    def handle_input(self):
        """Process input - override this for custom controls"""
        move_speed = self.camera.move_speed * self.dt
        look_speed = 2.0 * self.dt
        
        # Movement (WASD + QE)
        movement = Vector3(0, 0, 0)
        
        if 'w' in self.keys_pressed:
            movement.z += move_speed
        if 's' in self.keys_pressed:
            movement.z -= move_speed
        if 'a' in self.keys_pressed:
            movement.x -= move_speed
        if 'd' in self.keys_pressed:
            movement.x += move_speed
        if 'q' in self.keys_pressed:
            movement.y += move_speed
        if 'e' in self.keys_pressed:
            movement.y -= move_speed
        
        if movement.magnitude() > 0:
            self.camera.move_relative(movement)
        
        # Jumping
        if 'space' in self.keys_pressed:
            self.camera.jump()
        
        # Camera rotation (Arrow keys)
        if 'Up' in self.keys_pressed:
            self.camera.rotation.x -= look_speed
        if 'Down' in self.keys_pressed:
            self.camera.rotation.x += look_speed
        if 'Left' in self.keys_pressed:
            self.camera.rotation.y -= look_speed
        if 'Right' in self.keys_pressed:
            self.camera.rotation.y += look_speed
        
        # Clamp vertical rotation
        self.camera.rotation.x = max(-1.5, min(1.5, self.camera.rotation.x))
    
    def add_object(self, obj):
        """Add an object to the scene. Object should have get_vertices() and get_edges() methods"""
        self.objects.append(obj)
        return obj
    
    def remove_object(self, obj):
        """Remove an object from the scene"""
        if obj in self.objects:
            self.objects.remove(obj)
    
    def draw_line(self, p1, p2, color='white'):
        """Draw a line between two 3D points"""
        try:
            p1_2d = self.camera.project_to_2d(p1)
            p2_2d = self.camera.project_to_2d(p2)
            
            # Skip lines that are too far off screen
            if (abs(p1_2d[0]) > 2000 or abs(p1_2d[1]) > 2000 or
                abs(p2_2d[0]) > 2000 or abs(p2_2d[1]) > 2000):
                return
            
            self.pen.color(color)
            self.pen.penup()
            self.pen.goto(p1_2d[0], p1_2d[1])
            self.pen.pendown()
            self.pen.goto(p2_2d[0], p2_2d[1])
        except:
            pass  # Skip problematic lines
    
    def draw_filled_polygon(self, vertices_3d, fill_color=None, outline_color='white', texture=None):
        """Draw a filled polygon (triangle or quad) with optional texture"""
        try:
            # Project all vertices to 2D
            vertices_2d = []
            for vertex in vertices_3d:
                vertex_2d = self.camera.project_to_2d(vertex)
                # Skip if too far off screen
                if abs(vertex_2d[0]) > 2000 or abs(vertex_2d[1]) > 2000:
                    return
                vertices_2d.append(vertex_2d)
            
            # Set up pen for filling
            if fill_color or texture:
                if texture and hasattr(texture, 'get_color_at'):
                    # Custom texture - use center point for now (simplified)
                    center_2d = (
                        sum(v[0] for v in vertices_2d) / len(vertices_2d),
                        sum(v[1] for v in vertices_2d) / len(vertices_2d)
                    )
                    # Normalize coordinates for texture lookup
                    tex_u = (center_2d[0] + 400) / 800  # Map screen to 0-1
                    tex_v = (center_2d[1] + 300) / 600
                    fill_color = texture.get_color_at(tex_u, tex_v)
                
                # Set fill color
                if isinstance(fill_color, tuple) and len(fill_color) == 3:
                    # RGB tuple (0-255)
                    r, g, b = fill_color
                    fill_color = f"#{r:02x}{g:02x}{b:02x}"
                
                self.pen.fillcolor(fill_color)
                self.pen.color(outline_color)
                
                # Draw filled polygon
                self.pen.penup()
                self.pen.goto(vertices_2d[0][0], vertices_2d[0][1])
                self.pen.begin_fill()
                self.pen.pendown()
                
                for vertex_2d in vertices_2d[1:]:
                    self.pen.goto(vertex_2d[0], vertex_2d[1])
                
                # Close the polygon
                self.pen.goto(vertices_2d[0][0], vertices_2d[0][1])
                self.pen.end_fill()
            
            # Draw outline if requested
            if outline_color and outline_color != 'none':
                self.pen.color(outline_color)
                self.pen.penup()
                self.pen.goto(vertices_2d[0][0], vertices_2d[0][1])
                self.pen.pendown()
                
                for vertex_2d in vertices_2d[1:]:
                    self.pen.goto(vertex_2d[0], vertex_2d[1])
                
                # Close the outline
                self.pen.goto(vertices_2d[0][0], vertices_2d[0][1])
        
        except:
            pass  # Skip problematic polygons
    
    def draw_object(self, obj):
        """Draw a 3D object. Object must have get_vertices() and get_edges() methods"""
        if not hasattr(obj, 'get_vertices') or not hasattr(obj, 'get_edges'):
            return
        
        vertices = obj.get_vertices()
        
        # Check if object supports faces (filled rendering)
        if hasattr(obj, 'get_faces') and hasattr(obj, 'render_mode'):
            faces = obj.get_faces()
            render_mode = getattr(obj, 'render_mode', 'wireframe')
            
            if render_mode in ['filled', 'textured']:
                # Draw filled faces
                for face in faces:
                    face_vertices = [vertices[i] for i in face['indices']]
                    
                    # Get face properties
                    fill_color = face.get('color', getattr(obj, 'color', 'white'))
                    outline_color = face.get('outline', 'white')
                    texture = face.get('texture', None)
                    
                    # Draw the face
                    self.draw_filled_polygon(
                        face_vertices, 
                        fill_color=fill_color, 
                        outline_color=outline_color if render_mode == 'filled' else 'none',
                        texture=texture
                    )
                return
        
        # Default wireframe rendering
        edges = obj.get_edges()
        color = getattr(obj, 'color', 'white')
        
        for edge in edges:
            if edge[0] < len(vertices) and edge[1] < len(vertices):
                self.draw_line(vertices[edge[0]], vertices[edge[1]], color)
    
    def update_physics(self):
        """Update physics for camera and objects"""
        # Update camera physics
        self.camera.update(self.dt, self.gravity)
        
        # Update objects that have physics
        for obj in self.objects:
            if hasattr(obj, 'update'):
                obj.update(self.dt, self.gravity)
    
    def check_collisions(self):
        """Override this method to implement collision detection"""
        pass
    
    def render(self):
        """Render the scene"""
        self.pen.clear()
        
        # Draw all objects
        for obj in self.objects:
            self.draw_object(obj)
        
        # Draw UI
        self.draw_ui()
        
        # Update screen
        self.screen.update()
    
    def draw_ui(self):
        """Draw UI elements - override for custom UI"""
        self.pen.color('white')
        self.pen.penup()
        
        # FPS counter
        self.pen.goto(-390, 280)
        self.pen.write(f"FPS: {self.current_fps:.0f}", font=("Arial", 12, "normal"))
        
        # Camera position
        pos = self.camera.position
        self.pen.goto(-390, 260)
        self.pen.write(f"Camera: ({pos.x:.0f}, {pos.y:.0f}, {pos.z:.0f})", 
                      font=("Arial", 10, "normal"))
        
        # Controls
        self.pen.goto(-390, -280)
        self.pen.write("WASD: Move | QE: Up/Down | SPACE: Jump | Arrows: Look", 
                      font=("Arial", 8, "normal"))
    
    def update_fps(self):
        """Update FPS counter"""
        self.frame_count += 1
        current_time = time.time()
        
        if current_time - self.last_fps_time >= 1.0:
            self.current_fps = self.frame_count
            self.frame_count = 0
            self.last_fps_time = current_time
    
    def update(self):
        """Main update loop - called every frame"""
        self.handle_input()
        self.update_physics()
        self.check_collisions()
        self.render()
        self.update_fps()
    
    def run(self):
        """Start the main engine loop"""
        self.running = True
        
        try:
            while self.running:
                self.update()
                time.sleep(self.dt)
                
        except turtle.Terminator:
            pass
        except KeyboardInterrupt:
            print("Engine stopped by user")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the engine"""
        self.running = False
        try:
            self.screen.bye()
        except:
            pass