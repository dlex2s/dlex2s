#создай игру "Лабиринт"!
import pygame
# treasure
# mixer.music.load('jungles.ogg')
# mixer.music.play()

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()
loop = True
WIDTH = 500
HEIGHT = 700
FPS = 60
backgorund = pygame.transform.scale(
    pygame.image.load('.background.jpg'),
    (HEIGHT, WIDTH)
)

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('labirint')


pygame.mixer.music.load('jungles.ogg')

pygame.mixer.music.play(-1)


# class Sprite():
#     def __init__(self, texture, x, y):
#         self.texture = texture
#         self.x = x
#         self.y = y

class GameSprite(pygame.sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[pygame.K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed

        if keys_pressed[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[pygame.K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__(image, player_x, player_y, speed)
        self.right = True

    def update(self):
        if self.rect.x >= 530 and not self.right:
            self.rect.x -= self.speed
            if self.rect.x <= 530:
                self.right = True


        elif self.rect.x <= 650 and self.right:
            self.rect.x += self.speed
            if self.rect.x >= 650:
                self.right = False

class Wall(pygame.sprite.Sprite):
    def __init__(
        self, 
        color: tuple,
        wall_x: int,
        wall_y: int,
        wall_width: int, 
        wall_height: int,
        screen: pygame.Surface,
    ):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        # картика стены - прямоугольник нужных размеров и цвета
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.screen = screen

    def draw_wall(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


#Персонажи
Hero = GameSprite("hero.png", 500, 400, 4)
cyborg = GameSprite("cyborg.png", 600, 400, 4)
#Вывод персонажей
hero1 = Player("hero.png", 100 ,400, 5)
cyborg1 = Enemy("cyborg.png", 470, 100, 5)

w1 = Wall((0,0,0), 40, 200, 25, 400, screen)
w2 = Wall([0,0,0], 250, 300, 25, 300, screen)
w3 = Wall([0,0,0], 400, 150, 25, 350, screen)
w4 = Wall([0,0,0], 270, 0, 25, 200, screen)
w5 = Wall([0,0,0], 150, 0, 25, 320, screen)
w6 = Wall([0,0,0], 550, 0, 25, 300, screen)
w7 = Wall([0,0,0], 550, 385, 25, 300, screen)

finish = False
final = GameSprite('treasure.png', 590, 20, 0)

pygame.font.init()
pygame.font = pygame.font.Font(None, 70)
win = pygame.font.render("YOU WIN!", True, (255, 215, 0))
lose = pygame.font.render("YOU LOSE!", True, (180, 0, 0))

while loop:
    clock.tick(FPS)
    pygame.display.update()
    screen.blit(backgorund, (0,0))
    clock.tick(60)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # hero1.update()
    # cyborg1.update()
    # hero1.reset()
    # cyborg1.reset()

    if finish != True:
        hero1.update()
        cyborg1.update()
        final.update()

        screen.blit(backgorund, ((0, 0)))
        hero1.reset()
        cyborg1.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

    if (
        pygame.sprite.collide_rect(hero1, cyborg)
        or pygame.sprite.collide_rect(hero1, w1)
        or pygame.sprite.collide_rect(hero1, w2)
        or pygame.sprite.collide_rect(hero1, w3)
        or pygame.sprite.collide_rect(hero1, w4)
        or pygame.sprite.collide_rect(hero1, w5)
        or pygame.sprite.collide_rect(hero1, w6)
        or pygame.sprite.collide_rect(hero1, w7)
        or pygame.sprite.collide_rect(hero1, cyborg1)

    ):
        finish = True
        screen.blit(lose, (200, 200))
        kick = pygame.mixer.Sound('kick.ogg')
        kick.play()
   

    if pygame.sprite.collide_rect(hero1, final):
        finish = True
        screen.blit(win, (200, 200))
        money = pygame.mixer.Sound('money.ogg')
        money.play()

    pygame.display.update()




