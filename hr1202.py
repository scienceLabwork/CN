# CN LAB Q3 Byte stuffing
delimeter = "ESC"
flag = "RUD"

x = []
k = []
ml = int(input("Insert the number of frames: "))
for i in range(ml):
    frame = input("Insert Frame{}: ".format(str(i+1)))
    x.append(frame)
    k.append(frame)

    if(delimeter in x[i]):
        m = x[i].index(delimeter)
        x[i] = list(x[i])
        x[i].insert(m,"\033[1;32m"+delimeter+"\033[0m")
        x[i] = ''.join(x[i])
        k[i] = list(k[i])
        k[i].insert(m,"\033[1;31m")
        k[i].insert(m+len(delimeter)+1, "\033[0m")
        k[i] = ''.join(k[i])
        print(1)

    if(flag in x[i]):
        m = x[i].index(flag)
        x[i] = list(x[i])
        x[i].insert(m,"\033[1;32m"+delimeter+"\033[0m")
        x[i] = ''.join(x[i])
        k[i] = list(k[i])
        k[i].insert(m,"\033[1;31m")
        k[i].insert(m+len(delimeter)+1, "\033[0m")
        k[i] = ''.join(k[i])
        print(1)

print("\nSENDER SIDE:")
print(flag+''.join(x)+flag)

print("\nRECEIVER SIDE:")
print(flag+''.join(k)+flag)