import random


class GenerateMaze(): 

    # widthとheightは共に奇数かつ5以上の整数
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [list('#'*width) for _ in range(height)]
        self._dig_walls()

    def _search_directions(self, y , x):
        directions = []
        if x - 2 > 0 and self.maze[y][x-2] == '#':
            directions.append('L')
        if x + 2 < self.width and self.maze[y][x+2] == '#':
            directions.append('R')
        if y - 2 > 0 and self.maze[y-2][x] == '#':
            directions.append('U')
        if y + 2 < self.height and self.maze[y+2][x] == '#':
            directions.append('D')
        return directions

    def _dig_walls(self):
        y = random.choice([i for i in range(1, self.height, 2)])
        x = random.choice([i for i in range(1, self.width, 2)])
        stack = [(y, x)]
        self.maze[y][x] = ' '
        while stack:
            directions = self._search_directions(y, x)
            if directions == []:
                stack.pop()
                if stack:
                    y, x = stack[-1]
                continue

            choiced = random.choice(directions)
            if choiced == 'L':
                for i in range(1, 3):
                    self.maze[y][x-i] = ' '
                x -= i
            elif choiced == 'R':
                for i in range(1, 3):
                    self.maze[y][x+i] = ' '
                x += i
            elif choiced == 'U':
                for i in range(1, 3):
                    self.maze[y-i][x] = ' '
                y -= i
            elif choiced == 'D':
                for i in range(1, 3):
                    self.maze[y+i][x] = ' '
                y += i
            stack.append((y, x))

    def print_maze(self, print_width=2):
        for line in self.maze:
            for char in line:
                print(char.center(print_width), end='')
            print()

    # 全角で出力
    def _print_maze_large(self):
        for lines in self.maze:
            for line in lines:
                if line == '#':
                    print('＃', end='')
                elif line == ' ':
                    print('　', end='')
                elif line == 'S':
                    print('Ｓ', end='')
                elif line == 'G':
                    print('Ｇ', end='')
            print()

    # startとgoalはそれぞれタプルで(y,x)の座標
    def preset_start_goal(self, start=None, goal=None):
        if start is None:
            self.start = (self.height-2, 0)
            self.maze[self.height-2][0] = 'S'
        else:
            self.start = start
            self.maze[start[0]][start[1]] = 'S'

        if goal is None:
            self.goal = (1, self.width-1)
            self.maze[1][self.width-1] = 'G'
        else:
            self.goal = goal
            self.maze[goal[0]][goal[1]] = 'G'

    def regenerate(self):
        self.maze = [list('#'*width) for _ in range(height)]
        self._dig_walls()


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

    maze = GenerateMaze(width, height)
    maze.preset_start_goal()
    maze.print_maze()
