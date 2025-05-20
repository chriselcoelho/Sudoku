import random

def generate_sudoku(difficulty='easy'):
    base = 3
    side = base * base

    def pattern(r,c): return (base*(r%base)+r//base+c)%side
    def shuffle(s): return random.sample(s, len(s))
   

    rBase = range(base)
    rows = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, side +1))

    board =[[nums[pattern(r,c)] for c in cols] for r in rows]

    squares = side * side
    empties = {'easy': 20, 'medium': 40, 'hard': 60}.get(difficulty, 20)
    for _ in range(empties):
        x, y = random.randint9 (0, side-1), random.randint(0,side-1)
        board[x][y] = 0
    
    return board