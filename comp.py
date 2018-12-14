import math
def find(s):
    n=s
    j=0
    s1=""
    s2=""
    for i in n:
        if i.isnumeric():
            s1=s1+n[j]
            j=j+1
        else:
            s1=s1+"_"+n[j]+"_"
            j=j+1
    j=0
    for i in s1:
        if i=='_' and (j==0 or j==len(s1)-1):
            j=j+1
            continue
        else:
            s2=s2+i
        j=j+1
    b=s2.split("_")
    if b[0]=='-':
        b.remove(b[0])
        b.insert(1,-int(b[0]))
        b.remove(b[0])
    val=int(b[0])
    b.remove(b[0])
    b.insert(0,val)
    if b[1]=='-' or b[1]=='+':
        if b[1]=='-':
            val=-int(b[2])
        else:
            val=int(b[2])
        b.remove(b[1])
        b.insert(1,'+')
        b.insert(3,val)
        b.remove(b[2])
    return b
def modulus(a):
    if a=='':
        return 0
    s=find(a)
    ans=(math.pow(int(s[0])*int(s[0])+int(s[2])*int(s[2]),1/2))
    return ans
def argument(a):
    if a=='':
        return 0
    s=find(a)
    ans=math.atan(int(s[2])/int(s[0]))*180/3.14
    return ans
def ab(a,b,ch):
    if a=='' or b=='':
        return 0
    s1=find(a)
    s2=find(b)
    ans=""
    if ch=='+':
        s=s1[0]+s2[0]
        ans=ans+str(s)
        s=s1[2]+s2[2]
        if s>=0:
            ans=ans+"+"+str(s)+"i"
        if s<0:
            s=-s
            ans=ans+"-"+str(s)+"i"
    if ch=='-':
        s=s1[0]-s2[0]
        ans=ans+str(s)
        s=s1[2]-s2[2]
        if s>=0:
            ans=ans+"+"+str(s)+"i"
        if s<0:
            s=-s
            ans=ans+"-"+str(s)+"i"
    if ch=='*':
        s=s1[0]*s2[0]-s1[2]*s2[2]
        ans=ans+str(s)
        s=s1[0]*s2[2]+s1[2]*s2[0]
        if s>=0:
            ans=ans+"+"+str(s)+"i"
        if s<0:
            s=-s
            ans=ans+"-"+str(s)+"i"
    if ch=='/':
        s=(s1[0]*s2[0]+s1[2]*s2[2])/(s2[0]*s2[0]+s2[2]*s2[2])
        ans=ans+str(s)
        s=(-(s1[0]*s2[2])+s1[2]*s2[0])/(s2[0]*s2[0]+s2[2]*s2[2])
        if s>=0:
            ans=ans+"+"+str(s)+"i"
        if s<0:
            s=-s
            ans=ans+"-"+str(s)+"i"
    return ans
def abc(a,b,c,ch1,ch2):
    if a=='' or b=='' or c=='':
        return 0
    ans=""
    s1=find(a)
    s2=find(b)
    s3=find(c)
    if ch1=='+' and ch2=='+':
        s=s1[0]+s2[0]+s3[0]
        ans=ans+str(s)
        s=s1[2]+s2[2]+s3[2]
        if s>=0:
            ans=ans+"+"+str(s)+"i"
        else:
            ans=ans+"-"+str(s)+"i"
    if ch1=='-' and ch1=='-':
        s=s1[0]-s2[0]-s3[0]
        ans=ans+str(s)
        s=s1[2]-s2[2]-s3[2]
        if s>=0:
            ans=ans+"+"+str(s)+"i"
        else:
            ans=ans+"-"+str(s)+"i"
    if ch1=='+' and ch2=='-':
        s=s1[0]+s2[0]-s3[0]
        ans=ans+str(s)
        s=s1[2]+s2[2]-s3[2]
        if s>=0:
            ans=ans+"+"+str(s)+"i"
        else:
            ans=ans+"-"+str(s)+"i"
    if ch1=='*' and ch2=='*':
        ans=ab(a,b,'*')
        ans=ab(ans,c,'*')
    if ch1=='*' and ch2=='/':
        ans=ab(a,b,'*')
        ans=ab(ans,c,"/")
    if ch1=='/' and ch2=='*':
        ans=ab(b,c,'*')
        ans=ab(a,ans,'/')
    return ans

