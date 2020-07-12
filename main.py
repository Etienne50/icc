import pygame
pygame.init()

win = pygame.display.set_mode((700,700))
pygame.display.set_caption("la true")
reloj = pygame.time.Clock()

humanito = pygame.image.load("humanito.png")

class jugador(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.contapasos = 0
        self.visible = True

    def draw(self, win):
        win.blit(humanito, (self.x, self.y))
        #pygame.draw.rect(win, (255,0,0), (self.x, self.y, 90, 50))

def pprincipal():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
        win.fill((0,0,0))
        principal = pygame.font.SysFont("arial", 100)
        textoprinc = principal.render("COVID RUN", 1, (0,255,0))
        win.blit(textoprinc, (475 - (textoprinc.get_width()/2),250))
        pygame.display.update()



def inicio(text):
    principal = pygame.font.SysFont("arial", 100)
    textoprinc = principal.render("COVID RUN", 1, (0,255,0))
    win.blit(textoprinc, (475- (text.get_width()/2),250))
    pygame.display.update()
    i = 0
    while i < 300:
        i +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 301
                pygame.quit()
def redrawGameWindow():
    hombre.draw(win)
    inicio(win)
    pygame.display.update()

empezar = 0
hombre = jugador(325, 600, 90, 50)
corre = True
while corre: #MAIN LOOOOOP

    reloj.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corre = False

    teclas = pygame.key.get_pressed()


    if teclas[pygame.K_RIGHT] and hombre.x < 700 - hombre.width - hombre.vel:
        hombre.x += hombre.vel

    elif teclas[pygame.K_LEFT] and hombre.x > hombre.vel:
        hombre.x -= hombre.vel
    else:
        hombre.contapasos = 0
    win.fill((250,250,250))
    redrawGameWindow()
    #pprincipal()
pygame.quit()
