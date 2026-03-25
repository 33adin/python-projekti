import tkinter as tk
import random

# default difficulty
AI_SPEED = 3
AI_ERROR = 35

root = tk.Tk()
root.title("Ping Pong AI")

WIDTH, HEIGHT = 600, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# loptica
ball = canvas.create_oval(290, 190, 310, 210, fill="white")
ball_dx = 4
ball_dy = 3

# palice
paddle_player = canvas.create_rectangle(20, 160, 30, 240, fill="blue")
paddle_ai = canvas.create_rectangle(570, 160, 580, 240, fill="red")

# score
score_player = 0
score_ai = 0
score_text = canvas.create_text(
    WIDTH//2, 20,
    fill="white",
    font=("Arial", 16),
    text="0 : 0"
)

# difficulty info
difficulty_text = canvas.create_text(
    WIDTH//2, 40,
    fill="gray",
    font=("Arial", 10),
    text="Difficulty: MEDIUM | 1=Easy 2=Medium 3=Hard"
)

player_speed = 0

# -----------------------
def show_message(text):
    msg = canvas.create_text(
        WIDTH//2,
        HEIGHT//2,
        text=text,
        fill="yellow",
        font=("Arial", 26, "bold")
    )
    root.after(1000, lambda: canvas.delete(msg))

# -----------------------
def set_easy(event=None):
    global AI_SPEED, AI_ERROR
    AI_SPEED = 2
    AI_ERROR = 60
    canvas.itemconfig(difficulty_text,
        text="Difficulty: EASY | 1=Easy 2=Medium 3=Hard")
    show_message("EASY")

def set_medium(event=None):
    global AI_SPEED, AI_ERROR
    AI_SPEED = 3
    AI_ERROR = 35
    canvas.itemconfig(difficulty_text,
        text="Difficulty: MEDIUM | 1=Easy 2=Medium 3=Hard")
    show_message("MEDIUM")

def set_hard(event=None):
    global AI_SPEED, AI_ERROR
    AI_SPEED = 5
    AI_ERROR = 10
    canvas.itemconfig(difficulty_text,
        text="Difficulty: HARD | 1=Easy 2=Medium 3=Hard")
    show_message("HARD")

# -----------------------
def set_speed(val):
    global player_speed
    player_speed = val

canvas.focus_set()

canvas.bind("<KeyPress-w>", lambda e: set_speed(-6))
canvas.bind("<KeyPress-s>", lambda e: set_speed(6))
canvas.bind("<KeyRelease-w>", lambda e: set_speed(0))
canvas.bind("<KeyRelease-s>", lambda e: set_speed(0))

canvas.bind("<KeyPress-W>", lambda e: set_speed(-6))
canvas.bind("<KeyPress-S>", lambda e: set_speed(6))
canvas.bind("<KeyRelease-W>", lambda e: set_speed(0))
canvas.bind("<KeyRelease-S>", lambda e: set_speed(0))

canvas.bind("1", set_easy)
canvas.bind("2", set_medium)
canvas.bind("3", set_hard)

# -----------------------
def move_player():
    canvas.move(paddle_player, 0, player_speed)
    pos = canvas.coords(paddle_player)

    if pos[1] < 0:
        canvas.move(paddle_player, 0, -pos[1])
    if pos[3] > HEIGHT:
        canvas.move(paddle_player, 0, HEIGHT - pos[3])

# -----------------------
def move_ai():
    bx1, by1, bx2, by2 = canvas.coords(ball)
    px1, py1, px2, py2 = canvas.coords(paddle_ai)

    ball_center = (by1 + by2) / 2
    paddle_center = (py1 + py2) / 2

    # prati samo kad loptica ide prema AI
    if ball_dx > 0:
        error = random.randint(-AI_ERROR, AI_ERROR)
        target = ball_center + error

        diff = target - paddle_center

        # smoothing
        move = diff * 0.15

        # limit brzine
        if move > AI_SPEED:
            move = AI_SPEED
        if move < -AI_SPEED:
            move = -AI_SPEED

        # deadzone
        if abs(diff) > 3:
            canvas.move(paddle_ai, 0, move)

    pos = canvas.coords(paddle_ai)

    if pos[1] < 0:
        canvas.move(paddle_ai, 0, -pos[1])
    if pos[3] > HEIGHT:
        canvas.move(paddle_ai, 0, HEIGHT - pos[3])

# -----------------------
def update_ball():
    global ball_dx, ball_dy, score_player, score_ai

    canvas.move(ball, ball_dx, ball_dy)
    bx1, by1, bx2, by2 = canvas.coords(ball)

    # zidovi
    if by1 <= 0 or by2 >= HEIGHT:
        ball_dy *= -1

    # player collision (FIXED)
    px1, py1, px2, py2 = canvas.coords(paddle_player)
    if bx1 <= px2 and py1 < by2 and py2 > by1:
        ball_dx = abs(ball_dx)
        canvas.move(ball, 8, 0)

    # AI collision (FIXED)
    ax1, ay1, ax2, ay2 = canvas.coords(paddle_ai)
    if bx2 >= ax1 and ay1 < by2 and ay2 > by1:
        ball_dx = -abs(ball_dx)
        canvas.move(ball, -8, 0)

    # score
    if bx1 <= 0:
        score_ai += 1
        canvas.coords(ball, 290, 190, 310, 210)
        ball_dx = 4

    if bx2 >= WIDTH:
        score_player += 1
        canvas.coords(ball, 290, 190, 310, 210)
        ball_dx = -4

    canvas.itemconfig(score_text, text=f"{score_player} : {score_ai}")

    move_player()
    move_ai()

    root.after(20, update_ball)

update_ball()
root.mainloop()
