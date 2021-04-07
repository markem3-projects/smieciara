import pygame
import sys
from world import set_world, World, Agent
x = 0
y = 1
window = pygame.display.set_mode((800, 560))
cell_size = 40
world_map_file = set_world('worldmap.txt')
pygame.init()
world = World(world_map_file, cell_size)
sprites = pygame.sprite.Group()
agent = Agent(world.get_world_cell_size())
sprites.add(agent)
window.fill((0, 0, 0))
while True:
    world.draw(window)
    sprites.update()
    sprites.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if x + 1 > 13:
                    agent.move("U")
                elif (int(world_map_file[x+1][y]) > 0):
                        agent.move('S')
                        x = x+1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if x-1 < 0:
                    agent.move("U")
                elif (int(world_map_file[x-1][y])>0):
                        agent.move('N')
                        x=x-1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if y+1 > 19:
                    agent.move("U")
                elif (int(world_map_file[x][y+1])>0):
                     agent.move('E')
                     y=y+1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if y - 1 < 0:
                    agent.move("U")
                elif (int(world_map_file[x ][y-1])>0):
                     agent.move('W')
                     y=y-1
    pygame.display.update()
