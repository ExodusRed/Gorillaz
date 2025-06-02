import tkinter as tk

class Style():
    def __init__(self, bg, fg, font, font_size):
        self.bg = bg
        self.fg = fg
        self.font = font
        self.font_size = font_size
        self.title_font_size = int(font_size*1.2)

        

        self.title_font_size = 18

        # print(self.font_size, self.title_font_size)

class BootView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        self["bg"] = "red"


        # Test
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        # self.config(bg="grey")

        self.mission_text = """Your mission is to hit your opponent with the exploding 
        banana by varying the angle and pwoer of your throw, taking
        into account wind speed, gravity, and the city skyline.
        The wind speed is shown by a directional arrow at the bottom of the playing field, 
        its length relative to its strength."""

        # TEMP
        # style = Style("black", "white", "Fixedsys", 16)
        self.style = Style("black", "white", "Terminal", 17)

        self.create_widgets(self.style)

        # Binding keys
        self.bind("<Configure>", self.on_configure)
        self.bind("<Key>", self.on_continue)
        # master.bind("<Key>", self.on_continue)
        # self.bind("<Button-1>", self.on_continue)
        # self.bind("<Key>", lambda e: print("key pressed..."))
        # self.focus_set() # Need focus to register events

        # self.bind("<Return>", self.on_ret)

        print("Should be binded")

        # self.focus_set()


        # TEMP
        # self.style = Style("black", "white", "Terminal", 17)

    def on_ret(self, event):
        print("Return.")

    def ps(self, x, y):
        self.update()
        print("After Delay:")
        print(x, y)

    def get_frame_size(self):
        # self.after(100, )
        pass

    # def wait_for_size(self, delay=10):
    #     width, height = self.winfo_width(), self.winfo_height()
    #     if width > 1 and height > 1:
    #         # callback((width, height))
    #         return (width, height)
    #     else:
    #         self.after(delay, lambda: self.wait_for_size(callback, delay))


    def wait_for_size(self, delay=10):
        loaded = False
        while (not loaded):
            width, height = self.winfo_width(), self.winfo_height()
            if (width > 1 and height > 1):
                loaded = True
                return (width, height)
            else:
                self.after_idle(delay)

    def animate(self, width, height):
        print("Animating...")

    def start_animation(self, width, height, style):
        # Drawing starts
        self.update()
        print("On Anim:")
        print("Loading...") # Starts actually earlier / Temp
        print(width, height)
        # print(self.winfo_screenheight(), self.winfo_height())
        # self.after(100, lambda: self.ps(self.winfo_width(), self.winfo_height()))
        # w, h = self.wait_for_size()
        for item in range (12):
            star = tk.Label(self, text="*", bg=style.bg, fg="red", font=(style.font, int(style.font_size * 1.6)), padx=0, pady=0, bd=0)
            star.place(x=(width - (width * item)), y=0, width=10, height=10)

    def on_configure(self, event):
        print("On Config")
        if (event.width > 1 and event.height > 1):
            self.unbind("<Congfigure>")
            # self.animate(event.width, event.height)
            self.start_animation(event.width, event.height, self.style)

                            

    def create_widgets(self, style):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.content_frame = tk.Frame(self, bg="violet")
        self.text_frame = tk.Frame(self.content_frame, bg="purple")

        self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)

        self.config(bg="green")

        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=1)


        self.title_label = tk.Label(self.text_frame, text="Python GORILLAS", bg=style.bg, fg=style.fg, font=(style.font, style.title_font_size))
        self.legal_notice = tk.Label(self.text_frame, text="Copyleft (\u2183)", bg=style.bg, fg=style.fg, font=(style.font, style.font_size))
        self.mission_notice = tk.Label(self.text_frame, text=self.mission_text, bg=style.bg, fg=style.fg, font=(style.font, style.font_size))

        self.prompt_label = tk.Label(self, text="<Press any key to continue>", bg=style.bg, fg=style.fg, font=(style.font, style.font_size))

        self.content_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.text_frame.grid(row=0, column=0, padx=10, pady=10)

        self.title_label.grid(row=0, column=0, pady=2)
        self.legal_notice.grid(row=1, column=0, pady=2)
        self.mission_notice.grid(row=2, column=0)

        self.prompt_label.grid(row=1, column=0, pady=(0, 80))


        # dev
        # self.start_animation(style)
        

    def on_continue(self, event):
        # self.controller.start_presets()
        print("Continue...")
        self.controller.view_controller.show_view("presets_view")



