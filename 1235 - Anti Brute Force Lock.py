'''
Juan Pablo Ovalles Ceron
8971870
Tarea 4
Anti Brute Force Lock

PSA is quite confident that this new system will slow down the cracking, giving them enough time
to identify and catch the robbers. In order to determine the minimum number of rolling needed, PSA
wants you to write a program. Given all the keys, calculate the minimum number of rolls needed to
unlock the safe.
Input
The first line of input contains an integer T, the number of test cases follow. Each case begins with
an integer N (1 ≤ N ≤ 500), the number of keys. The next N lines, each contains exactly four digits
number (leading zero allowed) representing the keys to be unlocked.
Output
For each case, print in a single line the minimum number of rolls needed to unlock all the keys
'''

from sys import stdin
from heapq import heappush,heappop

def cambios(a, b):
    ans = 0
    for i in range(4):
        resta = abs(int(a[i])-int(b[i]))
        ans += min(resta, 10-resta)
    return ans

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        codes = stdin.readline().split()[1:]
        G = [[] for _ in range(len(codes))]
        inicial = 20
        it = 0
        for i in range(len(codes)):
            tmp = cambios('0000', codes[i])
            if tmp < inicial: inicial = tmp; it = i

        for i in range(len(codes)):
            for j in range(i+1, len(codes)):
                dist = cambios(codes[i], codes[j])
                G[i].append((j, dist))
                G[j].append((i, dist))
        c, p, cont = prim(G)
        dist, pred = dijkstra(G, 0)
        
        print(c)
        print(inicial+cont)

def prim(G):
  visited = [False for i in range(len(G))]
  c = [ INF ]*len(G) ; c[0] = 0
  cont = 0
  p = [-1] * len(G)
  pqueue = list()
  heappush(pqueue, (c[0], 0))
  
  while len(pqueue)!=0:
    du,u = heappop(pqueue)
    visited[u] = True
    if c[u] == du:
      for v,duv in G[u]:
        if not visited[v] and duv<c[v]:
          c[v] = duv
          p[v] = u
          heappush(pqueue, (c[v], v))
  for costo in c:
        cont += costo
  return c, p, cont
main()
