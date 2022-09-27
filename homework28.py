import math

def maxim(a,b,c):
    if a>b and a>c:
        maxim=a
    if b>a and b>c:
        maxim=b
    if c>a and c>b:
        maxim=c
    if a==b==c:
        maxim=a
    return maxim

def minim(a,b,c):
    if a<b and a<c:
        minim=a
    if b<a and b<c:
        minim=b
    if c<a and c<b:
        minim=c
    if a==b==c:
        minim=a
    return minim

def cmmdc(a,b,c):
    divisor = minim(a,b,c)
    while divisor > 0:
        if a%divisor == 0 and b%divisor == 0 and c%divisor==0:
            break
    return divisor

def cmmmc(a,b,c):
    i=maxim(a,b,c)
    while True:
        if(i%a==0) and (i%b==0) and (i%c==0):
            q = i
            break
        i+=1
    return q

def divizorii(a,b,c):
    ddiv=[]
    for i in range(1, minim(a,b,c)+1):
        if a%i==b%i==c%i==0:
            ddiv.append(i)
    return ddiv

def multipli_3_mici(a,b,c):
    q=[]
    if a>b and a>c:
        mult=a
    elif b>a and b>c:
        mult=b
    else:
        mult=c
    while len(q)<3:
        if ((mult%a==0)and(mult%b==0))and(mult%c==0):
            q.append(mult)
            mult +=1
        else:
            mult +=1
    return q

def triunghi(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        q=(a+b+c)/2
        aria=round(math.sqrt(q*(q-a)*(q-b)*(q-c)),2)
        perimetru=q*2
        return print("Laturile pot forma un triunghi,Aria este: ",aria,", iar Perimetrul este: ",perimetru)
    else:
        return print("Laturile nu corespund conditiei!")

def ecuatia_grad2(a,b,c):
    d=((b**2)-(4*(a*c)))
    if d>0:
        rd=math.sqrt(int(d))
        x1=round((-b-rd)/(2*a),2)
        x2=round((-b+rd)/(2*a),2)
        return print("Solutiile ecuatiei sunt: ",x1,"si",x2)
    elif d==0:
        rd=math.sqrt(int(d))
        x1=x2=round((-b)/(4*a),2)
        return print("x1 este egal cu x2 si este egal cu: ",x1)
    elif d<0:
        return print("Nu sunt solutii reale")


x=int(input("Introduceti 1 numar: "))
y=int(input("Introduceti 2 numar: "))
z=int(input("Introduceti 3 numar: "))

#a
print("Cel mai mic numar este:",minim(x,y,z))
#b
print("Cel mai mare numar este:",maxim(x,y,z))
#c
print("Cel mai mare divizor comun este:",cmmdc(x,y,z))
#d
print("Cel mai mic multiplu este:",cmmmc(x,y,z))
#e
print("Divizorii comuni sunt:",divizorii(x,y,z))
#f
print("Cei mai mici 3 multipli comuni sunt:",multipli_3_mici(x,y,z))
#g
triunghi(x,y,z)
#h
ecuatia_grad2(x,y,z)