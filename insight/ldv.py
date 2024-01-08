import tkinter as tk
from PIL import Image, ImageTk


def is_intersect(segment, rect):
    # Thank you ChatGPT
    (x1, y1), (x2, y2) = segment
    (rx1, ry1), (rx2, ry2) = rect
    if y1 == y2:
        if not (ry1 <= y1 <= ry2):
            return False
        return (rx1 <= x1 <= rx2 or rx1 <= x2 <= rx2 or (x1 <= rx1 and x2 >= rx2))
    if x1 == x2:
        if not (rx1 <= x1 <= rx2):
            return False
        return (ry1 <= y1 <= ry2 or ry1 <= y2 <= ry2 or (y1 <= ry1 and y2 >= ry2))
    if (x1 < rx1 and x2 < rx1) or (y1 < ry1 and y2 < ry1) or (x1 > rx2 and x2 > rx2) or (y1 > ry2 and y2 > ry2):
        return False
    m = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
    c = y1 - m * x1
    def intersect_x(y):
        return (y - c) / m if m != 0 else x1
    def intersect_y(x):
        return m * x + c if m != float('inf') else y1
    sides = [(rx1, intersect_y(rx1)), (rx2, intersect_y(rx2)), (intersect_x(ry1), ry1), (intersect_x(ry2), ry2)]
    for (ix, iy) in sides:
        if rx1 <= ix <= rx2 and ry1 <= iy <= ry2 and min(x1, x2) <= ix <= max(x1, x2) and min(y1, y2) <= iy <= max(y1, y2):
            return True
    return False


class GridApp:
    def __init__(self, root):
        self.root = root
        root.title("Insight calculator")
        self.create_grid()
        self.create_buttons()
        self.mode = "paint"  # Default mode
        self.player_row, self.player_col = 0, 0
        self.update_player_position()

    def create_grid(self):
        self.cells = {}
        for row in range(10):
            for col in range(10):
                frame = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
                frame.grid(row=row, column=col)
                label = tk.Label(master=frame, text=" ", width=4, height=2, bg="white")
                label.pack()
                label.bind("<Button-1>", self.handle_click)
                self.cells[label] = (row, col)

    def create_buttons(self):
        side_panel = tk.Frame(self.root)
        side_panel.grid(row=0, column=11, rowspan=10)
        paint_icon = Image.open("paint.png").resize((20, 20))
        move_icon = Image.open("move.png").resize((20, 20))
        calculate_icon = Image.open("calculate.png").resize((20, 20))
        paint_icon = ImageTk.PhotoImage(paint_icon)
        move_icon = ImageTk.PhotoImage(move_icon)
        calculate_icon = ImageTk.PhotoImage(calculate_icon)
        paint_button = tk.Button(side_panel, image=paint_icon, command=lambda: self.set_mode("paint"))
        paint_button.image = paint_icon
        paint_button.pack()
        move_button = tk.Button(side_panel, image=move_icon, command=lambda: self.set_mode("move"))
        move_button.image = move_icon
        move_button.pack()
        calculate_button = tk.Button(side_panel, image=calculate_icon, command=self.calculate_visibility)
        calculate_button.image = calculate_icon
        calculate_button.pack()

    def set_mode(self, mode):
        self.mode = mode

    def handle_click(self, event):
        label = event.widget
        row, col = self.cells[label]

        if self.mode == "paint" and (row, col) != (self.player_row, self.player_col):
            current_color = label.cget("bg")
            if current_color != "grey":
                label.config(bg="grey")
            else:
                label.config(bg="white")
        elif self.mode == "move":
            if label.cget("bg") != "grey":
                self.player_row, self.player_col = row, col
                self.update_player_position()

    def update_player_position(self):
        for label, (row, col) in self.cells.items():
            if label.cget("text") == "P":
                label.config(text=" ")
        for label, (row, col) in self.cells.items():
            if row == self.player_row and col == self.player_col:
                label.config(text="P")

    def calculate_visibility(self):
        obstacles = []
        for label, (row, col) in self.cells.items():
            if label.cget("bg") == "grey":
                rect = [[col + 0.001, row + 0.001], [col + 1 - 0.001, row + 1 - 0.001]]
                obstacles.append(rect)

        player_center = (self.player_col + 0.5, self.player_row + 0.5)
        for label, (row, col) in self.cells.items():
            if label.cget("bg") != "grey":
                cell_center = (col + 0.5, row + 0.5)
                segment = [player_center, cell_center]
                intersect = any(is_intersect(segment, rect) for rect in obstacles)
                if intersect:
                    label.config(bg="#faa0af")
                else:
                    label.config(bg="#d7ffc7")

if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()
