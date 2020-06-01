import random as r
def pswd_generator(a,b,c,d):
    password=''
    for i in range(2):
        p1=r.choice(a)
        password+=p1
        p2=r.choice(b)
        password+=p2
        p3=r.choice(c)
        password+=p3
        p4=r.choice(d)
        password+=p4
    print("\n",password)
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b='0123456789'
c='abcdefghijklmnopqrstuvwxyz'
d='!@#$%&*~'
pswd_generator(a,b,c,d)



