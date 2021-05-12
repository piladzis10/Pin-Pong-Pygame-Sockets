from network import Network
import pygame as py
from game import Game
from game_loby import *
py.font.init()

WIDTH,HEIGHT = 500,500
WIN = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Pin Pong")
win = None


def draw_player(x, y,width, height, win, color):
    py.draw.rect(win,color, (x,y, width, height))

def draw_ball(x, y, radius, win,color):
    py.draw.circle(win, color, (x,y), radius)


def main():
    global win
    run = True
    clock = py.time.Clock()

    n = Network()

    server_data = n.connect()
    p1 = server_data[0]
    p1.ready = True
    
    ball = server_data[1]

    def draw_win(win):
        win.fill((255,255,255))

        draw_player(p1.x, p1.y, p1.width, p1.height, win, (255,0,0))
        draw_player(p2.x, p2.y, p2.width, p2.height, win, (0,255,0))
        draw_ball(ball.x, ball.y, ball.radius,win, (0,0,255))

        py.display.update()

    while run:
        clock.tick(60)

        try:
            server_data = n.send_recieve(p1)
        except:
            if (p1.p == 0 and ball.y > 250) or (p1.p == 1 and ball.y < 250):
                win = "p1"
            else:
                win = "p2"
            break
        
        p2 = server_data[0]
        ball = server_data[1]

        if p1.ready and p2.ready:

            for event in py.event.get():
                if event.type == py.QUIT:
                    run = False
            keys = py.key.get_pressed()
            if keys[py.K_w] or keys[py.K_UP]:
                p1.y -= p1.vel
                if p1.p == 0:
                    if p1.y < 300:
                        p1.y = 300
                else:
                    if p1.y < 0:
                        p1.y = 0

            if keys[py.K_s] or keys[py.K_DOWN]:
                p1.y += p1.vel
                if p1.p == 0:
                    if p1.y > HEIGHT - p1.height:
                        p1.y = HEIGHT - p1.height
                else:
                    if p1.y > 200 - p1.height:
                        p1.y = 200 - p1.height
            
            if keys[py.K_a] or keys[py.K_LEFT]:
                p1.x -= p1.vel
                if p1.x < 0:
                    p1.x = 0
            
            if keys[py.K_d] or keys[py.K_RIGHT]:
                p1.x += p1.vel 
                if p1.x > WIDTH- p1.width:
                    p1.x = WIDTH - p1.width

            draw_win(WIN)
        else:
            waiting_loby(WIN, WIDTH, HEIGHT, "Waiting for opponent!")
while True:
    if win == None:
        game_loby(WIN, HEIGHT,WIDTH, "")
    elif win == "p2":
        game_loby(WIN, HEIGHT,WIDTH, "You won!")
    elif win == "p1":
        game_loby(WIN, HEIGHT,WIDTH, "You lost!")
    main()
