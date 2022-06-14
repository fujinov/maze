from collections import deque
from copy import deepcopy

from generate import GenerateMaze


class SearchMaze(GenerateMaze):

    def __init__(self, width, height, start=None, goal=None):
        super().__init__(width, height)
        self.spare = deepcopy(self.maze)
        if start is None or goal is None:
            super().preset_start_goal()
        else:
            super().preset_start_goal(start, goal)
        self.START = (self.start[0], self.start[1]+1)
        self.GOAL = (self.goal[0], self.goal[1]-1)
    
    def reset_root(self):
        self.maze = deepcopy(self.spare)

    def dfsearch(self):
        steps = 1
        stack = [self.START]

        while stack:
            y, x = stack.pop()
            self.maze[y][x] = str(steps)
            if y == self.GOAL[0] and x == self.GOAL[1]:
                break
        
            for yi, xi in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
                if self.maze[yi][xi] == ' ':
                    stack.append((yi, xi))
            steps += 1

    def bfsearch(self):
        distance = [[-1]*self.width for _ in range(self.height)]
        distance[self.START[0]][self.START[1]] = 1
        que = deque([self.START])

        while que:
            y, x = que.popleft()
            self.maze[y][x] = str(distance[y][x])
            if y == self.GOAL[0] and x == self.GOAL[1]:
                break
        
            for yi, xi in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
                if self.maze[yi][xi] == ' ':
                    que.append((yi, xi))
                    distance[yi][xi] = distance[y][x] + 1

    def shortest_distance(self):
        self.bfsearch()
        y, x = self.GOAL
        count = int(self.maze[self.GOAL[0]][self.GOAL[1]])
        shortest_list = [self.START, self.GOAL]

        while count > 1:
            count -= 1
            for yi, xi in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
                if self.maze[yi][xi] == str(count):
                    y, x = yi, xi
                    shortest_list.append((y, x))
                    break

        self.reset_root()
        for yi, xi in shortest_list:
            self.maze[yi][xi] = '.'


if __name__ == '__main__':

    def input_check(user):
        if user < 5 or user % 2 == 0:
            return False
        else:
            return True

    while True:
        width = int(input('Width = '))
        height = int(input('Height = '))
        if all([input_check(width), input_check(height)]):
            break
        else:
            print('幅と高さは5以上の奇数にしてください。')

    maze = SearchMaze(width, height)
    maze.print_maze()

    while True:
        print('1.深さ優先探索 2.幅優先探索 3.最短経路 4.プログラムの終了')
        user = input('番号を入力 = ')
        if user == '1':
            maze.dfsearch()
        elif user == '2':
            maze.bfsearch()
        elif user == '3':
            maze.shortest_distance()
        elif user == '4':
            break
        maze.print_maze()
        maze.reset_root()
