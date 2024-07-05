import heapq
class node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self,nxt):
        return self.freq < nxt.freq
    
def printNodes(node, val = ''):
    newVal = val + str(node.huff)
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


char = []
freq = []

n = int(input("Enter the number of inputs: \n"))
for i in range(n):
    ch = input("Enter character: ")
    char.append(ch)
    cha = int(input("Enter freq for charcter: "))
    freq.append(cha)

print(char,freq)

nodes = []
for x in range (len(char)):
    heapq.heappush(nodes, node(freq[x], char[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    heapq.heappush(nodes,newNode)

printNodes(nodes[0])