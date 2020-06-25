# cook your dish here
t = int(input())


for j in range(t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    items = input().split()
    items = [int(i) for i in items]
    loss = 0
    for i in items:
        if(i>k):
            loss += (i-k)
    print(loss)