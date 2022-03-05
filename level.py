from direction import Direction


class Level:
    class GameObj:
        def __init__(self, r, c):
            self.r = r
            self.c = c

    class Wall(GameObj):
        def __init__(self, r, c):
            super().__init__(r, c)
            self.color = "C8C8C8"

    class ExitWall(GameObj):
        def __init__(self, color, r, c):
            super().__init__(r, c)
            self.color = color

    class Ball(GameObj):
        def __init__(self, color, r, c):
            super().__init__(r, c)
            self.color = color

        def move(self, direct: Direction):
            if direct == Direction.UP:
                self.r -= 1
            elif direct == Direction.DOWN:
                self.r += 1
            elif direct == Direction.LEFT:
                self.c -= 1
            elif direct == Direction.RIGHT:
                self.c += 1

        def pos(self):
            return self.r, self.c

    def __init__(self):
        self.grid = []
        self.title = ''
        self.balls = []

    def load_file(self, filename):
        f_data = []
        with open(filename, "r") as f:
            self.title = f.readline()
            for line in f.readlines():
                f_data.append(line.split())

        self.grid = self.parse_f_data(f_data)

    def parse_f_data(self, f_data):
        lvl_grid = []
        for line_idx in range(len(f_data)):
            lvl_line = []
            for col_idx in range(len(f_data[line_idx])):
                e = f_data[line_idx][col_idx]
                if e == '1':
                    lvl_line.append(self.Wall(line_idx, col_idx))
                elif e.startswith("+"):
                    lvl_line.append(self.ExitWall(e[1:], line_idx, col_idx))
                elif e.startswith("-"):
                    lvl_line.append(self.Ball(e[1:], line_idx, col_idx))
                elif e == '0':
                    lvl_line.append(0)
                else:
                    raise Exception("can't parse file!")
            lvl_grid.append(lvl_line[:])
        return lvl_grid


class LevelController:
    def __init__(self, level):
        self.level = level
        self.balls = self.get_balls()

    def check_win_cond(self):
        return len(self.balls) == 0

    def get_balls(self):
        balls = []
        for r in self.level.grid:
            for e in r:
                if isinstance(e, Level.Ball):
                    balls.append(e)
        return balls

    def get_game_obj(self, r, c):
        return self.level.grid[r][c]

    def move_ball(self, ball: Level.Ball, direct: Direction):
        while True:
            curr_r, curr_c = ball.pos()
            if direct == Direction.UP:
                next_r, next_c = curr_r-1, curr_c
            elif direct == Direction.DOWN:
                next_r, next_c = curr_r+1, curr_c
            elif direct == Direction.LEFT:
                next_r, next_c = curr_r, curr_c-1
            elif direct == Direction.RIGHT:
                next_r, next_c = curr_r, curr_c+1
            else:
                raise Exception("can't find direction")

            next_obj = self.level.grid[next_r][next_c]

            if next_obj == 0:
                self.level.grid[curr_r][curr_c] = 0
                self.level.grid[next_r][next_c] = ball
                ball.move(direct)
            elif isinstance(next_obj, Level.Wall) or isinstance(next_obj, Level.Ball):
                break
            elif isinstance(next_obj, Level.ExitWall):
                if next_obj.color == ball.color:
                    self.level.grid[curr_r][curr_c] = 0
                    self.balls.remove(ball)
                    break
                else:
                    break


if __name__ == '__main__':
    lvl = Level()
    lvl.load_file("levels/level_1.txt")
    c = LevelController(lvl)
    ball1 = c.get_game_obj(1, 1)
    c.move_ball(ball1, Direction.RIGHT)
    print()