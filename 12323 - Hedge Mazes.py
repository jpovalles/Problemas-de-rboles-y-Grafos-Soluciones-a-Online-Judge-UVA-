'''
Tarea 3: Hedges Mazes
Juan Pablo Ovalles Ceron
8971870

The Queen loves to stroll through a maze’s rooms and corridors in the late afternoon. Her servants choose a different
challenge for every day, that consists of finding a simple path from a start room to an end room in a maze. A simple path is
a sequence of distinct rooms such that each pair of consecutive rooms in the sequence is connected by a corridor. In this
case the first room of the sequence must be the start room, and the last room of the sequence must be the end room. The
Queen thinks that a challenge is good when, among the routes from the start room to the end room, exactly one of them is a
simple path. Can you help the Queen’s servants to choose a challenge that pleases the Queen?
For doing so, write a program that given the description of a maze and a list of queries defining the start and end rooms,
determines for each query whether that choice of rooms is a good challenge or not.

Input
Each test case is described using several lines. The first line contains three integers R, C and Q representing respectively
the number of rooms in a maze (2 ≤ R ≤ 104), the number of corridors (1 ≤ C ≤ 105), and the number of queries
(1 ≤ Q ≤ 1000). Rooms are identified by different integers from 1 to R. Each of the next C lines describes a corridor using
two distinct integers A and B, indicating that there is a corridor connecting rooms A and B (1 ≤ A < B ≤ R). After that,
each of the next Q lines describes a query using two distinct integers S and T indicating respectively the start and end
rooms of a challenge (1 ≤ S < T ≤ R). You may assume that within each test case there is at most one corridor connecting
each pair of rooms, and no two queries are the same.
The last test case is followed by a line containing three zeros.
The input must be read from standard input.

Output
For each test case output Q + 1 lines. In the i-th line write the answer to the i-th query. If the rooms make a good challenge,
then write the character ‘Y’ (uppercase). Otherwise write the character ‘N’ (uppercase). Print a line containing a single
character ‘-’ (hyphen) after each test case.
The output must be written to standard output.
'''

from sys import stdin, setrecursionlimit

G = []
copyG = []
visited = []
low = []
p = []
cmp = []
t, n = int(), int()

setrecursionlimit(1000000)

def main():
    global G, n, copyG, low, p, visited, t, cmp
    n, e, q = map(int, stdin.readline().split())

    while n != 0 or e != 0 or q != 0:
        copyG = [[] for _ in range(n)]
        G = [[] for _ in range(n)]
        cmp = [-1 for _ in range(n)]
        visited = [False for _ in range(n)]
        low = [-1 for _ in range(n)]
        p = [-1 for _ in range(n)]
        t = 0
        for _ in range(e):
            u, w = map(int, stdin.readline().split())
            u, w = u-1, w-1
            G[u].append(w)
            G[w].append(u)
        bridgesTarjan()
        dfs()

        for _ in range(q):
            u, w = map(int, stdin.readline().split())
            u, w = u-1, w-1
            
            if cmp[u] == -1 or cmp[w] == -1:
                print('N')
            elif cmp[u] == cmp[w]:
                print('Y')
            else:
                print('N')
            
        print("-")
        
        n, e, q = map(int, stdin.readline().split())


def bridgesTarjan():
    global low, visited, p, copyG
    for i in range(n):
        low[i] = visited[i] = p[i] = -1
    for i in range(n):
        if visited[i] == -1:
            bridgesAux(i)

def bridgesAux(v):
    global low, visited, p, bridgesSet, t, copyG
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            p[w] = v
            bridgesAux(w)
            low[v] = min(low[v], low[w])
            if low[w] > visited[v]:
                copyG[v].append(w)
                copyG[w].append(v)  
        elif w != p[v]:
            low[v] = min(low[v], visited[w])

            
def dfs():
    global vis, copyG, cmp
    i = 0
    vis = [False for _ in range(len(G))]
    for u in range(len(copyG)):
        if not vis[i] and len(copyG[i])!= 0:
            dfsAux(u, i)
        i += 1

def dfsAux(u, i):
    global vis, copyG, cmp

    vis[u] = True
    cmp[u] = i
    for v in copyG[u]:
        if not vis[v] and len(copyG[v])!= 0:
          dfsAux(v, i)
          
main()
