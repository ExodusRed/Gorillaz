class BootController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # active_binds = {}

        self.view.focus()
        # self.view.bind("<Key>", lambda e: print(e.keysym))
        self.view.bind("<Key>", lambda e: self.view.master.view_controller.show_view("preset"))
