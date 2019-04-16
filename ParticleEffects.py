import pygame
import sys
import random
if pygame.get_init():
    pygame.init()

class particle:
    #x, y, israndom, ptype, spread
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self,surface, x, y, israndom, spread, ptype, grav, drag, image, color = [0,255,255]):
        self.ttl = 0
        self.drag = drag
        self.i = 0
        self.surface = surface
        self.color = color
        self.grav = grav
        self.rx = 0
        self.ry = 0
        self.a = 0
        self.x = x
        self.y = y
        self.israndom = israndom
        self.ptype = ptype
        self.spread = spread
        self.image = image
        if israndom > 0:
            self.rx = float(random.gauss(0,self.spread)/10)
            self.ry = float(random.gauss(0,self.spread)/10)
    def parmove(self):
        if self.ptype == 0:
            self.surface.fill(self.color, ((self.x,self.y), (1, 1)))
        elif self.ptype == 1:
            pygame.draw.lines(self.surface, self.color, False,[(self.x,self.y),(self.x-self.rx,self.y+self.ry+self.a)])
        elif self.ptype == 2:
            if (self.color[0] > 1): self.color[0] -= 2
            if (self.color[1] > 1): self.color[1] -= 2
            if (self.color[2] > 1): self.color[2] -= 2
            self.surface.fill(self.color, ((self.x, self.y), (1, 1)))
        elif self.ptype == 3:
            if (self.color[0] > 1): self.color[0] -= 2
            if (self.color[1] > 1): self.color[1] -= 2
            if (self.color[2] > 1): self.color[2] -= 2
            pygame.draw.lines(self.surface, self.color, False,
                              [(self.x, self.y), (self.x - self.rx, self.y + self.ry + self.a)])

        self.rx *= self.drag
        self.ry *= self.drag
        self.x -= self.rx
        self.y = self.y + self.a + self.ry
        self.a += float(self.grav)
        self.ttl += 1
        return self.surface
    def getA(self):
        return self.a
    def setA(self,a):
        self.a = a
    def getY(self):
        return self.y
    def getX(self):
        return self.x
    def getTTL(self):
        return self.ttl
    def __del__(self):
        del self.i
        del self.surface
        del self.color
        del self.grav
        del self.rx
        del self.ry
        del self.a
        del self.x
        del self.y
        del self.israndom
        del self.ptype
        del self.spread
        del self.image



if __name__ == "__main__":
    print("STARTED AS MAIN, TESTBED ACTIVATED")
    screen = pygame.display.set_mode([1600,900],pygame.FULLSCREEN)
    objlist = []
    cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    #for x in range(300):
    #    x = particle(screen,800,450,1,5.0,1,0.03,0.99,0,(130,130,230))
    #    objlist.append(x)

    keys = pygame.key.get_pressed()
    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: sys.exit()

        pygame.time.wait(10)
        screen.fill((0, 0, 0))
        #screen.fill((0, 0, 0))
        for x in range(len(objlist)):
            try:
                screen = objlist[x].parmove()
            except IndexError:
                x = 0
            if objlist[x].getY() >800:
                objlist[x].setA(objlist[x].getA()*-0.5)
            if objlist[x].getTTL() > 100:
                del objlist[x]
                print("delobj")
                #print(range(len(objlist)), len(objlist))
        if pygame.mouse.get_pressed() == (1,0,0):
            a, b = pygame.mouse.get_pos()
            for x in range(30):
                x = particle(screen, a, b, 1, 100.0, 2, 1, 0.9, 0, [200, 150, 20])
                objlist.append(x)
                x = particle(screen, a, b, 1, 100.0, 3, 1, 0.99, 0, [250, 200, 100])
                objlist.append(x)



        pygame.display.flip()