



from PyQt6.QtWidgets import QVBoxLayout, QWidget, QListWidget, QHBoxLayout, QPushButton, QStatusBar, QGroupBox, QLayout, QStackedLayout, QLabel, QScrollArea, QGridLayout, QProgressBar
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize, QRect
from PyImageLabeling.model.Utils import Utils

from PyImageLabeling.view.ZoomableGraphicsView import ZoomableGraphicsView

from PyImageLabeling.view.QWidgets import QBlanckWidget1, QSeparator1
import os

class Builder:

    def __init__(self, view):
        self.view = view

    def build(self):

        # Central widget
        self.view.central_widget = QWidget()
        self.view.setCentralWidget(self.view.central_widget)
        self.view.main_layout = QGridLayout(self.view.central_widget)
        self.view.main_layout.setSpacing(0)
        #self.view.main_layout.setRowMinimumHeight(0, 1000)
        
        self.build_labeling_bar()
        self.build_graphics_view()
        self.build_label_bar()
        self.build_image_bar()
        self.build_file_bar()
        self.build_status_bar()

        #self.build_apply_cancel_bar()

    # def build_apply_cancel_bar(self):
    #     self.apply_cancel_bar_container = QWidget()
    #     apply_cancel_bar_layout = QHBoxLayout(self.apply_cancel_bar_container)

    #     for button in self.view.config["apply_cancel_bar"]:
    #         button_name = button["name"]
    #         self.view.buttons_apply_cancel_bar[button_name] = QPushButton()
    #         self.view.buttons_apply_cancel_bar[button_name].setToolTip(button["tooltip"]) # Detailed tooltip
    #         self.view.buttons_apply_cancel_bar[button_name].setObjectName("permanent")
    #         icon_path = Utils.get_icon_path(button["icon"])
    #         if os.path.exists(icon_path):
    #             self.view.buttons_apply_cancel_bar[button_name].setIcon(QIcon(icon_path))
    #             self.view.buttons_apply_cancel_bar[button_name].setIconSize(QSize(*self.view.config["window_size"]["icon"]))
    #         self.view.buttons_apply_cancel_bar[button_name].clicked.connect(getattr(self.view.controller, button["name"]))
    #         self.view.buttons_apply_cancel_bar[button_name].setCheckable(button["checkable"])

    #         apply_cancel_bar_layout.addWidget(self.view.buttons_apply_cancel_bar[button_name])
    #     self.apply_cancel_bar_container.setGeometry(QRect(0, 0, 200, 220))
    #     self.view.main_layout.addWidget(self.apply_cancel_bar_container)

    def build_status_bar(self):
        self.view.statusBar().showMessage('Ready')
        self.view.progressBar = QProgressBar()
        self.view.statusBar().addPermanentWidget(self.view.progressBar) 
        
    def build_file_bar(self):
        self.view.file_bar_container = QWidget()
        self.view.file_bar_layout = QVBoxLayout(self.view.file_bar_container)
        self.file_bar_scroll = QScrollArea()
        self.file_bar_button_container = QWidget()
        self.file_bar_button_container.setObjectName("file_bar")

        self.file_bar_button_layout = QHBoxLayout(self.file_bar_button_container)
        
        for button in self.view.config["file_bar"]:
            button_name = button["name"]
            self.view.buttons_file_bar[button_name] = QPushButton()
            self.view.buttons_file_bar[button_name].setToolTip(button["tooltip"]) # Detailed tooltip
            self.view.buttons_file_bar[button_name].setObjectName("permanent")
            icon_path = Utils.get_icon_path(button["icon"])
            if os.path.exists(icon_path):
                self.view.buttons_file_bar[button_name].setIcon(QIcon(icon_path))
                self.view.buttons_file_bar[button_name].setIconSize(QSize(*self.view.config["window_size"]["icon"]))
            self.view.buttons_file_bar[button_name].clicked.connect(getattr(self.view.controller, button["name"]))
            self.view.buttons_file_bar[button_name].setCheckable(button["checkable"])
            if 'previous' in button_name or 'next' in button_name or 'save' in button_name:
                self.view.buttons_file_bar[button_name].setEnabled(False)

            self.file_bar_button_layout.addWidget(self.view.buttons_file_bar[button_name])
        self.view.file_bar_layout.addWidget(self.file_bar_button_container)
        self.file_bar_button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.view.file_bar_list = QListWidget()
        self.view.file_bar_list.itemSelectionChanged.connect(self.view.file_bar_select)
        #self.view.file_bar_list.itemClicked.connect(self.view.controller.on_file_double_clicked)
        """
        self.file_bar_list.addItem("un tres llllllllllllllllllllllllloooooooooooooooooonnnnnnnnnnnnnnnnnnnng fichier.png")
        for i in range(100):
            self.file_bar_list.addItem("file_"+str(i)+".png")
        """
        self.view.file_bar_list.setMinimumWidth(0)
        
        self.view.file_bar_layout.setSpacing(0)
        self.view.file_bar_layout.setContentsMargins(0,0,0,10)

        
        self.view.file_bar_container.setMinimumWidth(self.view.config["window_size"]["file_bar"]["width"])
        self.view.file_bar_container.setMaximumWidth(self.view.config["window_size"]["file_bar"]["width"])
        
        #self.view.file_bar_container.setMinimumHeight(self.view.config["window_size"]["file_bar"]["width"])
        #self.view.file_bar_container.setMaximumHeight(700)
        

        self.view.file_bar_layout.addWidget(self.view.file_bar_list)
        
        self.view.main_layout.addWidget(self.view.file_bar_container, 0, 3, 3, 1)

    def build_labeling_bar(self):
        self.labeling_bar_container = QWidget()
        self.labeling_bar_scroll = QScrollArea()
        labeling_bar_layout = QVBoxLayout(self.labeling_bar_container)
        #left_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        setting_buttons = {}
        for category in self.view.config["labeling_bar_setting"]:
            category_name = tuple(category.keys())[0]
            if "Setting" in category_name:
                for button in category[category_name]:
                    # Extract the base name (remove "_setting" suffix)
                    base_name = button["name"].replace("_setting", "")
                    setting_buttons[base_name] = button

        for category_key in self.view.config["labeling_bar"].keys():
            category = self.view.config["labeling_bar"][category_key]
            category_name = category["name_view"]
            frame = QGroupBox()
            frame.setTitle(category_name)
            buttons_layout = QVBoxLayout(frame)
            
            for button in category["buttons"]:
                button_name = button["name"]
                self.view.buttons_labeling_bar[button_name] = QPushButton(button["name_view"])
                self.view.buttons_labeling_bar[button_name].setToolTip(button["tooltip"]) # Detailed tooltip
                icon_path = Utils.get_icon_path(button["icon"])
                if os.path.exists(icon_path):
                    self.view.buttons_labeling_bar[button_name].setIcon(QIcon(icon_path))
                    self.view.buttons_labeling_bar[button_name].setIconSize(QSize(*self.view.config["window_size"]["icon"])) 
                self.view.buttons_labeling_bar[button_name].clicked.connect(getattr(self.view.controller, button["name"]))
                self.view.buttons_labeling_bar[button_name].setCheckable(button["checkable"])
                self.view.buttons_labeling_bar[button_name].setEnabled(False)
                
                if button_name in setting_buttons:
                    setting_button_config = setting_buttons[button_name]
                    
                    # Create horizontal layout: tool button + setting button
                    h_layout = QHBoxLayout()
                    self.view.buttons_labeling_bar[button_name].setObjectName("with_parameters")
                    h_layout.addWidget(self.view.buttons_labeling_bar[button_name])
                    
                    # Create setting button
                    setting_button_name = setting_button_config["name"]
                    self.view.buttons_labeling_bar[setting_button_name] = QPushButton()
                    self.view.buttons_labeling_bar[setting_button_name].setObjectName("setting_button")
                    self.view.buttons_labeling_bar[setting_button_name].setToolTip(setting_button_config["tooltip"])
                    
                    setting_icon_path = Utils.get_icon_path(setting_button_config["icon"])
                    if os.path.exists(setting_icon_path):
                        self.view.buttons_labeling_bar[setting_button_name].setIcon(QIcon(setting_icon_path))
                        self.view.buttons_labeling_bar[setting_button_name].setIconSize(QSize(*self.view.config["window_size"]["icon"]))
                    
                    self.view.buttons_labeling_bar[setting_button_name].clicked.connect(getattr(self.view.controller, setting_button_name))
                    self.view.buttons_labeling_bar[setting_button_name].setCheckable(setting_button_config["checkable"])
                    self.view.buttons_labeling_bar[setting_button_name].setEnabled(False)

                    h_layout.setSpacing(0)
                    h_layout.addWidget(self.view.buttons_labeling_bar[setting_button_name])
                    
                    buttons_layout.addLayout(h_layout)
                else:
                    # No setting button, add main button directly
                    self.view.buttons_labeling_bar[button_name].setObjectName("without_parameters")
                    buttons_layout.addWidget(self.view.buttons_labeling_bar[button_name])

            labeling_bar_layout.addWidget(frame)

        #self.labeling_bar_container.setMinimumWidth(self.view.config["window_size"]["labeling_bar"]["width"])    
        #self.labeling_bar_container.setMaximumWidth(self.view.config["window_size"]["labeling_bar"]["width"])
        #labeling_bar_layout.setContentsMargins(0,0,0,self.view.config["window_size"]["margin"])
        #labeling_bar_layout.setSpacing(self.view.config["window_size"]["margin"])
        
        self.labeling_bar_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.labeling_bar_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.labeling_bar_scroll.setWidgetResizable(True)
        self.labeling_bar_scroll.setMinimumWidth(self.view.config["window_size"]["labeling_bar"]["width"])    
        self.labeling_bar_scroll.setMaximumWidth(self.view.config["window_size"]["labeling_bar"]["width"])
        
        self.labeling_bar_scroll.setMinimumHeight(self.view.config["window_size"]["labeling_bar"]["height"]) 
        self.labeling_bar_scroll.setMaximumHeight(583)     
        #self.labeling_bar_scroll.setMaximumWidth(self.view.config["window_size"]["labeling_bar"]["width"])
        labeling_bar_layout.setContentsMargins(0,0,0,0)
        #self.labeling_bar_scroll.setMaximumHeight(self.view.config["window_size"]["label_bar"]["height"])    

        #self.labeling_bar_container.setContentsMargins(0,0,0,self.view.config["window_size"]["margin"]) 
        #self.labeling_bar_scroll.setSpacing(self.view.config["window_size"]["margin"])
        self.labeling_bar_scroll.setWidget(self.labeling_bar_container)
        
        labeling_bar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.view.main_layout.addWidget(self.labeling_bar_scroll, 0, 0, 1, 1)  
        
    
    def build_graphics_view(self):
        self.graphics_view_container = QWidget()
        self.graphics_view_layout = QStackedLayout(self.graphics_view_container)
        

        self.view.zoomable_graphics_view = ZoomableGraphicsView(self.view)
        self.view.zoomable_graphics_view.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.graphics_view_layout.addWidget(self.view.zoomable_graphics_view)  
        
        self.view.main_layout.addWidget(self.graphics_view_container, 0, 1, 3, 1)
        self.graphics_view_container.setMinimumWidth(self.view.config["window_size"]["graphics_view"]["width"])    
        
        #self.right_layout_container.setMinimumSize(self.view.right_panel_width, self.view.right_panel_height)
    
    def build_image_bar(self):
        self.image_bar_container_1 = QWidget()
        
        self.image_bar_container_1.setMinimumHeight(self.view.config["window_size"]["image_bar"]["height"])
        self.image_bar_container_1.setMaximumHeight(self.view.config["window_size"]["image_bar"]["height"])
        
        self.view.image_bar_layout_1 = QVBoxLayout(self.image_bar_container_1)

        self.image_bar_container_2 = QWidget()
        self.image_bar_container_2.setObjectName("image_bar")
        self.view.image_bar_layout_1.addWidget(self.image_bar_container_2)
        self.view.image_bar_layout_1.setContentsMargins(0,0,0,self.view.config["window_size"]["margin"])

        self.view.image_bar_layout_1.setAlignment(Qt.AlignmentFlag.AlignRight)        

        self.view.image_bar_layout_2 = QVBoxLayout(self.image_bar_container_2)
        
        self.image_bar_container_2.setMinimumWidth(self.view.config["window_size"]["image_bar"]["width"])
        self.image_bar_container_2.setMaximumWidth(self.view.config["window_size"]["image_bar"]["width"])

        for button in self.view.config["image_bar"]:
            button_name = button["name"]
            self.view.buttons_image_bar[button_name] = QPushButton()
            self.view.buttons_image_bar[button_name].setObjectName("permanent")
            self.view.buttons_image_bar[button_name].setToolTip(button["tooltip"])
            icon_path = Utils.get_icon_path(button["icon"])
            if os.path.exists(icon_path):
                self.view.buttons_image_bar[button_name].setIcon(QIcon(icon_path))
                self.view.buttons_image_bar[button_name].setIconSize(QSize(*self.view.config["window_size"]["icon"])) 
            self.view.buttons_image_bar[button_name].clicked.connect(getattr(self.view.controller, button["name"]))
            self.view.buttons_image_bar[button_name].setCheckable(button["checkable"])
            self.view.buttons_image_bar[button_name].setEnabled(False)
            self.view.image_bar_layout_2.addWidget(self.view.buttons_image_bar[button_name])

        self.view.image_bar_layout_2.setAlignment(Qt.AlignmentFlag.AlignRight)  
        self.view.image_bar_layout_1.setContentsMargins(0, 10, 0, 10)     
        self.view.main_layout.addWidget(self.image_bar_container_1, 2, 0, 1, 1)

    def build_label_bar(self):
        self.label_bar_container = QWidget()
        self.label_bar_scroll = QScrollArea()
        self.label_bar_container.setObjectName("label_bar")
        self.view.label_bar_layout = QHBoxLayout(self.label_bar_container)
        
        self.view.label_bar_layout.addWidget(QBlanckWidget1())

        for button in self.view.config["label_bar"]["permanent"]:
            button_name = button["name"]
            self.view.buttons_label_bar_permanent[button_name] = QPushButton()
            self.view.buttons_label_bar_permanent[button_name].setObjectName("permanent")
            self.view.buttons_label_bar_permanent[button_name].setToolTip(button["tooltip"])
            self.view.buttons_label_bar_permanent[button_name].setCheckable(button["checkable"])
            self.view.buttons_label_bar_permanent[button_name].setEnabled(False)

            icon_path = Utils.get_icon_path(button["icon"])
            if os.path.exists(icon_path):
                self.view.buttons_label_bar_permanent[button_name].setIcon(QIcon(icon_path))
                self.view.buttons_label_bar_permanent[button_name].setIconSize(QSize(*self.view.config["window_size"]["icon"])) 
            self.view.buttons_label_bar_permanent[button_name].clicked.connect(getattr(self.view.controller, button["name"]))
            self.view.label_bar_layout.addWidget(self.view.buttons_label_bar_permanent[button_name])
        
        self.view.label_bar_layout.setContentsMargins(0,0,0,0)
        self.view.label_bar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.label_bar_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_bar_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.label_bar_scroll.setWidgetResizable(True)
        self.label_bar_scroll.setWidget(self.label_bar_container)
        self.label_bar_scroll.setMaximumHeight(self.view.config["window_size"]["label_bar"]["height"])    
        #self.label_bar_container.setMaximumHeight(self.view.config["window_size"]["label_bar"]["height"]) 
    
        self.view.main_layout.addWidget(self.label_bar_scroll, 4, 0, 1, 4) 
        self.view.main_layout.setRowMinimumHeight(2, 100)
        

        

    def build_new_layer_label_bar(self, label_id, name, labeling_mode, color):
        
        push_buttons = dict() # Dictionnary of push buttons for this label 
        
        new_layer_label_bar_container = QWidget()
        new_layer_label_bar_container.setObjectName("label_bar_new")

        new_layer_label_bar_layout = QHBoxLayout(new_layer_label_bar_container)
        new_layer_label_bar_layout.setContentsMargins(0,0,0,0)
        new_layer_label_bar_layout.setSpacing(0)
        new_layer_label_bar_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        # Activation button
        push_buttons["activation"] = QPushButton(name)
        push_buttons["activation"].setObjectName('activation')
        push_buttons["activation"].setCheckable(True)
        push_buttons["activation"].setChecked(True)
        push_buttons["activation"].clicked.connect(lambda: self.view.controller.select_label(label_id))    
        new_layer_label_bar_layout.addWidget(push_buttons["activation"])
        separator = QSeparator1()
        self.view.label_bar_layout.addWidget(separator)

        # The others buttons
        for button in self.view.config["label_bar"]["layer"]:        
            type_name_button = button["name"]
            
            push_buttons[type_name_button] = QPushButton()
            push_buttons[type_name_button].setObjectName(button["name"])
            push_buttons[type_name_button].setToolTip(button["tooltip"])
            push_buttons[type_name_button].setCheckable(button["checkable"])
            
            if type_name_button != "color":
                icon_path = Utils.get_icon_path(button["icon"])
                if os.path.exists(icon_path):
                    push_buttons[type_name_button].setIcon(QIcon(icon_path))
                    push_buttons[type_name_button].setIconSize(QSize(*self.view.config["window_size"]["icon"])) 

            if type_name_button == "color":
                push_buttons[type_name_button].setStyleSheet(Utils.color_to_stylesheet(color))
                push_buttons[type_name_button].clicked.connect(lambda: self.view.controller.color(label_id))
            
            elif type_name_button == "visibility":
                push_buttons[type_name_button].setChecked(True)
                push_buttons[type_name_button].clicked.connect(lambda: self.view.controller.visibility(label_id))
            
            elif type_name_button == "label_setting":
                push_buttons[type_name_button].clicked.connect(lambda: self.view.controller.label_setting(label_id))

            elif type_name_button == "remove_label":
                push_buttons[type_name_button].clicked.connect(lambda: self.view.controller.remove_label(label_id))
        
            new_layer_label_bar_layout.addWidget(push_buttons[type_name_button])
        

        self.view.label_bar_layout.addWidget(new_layer_label_bar_container)

        self.view.buttons_label_bar_temporary[label_id] = push_buttons # Usefull to control all buttons :)
        self.view.container_label_bar_temporary[label_id] = (new_layer_label_bar_container, separator) # Usefull to delete these qwidget :) 
        
        