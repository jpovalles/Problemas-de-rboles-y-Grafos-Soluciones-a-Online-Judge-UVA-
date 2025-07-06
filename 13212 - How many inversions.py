'''
Tarea 1: How many inversions?
Juan Pablo Ovalles Ceron
8971870

HumbertovMoralov in his student days, he is attended system engineering at “University of missing hill” . He was evaluated
in its first course of Analysis of Algorithms (at the first half of 1997) with the following topics and questions:
Inversions:
Let A[1 . . . n] an array of distinct integers of size n. If i < j and A[i] > A[j], then the pair (i, j) is called an inversionof
A.
Given the above definition about an inversion, HmbertovMoralovmust answer the following questions:
1. List all inversions in ⟨3, 2, 8, 1, 6⟩.
2. What array of size n, with all the numbers from the set 1, 2, 3, . . . , n has the largest amount of inversions? How
many inversions?
3. Write an algorithm to determine the number of inversions in any permutation of n elements with Θ(n logn) in the
worst case run time.

Input
The input may contain several test cases. Each input case begins with a positive integer n (1 ≤ n ≤ 106

) denoting the
length of A, followed by n distinct lines. Each line contains a positive integer from array A. For i ∈ [1, n], will meet that
0 ≤ A[i] ≤ 108

. The input ends with a test case in which n is zero, and this case must not be processed.

The input must be read from standard input.
Output
For each test case, your program must print a positive integer representing the total number of inversions in the array A.
Each valid test case must generate just one output line.
The output must be written to standard output.
'''


from sys import stdin

def leerImprimir():
    cases = int(stdin.readline())
    while cases != 0:
        numbers = []
        for i in range(cases):
            numbers.append(int(stdin.readline()))
        print(mergesort(numbers))
            
        cases = int(stdin.readline())
    

def mergesort(lista):
    inv = 0
    if len(lista) > 1:
        mid = len(lista)//2
        der = lista[mid:]
        izq = lista[:mid]

        inv += mergesort(der)   #organizo la subparte derecha e izquierda
        inv += mergesort(izq)

        l, r = 0, 0 #iteradores de las subpartes
        i = 0       #iterador de la lista principal

        while r != len(der) or l != len(izq):
            if r == len(der): lista[i], l = izq[l], l+1     # casos donde el iterador de una subparte llega al tope
            elif l == len(izq): lista[i], r = der[r], r+1
            else:
                if izq[l] <= der[r]:
                    lista[i] = izq[l]
                    l = l+1
                else:
                    lista[i] = der[r]           #El contador de inversiones suma mid-1 dado que si el numero
                    r, inv = r+1, inv+mid-l     #que se encuentra a la derecha es mayor significa que los numeros
                                                #restantes en la lista izquierda forman una inversion con el, y mid-1 entrega esa cantidad de numeros
            i += 1
    return inv

leerImprimir()

