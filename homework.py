import math

#a)Suma numerelor;
def sum(a,b):
    sum = a+b
    return print("a)Suma",sum)
#b)Prodsul numerelor;
def produs(a,b):
    prod = a*b
    return print("b)Produsul",prod)
#c)Media aritmetica a numerelor;
def media(a,b):
    med = (a+b)/2
    return print("c)Media Aritmetica",med)
#d)Cel mai mare divizor comun;
def mared(a,b):
    md = math.gcd(a,b)
    return print("d)Cel mai mare divizor comun",md)
#e)Cel mai mic multiplu comun;
def micm(a,b):
    mm = math.lcm(a,b)
    return print("e)Cel mai mic multiplu comun",mm)
#f)Numarul minim;
def minimul(a,b):
    minim = min(a,b)
    return print("f)Minimul",minim)
#g)Numarul maxim;
def maximul(a,b):
    maxim = max(a,b)
    return print("g)Maximul",maxim)
#h)a+b=c;
def sumaformat():
    a=int(input("dati primul numar intreg:"))
    b=int(input("dati al doilea numar intreg:"))
    c = a + b 
    return print("h)",a,"+", b ,"=",c)
#i)a*b=c;
def produsformat():
    a=int(input("dati primul numar intreg:"))
    b=int(input("dati al doilea numar intreg:"))
    c = a * b
    return print("i)",a,"*", b ,"=",c)
#j)Toti divizorii comuni;
def divizoricomuni(a,b):
    astr=[]
    bstr=[]
    for i in range (1,a+1):
        if (a%i==0):
            astr.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bstr.append(j)
    c=set(astr).intersection(bstr)
    z=list(c)
    return print("j)Divizorii comuni",z)
#k) Cinci multipli comuni;
def multiplicomun(a,b):
    cmc=[]
    if b>a:
        multi=b
    elif a>b:
        multi=a
    else:
        multi=b
    while len(cmc)<5:
        if ((multi%a==0)and(multi%b==0)):
            cmc.append(multi)
            multi +=1
        else:
            multi +=1
    return print("k) Cinci multipli comuni",cmc)

#l)Cifrele care se contin in ambele numere;
def cifrecomun(a,b):
    astr=[]
    bstr=[]
    for i in str(a):
        astr.append(int(i))
    for j in str(b):
        bstr.append(int(j))
    c=set(astr).intersection(bstr)
    z=list(c)
    if len(z)!=0:
        return print("l) Cifrele comune",z)
    else:
        return print("l) Nu au cifre comune")

#m)Cifrele care sunt in primul numar si nu sunt in al doilea;
def cifreprim(a,b):
    astr=[]
    bstr=[]
    for i in str(a):
        astr.append(int(i))
    for j in str(b):
        bstr.append(int(j))
    c=set(astr).difference(bstr)
    z=list(c)
    return print("m) Cifrele care se contin in 1 numar si nu sunt in al 2 sunt ",z)
#n)Prieteni; 
def friends(a,b):
    sum1 = 1
    sum2 = 1
    i = 2
    while(i * i <= a):
        if (a % i == 0):
            sum1 = (sum1 + i +math.floor(a / i))
        i += 1
    j = 2
    while(j * j <= b):
        if (b % j == 0):
            sum2 = (sum2 + i +math.floor(b / j))
        j += 1
        if sum1==sum2:
            return print("n) PRIETENI")
        else:
            return print("n) NU SUNT PRIETENI") 

r= int(input('a: '))
t= int(input('b: '))
#a)
sum(r,t)
#b)
produs(r,t)
#c)
media(r,t)
#d)
mared(r,t)
#e)
micm(r,t)
#f)
minimul(r,t)
#g)
maximul(r,t)
#h)
sumaformat()
#i)
produsformat()
#j)
divizoricomuni(r,t)
#k)
multiplicomun(r,t)
#l)
cifrecomun(r,t)
#m)
cifreprim(r,t)
#n)
friends(r,t)





