'''
Tarea 2: Exchange rates
Juan Pablo Ovalles Ceron
8971870

Using money to pay for goods and services usually makes life easier, but sometimes people prefer to trade items directly
without any money changing hands. In order to ensure a consistent “price”, traders set an exchange rate between items.
The exchange rate between two items A and B is expressed as two positive integers m and n, and says that m of item A is
worth n of item B. For example, 2 stoves might be worth 3 refrigerators. (Mathematically, 1 stove is worth 1.5 refrigerators,
but since it’s hard to find half a refrigerator, exchange rates are always expressed using integers.)
Your job is to write a program that, given a list of exchange rates, calculates the exchange rate between any two items.

Input
The input file contains one or more commands, followed by a line beginning with a period that signals the end of the file.
Each command is on a line by itself and is either an assertion or a query. An assertion begins with an exclamation point and
has the format
! m itema = n itemb
where itema and itemb are distinct item names and m and n are both positive integers less than 100. This command says
that m of itema are worth n of itemb. A query begins with a question mark, is of the form
? itema = itemb 
and asks for the exchange rate between itema and itemb, where itema and itemb are distinct items that have both appeared
in previous assertions (although not necessarily the same assertion).
The input must be read from standard input.

Output
For each query, output the exchange rate between itema and itemb based on all the assertions made up to that point.
Exchange rates must be in integers and must be reduced to lowest terms. If no exchange rate can be determined at that
point, use question marks instead of integers. Format all output exactly as shown in the example.
'''
from fractions import Fraction
from sys import stdin

G,name,code = list(),list(),dict()

def encode(s):
  global name,code,G
  if s not in code:
    code[s] = len(code)
    name.append(s)
    G.append(list())
  return code[s]

def main():
    global multi
    line = stdin.readline()
    while len(line)!=0 and line[0] != ".":
        tok = line.split()
        if tok[0][0]=='!':
            v0,c0,v1,c1 = int(tok[1]),encode(tok[2]),int(tok[4]),encode(tok[5])
            G[c0].append((c1, Fraction(v1, v0)))
            G[c1].append((c0, Fraction(v0, v1)))      
        else:
            c0,c1 = encode(tok[1]),encode(tok[3])
            ans = dfs(c0,c1)
              
            if ans:   # si el nodo buscado se encuentra se imprime el precios
                print("%d %s = %d %s" %(multi.denominator, name[c0], multi.numerator, name[c1]))
            else: print("? %s = ? %s" %(name[c0], name[c1]))

        line = stdin.readline()

def dfs(u, f):
    global vis, multi
    multi = 1
    vis = [False for _ in range(len(G))]
    if not vis[u]:
        dfsAux(u, f)
    return vis[f]   # retorna la visita del nodo buscado
    
        
def dfsAux(u, f):
  global vis, multi
  vis[u] = True
  
  if len(G[u]) == 0: multi 
  for v in G[u]:
    if not vis[v[0]] and not vis[f]:
      dfsAux(v[0], f)
      if vis[f]: multi *= v[1]  # solo si se visita el nodo buscado se empieza la multiplicacion

main()

