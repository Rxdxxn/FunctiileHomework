def cmmdc(a,b,c):
    divisor = min(a,b,c)
    while divisor > 0:
        if a%divisor == 0 and b%divisor == 0 and c%divisor==0:
            print('The GCD is', divisor)
        break
    divisor -= 1
    return 

x=int(input("Introduceti 1 numar: "))
y=int(input("Introduceti 2 numar: "))
z=int(input("Introduceti 3 numar: "))

(cmmdc(x,y,z))