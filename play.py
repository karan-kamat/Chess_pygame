from board import board
from position import pos


class play():
    def __init__(self):
        self.bo = board()

        def gen():
            i = 0
            c = ["white", "black"]
            while True:
                yield c[i]
                i = (i+1) % 2
        self.g = gen()
        self.illegal_p = pos(-1, -1)

    def start(self):
        bo = self.bo
        g = self.g
        while True:
            cur_color = next(g)
            bo.show_chessboard()
            curpos = pos(-1, -1)
            while True:
                print(f"Enter position to chose for {cur_color}:", end='')
                curpos.x, curpos.y = map(int, input().split())
                if curpos.isillegal() or bo.a[curpos] is None or bo.a[curpos].color != cur_color:
                    print("Wrong selection")
                    continue
                break
            bo.show_possible_moves(curpos, cur_color)
            pos_moves = bo.a[curpos].possible_move_positions()
            newpos = pos(-1, -1)
            while True:
                print(f"Enter position to move to:", end='')
                newpos.x, newpos.y = map(int, input().split())
                if newpos not in pos_moves:
                    print("Can't move there")
                    continue
                break
            # newpos.x,newpos.y=map(int,input("Enter position to move to:").split())
            pk = bo.move(curpos, newpos, cur_color)
            if bool(pk) == True:
                print(f"{cur_color} wins the game")
                break


p = play()
p.start()
