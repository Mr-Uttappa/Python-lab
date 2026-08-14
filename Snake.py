import tkinter as tk
import random

# Game settings
WIDTH = 400
HEIGHT = 400
SEG_SIZE = 20
UPDATE_DELAY = 100  # milliseconds

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game 🐍")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(SEG_SIZE*5, SEG_SIZE*5)]
        self.direction = "Right"
        self.food = self.create_food()

        self.root.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def create_food(self):
        x = random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
        y = random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
        return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Up","Down","Left","Right"]:
            self.direction = event.keysym

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= SEG_SIZE
        elif self.direction == "Down":
            head_y += SEG_SIZE
        elif self.direction == "Left":
            head_x -= SEG_SIZE
        elif self.direction == "Right":
            head_x += SEG_SIZE

        new_head = (head_x, head_y)

        # Check collisions
        if (head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in self.snake):
            self.game_over()
            return False

        self.snake.insert(0, new_head)

        # Check food
        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop()

        return True

    def draw_elements(self):
        self.canvas.delete("all")
        # Draw snake
        for (x, y) in self.snake:
            self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="lime", outline="black")
        # Draw food
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+SEG_SIZE, fy+SEG_SIZE, fill="red")

    def update_game(self):
        if self.move_snake():
            self.draw_elements()
            self.root.after(UPDATE_DELAY, self.update_game)

    def game_over(self):
        self.canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 24, "bold"))

# Run game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()


