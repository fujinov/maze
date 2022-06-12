import random


class GenerateMaze(): 

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [list('#'*width) for _ in range(height)]

    def random_yx(self):
        y = random.choice([i for i in range(1, self.height, 2)])
        x = random.choice([i for i in range(1, self.width, 2)])
        return y, x

    def search_directions(self, y , x):
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
    
    def dig_wall(self):
        y, x = self.random_yx()
        stack = [(y, x)]
        self.maze[y][x] = ' '
        while stack:
            directions = self.search_directions(y, x)
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

    def print_maze(self):
        for lines in self.maze:
            print(''.join(lines))

if __name__ == '__main__':        
    maze = GenerateMaze(25, 25)
    maze.dig_wall()
    maze.print_maze()