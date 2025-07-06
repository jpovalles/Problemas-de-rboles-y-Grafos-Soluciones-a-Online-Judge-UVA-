'''
RMQ with shifts
tarea 4

Juan Pablo Ovalles Ceron
8971870
'''

from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

#Segment tree is represented as a list
n, MAXN = int(), 1000
tree = []
def main():
    global tree
    cases = stdin.readline()
    numb = list(map(int, stdin.readline().split()))
    n, q = map(int, cases.split())
    tree = [0 for _ in range(2*n)]
    build(numb, 0, 0, n-1)
    for i in range(q):
        order = stdin.readline()
        if order[0] == "q":
            l, r = map(int, order[6:-2].split(','))
            print(querie(0,0,n-1,l-1,r-1))
        elif order[0] == "s":
            shiftPoses = list(map(int, order[6:-2].split(',')))
            numb2 = list(numb)
            for i in range(len(shiftPoses)):
                x = (i+1)%len(shiftPoses)
                a = shiftPoses[x]-1
                b = shiftPoses[i]-1
                numb2[b] = numb[a]
                update(0, 0, n-1, b, numb[a])
            numb = list(numb2)
        else: print("error")


#build the segment tree
def build(a, v, l, r):
    if l == r:
        tree[v] = a[l]
    else:
        m = l + ((r - l) >> 1)
        build(a, v + 1, l, m)
        build(a, v + 2 * (m - l + 1), m + 1, r)
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - l + 1)])

#sum query
def querie(v, L, R, l, r):
    ans = None
    if l > r: ans = float('inf')
    elif l == L and r == R:
        ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        ans = min(querie(v + 1, L, m, l, min(r, m)), querie(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r))
    return ans

#update query
def update(v, L, R, pos, h):
    if L == R: tree[v] = h
    else:
        m = L + ((R - L) >> 1)
        if pos <= m: update(v + 1, L, m, pos, h)
        else: update(v + 2 * (m - L + 1), m + 1, R, pos, h)
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - L + 1)])

main()

