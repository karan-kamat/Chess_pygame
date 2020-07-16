import pygame
from board import board as b
from piece import bishop, rook, queen, king, knight, pawn, piece
from position import pos


def main():
    pygame.init()
    screen_size = [600, 600]
    board = b()
    screen = pygame.display.set_mode(screen_size)
    background = pygame.image.load('chessboard2.png')
    grc = pygame.image.load('green_circle.png')

    br = pygame.image.load('BR.png')
    bn = pygame.image.load('Bkn.png')
    bb = pygame.image.load('BB.png')
    bk = pygame.image.load('BK.png')
    bp = pygame.image.load('Bp.png')
    bq = pygame.image.load('BQ.png')

    wr = pygame.image.load('WR.png')
    wn = pygame.image.load('Wkn.png')
    wb = pygame.image.load('WB.png')
    wk = pygame.image.load('WK.png')
    wp = pygame.image.load('Wp.png')
    wq = pygame.image.load('WQ.png')

    keep_alive = True

    def update_board(board):
        screen.blit(background, [0, 0])
        pieces = {"WK": wk, "WR": wr, "WQ": wq, "WB": wb, "Wk": wn, "Wp": wp,
                  "BK": bk, "BR": br, "BQ": bq, "BB": bb, "Bk": bn, "Bp": bp}
        for i in range(8):
            for j in range(8):
                square = board.a[pos(i, j)]
                if square is not None:
                    c = 'W' if square.color == "white" else 'B'
                    t = ''
                    if isinstance(square, rook):
                        t = 'R'
                    elif isinstance(square, bishop):
                        t = 'B'
                    elif isinstance(square, king):
                        t = 'K'
                    elif isinstance(square, queen):
                        t = 'Q'
                    elif isinstance(square, pawn):
                        t = 'p'
                    elif isinstance(square, knight):
                        t = 'k'
                    screen.blit(pieces[c+t], [5+75*j, 5+75*i])
    update_board(board)

    def gen():
        i = 0
        c = ["white", "black"]
        while True:
            yield c[i]
            i = (i+1) % 2
    g = gen()
    cur_color = next(g)
    pos_mov = []
    moving = False
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 72)
    check = font.render("CHECK", False, (0, 128, 0))
    def win(x): return font.render(str(x)+" WON", False, (0, 128, 0))

    while keep_alive:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN and not moving:
                x, y = event.pos
                pre = pos(y//75, x//75)
                if board.a[pre] is None or board.a[pre].color != cur_color:
                    continue
                pos_mov = board.a[pre].possible_move_positions()
                if pos_mov == []:
                    continue
                for p in pos_mov:
                    screen.blit(grc, [(p.y+.5)*75, (p.x+.5)*75])
                pygame.display.update()
                moving = True
                break
            if event.type == pygame.MOUSEBUTTONDOWN and moving:
                x, y = event.pos
                new = pos(y//75, x//75)
                if new not in pos_mov:
                    continue
                pk = board.move(pre, new, cur_color)
                update_board(board)
                if board.check(cur_color):
                    screen.blit(check, (200, 250))
                    pygame.display.update()
                if pk:
                    screen.blit(win(cur_color.upper()), (100, 250))
                    pygame.display.update()
                    clock.tick(1)
                    keep_alive = False
                pygame.display.update()
                # board.show_chessboard()
                cur_color = next(g)
                moving = False
            clock.tick(60)


if __name__ == '__main__':
    main()
