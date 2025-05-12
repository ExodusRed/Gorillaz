import tkinter as tk

from controller.main_controller import MainController


def main():
    root = tk.Tk()

    # Root Configuration
    root.title("Gorillas")
    # root.geometry("800x600")
    # root.geometry("640x480")
    root.geometry("1280x960")

    
    

    # root.configure(bg="#000000")

    # Main Controller
    main_controller = MainController(root)

    root.mainloop()



if __name__ == "__main__":
    main()