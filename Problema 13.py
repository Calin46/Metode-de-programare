v=[]
s=0

n=int(input("\nNumar elemente lista: "))


for i in range(n):
    valoare = int(input("Introduceti v[" + str(i) + "]: "))
    v.append(valoare)
    s=s+v[i]

m=s/n

print("\nSuma elementelor din lista este",s,".")
print("Media elementelor din lista este",m,".")
