n=int(input("Primul numar:"))
m=int(input("Al doilea numar:"))
a=n
b=m

while m!=n :
    if m>n :
        m-=n
    else :
        n-=m

print("Cmmdc al numerelor ",a," si ",b," este ",n,".\n")