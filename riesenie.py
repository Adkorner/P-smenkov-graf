# 11. zadanie: pismenkovy graf
# autor: Adam Lopaška
# datum: 30.5.2022


class Graph:
    def __init__(self, file_name):
        self.graf = {}
        with open(file_name, 'r') as file:
            for riadok in file:
                riadok = riadok[:-1].split(":")
                #print(riadok)
                if len(riadok) == 2:
                    v1 = riadok[0]
                    v2 = riadok[1]
                    try:
                        #self.graf[v1] = {}
                        self.graf[v1].add((v2,""))
                    except:
                        self.graf[v1] = set()
                        self.graf[v1].add((v2,""))
                    try:
                        #self.graf[v1] = {}
                        self.graf[v2].add((v1,""))
                    except:
                        self.graf[v2] = set()
                        self.graf[v2].add((v1,""))
                elif len(riadok) == 3:
                    v1 = riadok[0]
                    val = riadok[1]
                    v2 = riadok[2]
                    try:
                        #self.graf[v1] = {}
                        self.graf[v1].add((v2,val))
                    except:
                        self.graf[v1] = set()
                        self.graf[v1].add((v2,val))
                    try:
                        #self.graf[v1] = {}
                        self.graf[v2].add((v1,val))
                    except:
                        self.graf[v2] = set()
                        self.graf[v2].add((v1,val))              
        #print(self.graf)
    def get_edge(self, v1, v2):
        for v in self.graf[v1]:
            if v[0] == v2:
                return v[1]
        return None

    def vertices(self):
        mena = set()
        for v in self.graf:
            mena.add(v)
        return mena


    def solve(self, v1):
        nic = False
        for v,val in self.graf[v1]:
            if val == "" or val =="a":
                nic = True
        if nic is False:
            return []
        self.riesenie = []
        self.backtracking([v1],[],[])
        najdlhsie = []
        if len(self.riesenie) == 0:
            return []
        for cesta in self.riesenie:
            cesta = cesta[0]
            if najdlhsie == []:
                najdlhsie.append(cesta)
            elif len(najdlhsie[0]) < len(cesta):
                najdlhsie = [cesta]
            elif len(najdlhsie[0]) == len(cesta):
                najdlhsie.append(cesta)
        jedine = []
        for road in najdlhsie:
            if road not in jedine:
                jedine.append(road)
        return jedine

    def nemoze3(self,vrchol, hrany):
        nem = True
        for v2, val in self.graf[vrchol]:
            if (vrchol,v2,val) not in hrany and (v2,vrchol,val) not in hrany:
                nem = False
        return nem
        
    def backtracking(self,cesta,hrany,znaky):
        if self.nemoze3(cesta[-1],hrany) or self.nemoze(znaky): #self.graf[cesta[-1]] == set()
            if len(znaky) >=2:
                cesta = self.nemoze2(znaky, cesta)
            self.riesenie.append((cesta[:],znaky))
        else:
            for v, val in self.graf[cesta[-1]]:
                if (cesta[-1],v,val) not in hrany and (v,cesta[-1],val) not in hrany:
                    hrany.append((cesta[-1],v,val))
                    hrany.append((v,cesta[-1],val))
                    val = self.uprav(val,znaky)
                    self.backtracking(cesta + [v],hrany + [(cesta[-1],v,val),(v,cesta[-1],val)], znaky + [val])
                    hrany.pop()
                    hrany.pop()

    def uprav(self,val,znaky):
        if val == "":
            if len(znaky) == 0:
                return "a"
            if znaky[-1] == "c":
                return "a"
            elif znaky[-1] == "a":
                return "b"
            if znaky[-1] == "b":
                return "c"
        return val

    def nemoze(self, znaky):
        if len(znaky) == 0:
            return False
        if len (znaky) == 1:
            if znaky[0] != "a":
                return True
            else:
                return False
        if znaky[-2] == "a" and znaky[-1] != "b":
            return True
        elif znaky[-2] == "b" and znaky[-1] != "c":
            return True
        elif znaky[-2] == "c" and znaky[-1] != "a":
            return True
        return False

    def nemoze2(self, znaky,cesta):
        zmen = False
        if len(znaky) == 0:
            return False
        if len (znaky) == 1:
            if znaky[0] != "a":
                zmen =  True
        if znaky[-2] == "a" and znaky[-1] != "b":
            zmen =  True
        elif znaky[-2] == "b" and znaky[-1] != "c":
            zmen =  True
        elif znaky[-2] == "c" and znaky[-1] != "a":
            zmen =  True
        if zmen:
            return cesta[:-1]
        else:
            return cesta

if __name__ == '__main__':
    g = Graph('subor2.txt')
    #print(g.vertices())
    #print(g.get_edge("mo","qa"))
    print('vertices =', g.vertices())
    '''for v1, v2 in ('mo', 'ub'), ('er', 'ub'), ('er', 'mo'):
        print(f'get_edge({v1!r},{v2!r}) = {g.get_edge(v1,v2)!r}')'''
    riesenie = g.solve('qa')
    print('pocet rieseni =', len(riesenie))
    print(*riesenie, sep='\n')