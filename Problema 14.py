v=[]
s=0
max=0
min=0

n=int(input("\nNumar elemente lista: "))
print("\n")

for i in range(n):
    valoare = int(input("Introduceti v[" + str(i) + "]: "))
    v.append(valoare)

    if v[i]>max :
        max=v[i]
    if v[i]<min or min==0 :
        min=v[i]

print("\nCel mai mare numar din lista este ",max)
print("Cel mai mic numar din lista ",min,".\n")

