def num_cifre(a):
    num=0
    while a!=0:
        r=a%10
        a//=10
        num=num+1
    return (num)

def num_pare(a):
    b=[]
    while a>0:
        b.append(a%10)
        a//=10
    pare=[]
    for i in b:
        if i%2==0 :
            pare.append(i)
    c=len(pare)
    return (c)

def num_impare(a):
    b=[]
    while a>0:
        b.append(a%10)
        a//=10
    impare=[]
    for i in b:
        if i%2!=0 :
            impare.append(i)
    c=len(impare)
    return (c)

def suma(a):
    s=0
    while a>0:
        r=a%10
        a//=10
        s=s+r
    return (s)

def max(a):
    max=0
    while a>0:
        r=a%10
        a//=10
        if r>max:
            max=r
    return (max)

def min(a):
    min=9
    while a>0:
        r=a%10
        a//=10
        if r<min:
            min=r
    return (min) 

def media_aritmetica(a):
    s=0
    b=[]
    while a>0:
        r=a%10
        a//=10
        s=s+r
        b.append(r)
        numcifre=len(b)
        m=s//numcifre
    return (m)

def cifre_repetate(a):
    b=[]
    a=str(a)
    for i in a:
        if a.count(i)>=2:
            if i not in b:
                b.append(i)
    return (b)

def cifre_separate(a):
    sep=str(a)[::1]
    b=list(sep)
    c=' '.join(b)
    return (c)

def div(a):
    b=[]
    for i in range (1,a+1):
        if (a%i==0):
            b.append(i)
    return (b)

def invers(a):
    num_inversat=0
    while a>0:
        b=a%10
        num_inversat=(num_inversat*10)+b
        a//=10
        c=str(num_inversat)
    return (c)

def cel_mai_mare(a):
    b=[]
    while a>0:
        c=a%10
        b.append(c)
        a//=10
    b.sort(reverse=True)
    c="".join(str(i) for i in b)
    return (c)

def num_prim(a):
    if a<=1:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True
n= int(input('Introduceti numarul n: '))
if n<100000:
    print("In numar sunt",num_cifre(n),"cifre")
    print("In numar sunt",num_pare(n),"cifre pare")
    print("In numar sunt",num_impare(n),"cifre impare")
    print("Suma cifrelor este egala cu",suma(n))
    print("Cifra maxima este egala cu",max(n))
    print("Cifra minima este egala cu",min(n))
    print("Media aritmetica este egala cu",media_aritmetica(n))
    print("Cifre care se repeta de 2 sau mai multe ori sunt",cifre_repetate(n))
    print("Cifrele separate printr-un spatiu sunt",cifre_separate(n))
    print("Divizori sunt",div(n))
    print("Inversul numarului este",invers(n))
    print("Cel mai mare numaru posibil creat este",cel_mai_mare(n))
    if num_prim(n)==True:
        print("Numarul",n," este prim")
    else:
        print("Numarul",n,"nu este prim")
else:
    print("Numarul introdus nu corespunde conditiei")