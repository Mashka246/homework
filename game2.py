import tkinter
import random 

def prepare_and_start():
    global player, target, enemy, label
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_oval(player_pos[0], player_pos[1], player_pos[0] + step, player_pos[1] + step, fill='blue')

    target_pos = (random.randint(1, N_X - 1), * step, random.randint(1, N_Y - 1) * step)
    target = canvas.create_oval(target_pos[0], target_pos[1], target_pos[0] + step, target_pos[1] + step, fill='white')

    enemy_pos = (random.randint(1, N_X -1) * step, random.randint(1, N_Y - 1) * step)
    enemy = canvas.create_rectangle(enemy_pos[0], enemy_pos[1], enemy_pos[0] + step, enemy_pos[1] + step, fill='red')

    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)

def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    if xy[0] <= 0: canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH: canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0: canvas.move(obj, 0, HEIGHT)
    if xy[1] >= HEIGHT: canvas.move(obj, 0, -HEIGHT)

def move_enemy():
    directions = [(0, -step), (0, step), (-step, 0), (step, 0)]
    move_x, move_y = random.choice(directions)
    move_wrap(enemy, move_x, move_y)

def check_collision():
    player_coords = canvas.coords(player)
    target_coords = canvas.coords(target)
    enemy_coords = canvas.coords(enemy)

    if (player_coords[0] < target_coords[2] and player_coords[2] > target_coords[0] and
            player_coords[1] < target_coords[3] and player_coords[3] > target_coords[1]):
        label.config(text="Ты победил!")

    if (player_coords[0] < enemy_coords[2] and player_coords[2] > enemy_coords[0] and
            player_coords[1] < enemy_coords[3] and player_coords[3] > enemy_coords[1]):
        label.config(text="Ты проиграл!")
        show_death_screen()

def key_pressed(event):
    move_wrap(player, 0, 0)
    if event.keysym == 'Up': move_wrap(player, 0, -step)
    elif event.keysym == 'Down': move_wrap(player, 0, -step)
    elif event.keysym == 'Right': move_wrap(player, step, 0)
    elif event.keysym == 'Left': move_wrap(player, -step, 0)

    move_enemy()
    check_collision()

def show_death_screen():
    global label
    label.config(text="Ты проиграл! Координаты игрока: {}".format(canvas.coords(player)))
    master.update()

master = tkinter.Tk()
step = 32
N_X = 10
N_Y = 10
WIDTH = step * N_X * 2
HEIGHT = step * N_Y * 2

canvas = tkinter.Canvas(master, bg='#975CFF', width=WIDTH, height=HEIGHT)
player = None
target = None
enemy = None

label = tkinter.Label(master, text="Не попадись!")
restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start)
restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
master.bind("<KeyPress>", key_pressed)
master.mainloop()