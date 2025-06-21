import textwrap

class BootModel:
    def __init__(self):
        self.texts = {
            "title": "Python GORILLAS",
            "legal_notice": "Copyleft (\u2183)",
            "mission_objective": textwrap.dedent("""
                    Your mission is to hit your opponent with the exploding 
                    banana by varying the angle and power of your throw, taking
                    into account wind speed, gravity, and the city skyline.
                    The wind speed is shown by a directional arrow at the bottom 
                    of the playing field, its length relative to its strength.
                """).strip(),
            "prompt": "<Press any key to continue>"
        }

