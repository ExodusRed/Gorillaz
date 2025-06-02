from style import Style

class ViewController:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.views = {}
        self.view_classes = {}

        # self.style = Style()
        self.style = Style("black", "white", "Terminal", 18)


    def register_view(self, name: str, view_class, eager: bool = True):
        view = view_class(master=self.root, controller=self.controller, style=self.style)
        # view.grid(row=0, column=0, sticky="nsew")
        # self.views[view_name] = view

        self.view_classes[name] = view_class

        if eager:
            view = view_class(master=self.root, controller=self.controller, style=self.style)
            view.grid(row=0, column=0, sticky="nsew")
            self.views[name] = view

        # view.config(takefocus=1, bg="red") // Has got nothing to do here // keep for later, use below

    def show_view(self, name: str, **kwargs):

        # Unbind from previous frames?

        if name not in self.views:
            # Lazy-loading the view if it hasn't been instantiated yet
            view_class = self.view_classes[name]
            view = view_class(master=self.root, controller=self.controller, style=self.style, **kwargs)
            view.config(bg="blue") # Is overwritten?
            view.columnconfigure(0, weight=1)
            view.rowconfigure(0, weight=1)
            view.grid(row=0, column=0, sticky="nsew")
            self.views[name] = view
        else:
            view = self.views[name]
            if hasattr(view, "on_show"):
                view.on_show(**kwargs) # pass args for its init


        self.views[name].tkraise()