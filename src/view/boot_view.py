# import tkinter as tk

from model.boot_model import BootModel
from view.base_view import BaseView
from controller.boot_controller import BootController

class BootView(BaseView):
    def __init__(self, master):
        super().__init__(master)
        self.boot_model = BootModel()
        self.boot_controller = BootController()

        self.create_elements()

    def create_elements(self):
        # copyleft
            
        for item in self.boot_model.texts:
            print(item)
        # self.canvas = tk.self.Canvas()

    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

    def hide(self):
        self.grid_remove()

        