import pygame

class BaseSprite():
    def __init__(self,x, y, texture, speed, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [ w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)


class Hero(BaseSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed

class Wall:
    def __init__(self,x, y, color, w, h):
        self.hitbox = pygame.Rect(x, y, w, h,)
        self.hitbox.x = x
        self.hitbox.y = y
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)



class Enemy(BaseSprite) :
    def __init__(self, x1, y1, texture, speed, w, h, x2, y2):
        super().__init__(x1, y1, texture, speed, w, h)
        self.direction = "forward"
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


    def update(self):
        if self.direction == "forward":
            self.hitbox.x += self.speed
            if self.hitbox.x > self.x2:

        



pygame.init()
walls = [
    Wall(115, 80, [255, 0, 0], 100, 20)

    ]

window = pygame.display.set_mode([700, 500])
clook = pygame.time.Clock()
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, [700, 500])
hero = Hero(250, 250, "hero.png", 3, 50, 50)
enemy = Enemy(500,350 , "cyborg.png", 3, 50, 50)










game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    hero.update()



    window.fill([143,  123, 181  ])
    window.blit(background_img, [0,0])
    hero.draw(window)
    enemy.draw(window)
    pygame.display.flip()

    clook.tick(60)





