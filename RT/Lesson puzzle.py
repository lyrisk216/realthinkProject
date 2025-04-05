#RT Lesson puzzle
#V0.9
import pygame, random, time, sys
SCREEN_W, SCREEN_H = 1200, 600
class CLS_puzzle( object ):
    def __init__( self, fileName, spaceX, spaceY, sideLength):
        img = pygame.image.load( fileName )
        self.map = pygame.transform.scale(img, (SCREEN_W // 2, SCREEN_H))
        self.w, self.h = self.map.get_size()
        self.spaceX, self.spaceY = spaceX, spaceY
        self.sideLength = sideLength
        self.matrix = []
        for y in range( sideLength ):
            line = []
            for x in range( sideLength ):
                line.append( y * sideLength + x )
            self.matrix.append( line )
    def draw_block( self, scr, x, y ):
        if x == self.spaceX and y == self.spaceY:
            return

        w, h = self.w // self.sideLength, self.h // self.sideLength

        sx = (self.matrix[y][x] % self.sideLength) * w
        sy = (self.matrix[y][x] // self.sideLength) * h

        tx, ty = x * w + 1, y * h + 1
        scr.blit( self.map, (tx, ty), (sx, sy, w - 2, h - 2))
    def draw_matrix( self, scr ):
        scr.fill((240, 240, 0))
        scr.blit(self.map, (SCREEN_W // 2, 0))
        for y in range( self.sideLength ):
            for x in range( self.sideLength ):
                self.draw_block( scr, x, y )
    def move( self, vx, vy):
        x2, y2 = self.spaceX + vx, self.spaceY + vy
        if x2 < 0 or x2 >= self.sideLength or y2 < 0 or y2 >= self.sideLength:
            return
        self.matrix[self.spaceY][self.spaceX], self.matrix[y2][x2] = \
            self.matrix[y2][x2], self.matrix[self.spaceY][self.spaceX]
        self.spaceX, self.spaceY = x2, y2
        return
    def shuffle( self, n ):
        vx0, vy0 = 0, 0
        for i in range(n):
            while True:
                vx, vy = random.choice( [ [0, -1], [0, 1], [-1, 0], [1, 0] ] )
                if vx == -vx0 and vy == -vy0:
                    continue
                break
            self.move(vx, vy)
            vx0, vy0 = vx, vy
            self.draw_matrix( screen )
            pygame.display.update()
            clock.tick(20)
        return
#--- init ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
puzzle = CLS_puzzle( 'map_china.jpg', 0, 3, 4 )
puzzle.shuffle(50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            vx, vy = 0, 0
            if event.key == pygame.K_UP:
                vx, vy = 0, -1
            elif event.key == pygame.K_DOWN:
                vx, vy = 0, 1
            elif event.key == pygame.K_LEFT:
                vx, vy = -1, 0
            elif event.key == pygame.K_RIGHT:
                vx, vy = 1, 0
            if vx != 0 or vy != 0:
                puzzle.move(vx, vy)
        puzzle.draw_matrix( screen )
        pygame.display.update()
        clock.tick(50)

                  
