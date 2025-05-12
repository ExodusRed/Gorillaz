import tkinter as tk

class Style():
    def __init__(self, bg, fg, font, font_size):
        self.bg = bg
        self.fg = fg
        self.font = font
        self.font_size = font_size
        self.title_font_size = int(font_size*1.2)

        self.title_font_size = 18

        print(self.font_size, self.title_font_size)

class BootView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)


        # Test
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        self.config(bg="blue")


        self.mission_text = """Your mission is to hit your opponent with the exploding 
        banana by varying the angle and pwoer of your throw, taking
        into account wind speed, gravity, and the city skyline.
        The wind speed is shown by a directional arrow at the bottom of the playing field, 
        its length relative to its strength."""

        # TEMP
        # style = Style("black", "white", "Fixedsys", 16)
        style = Style("black", "white", "Terminal", 17)

        self.create_widgets(style)

        # Binding keys
        self.bind("<Key>", self.on_continue)
        self.focus_set() # Need focus to register events
                            

    def create_widgets(self, style):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.text_frame = tk.Frame(self, bg="purple")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.title_label = tk.Label(self.text_frame, text="Python GORILLAS", bg=style.bg, fg=style.fg, font=(style.font, style.title_font_size))
        self.legal_notice = tk.Label(self.text_frame, text="Copyleft (\u2183)", bg=style.bg, fg=style.fg, font=(style.font, style.font_size))
        self.mission_notice = tk.Label(self.text_frame, text=self.mission_text, bg=style.bg, fg=style.fg, font=(style.font, style.font_size))

        self.text_frame.grid(row=0, column=0)
        self.title_label.grid(row=0, column=0, pady=2)
        self.legal_notice.grid(row=1, column=0, pady=2)
        self.mission_notice.grid(row=2, column=0)

    def on_continue(self, event):
        self.controller.start_presets()



