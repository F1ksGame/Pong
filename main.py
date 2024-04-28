from pygame import *

window = display.set_mode((500, 500))
col1 = (0, 0, 255)
mw.fill(col1)
cloock = time. Clock()



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))  # вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#мяч и ракетка
recket1 = Player('racket.png', 30, 200, 4, 50, 150)
recket2 = Player('racet.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

#если мяч улетео дальше ракетки, выводим условие проигрыша для первого игрока
if ball.rect.x < 0:
finish = Truewindow.bilst(lose2, (200, 200))
game_over = True

#если мяч улетео дальше ракетки, выводим условие проигрыша для второго игрока
if ball.rect.x < 0:
finish = Truewindow.bilst(lose2, (200, 200))
game_over = True




while game:
    for i in event.get():
        if i.tyoe == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1
    
#экран
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)



run = True
finish = False
while run: 
    for i in event.get():
        if e.tyoe == QUIT:
            run = False
    if not finish:
        ball.reset()
        display.update()
    clock.tick(FPS)

display.update()
