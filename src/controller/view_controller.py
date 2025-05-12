class ViewController:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.views = {}
        self.view_classes = {}

    def register_view(self, name: str, view_class, eager: bool = True):
        view = view_class(master=self.root, controller=self.controller)
        # view.grid(row=0, column=0, sticky="nsew")
        # self.views[view_name] = view

        self.view_classes[name] = view_class

        if eager:
            view = view_class(master=self.root, controller=self.controller)
            view.grid(row=0, column=0, sticky="nsew")
            self.views[name] = view

    def show_view(self, name: str, **kwargs):
        if name not in self.views:
            # Lazy-loading the view if it hasn't been instantiated yet
            view_class = self.view_classes[name]
            view = view_class(master=self.root, controller=self.controller, **kwargs)
            # self.config(bg="pruple")
            view.grid(row=0, column=0, sticky="nsew")
            self.views[name] = view
        else:
            view = self.views[name]
            if hasattr(view, "on_show"):
                view.on_show(**kwargs)

        # self.root.config(bg="purple")
        
        view.focus_set() # Set focus for event binding
        self.views[name].tkraise()