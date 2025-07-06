'''
Tarea 2: Beverages
Juan Pablo Ovalles Ceron
8971870

Dilbert has just finished college and decided to go out with friends. Dilbert has some strange habits and thus he decided to
celebrate this important moment of his life drinking a lot. He will start drinking beverages with low alcohol content, like
beer, and then will move to a beverage that contains more alcohol, like wine, until there are no more available beverages.
Once Dilbert starts to drink wine he will not drink beer again, so the alcohol content of the beverages never decreases with
the time.
You should help Dilbert by indicating an order in which he can drink the beverages in the way he wishes.

Input
Each test case starts with 1 ≤ N ≤ 100, the number of available beverages. Then will follow N lines, informing the name
of each beverage, a name has less than 51 characters and has no white spaces. Then there is another line with an integer
0 ≤ M ≤ 200 and M lines in the form B1 B2 will follow, indicating that beverage B2 has more alcohol that beverage B1, so
Dilbert should drink beverage B1 before he starts drinking beverage B2. Be sure that this relation is transitive, so if there is
also a relation B2 B3 you should drink B1 before you can drink B3. There is a blank line after each test case. In the case
there is no relation between two beverages Dilbert should start drinking the one that appears first in the input. The input is
terminated by end of file (EOF).
The input must be read from standard input.

Output
For each test case you must print the message:
’Case #C: Dilbert should drink beverages in this order: B1 B2 . . . BN.’
where C is the number of the test case, starting from 1, and B1 B2 . . . BN is a list of the beverages such that the alcohol
content of beverage Bi+1 is not less than the alcohol content of beverage Bi−1. After each test case you must print a blank
line.
The output must be written to standard output.
'''

from sys import stdin

def topoSort(p):
  global inc, visited, topo
  
  if p < len(G):
    r, i = -1, 0
    while i < len(G) and r == -1:
      if visited[i] == 0 and inc[i] == 0: r = i
      i += 1
    if r != -1:
      for v in G[r]:
        inc[v] -= 1
      visited[r] = 1
      topo.append(r)
      topoSort(p + 1)

def main():
    global bevs, code, inc, G, topo, visited
    cont = 1
    line = stdin.readline()

    while line != "":
        code = dict()
        visited = [0 for _ in range(int(line))]
        bevs, topo = [], []
        inc, G = [0 for _ in range(int(line))], [[] for _ in range(int(line))]

        for i in range(int(line)):
            bev = stdin.readline().split()
            bevs.append(bev[0])
            code[i] = bev[0]

        line = stdin.readline()

        for i in range(int(line)):
            bevLine = stdin.readline().split()
            vis = bevs.index(bevLine[0])
            rec = bevs.index(bevLine[1])
            G[vis].append(rec)
            inc[rec] += 1
            
        topoSort(0)
        ans = "Case #%d: Dilbert should drink beverages in this order:" %(cont)
        for bev in topo:
            ans += " " + code[bev]
        ans += ".\n"
        print(ans)
        cont += 1
        line = stdin.readline()
        line = stdin.readline()

main()
