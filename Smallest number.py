n=int(input("Enter number of elements : "))
l=list(map(int,input("Enter the elements : ").split()))
for i in range(n-1):
    if l[i+1]!=(l[i]+1):
        print("Smallest positive missing natural number is",l[i]+1)
        break
else:
    print("Smallest positive missing natural number is",l[-1]+1)