from pygame import *
from random import randint
from time import time as timer

mixer.init()
mixer.music.load('4d2c4b287eb3e47.mp3')
mixer.music.play()

font.init()

win_width = 1080
win_height = 720

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
background = transform.scale(image.load('abst.jpg'), (win_width, win_height))

ball_speed = 8

speed_x = 6
speed_y = 6



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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        global speed_y, speed_x
        if self.rect.y > win_height - 30 or self.rect.y < 0:
            speed_y *= - 1


font1 = font.SysFont('Arial', 36)

ball = Ball('ping_pong_PNG.png', 500, 350, 30, 30, ball_speed)
player1 = Player1('7bf5.png', 20, 350, 30, 100, 10)
player2 = Player2('7bf5.png', 1000, 350, 30, 100, 10)

lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0 , 0))
lose2 = font1.render('PLAYER 2 LOSE', True, (180, 0 , 0))

if e.key == K_0:
                mixer.music.play()

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
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= - 1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (500, 300))


        display.update()
    time.delay(20)
