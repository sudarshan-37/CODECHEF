# cook your dish here
import sys
cost = 5
answer = []
change = {5:0,10:0,15:0}
t=int(input())
if(t<1 or t>100):
    sys.exit()
    

for value in range(t):
    money = []
    change = {0:0,5:0,10:0,15:0}
    ppl = int(input())
    if(ppl<1 or ppl>10**3):
        sys.exit()
    money = input().split()
    for turn in range(ppl):
        ret = int(money[turn]) - cost
        change[int(money[turn])] += 1
        if ret == 0:
            bool = True
            continue
        if change[ret] != 0:
            change[ret] -= 1
            bool = True
            continue
        elif(change[ret-5]>=2):
            change[ret-5]-=2
            bool = True
            continue
        elif change[ret] == 0 :
            bool = False
            break
    if bool == True:
        answer.append("YES")
    else:
        answer.append("NO")
for value in answer:
    print(value)