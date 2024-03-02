r1=[]
r2=[]
#k1,k2,k3,c1,c2,c3,c4
k1=[0,1.5,0.9,1.3,2.5,2.2,3]
k2=[1.5,0,0.5,0.8,0.5,1.1,4.2]
k3=[0.9,0.5,0,3.1,2.8,1.5,0.9]

c1=[1.3,0.8,3.1,0,0.8,0.9,2.1]
c2=[2.5,0.5,2.8,0.8,0,2.2,1.3]
c3=[2.2,1.1,1.5,0.9,2.1,0,0.7]
c4=[3,4.2,0.9,2.1,1.3,0.7,1]

m1=['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10']
m2=['item11', 'item12', 'item13', 'item14', 'item15', 'item16', 'item17', 'item18', 'item19', 'item20']
m3=['item21', 'item22', 'item23', 'item24', 'item25', 'item26', 'item27', 'item28', 'item29', 'item30']

prep1=[2,4,17,8,5,3,7,11,14,15]
prep2=[2,4,17,8,5,3,7,11,14,15]
prep3=[2,4,17,8,5,3,7,11,14,15]

cust_nos=4
l1=[]
l2=[]
l3=[]

for i in range(cust_nos):
    print("\n")
    print("C{0}: ".format(i+1))
    x='y'
    while x=='y':
        x=input("Do You want to order(y/n): ")
        #print(x)
        if x=='n':
            break
        l1.append("C{0}".format(i+1))
        ch=(input("Enter Kitchen to order from: "))
        if ch=="k1":
            l3.append('k1')
            print(m1)
            y=list(map(int,input("Enter item no.s to order : ").split()))
            for j in range(len(y)):
                y[j]-=1
        elif ch=="k2":
            l3.append('k2')
            print(m2)
            y=list(map(int,input("Enter item no.s to order : ").split()))
            for j in range(len(y)):
                y[j]-=11
        elif ch=="k3":
            l3.append('k3')
            print(m3)
            y=list(map(int,input("Enter item no.s to order : ").split()))
            for j in range(len(y)):
                y[j]-=21
        print(y)
        l2.append(y)
print(l1,l2)    
print(l3)

l4=[]
for i in range(len(l3)):
    if l3[i]=='k1':
        s=0
        for j in range (len(l2[i])):
            s+=prep1[l2[i][j]]
    elif l3[i]=='k2':
        s=0
        for j in range (len(l2[i])):
            s+=prep2[l2[i][j]]
    elif l3[i]=='k3':
        s=0
        for j in range (len(l2[i])):
            s+=prep3[l2[i][j]]
    l4.append(s)   
print(l4)


for i in range(len(l1)-1):
    order=[]
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j] and l3[i]==l3[j] and abs(l4[i]-l4[j])<=10:
            if i not in order:
                order.append(i)
            if j not in order:
                order.append(j)
    if len(r1)<=len(r2):
        for i in r2:
            if i in order:
                r2.extend(order)
                break
        else:
            r1.extend(order)
    else:
        r2.extend(order)

        
for i in range(len(l1)-1):
    order=[]
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j] and abs(l4[i]-l4[j])<=10 and l3[i]!=l3[j]:
            y=int(l3[j][1])-1
            #print("y",y)
            if l3[i]=='k1':
                a=k1[y]
            if l3[i]=='k2':
                a=k2[y]
            if l3[i]=='k3':
                a=k3[y]
            #print("a",a)
            if a<=1:
                if i not in order:
                    order.append(i)
                if j not in order:
                    order.append(j)
        #print(order)
    
    if len(r1)<=len(r2):
        for i in r2:
            if i in order:
                r2.extend(order)
                break
        else:
            r1.extend(order)
    else:
        for i in r1:
            if i in order:
                r1.extend(order)
                break
        else:
            r2.extend(order)


for i in range(len(l1)-1):
    order=[]
    for j in range(i+1,len(l1)):
        if l1[i]!=l1[j] and l3[i]==l3[j] and abs(l4[i]-l4[j])<=10:
            y=int(l1[j][1])+2
            if l1[i]=='C1':
                a=c1[y]
            if l1[i]=='C2':
                a=c2[y]
            if l1[i]=='C3':
                a=c3[y]
            if l1[i]=='C4':
                a=c4[y]
            #print(a,y,i,j)
            if a<=1:
                if i not in order:
                    order.append(i)
                if j not in order:
                    order.append(j)
    if len(r1)<=len(r2):
        for i in r2:
            if i in order:
                r2.extend(order)
                break
        else:
            r1.extend(order)
    else:
        for i in r1:
            if i in order:
                r1.extend(order)
                break
        else:
            r2.extend(order)


for i in range(len(l1)-1):
    order=[]
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j] and l3[i]!=l3[j] and abs(l4[i]-l4[j])<=10:
            y=int(l3[j][1])-1
            z=int(l1[i][1])+2
            if l3[i]=='k1':
                d1==k1[y]
                d2=k1[z]
            if l3[i]=='k2':
                d1=k2[y]
                d2=k2[z]
            if l3[i]=='k3':
                d1=k3[y]
                d2=k3[z]
            if l3[j]=='k1':
                a=k1[y]
            if l3[j]=='k2':
                a=k2[y]
            if l3[j]=='k3':
                a=k3[y]
            if d1+a<=d2+1:
                if i not in order:
                    order.append(i)
                if j not in order:
                    order.append(j)
    if len(r1)<=len(r2):
        for i in r2:
            if i in order:
                r2.extend(order)
                break
        else:
            r1.extend(order)
    else:
        for i in r1:
            if i in order:
                r1.extend(order)
                break
        else:
            r2.extend(order)


for i in range(len(l1)-1):
    order=[]
    for j in range(i+1,len(l1)):
        if l1[i]!=l1[j] and l3[i]==l3[j] and abs(l4[i]-l4[j])<=10:
            y=int(l1[i][1])+2
            z=int(l1[j][1])+2
            if l3[j]=='k1':
                d1=k1[y]
                d2=k1[z]
            if l3[j]=='k2':
                d1=k2[y]
                d2=k2[z]
            if l3[j]=='k3':
                d1=k3[y]
                d2=k3[z]
            if l1[i]=='C1':
                a=c1[z]
            if l1[i]=='C2':
                a=c2[z]
            if l1[i]=='C3':
                a=c3[z]
            if l1[i]=='C4':
                a=c4[z]
            if d1+a<=d2+1:
                if i not in order:
                    order.append(i)
                if j not in order:
                    order.append(j)
    if len(r1)<=len(r2):
        for i in r2:
            if i in order:
                r2.extend(order)
                break
        else:
            r1.extend(order)
    else:
        for i in r1:
            if i in order:
                r1.extend(order)
                break
        else:
            r2.extend(order)

print("\n")
print("Rider1: ",set(r1))
print("Rider2: ",set(r2))
