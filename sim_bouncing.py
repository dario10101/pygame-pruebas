import sys, pygame
pygame.init()

size = width, height = 650, 650
speed = [1, 5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("./images/sim.png")

ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    #limpiar la pantalla, para que la imagen no deje un rastro
    screen.fill(black)
    #copiar el contenido de la imagen (ball) a una posicion especifica (ballrect)
    screen.blit(ball, ballrect)
    #mostrar el lienzo ya dibujado
    pygame.display.flip()

