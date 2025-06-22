import tkinter as tk

from view.base_view import BaseView

class PresetView(BaseView):
    def __init__(self, master, scalar):
        super().__init__(master)
        print("Welcome to PresetView!")