x={}
print("How many elements :",end=' ')
n=int(input())

for i in range(n):
    print("Key :",end=' ')
    k=input()
    print("Value :",end=' ')
    v=int(input())
    x.update({k:v})

print("Dict is :",x)