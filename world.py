import pygame

grass = pygame.image.load("sprites/grass.png")
tree = pygame.image.load("sprites/tree.png")            # cost 0
house = pygame.image.load("sprites/house.png")          # cost 0
road = pygame.image.load("sprites/road.png")            # cost 1
brick = pygame.image.load("sprites/brick.png")          # cost 2
sand = pygame.image.load("sprites/sand.png")          # cost 3
hole = pygame.image.load("sprites/hole.png")            # cost 9
speed_bump = pygame.image.load("sprites/speedbump.png")  # cost 8
glass_bin = pygame.image.load("sprites/szklo.png")
paper_bin = pygame.image.load("sprites/papier.png")
plastic_bin = pygame.image.load("sprites/plastik.png")
other_bin = pygame.image.load("sprites/zmieszane.png")


def set_world(path):
    array = []
    with open(path) as f:
        content = f.read().splitlines()
        for line in content:
            array.append(line)
    return array


class WorldCell(pygame.Rect):
    def __init__(self, x, y, rect_size, terrain, img):
        self.rect_size = rect_size
        self.terrain = terrain
        self.img = pygame.transform.scale(img, (40, 40))
        super(WorldCell, self).__init__(x, y, self.rect_size, self.rect_size)

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 0), self)
        window.blit(self.img, self)


class World:
    def __init__(self, world_map, cell_size):
        self.cell_size = cell_size
        self.y_size = len(world_map)
        self.x_size = len(world_map[0])
        self.world_map = world_map
        self.world_cells = [[0 for x in range(self.x_size)] for y in range(self.y_size)]

    def draw(self, window):
        for i in range(self.y_size):
            for j in range(self.x_size):
                img = ''
                terrain = int(self.world_map[i][j]) #zczytywanie z planszy do terrain
                if terrain == 0:
                    if ((i*j)+j+i) % 2 == 0:
                        img = pygame.transform.scale(tree, (40, 40))
                    else:
                        img = pygame.transform.scale(house, (40, 40))
                if terrain == 1:
                    img = pygame.transform.scale(road, (40, 40))
                if terrain == 2:
                    img = pygame.transform.scale(brick, (40, 40))
                if terrain == 3:
                    img = pygame.transform.scale(sand, (40, 40))
                if terrain == 4:
                    img = pygame.transform.scale(glass_bin, (40, 40))
                if terrain == 5:
                    img = pygame.transform.scale(paper_bin, (40, 40))
                if terrain == 6:
                    img = pygame.transform.scale(plastic_bin, (40, 40))
                if terrain == 7:
                    img = pygame.transform.scale(other_bin, (40, 40))
                if terrain == 9:
                    img = pygame.transform.scale(hole, (40, 40))
                if terrain == 8:
                    img = pygame.transform.scale(speed_bump, (40, 40))

                self.world_cells[i][j] = WorldCell(j * self.cell_size, i * self.cell_size, self.cell_size, terrain, img)
                self.world_cells[i][j].draw(window)

    def get_world_cell_size(self):
        return self.cell_size

    def get_world_map(self):
        return int(self.world_map[x][y])


class Agent(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("sprites/agent.png"), (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (60, 20)  # agent position on start
        self.size = size

    def move(self, direction):
        if direction == "N":
            self.rect.center = [self.rect.center[0], self.rect.center[1] - self.size]
        if direction == "S":
            self.rect.center = [self.rect.center[0], self.rect.center[1] + self.size]
        if direction == "W":
            self.rect.center = [self.rect.center[0] - self.size, self.rect.center[1]]
            pygame.mixer.music.load('sprites/dzwiek.wav')
            pygame.mixer.music.play(1)
        if direction == "E":
            self.rect.center = [self.rect.center[0] + self.size, self.rect.center[1]]
        if direction == "U":
            self.rect.center = [self.rect.center[0], self.rect.center[1]]
    # def garbage_move(self, garbage_id):
    # if (garbage_id == 1):
    # ... garbage --> glass_bin
    # if (garbage_id == 2):
    #
class Garbage():
    def __init__(self, garbage_id):
        self.type = type
        #papier, plastik, szkło, mieszane
        if (garbage_id == 1):
            type = 'glass'
        elif (garbage_id == 2):
            type = 'paper'
        elif (garbage_id == 3):
            type = 'plastic'
        elif (garbage_id == 4):
            type = 'other'