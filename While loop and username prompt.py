from random import *
number = randint(1,10)
id = {""}
##username = input("Please create a username: ")
##print("Your ID is", username+str(number))
##finalname = username+str(number)
##id.update({finalname})

print(id)

while True:
    userInfo = input("Are you a new or returning user? ")
    if userInfo == "new":
        username = input("Please create a username: ")
        print("Your ID is", username+str(number))
        finalname = username+str(number)
        id.update({finalname})
        print(id)
    elif userInfo == "returning":
        confirm = input("Please enter your username: ")
        if confirm == finalname:
            print("Welcome back!")
