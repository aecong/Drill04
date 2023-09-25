from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
state = load_image('sleeping.png')
left = load_image('left.png')
diagonal_up = load_image('left_up.png')
diagonal_down = load_image('left_down.png')
up = load_image('up.png')
down = load_image('down.png')

def handle_events():
    global running, dx, dy
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx += 1
                if event.key == SDLK_UP:
                    dy += 1
                elif event.key == SDLK_DOWN:
                    dy -= 1
            elif event.key == SDLK_LEFT:
                dx -= 1
                if event.key == SDLK_UP:
                    dy += 1
                elif event.key == SDLK_DOWN:
                    dy -= 1
            elif event.key == SDLK_UP:
                dy += 1
                if event.key == SDLK_RIGHT:
                    dx += 1
                elif event.key == SDLK_LEFT:
                    dx -= 1
            elif event.key == SDLK_DOWN:
                dy -= 1
                if event.key == SDLK_RIGHT:
                    dx += 1
                elif event.key == SDLK_LEFT:
                    dx -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
          
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx -= 1
            elif event.key == SDLK_LEFT:
                dx += 1
            elif event.key == SDLK_UP:
                dy -= 1
            elif event.key == SDLK_DOWN:
                dy += 1
        

running = True
dx, dy = 0, 0
x, y = 800//2, 150
frame = 0
frameCut = 2
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    if dx == 0 and dy == 0:  # 가만히
        state.clip_draw(frame * 35, 0, 35, 20, x, y, 100, 50)
        frameCut = 2
    elif dx < 0 and dy == 0:  # 좌
        left.clip_draw(frame * 23, 0, 23, 33, x, y, 50, 90)
        frameCut = 3
    elif dx > 0 and dy == 0:  # 우
        left.clip_composite_draw(frame * 23, 0, 23, 33, 0, 'h', x, y, 50, 90)
        frameCut = 3
    elif dx == 0 and dy > 0:  # 상
        up.clip_draw(frame*28, 0, 28, 30, x, y, 60, 90)
        frameCut = 3
    elif dx == 0 and dy < 0:  # 하
        down.clip_draw(frame * 28, 0, 28, 30, x, y, 60, 90)
        frameCut = 3
    elif dx < 0 and dy > 0:  # 좌상
        diagonal_up.clip_draw(frame * 27, 0, 27, 32, x, y, 60, 90)
        frameCut = 3
    elif dx < 0 and dy < 0:  # 좌하
        diagonal_down.clip_draw(frame * 28, 0, 28, 32, x, y, 60, 90)
        frameCut = 3
    elif dx > 0 and dy > 0:  # 우상
        diagonal_up.clip_composite_draw(frame * 27, 0, 27, 32, 0, 'h', x, y, 60, 90)
        frameCut = 3
    elif dx > 0 and dy < 0:  # 우하
        diagonal_down.clip_composite_draw(frame * 28, 0, 28, 32, 0, 'h', x, y, 60, 90)
        frameCut = 3
    update_canvas()
    handle_events()
    frame = (frame + 1) % frameCut
    x += dx * 5
    y += dy * 5
    if x >= 800 or x <= 0:
        break
    if y >= 600 or y <= 0:
        break
    delay(0.05)
    get_events()

close_canvas()
