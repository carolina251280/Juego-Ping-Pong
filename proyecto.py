from pygame import *
#música de fondo
mixer.init()
mixer.music.load('musica_fondo.mp3')
mixer.music.play()
#Ventana del juego
ancho_ventana = 600
alto_ventana = 500
fondo = (180, 255, 133)
fondo_imagen = transform.scale(image.load('fondo.jpg'),(ancho_ventana, alto_ventana))
ventana = display.set_mode((ancho_ventana, alto_ventana))
ventana.fill(fondo)
clock = time.Clock()
FPS = 60
#Efectos de sonido
sonido_rebote = mixer.Sound('rebote.mp3')

jugar = True
fin = False

#clase padre para otros objetos
class GameSprite(sprite.Sprite):
 #constructor de clase
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Llamada al constructor de la clase (Sprite):
       sprite.Sprite.__init__(self)


       #cada objeto debe almacenar la propiedad image
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #cada objeto debe tener la propiedad rect – el rectángulo en el que está
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #método de dibujo del personaje en la ventana
   def reset(self):
       ventana.blit(self.image, (self.rect.x, self.rect.y))

#clase de jugador principal
class Player(GameSprite):
   #método para controlar el objeto con las teclas de las flechas
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < alto_ventana - 150:
            self.rect.y += self.speed
    
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < alto_ventana - 150:
            self.rect.y += self.speed
    


pelota = GameSprite('pelota.png', 200, 200,50, 50, 4)

plataforma1 = Player('isla2.png', 30, 200, 50, 150, 4)

plataforma2 = Player('isla1.png', 520, 200, 50, 150, 4)

font.init()
font = font.Font(None, 50)
perder_1 = font.render('PLAYER 1 LOSE', True, (245, 73, 39))
perder_2 = font.render('PLAYER 2 LOSE', True, (245, 73, 39))

cambio_x = 3
cambio_y = 3

while jugar:

    for e in event.get():
        if e.type == QUIT:
            jugar = False

    if fin != True:
        #ventana.fill(fondo)
        ventana.blit(fondo_imagen,(0, 0))
        plataforma1.update()
        plataforma2.update_1()
        pelota.update()

        pelota.rect.x += cambio_x
        pelota.rect.y += cambio_y

        if sprite.collide_rect(plataforma1, pelota) or sprite.collide_rect(plataforma2, pelota):
            cambio_x *= -1
            cambio_y *= 1
            sonido_rebote.play()

        if pelota.rect.y > alto_ventana - 50 or pelota.rect.y < 0:
            cambio_y *= -1
        
        #Pierde el jugador 1
        if pelota.rect.x < 0:
            ventana.blit(perder_1, (200, 200))
            fin = True
            jugar = True

        #Pierde el juagador 2
        if pelota.rect.x > ancho_ventana:
            ventana.blit(perder_2, (200, 200))
            fin = True
            jugar = True

        plataforma1.reset()
        plataforma2.reset()
        pelota.reset()

    display.update()
    clock.tick(FPS)