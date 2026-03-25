import tkinter as tk

# Glavni prozor
root = tk.Tk()
root.title("Ping-Pong igra - AI protivnik")

WIDTH, HEIGHT = 500, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Loptica
ball = canvas.create_oval(240, 190, 260, 210, fill="white")
ball_dx, ball_dy = 3, 3

# Palice
paddle_width, paddle_height = 10, 80
paddle_player = canvas.create_rectangle(20, 160, 30, 240, fill="blue")
paddle_ai = canvas.create_rectangle(470, 160, 480, 240, fill="red")

# Bodovi
score_player = 0
score_ai = 0
score_text = canvas.create_text(250, 20, fill="white", font=("Arial", 16), text="0 : 0")

# Kontrola palice igrača
player_speed = 0

def move_player():
    global player_speed
    canvas.move(paddle_player, 0, player_speed)
    pos = canvas.coords(paddle_player)
    if pos[1] < 0:
        canvas.move(paddle_player, 0, -pos[1])
    elif pos[3] > HEIGHT:
        canvas.move(paddle_player, 0, HEIGHT - pos[3])

def move_ai():
    bx, by, bx2, by2 = canvas.coords(ball)
    px, py, px2, py2 = canvas.coords(paddle_ai)
    # AI prati centar loptice
    center_ball = (by + by2) / 2
    center_paddle = (py + py2) / 2
    if center_ball > center_paddle:
        canvas.move(paddle_ai, 0, min(3, center_ball - center_paddle))
    elif center_ball < center_paddle:
        canvas.move(paddle_ai, 0, -min(3, center_paddle - center_ball))
    # Ograničenje
    pos = canvas.coords(paddle_ai)
    if pos[1] < 0:
        canvas.move(paddle_ai, 0, -pos[1])
    elif pos[3] > HEIGHT:
        canvas.move(paddle_ai, 0, HEIGHT - pos[3])

def update_ball():
    global ball_dx, ball_dy, score_player, score_ai
    canvas.move(ball, ball_dx, ball_dy)
    bx, by, bx2, by2 = canvas.coords(ball)

    # Sudari sa zidovima
    if by <= 0 or by2 >= HEIGHT:
        ball_dy *= -1

    # Sudari sa palicama
    if bx <= canvas.coords(paddle_player)[2] and canvas.coords(paddle_player)[1] < by2 and canvas.coords(paddle_player)[3] > by:
        ball_dx *= -1
    if bx2 >= canvas.coords(paddle_ai)[0] and canvas.coords(paddle_ai)[1] < by2 and canvas.coords(paddle_ai)[3] > by:
        ball_dx *= -1

    # Bodovi
    if bx <= 0:
        score_ai += 1
        canvas.coords(ball, 240, 190, 260, 210)
        ball_dx = 3
    if bx2 >= WIDTH:
        score_player += 1
        canvas.coords(ball, 240, 190, 260, 210)
        ball_dx = -3

    canvas.itemconfig(score_text, text=f"{score_player} : {score_ai}")
    move_player()
    move_ai()
    root.after(20, update_ball)

# Kontrole igrača
def key_press(event):
    global player_speed
    if event.keysym == "w":
        player_speed = -5
    elif event.keysym == "s":
        player_speed = 5

def key_release(event):
    global player_speed
    if event.keysym in ["w", "s"]:
        player_speed = 0

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

update_ball()
root.mainloop()
