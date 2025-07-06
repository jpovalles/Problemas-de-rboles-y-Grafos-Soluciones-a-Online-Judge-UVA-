'''
Tarea 2: Getting gold
Juan Pablo Ovalles Ceron
8971870

The game will consist of the player moving around on the grid for as long as she likes (or until she falls into a trap). The
player can move up, down, left and right (but not diagonally). She will pick up gold if she walks into the same square as the
gold is. If the player stands next to (i.e., immediately up, down, left, or right of) one or more traps, she will “sense a draft”
but will not know from what direction the draft comes, or how many traps she’s near. If she tries to walk into a square
containing a wall, she will notice that there is a wall in that direction and remain in the position where she was.
For scoring purposes, we want to show the player how much gold she could have gotten safely. That is, how much gold can
a player get playing with an optimal strategy and always being sure that the square she walked into was safe. The player
does not have access to the map and the maps are randomly generated for each game so she has no previous knowledge of
the game.
Input
The input file contains several test cases, each of them as described below.
The first line of input contains two positive integers W and H, neither of them smaller than 3 or larger than 50, giving the
width and the height of the map, respectively. The next H lines contain W characters each, giving the map. The symbols
that may occur in a map are as follows:
P — the player’s starting position
G — a piece of gold
T— a trap
# — a wall
. — normal floor
There will be exactly one ’P’ in the map, and the border of the map will always contain walls.
The input must be read from standard input.
Output
For each test case, write to the output the number of pieces of gold the player can get without risking falling into a trap, on
a line by itself.
The output must be written to standard output.
'''

from sys import stdin

def main():
    global G, gold
    
    filasCol = stdin.readline()
    while filasCol != "":
        G = []
        gold = 0
        filasCol = list(map(int, filasCol.split()))
        
        jgFila, jgCol = 0,0
        col = filasCol[0]
        filas = filasCol[1]

        for i in range(filas):
            line = stdin.readline()
            G.append([])
            for j in range(col):
                car = ""
                if line[j] != '#':
                    car = line[j]
                if line[j] == 'P':
                    jgFila, jgCol = i, j
                G[i].append([car, False])
        dfs(jgFila, jgCol)
        print(gold)
        filasCol = stdin.readline()


def dfs(jgFila, jgCol):
    vis = G[jgFila][jgCol][1]
    if not vis:
        dfsAux(jgFila, jgCol)

def dfsAux(jgFila, jgCol):
    global gold
    node = G[jgFila][jgCol]
    if G[jgFila][jgCol][0] == 'G': gold += 1
    G[jgFila][jgCol][1] = True
    if node[0] != 'T':
        if G[jgFila][jgCol-1][0] != 'T' and G[jgFila-1][jgCol][0] != 'T' and G[jgFila][jgCol+1][0] != 'T' and G[jgFila+1][jgCol][0] != 'T':
            if G[jgFila+1][jgCol][0] != '' and not G[jgFila+1][jgCol][1]:
                dfsAux(jgFila+1, jgCol)
            if G[jgFila][jgCol+1][0] != '' and not G[jgFila][jgCol+1][1]:
                dfsAux(jgFila, jgCol+1)
            if G[jgFila-1][jgCol][0] != '' and not G[jgFila-1][jgCol][1]:
                dfsAux(jgFila-1, jgCol)
            if G[jgFila][jgCol-1][0] != '' and not G[jgFila][jgCol-1][1]: 
                dfsAux(jgFila, jgCol-1)
main()

