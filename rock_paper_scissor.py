import random
a=["rock","paper","scissor"]
def cho(b):
    k=random.choice(a)
    if (b==1 and k=="rock" or b==2 and k=="paper" or b==3 and k=="scissors"):
        return "Draw"
    elif (b==1):
        if(k=="paper"):
            return "You lose!"
        elif(k=="scissor"):
            return "You Won!"
    elif (b==2):
        if(k=="rock"):
            return "You Won!"
        elif(k=="scissor"):
            return "You lose!"
    else:
        if(k=="rock"):
            return "You lose!"
        elif(k=="paper"):
            return "You Won!"
    
while(True):
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    print("4.Exit")
    print("Enter your choice:")
    b=int(input())
    if(1<=b<=3):
        print(cho(b))
    elif(b==4):
        print("Thanks for play! Exit gracefully :)")
        break
    else:
        print("Invalid Choice")
