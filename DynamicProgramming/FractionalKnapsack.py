'''
This is a greedy approach, not dynamic

'''

class  Item:
    def __init__(self, v,w):
        self.ratio = v/w
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.ratio < other.ratio

    def __str__(self):
        return "ITEM: (ratio: " + str(self.ratio) + ") (v: " + str(self.v) + ") (w: " + str(self.w)+")"

def KS(V, W, C):
    items = []
    for i in range(len(V)):
        items.append(Item(V[i], W[i]))
    #sort in reverse order according to ratio v/w
    items.sort(reverse=True)
    #keep track of how much weight you currently have taken
    takenW = 0
    for item in items:
        if item.w + takenW <= C: # if the whole item fits:
            print("Taken", item)
            takenW += item.w
        else:# otherwise take the fraction of that item that will result in filling the backpack
            ratio = (C - takenW) / item.w
            print("Taken ", ratio, "% of", item)
            break





V = [280, 100, 120, 120]
W = [40, 10, 20, 24]

KS(V,W, 60)
