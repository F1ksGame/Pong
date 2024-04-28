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

#экран
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

#мяч и ракетка
recket1 = Player('racket.png', 30, 200, 4, 50, 150)
recket2 = Player('racet.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)



#если мяч улетео дальше ракетки, выводим условие проигрыша для первого игрока
if ball.rect.x < 0:
    finish = Truewindow.bilst(lose2, (200, 200))
    game_over = True

#если мяч улетео дальше ракетки, выводим условие проигрыша для второго игрока
if ball.rect.x < 0:
    finish = Truewindow.bilst(lose2, (200, 200))
    game_over = True

recket1.reset()
recket2.reset()
ball.reset()


run = True
while run: 
    for i in event.get():
        if e.tyoe == QUIT:
            run = False
    window.blit(background 0, 0)
