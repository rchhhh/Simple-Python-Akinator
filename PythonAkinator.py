def rmvrai():
    for i in range(len(ma)):
        for j in range(len(ma[i][1])):
            if ma[-1][1].count(ma[i][1][j]) == 0  :
                ma[i][1][j] = "0"
    return

def rmfaux():
    for i in range(len(ma)-1):
        for j in range(len(ma[-1][1])):
            for s in range(ma[-1][1].count(ma[-1][1][j])):
                if ma[i][1].count(ma[-1][1][j]) > 0 :
                    ma[i][1].remove(ma[-1][1][j])
    return

def nestedlen(liste):
    size = 0
    for item in liste:
        if type(item) == list :
            size += nestedlen(item)
        else :
            size += 1
    return size

def supro():
    for i in range(len(ma)):
        if ma[i][1].count("0") > 0 :
            for g in range(ma[i][1].count("0")) :
                ma[i][1].remove("0")
    return

def suplist():
    c = len(ma)
    b = 0 #var du while suplist
    while b < c : 
        if len(ma[b][1]) == 0 :
            del ma[b]
            c = c-1
        
        else : 
            b = b+1
    return

def com() :
    oo = 0
    for i in range(len(ma)) : 
        for j in range(len(ma[i][1])) :
            oo += ma[i][1][j].count(ma[-1][1][0])
    return oo
#       
#        if type(item) == list :
#            oo += list.count(ma[0][1][0])
#    return

def testfin() : 
    if nestedlen(ma) == 2*len(ma) and len(ma) == com() :
        return 1
    else : 
        return 0

print("put a presentation text here of you want")                         

def rmvrai():
    for i in range(len(ma)):
        for j in range(len(ma[i][1])):
            if ma[-1][1].count(ma[i][1][j]) == 0  :
                ma[i][1][j] = "0"
    return

def rmfaux():
    for i in range(len(ma)-1):
        for j in range(len(ma[-1][1])):
            for s in range(ma[-1][1].count(ma[-1][1][j])):
                if ma[i][1].count(ma[-1][1][j]) > 0 :
                    ma[i][1].remove(ma[-1][1][j])
    return

def nestedlen(liste):
    size = 0
    for item in liste:
        if type(item) == list :
            size += nestedlen(item)
        else :
            size += 1
    return size

def supro():
    for i in range(len(ma)):
        if ma[i][1].count("0") > 0 :
            for g in range(ma[i][1].count("0")) :
                ma[i][1].remove("0")
    return

def suplist():
    c = len(ma)
    b = 0 #var du while suplist
    while b < c : 
        if len(ma[b][1]) == 0 :
            del ma[b]
            c = c-1
        
        else : 
            b = b+1
    return

def com() :
    oo = 0
    for i in range(len(ma)) : 
        for j in range(len(ma[i][1])) :
            oo += ma[i][1][j].count(ma[-1][1][0])
    return oo
#       
#        if type(item) == list :
#            oo += list.count(ma[0][1][0])
#    return

def testfin() : 
    if nestedlen(ma) == 2*len(ma) and len(ma) == com() :
        return 1
    else : 
        return 0



ma = [[attribute, [people, people2]]]
w = 0
#print(ma[-1][0])
while w != 1 : 
    ma = sorted(ma, key=nestedlen)
    a = input("Is the person " + ma[-1][0] + " ? ")
    if int(a) == 1 :
        rmvrai()
    else :
        rmfaux()
    
    supro()
    suplist()
    ma = sorted(ma, key=nestedlen)
    if testfin() == 1 :
        w = 1
    else : 
        del ma[-1]
print(ma[-1][1][0])