import pygame
import random
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

background= pygame.image.load("background.jpg")
cool= pygame.image.load("cool.png")
senti= pygame.image.load("senti.png")

def display_score(score):
  font = pygame.font.SysFont('Comic Sans MS', 30)
  score_text = 'Score: ' + str(score)
  text_img= font.render(score_text, True, (255,0,0))
  screen.blit(text_img, [20, 10])

def random_offset():
  return -1*random.randint(100, 1000)

senti_y= [random_offset(),random_offset(), random_offset()]
cool_x= 150
score= 0

def crashed(idx):
  global score
  global keep_alive
  score= score-50
  print('You have been sentified by senti-', idx, score)
  senti_y[idx]= random_offset()
  if score<-200:
    keep_alive = False


def update_senti_pos(idx):
  global score
  if  senti_y[idx]>600:
     senti_y[idx]=random_offset()
     score= score+5
     print('Score', score)
  else:
     senti_y[idx]= senti_y[idx]+5


keep_alive= True
clock=pygame.time.Clock()

while keep_alive:
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and cool_x < 300:
    cool_x = cool_x + 10
  elif keys[pygame.K_LEFT] and cool_x > 0:
    cool_x = cool_x - 10


  update_senti_pos(0)
  update_senti_pos(1)
  update_senti_pos(2) 


  screen.blit(background, [0, 0])
  screen.blit(cool, [cool_x, 500])
  screen.blit(senti, [10,  senti_y[0]])
  screen.blit(senti, [170,  senti_y[1]])
  screen.blit(senti, [320,  senti_y[2]])

  if senti_y[0]>500 and cool_x<70:
    crashed(0)

  if senti_y[1] > 500 and cool_x > 100 and cool_x < 200:
    crashed(1)

  if senti_y[2]>500 and cool_x>220:
    crashed(2)

  display_score(score)

  pygame.display.update()
  clock.tick(60)
