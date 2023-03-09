import pygame, sys
from settings import *
from tiles import *
from level import Level

#Setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_hegith))
clock = pygame.time.Clock()

#Tiles group
level = Level(level_map, screen)





level.bfs(level_map)
print(level.target_pos)
print(level.start_pos)
print(level.adj_list_numero)
print("dict", level.adj_list)


print(level.bfs_traversal_output)


print("path", level.path)
# print(level.bfs_traversal_output)
# print(level.level)

# list_tmp = []
# for parents in level.adj_list:
#     curr_list = level.adj_list.get(parents)
#     for i in curr_list:
#         if(i not in list_tmp):
#             list_tmp.append(i)
#     level.adj_list[parents] = list_tmp
#     list_tmp.clear()
#
# print(level.adj_list)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            level.game_status= True

    if level.game_status :
        screen.blit(level.background, (0, 0))
        level.run()
    else:
        screen.blit(level.gameover, (0,0))
    pygame.display.update()
    clock.tick(60)