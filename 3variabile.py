a=int(input("Introduceti primul num:"))
b=int(input("Introduceti al doilea num:"))
c=int(input("Introduceti al treilea num:"))
def divizor():
    x=[]
    for i in range(1, int(max(a,b,c)/2)+1):
        if a%i==0 and b%i==0 and c%i==0:
            x.append(i)
    return x

print("Cel mai mare divizor comun este:", divizor())

def multiplu():
    maimare=0
    if a > b & a >c:
        maimare = a
    elif b > c & b > a:
        maimare = b
    else:
        maimare = c

    while(True):
       if ((maimare % a == 0) and (maimare % b == 0) and (maimare % c == 0)):
           multiplu = maimare
           break
    maimare += 1

    return multiplu
print("Cel mai mic multiplu ai numerelor este=", multiplu())

def min():
    x=0
    if a<b and a<c:
        x=a
    elif b<a and b<c:
        x=b
    else:
        x=c
    return x

print("Minimul functiei este:", min())

def maxim():
    x=0
    if a>b and a>c:
        x=a
    elif b>a and b>c:
        x=b
    else:
        x=c
    return x

print("Maximul functiei este:", maxim())

