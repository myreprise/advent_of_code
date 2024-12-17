from collections import deque

with open('input.txt') as file:
    data = file.read().strip()

grid, instructions = data.split("\n\n")
grid = grid.split("\n")

R, C = len(grid), len(grid[0])
grid = [[grid[r][c] for c in range(C)] for r in range(R)]

BIG_G = []
for r in range(R):
    row = []
    for c in range(C):
        if grid[r][c]=='#':
            row.append('#')
            row.append('#')
        if grid[r][c]=='O':
            row.append('[')
            row.append(']')
        if grid[r][c]=='.':
            row.append('.')
            row.append('.')
        if grid[r][c]=='@':
            row.append('@')
            row.append('.')
    BIG_G.append(row)

G = BIG_G
C *= 2

for r in range(R):
    for c in range(C):
        if G[r][c] == '@':
            sr,sc = r,c
            G[r][c] = '.'

r,c = sr,sc
for inst in instructions:

    if inst == '\n':
        continue
    dr,dc = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}[inst]

    rr,cc = r+dr,c+dc
    if G[rr][cc]=='#':
        continue
    elif G[rr][cc]=='.':
        r,c = rr,cc
    elif G[rr][cc] in ['[', ']', 'O']:
        Q = deque([(r,c)])
        SEEN = set()
        ok = True
        while Q:
            rr,cc = Q.popleft()
            if (rr,cc) in SEEN:
                continue
            SEEN.add((rr,cc))
            rrr,ccc = rr+dr, cc+dc
            if G[rrr][ccc]=='#':
                ok = False
                break
            if G[rrr][ccc] == 'O':
                Q.append((rrr,ccc))
            if G[rrr][ccc]=='[':
                Q.append((rrr,ccc))
                assert G[rrr][ccc+1]==']'
                Q.append((rrr,ccc+1))
            if G[rrr][ccc]==']':
                Q.append((rrr,ccc))
                assert G[rrr][ccc-1]=='['
                Q.append((rrr,ccc-1))
        if not ok:
            continue
        while len(SEEN) > 0:
            for rr,cc in sorted(SEEN):
                rrr,ccc = rr+dr,cc+dc
                if (rrr,ccc) not in SEEN:
                    assert G[rrr][ccc] == '.'
                    G[rrr][ccc] = G[rr][cc]
                    G[rr][cc] = '.'
                    SEEN.remove((rr,cc))
        r = r+dr
        c = c+dc

answer = 0
for r in range(R):
    for c in range(C):
        if G[r][c] in ['[', 'O']:
            answer += 100*r+c

print(answer)
# answer is 1437468
