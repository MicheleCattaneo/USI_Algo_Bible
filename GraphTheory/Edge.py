class Edge:

    def __init__(self, src, dest, w):
        self.src = src
        self.dest = dest
        self.weight = w

    def __str__(self):
       return str(self.src) + " " + str(self.dest) + " " + str(self.weight)