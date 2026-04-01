q = int(input().strip())
s = ""
stack = []
for _ in range(q):
    ops = input().split()
    if ops[0] == '1':
        stack.append(s)
        s += ops[1]
    elif ops[0] == '2':
        stack.append(s)
        k = int(ops[1])
        s = s[:-k]
    elif ops[0] == '3':
        k = int(ops[1])
        print(s[k - 1])
    elif ops[0] == '4':
        s = stack.pop()

