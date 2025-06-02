import tkinter as tk
from controller.main_controller import MainController

def center_window(root):
    root.withdraw()
    root.update()
    width, height = root.winfo_width(), root.winfo_height()
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2 ) - (height // 2)

    root.geometry(f"+{x}+{y}")

    root.deiconify()

def main():
    root = tk.Tk()

    # Root Configuration
    root.title("Gorillas")

    # root.geometry("800x600")
    # root.geometry("640x480")
    # root.geometry("1280x960")
    root.geometry("1600x900")



    center_window(root)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.bind("<Escape>", lambda e: root.quit())

    # root.configure(bg="#000000")

    # Main Controller
    main_controller = MainController(root)

    root.mainloop()



if __name__ == "__main__":
    main()