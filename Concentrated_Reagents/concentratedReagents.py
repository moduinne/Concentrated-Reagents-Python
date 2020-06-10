class Reagent(object):
    def __init__(self,name,d,m,n,volM,volN):
        self.name = name
        self.d = d
        self.m = m
        self.n = n
        self.volM = volM
        self.volN = volN
    
    def __repr__(self):
        rep_str = "Name: {0}\nDensity: {1}\nMolarity: {2}\nNormality: {3}\nmL's needed to make 1L of 1M: {4} mL\nmL's needed to make 1L of 1N: {5} mL"
        return rep_str.format(self.n,self.dens,self.molar,self.norm,self.volM,self.volN)


chemDic = {}
path = "rhodium_scrap.txt"
file = open(path, "r")
line = file.readline()
index = 0
chemAtts = []
reagents = []
while line != "":
    res = index % 6
    chemAtts.append(line.strip())
    if res == 5:
        reagent = Reagent(chemAtts[0],
                          chemAtts[1],
                          chemAtts[2],
                          chemAtts[3],
                          chemAtts[4],
                          chemAtts[5])
        chemDic[reagent.name] = reagent
        chemAtts.clear()
    index += 1
    line = file.readline()	
file.close()
def show():
    for key in chemDic:
        print(key)
def start():
    show()
    print("\n--This program navigates the concentrated Reagents Above--")
    print("Type in the chemical of interest")
    print("m=concentrated molarity")
    print("d=concentrated density")
    print("n=concentrated normality")
    print("volM=mL's required to make 1000mL of 1M")
    print("volN=mL's required to make 1000mL of 1N")
    b = True
    allowed = ["show","quit","m","n","d","volM","volN"]
    attributes = ["m","n","d","volM","volN"]
    while b:
        q = input("Chemical of interest or known command: ")
        if q not in allowed and q not in chemDic:
            print("not a chemical in list or command try again")
        elif q in chemDic:
            p = input("m,n,d,volM,or volN: ")
            if p in attributes:
                if p =="m":
                    print (chemDic[q].m + " Molarity in concentrated form")
                elif p =="d":
                    print (chemDic[q].d + " g/mL Density in concentrated form")
                elif p =="volM":
                    print(chemDic[q].volM + " ml in 1000ml to make 1M solution")
                elif p == "volN":
                    print(chemDic[q].volN + " ml in 1000ml to make 1N solution")
                elif p == "n":
                    print(chemDic[q].n + " Normality in concentrated form")
            elif p not in attributes:
                print("error try again, no command of that type")
        elif q == "quit":
            b=False
        elif q == "show":
            show()
            
        

start()   
#print(chemDic["Acetic acid 99.5%"].volM)
