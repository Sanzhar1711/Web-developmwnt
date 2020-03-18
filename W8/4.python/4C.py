num = int(input('n: '))
input = input('list: ').split()

if len(input) != num:
    print
    "ERR:", num, "vs", len(input)
else:
    print
    len([x for x in input if int(x) > 0])
