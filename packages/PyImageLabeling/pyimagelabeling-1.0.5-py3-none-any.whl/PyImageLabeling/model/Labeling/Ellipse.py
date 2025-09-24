from PyImageLabeling.model.Core import Core
from PyQt6.QtWidgets import QGraphicsEllipseItem
from PyQt6.QtGui import QPen, QCursor, QBrush
from PyQt6.QtCore import Qt, QPointF, QRectF, QSizeF
import math

HANDLE_SIZE = 8  # Size of handles for resizing
HANDLE_DETECTION_DISTANCE = 15  # Distance for auto-showing handles

class EllipseItem(QGraphicsEllipseItem):
    def __init__(self, x, y, width, height, color=Qt.GlobalColor.red):
        super().__init__(x, y, width, height)

        self.pen = QPen(color, 2)
        self.pen.setStyle(Qt.PenStyle.SolidLine)
        self.setPen(self.pen)

        self.setFlags(
            QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable |
            QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsEllipseItem.GraphicsItemFlag.ItemSendsGeometryChanges
        )

        self.handles = {}  # Dictionary to track handles
        self.rotation_handle = None  # Rotation handle
        self.handle_selected = None
        self.mouse_press_pos = None
        self.handles_visible = False
        self.initial_rotation = 0
        self.initial_angle = 0
        
        # Accept hover events to detect mouse proximity
        self.setAcceptHoverEvents(True)
        
        self.update_handles()

    def get_ellipse_point(self, angle_degrees):
        """Get a point on the ellipse perimeter at the given angle"""
        rect = self.rect()
        center_x = rect.center().x()
        center_y = rect.center().y()
        
        # Semi-major and semi-minor axes
        a = rect.width() / 2  # horizontal radius
        b = rect.height() / 2  # vertical radius
        
        # Convert angle to radians
        angle_rad = math.radians(angle_degrees)
        
        # Parametric equations for ellipse
        x = center_x + a * math.cos(angle_rad)
        y = center_y + b * math.sin(angle_rad)
        
        return QPointF(x, y)

    def update_handles(self):
        """Update handle positions on the ellipse perimeter"""
        rect = self.rect()
        
        # Place handles at 0°, 90°, 180°, 270° on the ellipse perimeter
        right_point = self.get_ellipse_point(0)      # Right (0°)
        bottom_point = self.get_ellipse_point(90)    # Bottom (90°) 
        left_point = self.get_ellipse_point(180)     # Left (180°)
        top_point = self.get_ellipse_point(270)      # Top (270°)
        
        # Create handle rectangles centered on these points
        self.handles = {
            'right': QRectF(right_point - QPointF(HANDLE_SIZE/2, HANDLE_SIZE/2), QSizeF(HANDLE_SIZE, HANDLE_SIZE)),
            'bottom': QRectF(bottom_point - QPointF(HANDLE_SIZE/2, HANDLE_SIZE/2), QSizeF(HANDLE_SIZE, HANDLE_SIZE)),
            'left': QRectF(left_point - QPointF(HANDLE_SIZE/2, HANDLE_SIZE/2), QSizeF(HANDLE_SIZE, HANDLE_SIZE)),
            'top': QRectF(top_point - QPointF(HANDLE_SIZE/2, HANDLE_SIZE/2), QSizeF(HANDLE_SIZE, HANDLE_SIZE)),
            'rotation': QRectF(QPointF(rect.center()) - QPointF(HANDLE_SIZE/2, HANDLE_SIZE/2), QSizeF(HANDLE_SIZE, HANDLE_SIZE))
        }

    def hoverEnterEvent(self, event):
        """Mouse entered the item area"""
        self.check_handle_proximity(event.pos())
        super().hoverEnterEvent(event)

    def hoverMoveEvent(self, event):
        """Mouse moved within the item area"""
        self.check_handle_proximity(event.pos())
        self.update_cursor(event.pos())
        super().hoverMoveEvent(event)

    def hoverLeaveEvent(self, event):
        """Mouse left the item area"""
        self.handles_visible = False
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.update()
        super().hoverLeaveEvent(event)

    def check_handle_proximity(self, pos):
        """Check if mouse is near any handle and make them visible"""
        near_handle = False
        
        # Check handles
        for handle_rect in self.handles.values():
            if self.distance_to_rect(pos, handle_rect) < HANDLE_DETECTION_DISTANCE:
                near_handle = True
                break
        
        # Also show handles when selected
        if self.isSelected():
            near_handle = True
            
        if near_handle != self.handles_visible:
            self.handles_visible = near_handle
            self.update()

    def distance_to_rect(self, point, rect):
        """Calculate distance from point to rectangle"""
        center = rect.center()
        dx = abs(point.x() - center.x())
        dy = abs(point.y() - center.y())
        return math.sqrt(dx*dx + dy*dy)

    def update_cursor(self, pos):
        """Update cursor based on which handle is under mouse"""
        if not self.handles_visible:
            return
  
        # Check resize handles
        for name, rect in self.handles.items():
            if rect.contains(pos):
                if name in ['rotation']:
                    self.setCursor(Qt.CursorShape.OpenHandCursor)
                elif name in ['right', 'left']:
                    self.setCursor(Qt.CursorShape.SizeHorCursor)
                elif name in ['top', 'bottom']:
                    self.setCursor(Qt.CursorShape.SizeVerCursor)
                return
        
        self.setCursor(Qt.CursorShape.SizeAllCursor)

    def paint(self, painter, option, widget=None):
        super().paint(painter, option, widget)
        
        if self.handles_visible:
            # Draw resize handles
            painter.setPen(QPen(Qt.GlobalColor.black, 1, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.white, Qt.BrushStyle.SolidPattern))
            
            # Draw square handles for resize
            for name, handle_rect in self.handles.items():
                if name != 'rotation':
                    painter.drawRect(handle_rect)
            
            # Draw rotation handle (circular) at center
            if self.handles['rotation']:
                painter.setPen(QPen(Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                painter.setBrush(QBrush(Qt.GlobalColor.blue, Qt.BrushStyle.SolidPattern))
                painter.drawEllipse(self.handles['rotation'])

    def mousePressEvent(self, event):
        self.handle_selected = None
        self.mouse_press_pos = event.pos()

        if not self.handles_visible:
            super().mousePressEvent(event)
            return

        # Check handles
        for name, rect in self.handles.items():
            if rect.contains(event.pos()):
                self.handle_selected = name
                if name == 'rotation':
                    # Store initial rotation data for rotation handle
                    rect_center = self.rect().center()
                    rect_center_scene = self.mapToScene(rect_center)
                    mouse_scene_pos = self.mapToScene(event.pos())
                    self.initial_rotation = math.atan2(
                        mouse_scene_pos.y() - rect_center_scene.y(),
                        mouse_scene_pos.x() - rect_center_scene.x()
                    )
                    self.initial_angle = self.rotation()
                break

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.handle_selected == 'rotation':
            # Handle rotation
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            self.handles_visible = False
            rect_center = self.rect().center()
            self.setTransformOriginPoint(rect_center)
            
            # Map center to scene coordinates
            rect_center_scene = self.mapToScene(rect_center)
            
            # Calculate current mouse angle relative to ellipse center
            mouse_scene_pos = self.mapToScene(event.pos())
            current_mouse_angle = math.atan2(
                mouse_scene_pos.y() - rect_center_scene.y(),
                mouse_scene_pos.x() - rect_center_scene.x()
            )
            
            # Calculate angle difference and apply rotation
            angle_diff = math.degrees(current_mouse_angle - self.initial_rotation)
            new_rotation = self.initial_angle + angle_diff
            self.setRotation(new_rotation)
            
            self.update_handles()
            self.update()
            
        elif self.handle_selected and self.handle_selected != 'rotation':
            # Handle resizing
            pos = event.pos()
            rect = self.rect()
            self.handles_visible = False
            center = rect.center()
            
            if self.handle_selected == 'right':
                # Resize horizontally from right edge
                new_width = 2 * abs(pos.x() - center.x())
                new_width = max(10, new_width)  # Minimum width
                rect.setWidth(new_width)
                rect.moveCenter(center)
                
            elif self.handle_selected == 'left':
                # Resize horizontally from left edge
                new_width = 2 * abs(pos.x() - center.x())
                new_width = max(10, new_width)  # Minimum width
                rect.setWidth(new_width)
                rect.moveCenter(center)
                
            elif self.handle_selected == 'bottom':
                # Resize vertically from bottom edge
                new_height = 2 * abs(pos.y() - center.y())
                new_height = max(10, new_height)  # Minimum height
                rect.setHeight(new_height)
                rect.moveCenter(center)
                
            elif self.handle_selected == 'top':
                # Resize vertically from top edge
                new_height = 2 * abs(pos.y() - center.y())
                new_height = max(10, new_height)  # Minimum height
                rect.setHeight(new_height)
                rect.moveCenter(center)

            self.setRect(rect)
            self.update_handles()
            self.update()  # Force repaint to hide handles during resizing
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.handle_selected == 'rotation':
            self.setCursor(Qt.CursorShape.OpenHandCursor)
            event.accept()
        self.handle_selected = None
        self.handles_visible = True
        self.update()

        # Only call super if we didn't handle rotation
        if not (self.handle_selected == 'rotation' or event.isAccepted()):
            super().mouseReleaseEvent(event)

class Ellipse(Core):
    def __init__(self):
        super().__init__()
        self.first_click_pos = None
        self.current_ellipse = None
        self.is_drawing = False
        self.selected_ellipse = None  

    def ellipse(self):
        self.checked_button = self.ellipse.__name__
        self.zoomable_graphics_view.scene.selectionChanged.connect(self.update_selected_ellipse)
        
    def cleanup_temporary_ellipses(self):
        """Remove preview ellipses"""
        if self.current_ellipse:
            if self.current_ellipse in self.zoomable_graphics_view.scene.items():
                self.zoomable_graphics_view.scene.removeItem(self.current_ellipse)
            self.current_ellipse = None

    def start_ellipse_tool(self, current_position):
        """Mouse press → start drawing"""
        self.zoomable_graphics_view.change_cursor("ellipse")
        self.cleanup_temporary_ellipses()

        self.first_click_pos = QPointF(current_position.x(), current_position.y())
        self.color = self.get_labeling_overlay().get_color()
        self.is_drawing = True

        # Preview ellipse
        self.current_ellipse = QGraphicsEllipseItem(
            self.first_click_pos.x(),
            self.first_click_pos.y(),
            1, 1
        )
        pen = QPen(self.color, 2)
        pen.setStyle(Qt.PenStyle.DashLine)
        self.current_ellipse.setPen(pen)
        self.current_ellipse.setZValue(2)
        self.zoomable_graphics_view.scene.addItem(self.current_ellipse)

    def move_ellipse_tool(self, current_position):
        """Mouse move → resize preview ellipse"""
        if not self.is_drawing or not self.current_ellipse:
            return

        current_pos = QPointF(current_position.x(), current_position.y())
        x = min(self.first_click_pos.x(), current_pos.x())
        y = min(self.first_click_pos.y(), current_pos.y())
        w = abs(current_pos.x() - self.first_click_pos.x())
        h = abs(current_pos.y() - self.first_click_pos.y())

        self.current_ellipse.setRect(x, y, w, h)

    def end_ellipse_tool(self):
        """Mouse release → finalize ellipse"""
        if not self.is_drawing or not self.current_ellipse:
            return

        rect = self.current_ellipse.rect()
        self.cleanup_temporary_ellipses()

        if rect.width() > 5 and rect.height() > 5:
            final_ellipse = EllipseItem(
                rect.x(), rect.y(),
                rect.width(), rect.height(),
                self.color
            )
            final_ellipse.setZValue(2)
            final_ellipse.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable, True)
            self.zoomable_graphics_view.scene.addItem(final_ellipse)
            self.selected_ellipse = final_ellipse

        self.first_click_pos = None
        self.is_drawing = False
    
    def update_selected_ellipse(self):
        """Update selected_ellipse when user clicks on an ellipse"""
        selected_items = self.zoomable_graphics_view.scene.selectedItems()
        if selected_items:
            item = selected_items[-1]  # last selected item
            if isinstance(item, EllipseItem):
                self.selected_ellipse = item
        else:
            self.selected_ellipse = None

    def clear_ellipse(self):
        """Remove the currently selected ellipse from the scene"""
        if self.selected_ellipse:
            if self.selected_ellipse in self.zoomable_graphics_view.scene.items():
                self.view.zoomable_graphics_view.scene.removeItem(self.selected_ellipse)
            self.selected_ellipse = None