'''
Tarea 3: Doves and Bombs
Juan Pablo Ovalles Ceron
8971870

Unfortunately, your government spent so much money on gathering intelligence that it has a very limited amount left
to build bombs. As a result, it can bomb only one target. You have been charged with the task of determining the best
candidate railway stations in the empire to bomb, based on their “pigeon value”.
The “pigeon value” of a station is the minimum number of pigeons that after bombing this station, will be required to
broadcast a message from the empire central command to all non-bombed stations. The location of the empire central
command is unknown but we know that it is not located at a railway station. This implies, that when the central command
needs to send a message to some non-bombed station they have to use at least one pigeon and then the message can be
further transmitted by the railway.

Input
The input contains several test cases. The data for each case begins with a line containing the following two integers:
• n the number of railway stations in the empire (3 ≤ n ≤ 10 000). The stations will be numbered starting from 0, up to
n − 1
• m the number of stations to be identified as candidate bombing targets (1 ≤ m ≤ n).
Next few lines consists of pairs of integers. Each pair (x, y) indicates the presence of a bidirectional railway line connecting
railway stations x and y. This sequence is terminated by a line containing two minus 1 as shown in the sample input.
Input is terminated by a case where the value of n = m = 0. This case should not be processed.

The input must be read from standard input.

Output
For each case of input the output should give m most desirable railway stations to bomb. There should be exactly m lines,
each with two integers separated by a single space. The first integer on each line will be the number of a railway station,
and the second will be the “pigeon value” of the station. This list should be sorted, first by “pigeon value”, in descending
order, and within the same “pigeon value” by railway station numbers, in ascending order. Print a blank line after the output
for each set of input.
The output must be written to standard output.
'''

from sys import stdin, setrecursionlimit

G = []
vis = []
low = []
par = []
values = []

setrecursionlimit(1000000)

t = int() 
def main():
    global G, values, vis, low, par, values
    cases = list(map(int, stdin.readline().split()))
    while cases[0] != 0 or cases[1] != 0:
        G = [[] for _ in range(cases[0])]
        vis = [False for _ in range(cases[0])]
        low = [-1 for _ in range(cases[0])]
        par = [-1 for _ in range(cases[0])]
        values = [Station(i, 1) for i in range(cases[0])]
        t = 0
        
        line = list(map(int,stdin.readline().split()))
        while line[0] != -1:
            G[line[0]].append(line[1])
            G[line[1]].append(line[0])
            line = list(map(int,stdin.readline().split()))
        
        ap(cases[0])
        values.sort()
        for i in range(cases[1]):
            print(values[i])
        print()
        cases = list(map(int,stdin.readline().split()))

def ap(n):
    global low, vis, par,t, values
    
    for i in range(n):
        low[i] = vis[i] = par[i] = -1
    
    for i in range(n):
        if vis[i] == -1:
            apAux(i)

def apAux(v):
    global low, vis, par, t, values, values
    numHijos = 0
    t += 1
    vis[v] = low[v] = t

    for w in G[v]:
        if vis[w] == -1:
            numHijos += 1
            par[w] = v
            apAux(w)
            low[v] = min(low[v], low[w])

            if par[v] != -1 and low[w] >= vis[v]:
                values[v].pigeon += 1
                
        elif w != par[v]:
            low[v] = min(low[v], vis[w])

    if par[v] == -1 and numHijos > 1:
        values[v].pigeon = numHijos


class Station:
    def __init__(self, nodo, pigeon):
        self.nodo = nodo
        self.pigeon = pigeon
    def __repr__(self):
        return "%d %d" %(self.nodo, self.pigeon)

    def __gt__(self, sta):
        if self.pigeon == sta.pigeon:
            return self.nodo > sta.nodo
        else:
            return self.pigeon < sta.pigeon
main()



















