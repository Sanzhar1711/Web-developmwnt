import math

a = int(input())
b = int(input())

for num in range(math.sqrt(a),math.sqrt(b)):
    print(num*num)
num+=1