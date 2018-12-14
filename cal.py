import math
def cal1(a):
    s=a
    j=0
    s1=""
#    check=int('0')
#    for i in s:
#        if i.isalpha():
#            check=check+1
#            if check==1:
#                return int('0')
#        else:
#            check=int('0')
    for i in s:
        if i.isnumeric():
            s1=s1+s[j]
            j=j+1
        else:
            s1=s1+"_"+s[j]+"_"
            j=j+1
    b=s1.split("_")
    for i in range(len(b)):
        if i%2==0:
            b[i]=int(b[i])
    k=0
    while k<10:
        j=0
        for i in b:
            if i=='^':
                n=b[j-1]
                m=b[j+1]
                b[j-1]=math.pow(n,m)
                del(b[j])
                del(b[j])
            j=j+1
        k=k+1
    k=0
    while k<10:
        j=0
        for i in b:
            if i=='*':
                n=b[j-1]
                m=b[j+1]
                b[j-1]=m*n
                del(b[j])
                del(b[j])
            j=j+1
        k=k+1
    k=0
    while k<10:
        j=0
        for i in b:
            if i=='/':
                n=b[j-1]
                m=b[j+1]
                b[j-1]=n/m
                del(b[j])
                del(b[j])
            j=j+1
        k=k+1
        k=0
        while k<10:
            j=0
            for i in b:
                if i=='-':
                    n=b[j-1]
                    m=-b[j+1]
                    b[j-1]=n+m
                    del(b[j])
                    del(b[j])
                j=j+1
            k=k+1
        k=0
        while k<10:
            j=0
            for i in b:
                if i=='+':
                    n=b[j-1]
                    m=b[j+1]
                    b[j-1]=n+m
                    del(b[j])
                    del(b[j])
                j=j+1
            k=k+1
        return b[0]