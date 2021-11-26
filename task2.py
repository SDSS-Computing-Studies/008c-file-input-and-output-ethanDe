##### Task 2
"""Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches"""


def find(stock):
    filename = 'task02.csv'
    file = open(filename, 'r')
    alist = []
    count = 0
    for i in file:
        if stock in i:
            count = count + 1
            test = i.strip()
            lineData = test.split(",")
            
            alist.append(lineData[1])
    
    if len(alist) > 1:
        print(f"There are {len(alist)} stocks with that symbol")
    elif len(alist) == 1:
        print(alist)
    elif len(alist) == 0:
        print("No matches")

x = input("Enter a stock symbol: ")
find(x)