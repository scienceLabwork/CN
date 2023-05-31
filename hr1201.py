# CN LAB Q3 Bit stuffing
delimeter = "01111110"

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
        x[i][m:m+len(delimeter)] = ["\033[1;32m"]+x[i][m:m+len(delimeter)-2]+["0"]+x[i][m+len(delimeter)-2:m+len(delimeter)]+["\033[0m"]
        x[i] = ''.join(x[i])
        k[i] = list(k[i])
        k[i] = ["\033[1;31m"]+k[i][m:m+len(delimeter)-2]+k[i][m+len(delimeter)-2:m+len(delimeter)]+["\033[0m"]
        k[i] = ''.join(k[i])

print("\nSENDER SIDE:")
print(delimeter+''.join(x)+delimeter)

print("\nRECEIVER SIDE:")
print(delimeter+''.join(k)+delimeter)