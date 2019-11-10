class graph:
    def __init__(self):
        self.vert = []

    def add_vertex(self, n):
        length = len(self.vert)
        for i in range(length,n+length,1):
            self.vert += [[]]
        if len(self.vert) == length + n:
            return len(self.vert)
        else:
            return -1

    def add_edge(self, from_idx, to_idx, directed, weight):
        if from_idx < 0 or to_idx < 0:
            return False
        if directed == True:
            if to_idx not in self.vert[from_idx]:
                self.vert[from_idx] += [[to_idx,weight]]
            return True
        elif directed == False:
            if to_idx not in self.vert[from_idx]:
                self.vert[from_idx] += [[to_idx,weight]]
            if from_idx not in self.vert[to_idx]:
                self.vert[to_idx] += [[from_idx,weight]]
            return True
        return False

    def connectivity(self,vx,vy):
        out = self.path(vx,vy)
        for i in range(0,2,1):
            if out[i] == []:
                out[i] = [False]
            else:
                out[i] = [True]
        return out

    def path(self,vx,vy):
        out = [self.pathone(vx,vy),self.pathtwo(vy,vx)]
        print(out)
        for i in range(0,2,1):
            if out[i] == None:
                out[i] = []
        return out
    def pathone(self,vx,vy):
        visited1 = [False]*len(self.vert)
        path1 = []
        out1 = self.pathh(vx,vy,visited1,path1)
        return out1
    def pathtwo(self,vx,vy):
        visited2 = [False] * len(self.vert)
        path2 = []
        out2 = self.pathh(vx, vy, visited2, path2)
        return out2
    def pathh(self,vx,vy,visited,path):
        allvisit = True
        for i in visited:

            if i == False:
                allvisit = False
        if allvisit == True:
            return []


        visited[vx] = True
        path += [vx]
        if vx == vy:
            return path
        else:
            #print("richard")
            for i in range(0,len(self.vert[vx]),1):
                if visited[self.vert[vx][i][0]] == False:
                    return self.pathh(self.vert[vx][i][0],vy,visited,path)

    def traverse(self,start,typeBreath):
        out = []
        if typeBreath == True:
            x = queue()
        else:
            x = stack()
        dis = [False]*len(self.vert)
        pro = [False]*len(self.vert)
        if start == None:
            print("start1")
            for i in range(0,len(self.vert)):
                print("i",i)
                if dis[i] == False:
                    x.add(i)
                    dis[i] = True
            while x.empty() == False:
                w = x.remove()
                print("w",w)
                if pro[w] == False:
                    out += [w]
                    pro[w] = True
                    print("pro", pro)
                for y in range(len(self.vert[w])):
                    o = self.vert[w][y][0]
                    print("o",o)
                    if dis[o] == False:
                        x.add(o)
                        dis[o] = True
                        print("dis", dis)
                        print("outtttt", out)
            return out
        else:
            x.add(start)
            dis[start] = True
            while x.empty() == False:
                print("xxxxxxxxxxxxxxxxxxxxxxxxx",x.item)
                w = x.remove()
                if pro[w] == False:
                    out += [w]
                    pro[w] = True
                    print("pro",pro)
                for y in range(len(self.vert[w])):
                    o = self.vert[w][y][0]
                    print("o", o,dis[o])
                    if dis[o] == False:
                        x.add(o)
                        print("add",x.item)
                        dis[o] = True
                        print("dis",dis)
            return out

class queue:
    def __init__(self):
        self.item = []

    def add(self, val):
        self.item += [val]
        return True

    def remove(self):
        r = self.item[0]
        self.item = self.item[1:len(self.item)]
        return r

    def empty(self):
        return self.item == []

class stack:
    def __init__(self):
        self.item = []

    def empty(self):
        return self.item == []

    def add(self, item):
        self.item += [item]
        return True

    def remove(self):
        r = self.item[len(self.item)-1]
        self.item = self.item[0:len(self.item)-1]
        return r

x = graph()
x.add_vertex(8)
#x.add_edge(0,1,True,1)
x.add_edge(0,2,True,0.6)
x.add_edge(0,3,True,1.5)
x.add_edge(1,4,True,1)
x.add_edge(1,5,True,1)
#x.add_edge(6,5,True,1)
x.add_edge(6,0,True,1)
x.add_edge(3,6,True,1)
x.add_edge(3,6,True,1)
x.add_edge(3,7,True,1)
print(x.traverse(None,True))