print("Script to add peoples or atributes, can't remember what i put in french here")
lc = ["list of peoples you already added", "person1", "person2"]
ma = [[atrribute, [person]], [attribute, [person]]]
mb = [[atrribute, [person]], [attribute, [person]]]
a = int(input("Add person(1) or attribute(2) ? "))
if a == 1 :
    b = str(input("Person name ? "))
    for i in range(len(ma)) :
        z = int(input("Is the person " + ma[i][0] + "? > " ))
        if z == 1 :   
            mb[i][1].append(b)
else: 
    d = str(input("Atrribute name ? "))
    mb.append([d, []])
    for i in range(len(lc)) : 
        p = int(input(lc[i] + " corespond to the attribute ? "))
        if p == 1 :
            mb[-1][1].append(lc[i])
print(mb)
