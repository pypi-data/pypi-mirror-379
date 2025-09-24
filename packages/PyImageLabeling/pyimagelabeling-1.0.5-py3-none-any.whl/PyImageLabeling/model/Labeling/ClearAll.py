from PyQt6.QtGui import QPainter, QBitmap, QImage, QPixmap
from PyImageLabeling.model.Core import Core
from PyQt6.QtWidgets import QMessageBox

class ClearAll(Core):
    def __init__(self):
        super().__init__()

    def clear_all(self):
        msgBox = QMessageBox(self.view.zoomable_graphics_view)
        msgBox.setWindowTitle("Clear All")
        msgBox.setText("Are you sure you want to delete the selected label ?")
        msgBox.setInformativeText("The `Undo` method will be reset.")
        msgBox.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        msgBox.setDefaultButton(QMessageBox.StandardButton.No)
        msgBox.setModal(True)
        result = msgBox.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.get_current_image_item().get_labeling_overlay().reset()
        
    

