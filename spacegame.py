import pygame
import os

pygame.init()
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders game")
velocity = 5
fps = 60
bullet_velcoity = 5

bg = pygame.transform.scale(pygame.image.load(os.path.join("space invader/bg.png")),(WIDTH,HEIGHT))
ship_y = pygame.image.load(os.path.join("space invader/yellowship.png"))
yellow_ship = pygame.transform.rotate(pygame.transform.scale(ship_y,(60,40)),90)
ship_r = pygame.image.load(os.path.join("space invader/redship.png"))
red_ship = pygame.transform.rotate(pygame.transform.scale(ship_r,(60,40)),270)

def draw_window(yellow,red,yellow_bullet,red_bullet):
    screen.blit(bg,(0,0))
    screen.blit(yellow_ship,(yellow.x,yellow.y))
    screen.blit(red_ship,(red.x,red.y))
    for i in red_bullet:
       pygame.draw.rect(screen,"red",i)
    for i in yellow_bullet:
       pygame.draw.rect(screen,"yellow",i)
    pygame.display.update()


def red_ship_move (keypress,red):
    if keypress [pygame.K_LEFT]:
      red.x -= 1
    if keypress [pygame.K_RIGHT]:
      red.x += 1
    if keypress [pygame.K_UP]:
      red.y -= 1
    if keypress [pygame.K_DOWN]:
      red.y += 1

def yellow_ship_move (keypress,yellow):
    if keypress [pygame.K_a]:
      yellow.x -= 1
    if keypress [pygame.K_d]:
      yellow.x += 1
    if keypress [pygame.K_w]:
      yellow.y -= 1
    if keypress [pygame.K_s]:
      yellow.y += 1


def handle_bullets (yellow_bullet,red_bullet,yellow,red):
  for i in yellow_bullet:
    i.x = i.x + bullet_velcoity
    if red.colliderect(i):
      pygame.event.post(pygame.event.Event(RED_HIT))
  for i in red_bullet:
    i.x = i.x - bullet_velcoity
    if yellow.colliderect(i):
      pygame.event.post(pygame.event.Event(YELLOW_HIT))
    






def main():
  yellow = pygame.Rect(100,300,60,60)
  red = pygame.Rect(900,300,60,60)
  red_bullet = []
  yellow_bullet = []
  while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
          if i.key == pygame.K_RSHIFT:
            bullet = pygame.rect(red.x + red.width, red.y + red.height// 2 - 2, 10, 5)
            red_bullet.append(bullet)

          if i.key == pygame.K_LSHIFT:
            bullet = pygame.rect(yellow.x + yellow.width, yellow.y + yellow.height// 2 - 2, 10, 5)
            yellow_bullet.append(bullet)
    keypress = pygame.key.get_pressed()
    red_ship_move(keypress,red)
    yellow_ship_move(keypress,yellow)
    handle_bullets(yellow_bullet,red_bullet,yellow,red)
    draw_window(yellow,red,yellow_bullet,red_bullet)  


  main()



    
    
   
       


if __name__ == "__main__":
    main()




                                                           
                                                           