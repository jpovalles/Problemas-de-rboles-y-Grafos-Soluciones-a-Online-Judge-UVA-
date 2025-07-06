'''
Fire Stations
tarea 4
Juan Pablo Ovalles Ceron
8971870

A city is served by a number of fire stations. Some residents have complained that the distance from their houses to the
nearest station is too far, so a new station is to be built. You are to choose the location of the fire station so as to reduce the
distance to the nearest station from the houses of the disgruntled residents.
The city has up to 500 intersections, connected by road segments of various lengths. No more than 20 road segments
intersect at a given intersection. The location of houses and firestations alike are considered to be at intersections (the travel
distance from the intersection to the actual building can be discounted). Furthermore, we assume that there is at least one
house associated with every intersection. There may be more than one firestation per intersection.
Input
The input begins with a single positive integer on a line by itself indicating the number of the cases following, each of
them as described below. This line is followed by a blank line, and there is also a blank line between two consecutive
inputs.
The first line of input contains two positive integers: f , the number of existing fire stations (f ≤ 100) and i, the number
of intersections (i ≤ 500). The intersections are numbered from 1 to i consecutively. f lines follow; each contains the
intersection number at which an existing fire station is found. A number of lines follow, each containing three positive
integers: the number of an intersection, the number of a different intersection, and the length of the road segment connecting
the intersections. All road segments are two-way (at least as far as fire engines are concerned), and there will exist a route
between any pair of intersections.
The input must be read from standard input.
Output
For each test case, the output must follow the description below. The outputs of two consecutive cases will be separated by
a blank line.
You are to output a single integer: the lowest intersection number at which a new fire station should be built so as to
minimize the maximum distance from any intersection to the nearest fire station.
The output must be written to standard output.
'''

from sys import stdin

from heapq import heappush,heappop
from collections import deque
import time

INF = float('inf')

def main():
    global G
    st = time.time()
    cases = int(stdin.readline())
    stdin.readline()
    for j in range(cases):
        stat, inte = map(int, stdin.readline().split())
        G = [[] for _ in range(inte)]
        statList = list()

        for i in range(stat): statList.append(int(stdin.readline()))

        for i in range(len(statList)):
            statList[i] = statList[i]-1

        edge = stdin.readline()

        while edge != "\n" and edge != "":
            u, v, w = map(int, edge.split())
            u, v = u-1, v-1
            G[u].append((v, w))
            G[v].append((u, w))
            edge = stdin.readline()

        distMin = INF
        ans = 0
        for i in range(inte):
            statList.append(i)
            aux = dijkstraMod(G, statList)
            maxDist = max(aux)
            if maxDist < distMin: distMin, ans = maxDist, i;
            statList.pop()

        print(ans+1)
        if j != cases: print()
        
            
def dijkstraMod(G, s):
  dist = [ INF ]*len(G)
  pqueue = list()
  for station in s:
      dist[station] = 0
      heappush(pqueue, (dist[station], station))
  pred = [-1] * len(G)
  
  while len(pqueue)!=0:
    du,u = heappop(pqueue)
    if dist[u] == du:
      for v,duv in G[u]:
        if du+duv<dist[v]:
          dist[v] = du+duv
          pred[v] = u
          heappush(pqueue, (dist[v], v))
  return dist

main()
