class Node:

    def __init__(self, id, path):
        self.id = id
        self.path = path

    # define less than to put nodes in priority queue
    def __lt__(self, other):
        return self.path < other.path

    def __str__(self):
        return "id " + str(self.id) + " path: " + str(self.path)