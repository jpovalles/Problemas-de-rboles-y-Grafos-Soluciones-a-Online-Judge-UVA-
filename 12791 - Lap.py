'''
Tarea 1: Lap
Juan Pablo Ovalles Ceron
8971870

In motorsports it is very common that the leader pilot in a race, at a certain moment, overtakes the last pilot. The leader, at
this moment, is one lap ahead of the last pilot, who then becomes a straggler. In this task, given the time it takes for the
fastest pilot, and for the slowest pilot, to complete one lap, you have to determine in which lap the slowest pilot will become
a straggler. You should consider that, at the beginning, they are side by side at the start line of the circuit, both at the start of
lap number 1 (the first lap of the race); and that a new lap always begins right after the leader crosses the start line.

Input
The input contains several test cases. Each test case consists of one line with two integers X and Y (1 ≤ X < Y ≤ 2
50), the times, in seconds, that it takes for the fastest and the slowest pilot, respectively, to complete one lap.
The input must be read from standard input.

Output
For each test case in the input program should output line, containing one integer: the lap in which the slowest pilot will
become a straggler.
The output must be written to standard output.
'''

from sys import stdin

def leerImprimir():
    line = stdin.readline()
    while line != "":
        n = list(map(int, line.split()))
        print(biseccion(n[0], n[1]))
        line = stdin.readline()

def biseccion(fast, slow):
    low = 2
    high = slow
    ans = None
    mid = high     #Evita que el programa falle al ingresar el caso 1 2, 2 3, etc

    while high-low > 1:
        mid = (high + low)//2
        if slow <= mid*(slow-fast): high = mid
        else: low = mid
        if high-low == 1:
            if low*(slow-fast) < slow and high*(slow-fast) >= slow: mid, low = high, high     #Examinar el resultado en los extremos
            elif low*(slow-fast) > slow and high*(slow-fast) > slow: mid, high = low, low     #para no perder resultados
    return mid
leerImprimir()
