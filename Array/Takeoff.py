for _ in range(int(input())):
    n,p,q,r = map(int,input().split())
    count = 0
    for i in range(1,n+1):
        if(i%p==0 and i%q!=0 and i%r!=0):
            count+=1
        elif(i%p!=0 and i%q==0 and i%r!=0):
            count+=1
        elif(i%p!=0 and i%q!=0 and i%r==0):
            count+=1
        else:
            pass
    print(count)
