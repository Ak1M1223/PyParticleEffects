import pygame
import sys
import random
if pygame.get_init():
    pygame.init()

class Particle:
    #x, y, israndom, ptype, spread
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self,surface, x, y, israndom, spread, ptype, grav, drag, image, color = [0,255,255]):
        self.ttl = 0
        self.drag = drag
        self.surface = surface
        self.color = color
        self.grav = grav
        self.inertiax = 0
        self.inertiay = 0
        self.a = 0
        self.x = x
        self.y = y
        self.israndom = israndom
        self.ptype = ptype
        self.spread = spread
        self.image = image
        if israndom > 0:
            self.inertiax = float(random.gauss(0,self.spread)/10)
            self.inertiay = float(random.gauss(0,self.spread)/10)
    def particle_update(self):
        if self.ptype == 0:
            self.surface.fill(self.color, ((self.x,self.y), (1, 1)))
        elif self.ptype == 1:
            pygame.draw.lines(self.surface, self.color, False,[(self.x,self.y),(self.x-self.inertiax,self.y+self.inertiay+self.a)])
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
                              [(self.x, self.y), (self.x - self.inertiax, self.y + self.inertiay + self.a)])

        self.inertiax *= self.drag
        self.inertiay = self.inertiay * self.drag + self.a
        self.x -= self.inertiax
        self.y = self.y + self.inertiay
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
    def getInertiaY(self):
        return self.inertiay
    def getInertiaX(self):
        return self.inertiax
    def setY(self,y):
        self.y = y
    def setX(self,x):
        self.x = x
    def setInertiaY(self, y):
            self.inertiay = y
    def setInertiaX(self, x):
            self.inertiax = x
    def getTTL(self):
        return self.ttl
    def __del__(self):
        del self.surface
        del self.color
        del self.grav
        del self.inertiax
        del self.inertiay
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
    particle_list = []
    cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    #for x in range(300):
    #    x = Particle(screen,800,450,1,5.0,1,0.03,0.99,0,(130,130,230))
    #    particle_list.append(x)

    keys = pygame.key.get_pressed()
    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: sys.exit()

        pygame.time.wait(10)
        screen.fill((0, 0, 0))
        #screen.fill((0, 0, 0))
        for x in range(len(particle_list)):
            try:
                screen = particle_list[x].particle_update()
            except IndexError:
                x = 0
            if particle_list[x].getY() >=800:
                if (particle_list[x].getA() >= 0):
                    particle_list[x].setA(0)
                if (particle_list[x].getInertiaY() > 0):
                    particle_list[x].setInertiaY(particle_list[x].getInertiaY() * -0.3)
                #if (particle_list[x].getInertiaY() >= 0)
                #particle_list[x].setInertiaY(particle_list[x].getInertiaY()*(-1))
                particle_list[x].setY(800-particle_list[x].getY()+800)
            if particle_list[x].getTTL() > 200:
                del particle_list[x]
                #print("delobj")
                #print(range(len(particle_list)), len(particle_list))
        if pygame.mouse.get_pressed() == (1,0,0):
            a, b = pygame.mouse.get_pos()
            for x in range(30):
                x = Particle(screen, a, b, 1, 100.0, 3, 0.1, 0.97, 0, [250, 200, 100])
                particle_list.append(x)
        if pygame.mouse.get_pressed() == (0,0,1):
            a, b = pygame.mouse.get_pos()
            for x in range(30):
                x = Particle(screen, a, b, 1, 100.0, 0, 0.1, 0.98, 0, [255, 255, 255])
                particle_list.append(x)




        pygame.display.flip()
