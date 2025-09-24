from PyQt6.QtWidgets import QDialog, QSlider, QFormLayout, QDialogButtonBox, QSpinBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt

from PyImageLabeling.model.Utils import Utils

class PaintBrushSetting(QDialog):
    def __init__(self, zoomable_graphic_view, model):
        super().__init__(zoomable_graphic_view)
        self.setWindowTitle("Paint brush Settings")
        self.resize(500, 100)

        self.size_paint_brush = Utils.load_parameters()["paint_brush"]["size"] 
        self.max_size = int(min(model.get_current_image_item().image_qrectf.width(), model.get_current_image_item().image_qrectf.height()))
        self.min_size = 1
        if not (self.min_size <= self.size_paint_brush <= self.max_size):
            self.size_paint_brush = 5

        layout = QVBoxLayout()
        label = QLabel("Size of the brush in pixel:")
        layout.addWidget(label)

        slider_layout = QHBoxLayout()
        initial_size_paint_brush = self.ensure_even_value(self.size_paint_brush)
        # Tolerance slider and spinbox
        self.size_paint_brush_slider = QSlider(Qt.Orientation.Horizontal)
        self.size_paint_brush_slider.setRange(self.min_size, self.max_size)
        self.size_paint_brush_slider.setSingleStep(2)
        self.size_paint_brush_slider.setValue(initial_size_paint_brush)
        self.size_paint_brush_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        tick_interval = max(1, self.max_size // 20)
        self.size_paint_brush_slider.setTickInterval(tick_interval)

        self.size_paint_brush_spinbox = QSpinBox()
        self.size_paint_brush_spinbox.setRange(self.min_size, self.max_size)
        self.size_paint_brush_spinbox.setSingleStep(2)
        self.size_paint_brush_spinbox.setValue(initial_size_paint_brush)

        # Connect both ways to keep them synchronized
        self.size_paint_brush_spinbox.valueChanged.connect(self.size_paint_brush_slider.setValue)
        self.size_paint_brush_slider.valueChanged.connect(self.size_paint_brush_spinbox.setValue)
        
        # Update internal values when sliders change
        self.size_paint_brush_slider.valueChanged.connect(self.update_size_paint_brush)
        self.size_paint_brush_spinbox.valueChanged.connect(self.update_size_paint_brush)

        slider_layout.addWidget(self.size_paint_brush_slider)
        slider_layout.addWidget(self.size_paint_brush_spinbox)
        layout.addLayout(slider_layout)

        # Buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def ensure_even_value(self, value):
        """Ensure the value is even (pair). If odd, round to nearest even."""
        if value % 2 != 0:
            return value + 1
        return value
    
    def update_size_paint_brush(self, value):
        """Update internal tolerance value when slider changes"""
        self.size_paint_brush = self.ensure_even_value(value)

    def accept(self):
        """Override accept to ensure settings are updated before closing"""
        # Update internal values one final time
        self.size_paint_brush = self.size_paint_brush_slider.value()
        data = Utils.load_parameters()
        data["paint_brush"]["size"] = self.size_paint_brush
        Utils.save_parameters(data) 
        return super().accept()