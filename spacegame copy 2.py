import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()
width = 1000
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("space invader game")
velocity = 1
fps = 60
bullet_velocity = 1
font = pygame.font.SysFont('comicsans', 40)
BULLET_VEL = 7
MAX_BULLETS = 3
YELLOW_HIT = pygame.USEREVENT + 2
RED_HIT = pygame.USEREVENT + 1

background = pygame.transform.scale(pygame.image.load (os.path.join("space invader/bg.png")),(width,height))
ship1 = pygame.image.load(os.path.join("space invader/redship.png"))
ship1red = pygame.transform.rotate(pygame.transform.scale(ship1,(60,40)),90)
ship2 = pygame.image.load(os.path.join("space invader/yellowship.png"))
ship2yellow = pygame.transform.rotate(pygame.transform.scale(ship2,(60,40)),270)

def drawwindow(red, yellow, red_bullets, yellow_bullets,red_health,yellow_health):
    screen.blit(background, (0, 0))
    screen.blit(ship1red, (red.x, red.y))  # Use red Rect position
    screen.blit(ship2yellow, (yellow.x, yellow.y))  # Use yellow Rect position
    red_health_text = font.render("Health: " + str(red_health), 1, "red")  
    yellow_health_text = font.render("Health: " + str(yellow_health), 1, "yellow")
    screen.blit(yellow_health_text, (800, 10))
    screen.blit(red_health_text, (10, 10))
    for i in red_bullets:
        pygame.draw.rect(screen, "red", i)
    for i in yellow_bullets:
        pygame.draw.rect(screen, "yellow", i)

    pygame.display.update()

def yellow_ship_mov(key_press, yellow):
    if key_press[pygame.K_LEFT]:
        yellow.x -= velocity
    if key_press[pygame.K_RIGHT]:
        yellow.x += velocity
    if key_press[pygame.K_UP]:
        yellow.y -= velocity
    if key_press[pygame.K_DOWN]:
        yellow.y += velocity

def red_ship_mov(key_press, red):
    if key_press[pygame.K_a]:
        red.x -= velocity
    if key_press[pygame.K_d]:
        red.x += velocity
    if key_press[pygame.K_w]:
        red.y -= velocity
    if key_press[pygame.K_s]:
        red.y += velocity

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for i in yellow_bullets:
        i.x -= BULLET_VEL
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(i)
        elif i.x > width:
            yellow_bullets.remove(i)

    for i in red_bullets:
        i.x += BULLET_VEL
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(i)
        elif i.x < 0:
            red_bullets.remove(i)
                                                           
def main():
    red = pygame.Rect(100,300,60,40)
    yellow = pygame.Rect(700,300,60,40)

    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    while True:
            
        for i in pygame.event.get():
                
            if i.type == pygame.QUIT:
                    pygame.quit()

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LSHIFT:  # Corrected
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height// 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                if i.key == pygame.K_RSHIFT:  # Corrected
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height// 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)


            if i.type == RED_HIT:
                red_health -= 1
                

            if i.type == YELLOW_HIT:
                yellow_health -= 1        
        key_press = pygame.key.get_pressed()
        red_ship_mov(key_press, red)
        yellow_ship_mov(key_press, yellow)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        drawwindow(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
    main()
if __name__ == "__main__":
    main()
