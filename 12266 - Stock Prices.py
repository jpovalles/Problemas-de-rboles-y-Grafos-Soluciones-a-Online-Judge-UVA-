'''
Tarea 1: Stock Prices
Juan Pablo Ovalles Ceron
8971870

In this problem we deal with the calculation of stock prices. You need to know the following things about stock
prices:
• The ask price is the lowest price at which someone is willing to sell a share of a stock.
• The bid price is the highest price at which someone is willing to buy a share of a stock.
• The stock price is the price at which the last deal was established.
Whenever the bid price is greater than or equal to the ask price, a deal is established. A buy order offering the bid price is
matched with a sell order demanding the ask price, and shares are exchanged at the rate of the ask price until either the sell
order or the buy order (or both) is fulfilled (i.e., the buyer wants no more stocks, or the seller wants to sell no more stocks).
You will be given a list of orders (either buy or sell) and you have to calculate, after each order, the current ask price, bid
price and stock price.

Input
On the first line a positive integer: the number of test cases, at most 100. After that per test case:
• One line with an integer n (1 ≤ n ≤ 1000): the number of orders.
• n lines of the form ’order type x [shares at] y’, where order type is either ’buy’ or ’sell’, x (1 ≤ x ≤ 1000) is
the number of shares of a stock someone wishes to buy or to sell, and y (1 ≤ y ≤ 1000) is the desired price.
The input must be read from standard input.

Output
Per test case:
• n lines, each of the form ’ai bi si’, where ai, bi and si are the current ask, bid and stock prices, respectively, after the
i-th order has been processed and all possible deals have taken place. Whenever a price is not defined, output ’-’
instead of the price.
The output must be written to standard output.
'''


from sys import stdin

def leerDatos():
    cases = int(stdin.readline())
    
    while cases > 0:
        nOrders = int(stdin.readline())
        lines = []
        for i in range(nOrders):
            lines.append(stdin.readline().split())
        
        stocks(nOrders, lines)
        cases -= 1
    return 0


def stocks(numOrders, lines):
    nOrders = numOrders
    orders = lines
    buy = []
    sell = []
    stock = []
    i = 0
    while nOrders > 0:
        line = orders[i]
        #Registro de los precios con colas de prioridad implementadas con listas de listas
        #pues necesito tener el mayor numero a disposicion para el bid price
        if line[0] == "buy":
            buy.append([int(line[4]), int(line[1])])
            buy.sort()
        elif line[0] == "sell":
            sell.append([int(line[4]), int(line[1])])
            sell.sort(reverse = True)
            
        #Las operaciones se ejecutaran siempre que haya elementos en las colas y que el
        #bid price sea mayor que el ask price
        while len(buy)!=0 and len(sell)!= 0 and buy[-1][0] >= sell[-1][0]: 
            stock.append(sell[-1][0])   #Valor del trato
            
            #Comparar cantidades
            if buy[-1][1] > sell[-1][1]:    #Mas en compra
                buy[-1][1] = buy[-1][1] - sell[-1][1]
                sell.pop()
            elif buy[-1][1] < sell[-1][1]:  #Mas en venta
                sell[-1][1] = sell[-1][1] - buy[-1][1]
                buy.pop()
            else:                           #Igual cantidad
                sell.pop()
                buy.pop()
                
        if len(sell) == 0:
            print("-", end=" ")
        else:
            print(sell[-1][0], end=" ")
            
        if len(buy) == 0:
            print("-", end=" ")
        else:
            print(buy[-1][0], end=" ")

        if len(stock) == 0:
            print("-")
        else:
            print(stock[-1])
        nOrders -= 1
        i += 1
    return 0
leerDatos()
