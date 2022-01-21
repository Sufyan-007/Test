from random import randint
l=input("Enter space seperated list of words : ").split()
n=int(input("Enter number of guesses : "))
while(True):
    g=0
    w = l[randint(0,len(l)-1)]
    word=[[x,False] for x in w]
    while(g<n):
        print("Guesses remaining : ",n-g)
        for x in word:
            if x[1]:
                print(x[0],end="")
            else:
                print(end="_")
        print()
        s=input("Enter your guess : ")
        r=False
        f=True
        for i in range(len(word)):
            if word[i][0]==s:
                if word[i][1]==False:
                    word[i][1]=True
                    f=False
                else:
                    r=True
                    break
        if f:
            print("Wrong Guess")
            g+=1
        else:
            print("Correct Guess")
            g+=1
        if r:
            print("Already Entered, guess again")
        for x in word:
            if not x[1]:
                break
        else:
            print("You have guessed the word")
            break
    else:
        print("OUT OF GUESSES")
    print("The Word Was : ",w)
    c=input("Do you want to try again ? :(Y/N) ")
    if c!='Y':
        break
print("Thank you")