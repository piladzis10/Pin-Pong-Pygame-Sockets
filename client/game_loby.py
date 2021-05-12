import pygame as py

def waiting_loby(win, width, height, txt):
    win.fill((255,255,255))
    font = py.font.SysFont("comicsans", 60)
    text = font.render(txt,True, (0,0,0))
    win.blit(text, ((width - text.get_width())/2, (height - text.get_height())/2))

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            quit()
    py.display.update()

def game_loby(win, width,height, txt):
    run = True
    clock = py.time.Clock()

    while run:
        clock.tick(60)
        win.fill((255,255,255))
        font = py.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", True, (51,0,0))
        text2 = font.render(txt, True, (51,0,0))
        win.blit(text, ((width - text.get_width())/2, (height - text.get_height())/2))
        win.blit(text2, ((width - text2.get_width())/2, 350))

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                quit()
            if event.type == py.MOUSEBUTTONDOWN:
                run = False

        py.display.update()