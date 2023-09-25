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
            elif event.key == SDLK_LEFT:
                dx -= 1
            elif event.key == SDLK_UP:
                dy += 1
            elif event.key == SDLK_DOWN:
                dy -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
          
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx = 0
            elif event.key == SDLK_LEFT:
                dx = 0
            elif event.key == SDLK_UP:
                dy = 0
            elif event.key == SDLK_DOWN:
                dy = 0
        


pro = True

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    
   
    update_canvas()
    handle_events()
 
    delay(0.05)
    get_events()

close_canvas()
