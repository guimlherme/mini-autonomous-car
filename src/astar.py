from maps import get_grid_map
from decision_making.astar import find_path

world_map = get_grid_map()
world_map.remove_edge(6,11)
world_map.remove_edge(5,10)
# world_map.print()

path = find_path(world_map, 1, 13)

print("Found")
for p in path:
    print(p, end=' ')
print('')

path = find_path(world_map, 3, 13)
print("Found")
for p in path:
    print(p, end=' ')
print('')