import pygame
import os

pygame.font.init()

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, K_a, K_d, K_s, K_w
####################################################
WIDTH, HEIGHT = (800, 600)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)


# For title
pygame.display.set_caption("My First Game")


# def main():
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         WIN.fill(WHITE)
#         pygame.display.update()
#     pygame.quit()




#####################################################
# def draw_window():
#     WIN.fill(WHITE)
#     pygame.display.update()

# def main():
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         draw_window()
#     pygame.quit()



######################################################
# FPS = 60

# def draw_window():
#     WIN.fill(WHITE)
#     pygame.display.update()

# def main():
#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         draw_window()
#     pygame.quit()



##################################################  #########

# Add assets -  Create new folder 
# FPS = 60

# BLOSSOM = pygame.image.load("assets/blossom.png")
# BUBBLES = pygame.image.load("assets/bubbles.png")
# def draw_window():
#     WIN.fill(WHITE)
#     WIN.blit(BLOSSOM, (200, 200))
#     pygame.display.update()



# def main():
#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         draw_window()
#     pygame.quit()


# # Resize, try swapping the order


# Change transform rotate size alter pygame.transfom.rotate(image, 270)

# FPS = 60

# BLOSSOM = pygame.image.load("assets/blossom.png")
# BUBBLES = pygame.image.load("assets/bubbles.png")
# BLOSSOM = pygame.transform.scale(BLOSSOM, (55, 80))
# BUBBLES = pygame.transform.scale(BUBBLES, (55, 80))

# def draw_window():
#     WIN.fill(WHITE)
#     WIN.blit(BLOSSOM, (200, 200))
#     WIN.blit(BUBBLES, (600, 200))
#     pygame.display.update()



# def main():
#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         draw_window()
#     pygame.quit()


# # Resize, try swapping the order




# FPS = 60

# BLOSSOM = pygame.image.load("assets/blossom.png")
# BUBBLES = pygame.image.load("assets/bubbles.png")
# BLOSSOM = pygame.transform.scale(BLOSSOM, (55, 80))
# BUBBLES = pygame.transform.scale(BUBBLES, (55, 80))

# def draw_window(red, blue):
#     WIN.fill(WHITE)
#     WIN.blit(BLOSSOM, (red.x, red.y))
#     WIN.blit(BUBBLES, (blue.x, blue.y))
#     pygame.display.update()



# def main():
#     clock = pygame.time.Clock()
#     red = pygame.Rect(200, 200, 55, 80 )
#     blue = pygame.Rect(500, 200, 55, 80 )

#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         red.x+=1
#         draw_window(red, blue)
#     pygame.quit()


# # set the width heoght as separate variables and decrement blue



FPS = 60
VELOCITY = 2
BLOSSOM = pygame.image.load("assets/blossom.png")
BUBBLES = pygame.image.load("assets/bubbles.png")
BLOSSOM = pygame.transform.scale(BLOSSOM, (55, 80))
BUBBLES = pygame.transform.scale(BUBBLES, (55, 80))

# def draw_window(red, blue):
#     WIN.fill(WHITE)
#     WIN.blit(BLOSSOM, (red.x, red.y))
#     WIN.blit(BUBBLES, (blue.x, blue.y))
#     pygame.display.update()



# def main():
#     clock = pygame.time.Clock()
#     red = pygame.Rect(200, 200, 55, 80 )
#     blue = pygame.Rect(500, 200, 55, 80 )

#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         # red.x+=1
#         keys_pressed = pygame.key.get_pressed()
#         if keys_pressed[K_a]:
#             red.x-=VELOCITY
#         if keys_pressed[K_d]:
#             red.x+=VELOCITY
#         if keys_pressed[K_w]:
#             red.y-=VELOCITY
#         if keys_pressed[K_s]:
#             red.y+=VELOCITY
#         draw_window(red, blue)
#     pygame.quit()



# def r_handle_movement(keys_pressed, red):
#     if keys_pressed[K_a]:
#         red.x-=VELOCITY
#     if keys_pressed[K_d]:
#         red.x+=VELOCITY
#     if keys_pressed[K_w]:
#         red.y-=VELOCITY
#     if keys_pressed[K_s]:
#         red.y+=VELOCITY

# def b_handle_movement(keys_pressed, blue):
#     if keys_pressed[K_LEFT]:
#             blue.x-=VELOCITY
#     if keys_pressed[K_RIGHT]:
#         blue.x+=VELOCITY
#     if keys_pressed[K_UP]:
#         blue.y-=VELOCITY
#     if keys_pressed[K_DOWN]:
#         blue.y+=VELOCITY



# def main():
#     clock = pygame.time.Clock()
#     red = pygame.Rect(200, 200, 55, 80 )
#     blue = pygame.Rect(500, 200, 55, 80 )

#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         # red.x+=1
#         keys_pressed = pygame.key.get_pressed()
#         r_handle_movement(keys_pressed, red)
#         b_handle_movement(keys_pressed, blue)
#         draw_window(red, blue)
#     pygame.quit()



######################################################################
# # central BORDER + container
# BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# PURPLE = (255, 0, 0)
# def draw_window(red, blue):
#     WIN.fill(WHITE)
#     pygame.draw.rect(WIN, PURPLE, BORDER)
#     WIN.blit(BLOSSOM, (red.x, red.y))
#     WIN.blit(BUBBLES, (blue.x, blue.y))
#     pygame.display.update()


# def r_handle_movement(keys_pressed, red):
#     if keys_pressed[K_a] and red.x -VELOCITY>=0:
#         red.x-=VELOCITY
#     if keys_pressed[K_d] and red.x+ red.width + VELOCITY<BORDER.x:
#         red.x+=VELOCITY
#     if keys_pressed[K_w] and red.y-VELOCITY>0:
#         red.y-=VELOCITY
#     if keys_pressed[K_s] and red.y+ red.height + VELOCITY<HEIGHT :
#         red.y+=VELOCITY

# def b_handle_movement(keys_pressed, blue):
#     if keys_pressed[K_LEFT] and blue.x -VELOCITY>=BORDER.x+BORDER.width:
#             blue.x-=VELOCITY
#     if keys_pressed[K_RIGHT] and blue.x+ blue.width + VELOCITY<WIDTH:
#         blue.x+=VELOCITY
#     if keys_pressed[K_UP] and blue.y-VELOCITY>0:
#         blue.y-=VELOCITY
#     if keys_pressed[K_DOWN] and blue.y+ blue.height + VELOCITY<HEIGHT :
#         blue.y+=VELOCITY




# def main():
#     clock = pygame.time.Clock()
#     red = pygame.Rect(200, 200, 55, 80 )
#     blue = pygame.Rect(500, 200, 55, 80 )

#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False
#         # red.x+=1
#         keys_pressed = pygame.key.get_pressed()
#         r_handle_movement(keys_pressed, red)
#         b_handle_movement(keys_pressed, blue)
#         draw_window(red, blue)
#     pygame.quit()



#####################################################################3
# LASERS

# BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# LASER_VEL = 2
# PURPLE = (255, 0, 0)

# def draw_window(red, blue, red_lasers, blue_lasers):
#     WIN.fill(WHITE)
#     pygame.draw.rect(WIN, PURPLE, BORDER)
#     WIN.blit(BLOSSOM, (red.x, red.y))
#     WIN.blit(BUBBLES, (blue.x, blue.y))
#     for laser in red_lasers:
#         # WIN.blit(RED_LASER, (laser.x, laser.y))
#         pygame.draw.rect(WIN, (255, 0, 0), laser)
#     for laser in blue_lasers:
#         # WIN.blit(BLUE_LASER, (laser.x, laser.y))
#         pygame.draw.rect(WIN, (0, 0, 255), laser)

#     pygame.display.update()


# def r_handle_movement(keys_pressed, red):
#     if keys_pressed[K_a] and red.x -VELOCITY>=0:
#         red.x-=VELOCITY
#     if keys_pressed[K_d] and red.x+ red.width + VELOCITY<BORDER.x:
#         red.x+=VELOCITY
#     if keys_pressed[K_w] and red.y-VELOCITY>0:
#         red.y-=VELOCITY
#     if keys_pressed[K_s] and red.y+ red.height + VELOCITY<HEIGHT :
#         red.y+=VELOCITY

# def b_handle_movement(keys_pressed, blue):
#     if keys_pressed[K_LEFT] and blue.x -VELOCITY>=BORDER.x+BORDER.width:
#             blue.x-=VELOCITY
#     if keys_pressed[K_RIGHT] and blue.x+ blue.width + VELOCITY<WIDTH:
#         blue.x+=VELOCITY
#     if keys_pressed[K_UP] and blue.y-VELOCITY>0:
#         blue.y-=VELOCITY
#     if keys_pressed[K_DOWN] and blue.y+ blue.height + VELOCITY<HEIGHT :
#         blue.y+=VELOCITY


# def handle_lasers(red_lasers, blue_lasers, red, blue):
#     for laser in red_lasers:
#         laser.x += LASER_VEL
#         if blue.colliderect(laser):
#             red_lasers.remove(laser)
#     for laser in blue_lasers:
#         laser.x -= LASER_VEL
#         if red.colliderect(laser):
#             blue_lasers.remove(laser)

# def main():
#     clock = pygame.time.Clock()
#     red = pygame.Rect(200, 200, 55, 80 )
#     blue = pygame.Rect(500, 200, 55, 80 )
#     red_lasers = []
#     blue_lasers = []

#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if (event.type==pygame.QUIT):
#                 run = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LCTRL:
#                 laser = pygame.Rect(red.x+red.width, red.y + red.height//2 -2, 10, 5 )
#                 red_lasers.append(laser)
#             if event.key == pygame.K_RCTRL:
#                 laser = pygame.Rect(blue.x+blue.width, blue.y + blue.height//2 -2, 10, 5 )
#                 blue_lasers.append(laser)

#         keys_pressed = pygame.key.get_pressed()
#         r_handle_movement(keys_pressed, red)
#         b_handle_movement(keys_pressed, blue)

#         handle_lasers(red_lasers, blue_lasers, red, blue)
#         draw_window(red, blue, red_lasers, blue_lasers)
#     pygame.quit()


################################################################# 



RED_ATTACKED = pygame.USEREVENT + 1
BLUE_ATTACKED = pygame.USEREVENT + 2
NONE_ATTACKED = pygame.USEREVENT + 3
TOWNSVILLE = pygame.transform.scale(pygame.image.load("assets/townsville.jpg"), (WIDTH, HEIGHT))
MOJOJO = pygame.transform.scale(pygame.image.load("assets/mojojo.png"), (80, 130))
BG = pygame.image.load("assets/moving.jpg")

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
LASER_VEL = 2
PURPLE = (255, 0, 0)
FONT = pygame.font.SysFont('comicsans', 40)
def draw_window(red, blue, red_lasers, blue_lasers, red_life, blue_life, mojo_x):
    WIN.blit(TOWNSVILLE, (0,0))
    # pygame.draw.rect(WIN, PURPLE, BORDER)
    red_text = FONT.render(
        "Red Life: " + str(red_life), 1, WHITE)
    blue_text = FONT.render(
        "Blue Life: " + str(blue_life), 1, WHITE)
    WIN.blit(MOJOJO, (mojo_x, 30))
    WIN.blit(blue_text, (WIDTH - blue_text.get_width() - 10, 10))
    WIN.blit(red_text, (10, 10))
    WIN.blit(BLOSSOM, (red.x, red.y))
    WIN.blit(BUBBLES, (blue.x, blue.y))
    for laser in red_lasers:
        # WIN.blit(RED_LASER, (laser.x, laser.y))
        pygame.draw.rect(WIN, (255, 0, 0), laser)
    for laser in blue_lasers:
        # WIN.blit(BLUE_LASER, (laser.x, laser.y))
        pygame.draw.rect(WIN, (0, 0, 255), laser)

    pygame.display.update()


def r_handle_movement(keys_pressed, red):
    if keys_pressed[K_a] and red.x -VELOCITY>=0:
        red.x-=VELOCITY
    if keys_pressed[K_d] and red.x+ red.width + VELOCITY<BORDER.x:
        red.x+=VELOCITY
    if keys_pressed[K_w] and red.y-VELOCITY>0:
        red.y-=VELOCITY
    if keys_pressed[K_s] and red.y+ red.height + VELOCITY<HEIGHT :
        red.y+=VELOCITY

def b_handle_movement(keys_pressed, blue):
    if keys_pressed[K_LEFT] and blue.x -VELOCITY>=BORDER.x+BORDER.width:
            blue.x-=VELOCITY
    if keys_pressed[K_RIGHT] and blue.x+ blue.width + VELOCITY<WIDTH:
        blue.x+=VELOCITY
    if keys_pressed[K_UP] and blue.y-VELOCITY>0:
        blue.y-=VELOCITY
    if keys_pressed[K_DOWN] and blue.y+ blue.height + VELOCITY<HEIGHT :
        blue.y+=VELOCITY


def handle_lasers(red_lasers, blue_lasers, red, blue):
    for laser in red_lasers:
        laser.x += LASER_VEL
        if blue.colliderect(laser):
            pygame.event.post(pygame.event.Event(BLUE_ATTACKED))
            red_lasers.remove(laser)
    for laser in blue_lasers:
        laser.x -= LASER_VEL
        if red.colliderect(laser):
            pygame.event.post(pygame.event.Event(RED_ATTACKED))
            blue_lasers.remove(laser)
            
def handleMojojo(mojo_x, mojo_right, mojo_left):
    global MOJOJO
    if (mojo_x + MOJOJO.get_rect().width >= WIDTH and mojo_right==True):
        MOJOJO = pygame.transform.flip(MOJOJO, True, False)
        mojo_right = False
        mojo_left = True
    elif (mojo_x <= 0 and mojo_left==True):
        MOJOJO =pygame.transform.flip(MOJOJO, True, False)
        mojo_right = True
        mojo_left = False
    else:
        if mojo_right:
            mojo_x+=1
        elif mojo_left:
            mojo_x-=1
    return mojo_x, mojo_right, mojo_left
def main():
    clock = pygame.time.Clock()
    red = pygame.Rect(200, 200, 55, 80 )
    blue = pygame.Rect(500, 200, 55, 80 )
    red_lasers = []
    blue_lasers = []
    red_life = 100
    blue_life = 100
    mojo_x, mojo_right, mojo_left = 0, True, False
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                laser = pygame.Rect(red.x+red.width, red.y + red.height//2 -2, 10, 5 )
                red_lasers.append(laser)
            if event.key == pygame.K_RCTRL:
                laser = pygame.Rect(blue.x+blue.width, blue.y + blue.height//2 -2, 10, 5 )
                blue_lasers.append(laser)
        if event.type == RED_ATTACKED:
            red_life -= 1
            pygame.event.post(pygame.event.Event(NONE_ATTACKED))


        if event.type == BLUE_ATTACKED:
            blue_life -= 1
            pygame.event.post(pygame.event.Event(NONE_ATTACKED))

        keys_pressed = pygame.key.get_pressed()
        r_handle_movement(keys_pressed, red)
        b_handle_movement(keys_pressed, blue)
        mojo_x, mojo_right, mojo_left = handleMojojo(mojo_x, mojo_right, mojo_left)
        handle_lasers(red_lasers, blue_lasers, red, blue)
        draw_window(red, blue, red_lasers, blue_lasers, red_life, blue_life, mojo_x)
    pygame.quit()

if __name__ ==  '__main__':
    main()
