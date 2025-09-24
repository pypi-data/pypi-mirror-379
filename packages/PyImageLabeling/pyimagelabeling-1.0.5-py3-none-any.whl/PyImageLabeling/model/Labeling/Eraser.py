from PyQt6.QtCore import Qt, QPointF, QRectF, QPoint, QRect
from PyQt6.QtGui import QPixmap, QPainter, QBrush, QColor, QPainterPath, QPen
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsPathItem, QGraphicsItem
from PyImageLabeling.model.Core import Core
import math
from PyImageLabeling.model.Utils import Utils

class EraserBrushItem(QGraphicsItem):

    def __init__(self, core, x, y, color, size, absolute_mode):
        super().__init__()
        self.core = core
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.absolute_mode = absolute_mode
        self.labeling_overlay_painter = self.core.get_current_image_item().get_labeling_overlay().get_painter()
        self.image_pixmap = self.core.get_current_image_item().get_image_pixmap()

        # Compute the good qrect to avoid going beyond the painting area  
        self.qrectf = QRectF(int(self.x)-(self.size/2)-5, int(self.y)-(self.size/2)-5, self.size+10, self.size+10)
        self.qrectf = self.qrectf.intersected(core.get_current_image_item().get_qrectf())
        alpha_color = Utils.load_parameters()["load"]["alpha_color"] 

        # Create a fake texture with the good image inside 
        self.eraser_texture = QPixmap(self.size, self.size) 
        self.eraser_texture.fill(QColor(*alpha_color))
        
        painter = QPainter(self.eraser_texture)
        
        painter.drawPixmap(QRect(0, 0, self.size, self.size), self.image_pixmap, QRect(int(self.x-(self.size/2)), int(self.y-(self.size/2)), self.size, self.size))
        painter.setOpacity(self.core.get_current_image_item().get_labeling_overlay().get_opacity())
        # for other_labeling_overlay_pixmap in self.core.get_current_image_item().get_labeling_overlay_pixmaps():
        #     painter.drawPixmap(QRect(0, 0, self.size, self.size), other_labeling_overlay_pixmap, QRect(int(self.x-(self.size/2)), int(self.y-(self.size/2)), self.size, self.size))
        for labeling_overlay in self.core.get_current_image_item().get_labeling_overlays():
            if labeling_overlay != self.core.get_current_image_item().get_labeling_overlay() and labeling_overlay.label.get_visible():
                painter.drawPixmap(QRect(0, 0, self.size, self.size), labeling_overlay.labeling_overlay_pixmap, QRect(int(self.x-(self.size/2)), int(self.y-(self.size/2)), self.size, self.size))
            
        painter.end()

        # Use the fake texture as a QBrush texture of a draw point 
        self.eraser_pixmap = QPixmap(self.size, self.size) 
        self.eraser_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(self.eraser_pixmap)
        self.qbrush = QBrush()
        self.qbrush.setTexture(self.eraser_texture)
        self.pen = QPen(self.qbrush, self.size)
        self.pen.setCapStyle(Qt.PenCapStyle.RoundCap) 
        painter.setPen(self.pen)
        painter.drawPoint(int(self.size/2), int(self.size/2))
        painter.end()



    def boundingRect(self):
        return self.qrectf

    def paint(self, painter, option, widget):
        painter.drawPixmap(int(self.x-(self.size/2)), int(self.y-(self.size/2)), self.eraser_pixmap) 
        
        pen = QPen(Qt.GlobalColor.black, self.size)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap) 

        if self.absolute_mode == 1:
            # Apply eraser to all labeling overlays
            for labeling_overlay in self.core.get_current_image_item().get_labeling_overlays():
                overlay_painter = labeling_overlay.get_painter()
                overlay_painter.setPen(pen)
                overlay_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)
                overlay_painter.drawPoint(int(self.x), int(self.y))
        else:
            # Apply eraser only to current labeling overlay
            self.labeling_overlay_painter.setPen(pen)
            self.labeling_overlay_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)
            self.labeling_overlay_painter.drawPoint(int(self.x), int(self.y))
        
class Eraser(Core):
    def __init__(self):
        super().__init__()
        self.last_position_x, self.last_position_y = None, None
        self.point_spacing = 2
        self.eraser_brush_items = []

    def eraser(self):
        self.checked_button = self.eraser.__name__      

    def start_eraser(self, current_position):
        self.view.zoomable_graphics_view.change_cursor("eraser")
        
        self.current_position_x = int(current_position.x())
        self.current_position_y = int(current_position.y())

        self.size_eraser_brush = Utils.load_parameters()["eraser"]["size"] 
        self.absolute_mode = Utils.load_parameters()["eraser"]["absolute_mode"]
        self.color = self.get_current_label_item().get_color()
        
        eraser_brush_item = EraserBrushItem(self, self.current_position_x, self.current_position_y, self.color, self.size_eraser_brush, self.absolute_mode)
        eraser_brush_item.setZValue(4) # To place in the top of the item
        self.zoomable_graphics_view.scene.addItem(eraser_brush_item) # update is already call in this method
        self.eraser_brush_items.append(eraser_brush_item)
        
        self.last_position_x, self.last_position_y = self.current_position_x, self.current_position_y

    def move_eraser(self, current_position):
        self.current_position_x = int(current_position.x())
        self.current_position_y = int(current_position.y())

        if Utils.compute_diagonal(self.current_position_x, self.current_position_y, self.last_position_x, self.last_position_y) < self.point_spacing:
            return 
        
        eraser_brush_item = EraserBrushItem(self, self.current_position_x, self.current_position_y, self.color, self.size_eraser_brush, self.absolute_mode)
        eraser_brush_item.setZValue(4) # To place in the top of the item
        self.zoomable_graphics_view.scene.addItem(eraser_brush_item) # update is already call in this method
        self.eraser_brush_items.append(eraser_brush_item)
        
        self.last_position_x, self.last_position_y = self.current_position_x, self.current_position_y

    def end_eraser(self):  
        # Remove the dislay of all these item
        for item in self.eraser_brush_items:
            self.zoomable_graphics_view.scene.removeItem(item)
        self.eraser_brush_items.clear()

        if self.absolute_mode == 1:
            # Update all labeling overlays
            for labeling_overlay in self.get_current_image_item().get_labeling_overlays():
                labeling_overlay.update()
                labeling_overlay.reset_pen()
        else:
            # Update only current labeling overlay
            self.get_current_image_item().update_labeling_overlay()
            self.get_current_image_item().get_labeling_overlay().reset_pen()