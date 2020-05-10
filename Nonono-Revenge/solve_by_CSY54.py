from PIL import Image
from z3 import *
from time import clock

black = []
white = []

def parse(filename):
    f = open(filename, 'r')

    H, W = map(int, f.readline().split(' '))

    row = [map(int, f.readline().split()) for i in range(H)]
    col = [map(int, f.readline().split()) for i in range(W)]

    assert(len(row) == H)
    assert(len(col) == W)

    return (H, W, row, col)

def parse_hint():
    global black, white

    img = Image.open('hint.png')
    W, H = img.size
    pix = img.load()

    for i in range(H):
        for j in range(W):
            if pix[j, i] == (0x00, 0x00, 0x00, 0xff): # is black
                black.append((j, i))
            elif pix[j, i] == (0xff, 0xff, 0xff, 0xff):
                white.append((j, i))

def to_pic(W, H, res, filename):
    img = Image.new('1', (W, H))
    pix = img.load()
    for i in range(H):
        for j in range(W):
            pix[j, i] = res[i][j]
    img.save('{}_solved.png'.format(filename))

def solve(filename):
    print('[+] Parsing file')
    start_time = clock()
    H, W, row, col = parse('{}.txt'.format(filename))
    print('...... {}'.format(clock() - start_time))

    s = Solver()

    x = [[Bool('x_{}_{}'.format(i, j)) for j in range(W)] for i in range(H)]
    r = [[Int('r_{}_{}'.format(i, j)) for j in range(len(row[i]))] for i in range(H)]
    c = [[Int('c_{}_{}'.format(i, j)) for j in range(len(col[i]))] for i in range(W)]

    print('[+] r')
    start_time = clock()
    for i in range(H):
        for j in range(len(row[i])):
            s.add(0 <= r[i][j], r[i][j] <= W - row[i][j])
            if j == len(row[i]) - 1:
                continue
            s.add(r[i][j] + row[i][j] < r[i][j + 1])
    print('...... {}'.format(clock() - start_time))

    print('[+] c')
    start_time = clock()
    for i in range(W):
        for j in range(len(col[i])):
            s.add(0 <= c[i][j], c[i][j] <= H - col[i][j])
            if j == len(col[i]) - 1:
                continue
            s.add(c[i][j] + col[i][j] < c[i][j + 1])
    print('...... {}'.format(clock() - start_time))

    print('[+] continuous')
    start_time = clock()
    for i in range(H):
        for j in range(W):
            r_con = [And(r[i][k] <= j, j < r[i][k] + row[i][k]) for k in range(len(row[i]))]
            c_con = [And(c[j][k] <= i, i < c[j][k] + col[j][k]) for k in range(len(col[j]))]

            s.add(x[i][j] == Or(r_con))
            s.add(x[i][j] == Or(c_con))
    print('...... {}'.format(clock() - start_time))

    print('[+] hint')
    start_time = clock()
    for pos in black:
        j, i = pos
        s.add(x[i][j] == False)

    for pos in white:
        j, i = pos
        s.add(x[i][j] == True)
    print('...... {}'.format(clock() - start_time))

    print('solving...')
    start_time = clock()
    if s.check() == sat:
        print('solvable!')
        m = s.model()
        res = [[is_true(m[x[i][j]]) for j in range(W)] for i in range(H)]
        to_pic(W, H, res, filename)
    else:
        print('unsolvable!')
    print('...... {}'.format(clock() - start_time))

parse_hint()
solve('nonono_revenge')
