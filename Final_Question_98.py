"""
0 = 갈 수 있는 곳
1 = 벽
2 = 먹이

1. 가장 오른쪽 아래, 움직일 수 없을 때, 먹이를 찾았을 때 => 중지
2. 개미는 2,2 에서 출발
3. 개미는 우 -> 하 로만 이동
"""
import sys
maze = []
maze_size = 10
x, y = 1, 1

for _ in range(maze_size):
    maze.append(list(map(int, sys.stdin.readline().split())))

while True:
    if maze[x][y] == 2:
        maze[x][y] = 9
        break

    elif x == y == 8:
        maze[x][y] = 9
        break

    if maze[x][y + 1] != 1:
        maze[x][y] = 9
        y += 1
    else:
        if maze[x + 1][y] == 1:
            maze[x][y] = 9
            break
        else:
            maze[x][y] = 9
            x += 1

for i in maze:
    for j in i:
        print(j, end=' ')
    print()

