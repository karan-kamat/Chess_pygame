from abc import ABC, abstractmethod
from position import pos


class piece(ABC):
    def __init__(self, color, posit, boa):
        self.color = color
        self.posit = posit
        self.boa = boa
    illegal_p = pos(-1, -1)

    def occupied_by_ally(self, p):
        if p == self.illegal_p or self.boa.a[p] is None:
            return False
        if self.boa.a[p].color == self.color:
            return True
        return False

    def occupied_by_enemy(self, p):
        if p == self.illegal_p or self.boa.a[p] is None:
            return False
        if self.boa.a[p].color != self.color:
            return True
        return False

    @abstractmethod
    def possible_move_positions(self):
        pass


class pawn(piece):
    def __init__(self, color, posit, boa):
        super().__init__(color, posit, boa)

    def possible_move_positions(self):
        all = []
        p = self.posit.copy()
        if self.color == "white":
            m = p.copy().xs()
            n = m.copy().xs()
            start = 6
            end = 0
        else:
            m = p.copy().xp()
            n = m.copy().xp()
            start = 1
            end = 7
        u = m.copy().ys()
        v = m.copy().yp()
        if p.x == end:
            all.append(self.posit)
            return all
        if self.occupied_by_enemy(u):
            all.append(u)
        if self.occupied_by_enemy(v):
            all.append(v)
        if not (self.occupied_by_ally(m) or self.occupied_by_enemy(m)):
            all.append(m)
        if p.x == start:
            if not (self.occupied_by_ally(m) or self.occupied_by_enemy(m)):
                all.append(n)
        return all


class rook(piece):
    def __init__(self, color, posit, boa):
        super().__init__(color, posit, boa)

    def possible_move_positions(self):
        all = []
        func = [pos.xp, pos.xs, pos.yp, pos.ys]
        for ifunc in func:
            p = self.posit.copy()
            while True:
                ifunc(p)
                if p == self.illegal_p or self.occupied_by_ally(p):
                    break
                if self.occupied_by_enemy(p):
                    all.append(p.copy())
                    break
                all.append(p.copy())
        return all


class bishop(piece):
    def __init__(self, color, posit, boa):
        super().__init__(color, posit, boa)

    def possible_move_positions(self):
        all = []
        func = [pos.d1, pos.d2, pos.d3, pos.d4]
        for ifunc in func:
            p = self.posit.copy()
            while True:
                ifunc(p)
                if p == self.illegal_p or self.occupied_by_ally(p):
                    break
                if self.occupied_by_enemy(p):
                    all.append(p.copy())
                    break
                all.append(p.copy())
        return all


class queen(piece):
    def __init__(self, color, posit, boa):
        super().__init__(color, posit, boa)

    def possible_move_positions(self):
        all = []
        func = [pos.d1, pos.d2, pos.d3, pos.d4, pos.xp, pos.xs, pos.yp, pos.ys]
        for ifunc in func:
            p = self.posit.copy()
            while True:
                ifunc(p)
                if p == self.illegal_p or self.occupied_by_ally(p):
                    break
                if self.occupied_by_enemy(p):
                    all.append(p.copy())
                    break
                all.append(p.copy())
        return all


class king(piece):
    def __init__(self, color, posit, boa):
        super().__init__(color, posit, boa)

    def possible_move_positions(self):
        all = []
        func = [pos.d1, pos.d2, pos.d3, pos.d4, pos.xp, pos.xs, pos.yp, pos.ys]
        for ifunc in func:
            p = self.posit.copy()
            ifunc(p)
            if p == self.illegal_p or self.occupied_by_ally(p):
                continue
            all.append(p.copy())
        return all


class knight(piece):
    def __init__(self, color, posit, boa):
        super().__init__(color, posit, boa)

    def possible_move_positions(self):
        all = []
        func1 = [pos.xp, pos.xp, pos.xs, pos.xs, pos.yp, pos.ys, pos.yp, pos.ys]
        func2 = [pos.d1, pos.d2, pos.d3, pos.d4, pos.d1, pos.d2, pos.d3, pos.d4]
        for ifunc1, ifunc2 in zip(func1, func2):
            p = self.posit.copy()
            ifunc1(p)
            ifunc2(p)
            if p == self.illegal_p or self.occupied_by_ally(p):
                continue
            all.append(p.copy())
        return all
