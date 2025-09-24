from PyImageLabeling.controller.Events import Events


class ImageEvents(Events):
    def __init__(self):
        super().__init__()

    def zoom_plus(self):
        self.desactivate_buttons_labeling_image_bar(self.zoom_plus.__name__)
        self.all_events(self.zoom_plus.__name__)
        self.view.zoomable_graphics_view.change_cursor("zoom_plus")
        self.model.zoom_plus()
        
    def zoom_minus(self):
        self.desactivate_buttons_labeling_image_bar(self.zoom_minus.__name__)
        self.all_events(self.zoom_minus.__name__)
        self.view.zoomable_graphics_view.change_cursor("zoom_minus")
        self.model.zoom_minus()

    def move_image(self):
        self.desactivate_buttons_labeling_image_bar(self.move_image.__name__)
        self.all_events(self.move_image.__name__)
        self.view.zoomable_graphics_view.change_cursor("move")
        self.model.move_image()
        
    def reset_move_zoom_image(self):
        self.all_events(self.reset_move_zoom_image.__name__)
        self.model.reset_move_zoom_image()



        
