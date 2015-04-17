import time
import datetime
from random import *
from polyBlueClient import PolyBlueClient

Id = {'Poly-Pro': 'Admin'} # list for sorting users
Log1 = [] # log of activity
##username = input("Please create a username: ")
##p.sendOutput("Your ID is", username+str(number))
##finalname = username+str(number)
##id.update({finalname})
p = PolyBlueClient('Commuters-1')#bluemix domain


while True: # promping new/ returning user
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%m-%d-%Y %H:%M")
    number = randint(1,10)
    userInfo = p.getInput("Are you a new user? ")
    
    if userInfo == "yes":
        username = p.getInput("Please create a username: ")
        st = datetime.datetime.fromtimestamp(ts).strftime("%m-%d-%Y %H:%M") # current date & time 
        p.sendOutput("Your ID is %s" %username+str(number))
        p.sendOutput(st)
        finalname = username+str(number) # generated account
        Id[finalname] = username
        st = datetime.datetime.fromtimestamp(ts).strftime("%m-%d-%Y %H:%M")
    elif userInfo == "no":
        confirm = p.getInput("Please enter your username: ")
        if confirm in Id.keys():
            p.sendOutput("Welcome back! %s" %Id[confirm])
            st = datetime.datetime.fromtimestamp(ts).strftime("%m-%d-%Y %H:%M")
            Log1.append(Id[confirm]+" "+ st+" logon")
##        while confirm == 'Poly-Pro':
##            p.sendOutput(Log1)
                        
            confirm = p.getInput("Please enter your username to logoff: ")
            if confirm in Id.keys():
                p.sendOutput("Goodbye! %s" %Id[confirm])
                p.sendOutput(st)
                st = datetime.datetime.fromtimestamp(ts).strftime("%m-%d-%Y %H:%M")
                Log1.append(Id[confirm]+" "+ st+" logoff")
    
             
        
p.close()
            
   



