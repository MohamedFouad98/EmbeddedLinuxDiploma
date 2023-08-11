#!/usr/bin/python3
def check_password1(user,Pass):
    users={"ahmed":1394,"ali":6078,"amr":9345}
    if user in users and Pass == users[user]:
        print("welcome "+user)
    else :
        print("Incorrect uesername or password")
    
username=(input("please enter your name: ")).lower()
password=int(input("please enter your password: "))

check_password1(username,password)