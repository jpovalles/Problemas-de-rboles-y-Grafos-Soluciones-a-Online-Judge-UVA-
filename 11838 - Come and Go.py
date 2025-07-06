'''
Tarea 3: Come and Go
Juan Pablo Ovalles Ceron
8971870

In a certain city there are N intersections connected by one-way and two-way streets. It is a modern city, and several of the
streets have tunnels or overpasses. Evidently it must be possible to travel between any two intersections. More precisely
given two intersections V and W it must be possible to travel from V to W and from W to V.
Your task is to write a program that reads a description of the city street system and determines whether the requirement of
connectedness is satisfied or not.

Input
The input contains several test cases. The first line of a test case contains two integers N and M, separated by a space,
indicating the number of intersections (2 ≤ N ≤ 2 000) and number of streets (2 ≤ M ≤ N(N − 1)/2). The next M lines
describe the city street system, with each line describing one street. A street description consists of three integers V, W and
P, separated by a blank space, where V and W are distinct identifiers for intersections (1 ≤ V, W ≤ N, V , W ) and P can
be 1 or 2; if P = 1 the street is one-way, and traffic goes from V to W; if P = 2 then the street is two-way and links V and
W. A pair of intersections is connected by at most one street.
The last test case is followed by a line that contains only two zero numbers separated by a blank space.
The input must be read from standard input.

Output
For each test case your program should print a single line containing an integer G, where G is equal to one if the condition
of connectedness is satisfied and G is zero, otherwise.
The output must be written to standard output.
'''
from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)
visited,disc,fin,time = None,None,None,None

G = []

def main():
    global G

    n, m = list(map(int, stdin.readline().split()))
    while n != 0 and n != 0:
        G = [[] for _ in range(n)]
        for i in range(m):
            v, w, p = list(map(int, stdin.readline().split()))
            v, w = v-1, w-1
            if p == 1:
                G[v].append(w)
            else:
                G[v].append(w)
                G[w].append(v)
        dfs(G, range(len(G)))
        fin.reverse()
        GT = reverse(G)
        scc = dfs(GT, fin)
        if len(scc) <= 1: print(1)
        else: print(0)
        n, m = list(map(int, stdin.readline().split()))

def reverse(G):
  ans = [ list() for _ in G ]
  for u in range(len(G)):
    for v in G[u]:
      ans[v].append(u)
  return ans

def dfs(G, order):
  global visited,disc,fin,time
  ans = list()
  visited,disc,fin,time = list(),list(),list(),0
  for _ in G:
    visited.append(0)
    disc.append(None)
  for u in order:
    if visited[u]==0:
      ans.append(list())
      dfs_visit(G, u, ans[-1])
  return ans
    
def dfs_visit(G, u, comp):
  global visited,disc,fin,time
  visited[u],disc[u],time = 1,time,time+1
  comp.append(u)
  for v in G[u]:
    if visited[v]==0:
      dfs_visit(G, v, comp)
  visited[u],time = 2,time+1
  fin.append(u)


main()
