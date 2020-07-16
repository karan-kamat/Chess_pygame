from piece import bishop, rook, queen, king, knight, pawn, piece
from position import pos


class board:
    a = {pos(i, j): None for i in range(8) for j in range(8)}

    def __init__(self):
        for i in range(8):
            self.a[pos(1, i)] = pawn("black", pos(1, i), self)
            self.a[pos(6, i)] = pawn("white", pos(6, i), self)
        for tup in [("black", 0), ("white", 7)]:
            self.a[pos(tup[1], 0)] = rook(tup[0], pos(tup[1], 0), self)
            self.a[pos(tup[1], 7)] = rook(tup[0], pos(tup[1], 7), self)
            self.a[pos(tup[1], 1)] = knight(tup[0], pos(tup[1], 1), self)
            self.a[pos(tup[1], 6)] = knight(tup[0], pos(tup[1], 6), self)
            self.a[pos(tup[1], 2)] = bishop(tup[0], pos(tup[1], 2), self)
            self.a[pos(tup[1], 5)] = bishop(tup[0], pos(tup[1], 5), self)
            self.a[pos(tup[1], 3)] = queen(tup[0], pos(tup[1], 3), self)
            self.a[pos(tup[1], 4)] = king(tup[0], pos(tup[1], 4), self)
    '''
	def show_possible_moves(self,current_pos,current_color):
		if current_color!=self.a[current_pos].color:
			return
		[print(i) for i in self.a[current_pos].possible_move_positions()]
	#'''

    def move(self, current_pos, new_pos, current_color):
        current_piece = self.a[current_pos]
        pos_mov = current_piece.possible_move_positions()
        is_king = False
        if (new_pos not in pos_mov) or (current_color != current_piece.color):
            return
        if current_piece.occupied_by_enemy(new_pos):
            enemy_piece = self.a[new_pos]
            if isinstance(enemy_piece, king):
                is_king = True
            del enemy_piece
        if new_pos == current_pos:
            del current_piece
            pie = [rook, knight, bishop, queen]
            choice = int(
                input("Your pawn is being promoted.Choose an option for it to be 1)Rook 2)Knight 3)Bishop 4)Queen"))
            self.a[current_pos] = pie[choice-1](current_color, current_pos, self)
            return
        current_piece.posit = new_pos
        self.a[current_pos] = None
        self.a[new_pos] = current_piece
        return is_king
    '''
	def show_chessboard(self):
		for i in range(8):
			for j in range(8):
				square=self.a[pos(i,j)]
				if square is None:
					print("  ",end=" ")
				else:
					c='W' if square.color=="white" else 'B'
					t=''
					if isinstance(square,rook):t='R'
					elif isinstance(square,bishop):t='B'
					elif isinstance(square,king):t='K'
					elif isinstance(square,queen):t='Q'
					elif isinstance(square,pawn):t='p'
					elif isinstance(square,knight):t='k'
					print(c+t,end=" ")
			print()
	#'''

    def check(self, color):
        allall = []
        for p in self.a:
            if(self.a[p] is not None and self.a[p].color == color):
                allall.extend(self.a[p].possible_move_positions())
        for p in allall:
            if (self.a[p] is not None and isinstance(self.a[p], king)):
                return True
        return False
