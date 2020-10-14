class pos:
    def __init__(self, x, y):
        self.size_of_chessboard=8
        if 0 <= x < self.size_of_chessboard and 0 <= y < self.size_of_chessboard:
            self.x = x
            self.y = y
        else:
            self.x = -1
            self.y = -1

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def isillegal(self):
        if 0 <= self.x < self.size_of_chessboard and 0 <= self.y < self.size_of_chessboard:
            return False
        else:
            return True

    def illegal(self):
        self.x = -1
        self.y = -1

    def copy(self):
        return pos(self.x, self.y)

    def xp(self):  # x+1
        if 0 <= self.x < self.size_of_chessboard-1:
            self.x += 1
        else:
            self.illegal()
        return self.copy()

    def xs(self):  # x-1
        if self.size_of_chessboard > self.x > 0:
            self.x -= 1
        else:
            self.illegal()
        return self.copy()

    def yp(self):  # y+1
        if 0 <= self.y < self.size_of_chessboard-1:
            self.y += 1
        else:
            self.illegal()
        return self.copy()

    def ys(self):  # y-1
        if self.size_of_chessboard > self.y > 0:
            self.y -= 1
        else:
            self.illegal()
        return self.copy()

    def d1(self):  # x+1,y+1
        self.xp()
        self.yp()
        return self.copy()

    def d2(self):  # x+1,y-1
        self.xp()
        self.ys()
        return self.copy()

    def d3(self):  # x-1,y+1
        self.xs()
        self.yp()
        return self.copy()

    def d4(self):  # x-1,y-1
        self.xs()
        self.ys()
        return self.copy()
