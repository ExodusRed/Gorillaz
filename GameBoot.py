import tkinter as tk
import random
import math

WIDTH = 800
HEIGHT = 600

WIDTH = 640
HEIGHT = 350


BUILDING_COUNT = 10
BUILDING_WIDTH = WIDTH // BUILDING_COUNT
GRAVITY = 9.8
EXPLOSION_RADIUS = 30
MAX_LIVES = 3

class Player:
    def __init__(self, canvas, x, color, buildings, tag, life_label):
        self.canvas = canvas
        self.x = x
        self.color = color
        self.tag = tag
        self.lives = MAX_LIVES
        self.life_label = life_label
        self.y = self.find_rooftop_y(buildings)
        self.oval = self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20,
                                            fill=self.color, tags=self.tag)
        self.update_life_label()

    def find_rooftop_y(self, buildings):
        player_center_x = self.x + 10
        for b in buildings:
            if b.x <= player_center_x <= b.x + b.width:
                return b.get_rooftop_y() - 20
        return HEIGHT - 40

    def is_hit(self, px, py):
        coords = self.canvas.coords(self.oval)
        if coords:
            x1, y1, x2, y2 = coords
            return x1 <= px <= x2 and y1 <= py <= y2
        return False

    def lose_life(self):
        self.lives -= 1
        self.update_life_label()
        return self.lives

    def update_life_label(self):
        hearts = "❤️" * self.lives + "💀" * (MAX_LIVES - self.lives)
        self.life_label.config(text=hearts)

    def remove(self):
        self.canvas.delete(self.oval)
        self.life_label.config(text="💀")

class Building:
    def __init__(self, canvas, x, width, height):
        self.canvas = canvas
        self.x = x
        self.width = width
        self.height = height
        self.y = HEIGHT - height
        self.pixels = set()
        self.window_map = {}

        for i in range(self.x, self.x + self.width):
            for j in range(self.y, HEIGHT):
                self.pixels.add((i, j))

        for row in range(self.y + 5, HEIGHT - 10, 15):
            for col in range(self.x + 3, self.x + self.width - 8, 12):
                if (col, row) in self.pixels:
                    self.window_map[(col, row)] = random.choice(["on", "off"])

        self.render()

    def render(self):
        self.canvas.delete(f"building_{self.x}")
        for (i, j) in self.pixels:
            self.canvas.create_rectangle(i, j, i + 1, j + 1,
                                         fill="gray", outline="", tags=f"building_{self.x}")

        for (wx, wy), state in self.window_map.items():
            if all((wx + dx, wy + dy) in self.pixels for dx in range(6) for dy in range(8)):
                color = "yellow" if state == "on" else "black"
                self.canvas.create_rectangle(wx, wy, wx + 6, wy + 8,
                                             fill=color, outline="", tags=f"building_{self.x}")

    def check_collision(self, x, y):
        return (int(x), int(y)) in self.pixels

    def explode(self, cx, cy):
        self.pixels = {p for p in self.pixels if math.hypot(p[0] - cx, p[1] - cy) > EXPLOSION_RADIUS}
        to_remove = [pos for pos in self.window_map
                     if any(math.hypot(pos[0] + dx - cx, pos[1] + dy - cy) <= EXPLOSION_RADIUS
                            for dx in range(6) for dy in range(8))]
        for key in to_remove:
            del self.window_map[key]
        self.render()

    def get_rooftop_y(self):
        return self.y

class Projectile:
    def __init__(self, game, canvas, x, y, angle, speed, buildings, direction):
        self.game = game
        self.canvas = canvas
        self.x = x
        self.y = y
        self.angle = math.radians(angle)
        self.speed = speed
        self.time = 0
        self.buildings = buildings
        self.direction = direction
        self.dot = self.canvas.create_oval(x, y, x + 5, y + 5, fill="red", tags="projectile")
        self.animate()

    def animate(self):
        self.time += 0.2
        dx = self.direction * self.speed * math.cos(self.angle)
        dy = -self.speed * math.sin(self.angle) + GRAVITY * self.time
        self.x += dx * 0.2
        self.y += dy * 0.2
        self.canvas.move(self.dot, dx * 0.2, dy * 0.2)

        opponent = self.game.player2 if self.game.current_player == 1 else self.game.player1
        if opponent.is_hit(self.x, self.y):
            self.canvas.delete(self.dot)
            lives_left = opponent.lose_life()
            if lives_left <= 0:
                opponent.remove()
                self.game.end_game(winner=self.game.current_player)
            else:
                self.game.switch_turn()
            return

        for building in self.buildings:
            if building.check_collision(self.x, self.y):
                building.explode(self.x, self.y)
                self.canvas.delete(self.dot)
                self.game.switch_turn()
                return

        if 0 < self.x < WIDTH and 0 < self.y < HEIGHT:
            self.canvas.after(30, self.animate)
        else:
            self.canvas.delete(self.dot)
            self.game.switch_turn()

class GorillaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Gorillas mit Leben und Anzeige")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="skyblue")
        self.canvas.pack()
        self.buildings = self.generate_buildings()

        self.status_frame = tk.Frame(self.root)
        self.status_frame.pack()

        tk.Label(self.status_frame, text="Spieler 1:").grid(row=0, column=0)
        self.life_label_1 = tk.Label(self.status_frame, text="")
        self.life_label_1.grid(row=0, column=1)

        tk.Label(self.status_frame, text="Spieler 2:").grid(row=0, column=2)
        self.life_label_2 = tk.Label(self.status_frame, text="")
        self.life_label_2.grid(row=0, column=3)

        self.player1 = Player(self.canvas, 40, "orange", self.buildings, tag="p1", life_label=self.life_label_1)
        self.player2 = Player(self.canvas, WIDTH - 60, "blue", self.buildings, tag="p2", life_label=self.life_label_2)
        self.current_player = 1

        self.create_controls()

    def generate_buildings(self):
        return [Building(self.canvas, i * BUILDING_WIDTH, BUILDING_WIDTH,
                         random.randint(100, 400)) for i in range(BUILDING_COUNT)]

    def create_controls(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        self.info_label = tk.Label(control_frame, text="Spieler 1 ist am Zug")
        self.info_label.grid(row=0, column=0, columnspan=5)

        tk.Label(control_frame, text="Angle:").grid(row=1, column=0)
        self.angle_entry = tk.Entry(control_frame, width=5)
        self.angle_entry.grid(row=1, column=1)

        tk.Label(control_frame, text="Speed:").grid(row=1, column=2)
        self.speed_entry = tk.Entry(control_frame, width=5)
        self.speed_entry.grid(row=1, column=3)

        self.shoot_button = tk.Button(control_frame, text="Shoot", command=self.shoot)
        self.shoot_button.grid(row=1, column=4)

    def shoot(self):
        try:
            angle = float(self.angle_entry.get())
            speed = float(self.speed_entry.get())
            player = self.player1 if self.current_player == 1 else self.player2
            direction = 1 if self.current_player == 1 else -1
            Projectile(self, self.canvas, player.x + 10, player.y, angle, speed, self.buildings, direction)
            self.shoot_button.config(state="disabled")
        except ValueError:
            print("Ungültiger Eingabewert")

    def switch_turn(self):
        self.current_player = 2 if self.current_player == 1 else 1
        self.info_label.config(text=f"Spieler {self.current_player} ist am Zug")
        self.shoot_button.config(state="normal")
        self.angle_entry.delete(0, tk.END)
        self.speed_entry.delete(0, tk.END)

    def end_game(self, winner):
        self.info_label.config(text=f"Spieler {winner} hat gewonnen!")
        self.shoot_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = GorillaGame(root)
    root.mainloop()
