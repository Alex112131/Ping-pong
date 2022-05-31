from pygame import *
from random import randint
from time import time as timer

mixer.init()
mixer.music.load('0ee26c7ba49bf25.mp3')
mixer.music.play()

win_width = 1080
win_height = 720

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
background = transform.scale(image.load('abst.jpg'), (win_width, win_height))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        pass



#font.init()
#font1 = font.SysFont('Arial', 36)

ball = Ball('ping_pong_PNG.png', 500, 350, 50, 50, 8)
player1 = Player1('7bf5.png', 20, 350, 30, 100, 10)
player2 = Player2('7bf5.png', 1000, 350, 30, 100, 10)

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    if not finish:
        window.blit(background, (0,0))
#        text = font1.render('Счет: ' + str(score), 1, (255,255,255))
#        window.blit(text, (10,20))
#        text_lose = font1.render('Пропущено: ' + str(lost), 1, (255,255,255))
#        window.blit(text_lose, (10,50))
        player1.update()
        player2.update()
        player1.reset()
        player2.reset()
        ball.update()
        ball.reset()


        display.update()
    time.delay(20)
