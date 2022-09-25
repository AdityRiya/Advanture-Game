name = input("What's your name? ")
print('Welcome,',name ,'to the game. ')
print("let's start the game.")
answer = input('Your are in Nstu Main Gate. Do You want to go in?(Yes/No) ').lower()
if answer == "yes":
    print("Now you can see the Proshashonik Bluiding , Academic 1 , Academic 2 and Auditorium .")
    answer = input("Want to go right or left? ").lower()
elif answer == "no":
    print("The Tour is over.")
else:
    print("Not a valid answer.")
