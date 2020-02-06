from array import*

x=array('i',[])

print('how many elements :',end=" ")
n=int(input())

for i in range(n):
    print("Enter element :",end=" ")
    x.append(int(input()))
print('Original Array :',x)

print('Enter element to search :',end=" ")
s=int(input())

try:
    pos=x.index(s)
    print('Value found at position :',pos+1)
except ValueError:
    print("Not found")

print(len(x))

# class BookX:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self, other):
#         return self.pages+other.pages
# class Booky:
#     def __init__(self,pages):
#         self.pages = pages
#
# b1=BookX(100)
# b2=Booky(200)
# print(b1+b2)

