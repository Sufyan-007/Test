N=int(input("Enter a number : "))
e=0
o=0
while N>0:
    d=N%10
    N=N//10
    if d%2==0:
        e+=d
    else:
        o+=d
print(e,o)