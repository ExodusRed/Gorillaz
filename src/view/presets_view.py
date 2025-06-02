import tkinter as tk

class PresetsView(tk.Frame):
    def __init__(self, master, controller, style): # style as arg.
        super().__init__(master)
        self.inputs = {}
        self.name1: str = ""
        self.name2: str = ""
        self.gravity: float = ""

        self.texts = []

        self.controller = controller
        self.style = style

        self.controller.on_presets_done(self.name1, self.name2, self.gravity)

        self["bg"]="orange"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.get_inputs()

    print("test")

    def focus_entry(self, element):
        # Todo: 
        # element.after(50, lambda: )
        # pass
        for i in range(10):
            print(i)

    def get_inputs(self):
        print("Getting Inputs...")
        # for item in self.inputs:
            # print(item)
            # Start animation for each item, but only as long as the input is made, 
            # So make label editable
            
            # Start Animation
            # Make Content editable
            # Set focus on Element
            
        self.focus_entry("T")


    def create_widgets(self):
        # Getting user Input // Presets for the game
        content_frame = tk.Frame(self, bg="red")
        input_frame = tk.Frame(content_frame, bg="cyan")

        content_frame.columnconfigure(0, weight=1)
        content_frame.rowconfigure(0, weight=1)

        # input_frame.columnconfigure(0, weight=1)
        # input_frame.rowconfigure(0, weight=1)

        # Instead of creating a input label for each input, maybe use the same label and just reset and reposition for each

        p1_lbl = tk.Label(input_frame, text="Name of Player 1 (Default = `Player 1`):", bg=self.style.bg, fg=self.style.fg, font=(self.style.font, self.style.font_size))
        # input_lbl = tk.Label(input_frame, text="_", bg=self.style.bg, fg=self.style.fg, font=(self.style.font, self.style.font_size))
        input_lbl = tk.Entry(input_frame)

        p2_lbl = tk.Label(input_frame, text="Name of Player 2 (Default = `Player 2`):", bg=self.style.bg, fg=self.style.fg, font=(self.style.font, self.style.font_size))

        total_points_lbl = tk.Label(input_frame, text="Play to how many total points (Default = 3)?", bg=self.style.bg, fg=self.style.fg, font=(self.style.font, self.style.font_size))
        gravity_lbl = tk.Label(input_frame, text="Gravity in Meters/Sec (Earth = 9.8)?", bg=self.style.bg, fg=self.style.fg, font=(self.style.font, self.style.font_size))

        # Print buffer Line after input has been made
        # --------------

        info_lbl = tk.Label(input_frame, text="--------------\nV = View Intro\nP = Play Game\n\nYour Choice?", bg=self.style.bg, fg=self.style.bg, font=(self.style.font, self.style.font_size))

        # Rendering
        content_frame.grid(sticky="nsew")
        input_frame.grid()

        p1_lbl.grid(row=0, column=0)
        input_lbl.grid(row=0, column=1)

        p2_lbl.grid(row=1, column=0)

        total_points_lbl.grid(row=2, column=0)
        gravity_lbl.grid(row=3, column=0)

        info_lbl.grid(row=4, column=0)





