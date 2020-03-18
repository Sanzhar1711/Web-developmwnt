a = [int(i) for i in input().split()]
b = filter(lambda x: x%2==0, a)
print(*b)