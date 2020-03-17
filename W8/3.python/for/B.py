a = int(input())
b = int(input())
c = int(input())
d = int(input())

for num in range(a,b):
    if(num % c == d):
        print(num)
    num+=1