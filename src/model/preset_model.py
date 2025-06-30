class PresetModel:
    def __init__(self):
        self.QUESTIONS = {
            "q0": "Name of Player 1 (Default = 'Player 1'): ",
            "q1": "Name of Player 2 (Default = 'Player 2'): ",
            "q2": "Play to how many total points (Default = 3)? ",
            "q3": "Gravity in Meters/Sec (Earth = 9.8)? ",
            "q4": "--------------\n\nV = View Intro\nP = Playe Game\n\nYour Choice?"
        }

        self.answers = {}
