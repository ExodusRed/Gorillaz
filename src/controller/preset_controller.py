class PresetController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # active_binds = {}

        self.current_input = ""

        self.current_question_index = 0

        self.view.focus()
        self.view.bind("<Key>", lambda e: self.on_key_press(event = e))
        # self.view.bind("<Delete>", lambda e: self.on_key_press(event = e))

    def on_key_press(self, event):
        print(event.keysym)
        if event.keysym == "Return":
            self.current_question_index += 1
        elif event.keysym == "BackSpace":
            self.view.delete_from_input()
        elif event.keysym == "Shift_L" or event.keysym == "Shift_R":
            pass
        elif event.char.isprintable():
            # self.current_input += 
            # self.current_input += event.char
            # self.view.update_prompt_and_input(self.current_input, self.current_question_index)
            # self.view.update_prompt_and_input(event.char, self.current_question_index)
            # self.view.update_prompt_and_input(event.char, self.current_question_index)
            print(event.char)
            self.view.update_input(event.char)

        
