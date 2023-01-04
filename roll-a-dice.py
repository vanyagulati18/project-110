import random
response="y"
while response=="y":
    no = random.randint(1,6)
    if(no==1):
        print("1")
    elif(no==2):
        print("2")
    elif(no==3):
        print("3")
    elif(no==4):
        print("4")
    elif(no==5):
        print("5")
    else:
        print("6")
    response = input("Do you want to roll a dice? y or n")
    print("\n")
