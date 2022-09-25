name = input("What's your name? ")
print('Welcome,',name ,'to the game. ')
print("let's start the game.")
answer = input('Your are in Nstu Main Gate. Do You want to go in?(Yes/No) ').lower()
if answer == "yes":
    print("Now you can see the Proshashonik Bluiding , Academic 1 , Academic 2 and Auditorium .")
    answer = input("Want to go right or left? ").lower()
    if answer == "right":
        print("Now you can see neel dighi , and in the left you can see Library ")
        answer = input("Do you wanna go  forward?" ).lower()
        if answer == "yes":
            print("here you can see 2 female hall of nstu")
        elif answer == "no":
            print("Tour is over.")
        else: 
            print("Not a valid answer.")
    elif answer == "left":
        print("here you can see Two Male Hall of the nstu and one Female hall of the nstu.") 
        answer = input("Do you wanna go  forward?" ).lower()
        if answer == "yes":
            print("here you can see 2 female hall of nstu")
        elif answer == "no":
            print("Tour is over.") 
        else: 
            print("Not a valid answer.")
    else: 
        print("Not a valid answer.")
elif answer == "no":
    print("The Tour is over.")
else:
    print("Not a valid answer.")
