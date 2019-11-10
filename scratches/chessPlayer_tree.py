class tree:
    def __init__(self,x):
        self.store = [x,[]]
    def AddSuccessor(self,x):
        self.store[1] += [x]
        return True
    def Successor(self):
        return self.store[1]
    def Get_LevelOrder(self):
        out = []
        x = queue()
        x.enqueue(self.store)
        while x.empty() == False:
            r = x.dequeue()
            out += [r[0]]
            for node in r[1]:
                x.enqueue(node.store)
        return out

class queue:
    def __init__(self):
        self.x = []
    def enqueue(self,val):
        self.x += [val]
        return True
    def dequeue(self):
        r = self.x[0]
        self.x = self.x[1:len(self.x)]
        return r
    def empty(self):
        if len(self.x) == 0:
            return True
        else:
            return False

