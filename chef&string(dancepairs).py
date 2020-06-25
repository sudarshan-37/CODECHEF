t = int(input())

for i in range(t):
    
    s = input()
    l = len(s)
    count = 0
    i = 1
    while(i<l):

        if(s[i]=='x'):
            if(s[i-1]=='y'):
                count += 1
                i += 2
            else:
                i += 1
        
        else:
            if(s[i-1]=='x'):
                count += 1
                i += 2
            else:
                i += 1
            
    print(count)