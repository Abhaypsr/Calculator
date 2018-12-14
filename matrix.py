
def determinant(a,r,c):
    if r==2 and c==2:
        ans=a[0]*a[3]-a[2]*a[1]
    if r==3 and c==3:
        ans=a[0]*(a[4]*a[8]-a[5]*a[7])-a[1]*(a[3]*a[8]-a[5]*a[6])+a[2]*(a[3]*a[7]-a[4]*a[6])
    print(ans)
    return ans

def ab(a,r1,c1,b,r2,c2,ch):
    ans=[]
    if ch=='+':
        if r1==r2 and c1==c2:
            for i in range(r1*c1):
                ans.append(a[i]+b[i]) 
    if ch=='-':
            if r1==r2 and c1==c2:
                for i in range(r1*c1):
                    ans.append(a[i]-b[i]) 
    if ch=='*':
        s=0
        v=0
        if c1==r2:
            for i in range(r1):
                if i==0:
                    p=0
                if i==1:
                    p=c1
                if i==2:
                    p=2*c1
                for j in range(c2):
                    k=p
                    v=j
                    s=0
                    for q in range(r2):
                        s=s+a[k]*b[v]
                        k=k+1
                        v=v+c2
                    ans.append(s)
    print(ans)
    return ans
