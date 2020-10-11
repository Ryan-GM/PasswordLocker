#!/usr/bin/env python3.7
from user import User
from credential import Creds
import re

def create_creds(snapchat,instagram,twitter):
    new_creds = Creds(snapchat, instagram, twitter)
    return new_creds

def save_creds(creds):
    credential.save_creds()

def display_creds():
    return Creds.display_creds()

def del_creds(creds):
    credential.delete_creds()

def find_creds(search_name):
        for credential in cls.creds_list:
            if creds.snapchat == snapchat:
                return credential
            elif creds.instagram == instagram:
                return credential
            elif creds.twitter == twitter:
                return credential

def create_account(F_name, L_name, P_word):
    new_user = User(F_name, L_name, P_word)
    return new_user

def save_account(user):
    user.save_user()

def display_user():
    return User.display_user()

def main():
    print("Welcome to password locker!!")
    print(" ")
    print("On getting started use the below short codes")
    print(" ")
    print("""Your Guides
    ca - Create new_account
    cc - Create new_credential
    dea - Display existing accounts
    gp - Generate password
    dc - Delete credential
    ex - Exit password locker""")
    print(" ")
    short_code = input() .lower()
    if short_code == 'ca':
        print("WANT TO CREATE A NEW ACCOUNT??")
        print(" ")
        print("Your first name??")
        F_name = input()
        print(" ")
        print("Your second name??")
        L_name = input()
        print(" ")
        print("Your password??")
        P_word = input()
        print(" ")
        save_account(create_account(F_name,L_name,P_word))
        print(f"New Account {F_name} {L_name} {P_word} has been created :)")
        print('\n')
    
    elif short_code == 'cc':
        print("WANT TO CREATE NEW CREDENTIALS??")
        print(" ")
        print("Which credentials would you like created??")
        social = input() .lower()
        if social == 'snapchat':
            print("Your snapchat??")
            snapchat = input()
            print("Your password??")
            P_word = input()
            print(" ")
            save_creds(create_creds(snapchat,twitter,instagram))
            print(f"New Credentials {creds.snapchat} {user.P_word} has been created :)")
            print(" ")
        elif social == 'twitter':
            print("Your twitter??")
            twitter = input()
            print("Your password??")
            P_word = input()
            print(" ")
            save_creds(create_creds(snapchat,twitter,instagram))
            print(f"New Credentials {creds.twitter} {user.P_word} has been created :)")
            print(" ")
        elif social == 'instagram':
            print("Your instagram??")
            instagram = input()
            print("Your password??")
            P_word = input()
            print(" ")
            save_creds(create_creds(snapchat,twitter,instagram))
            print(f"New Credentials {creds.instagram} {user.P_word} has been created :)")
            print(" ")
        
        print('\n')
        print('\n')

    elif short_code == 'dea':
        print("WHICH WOULD YOU LIKE TO DISPLAY??")
        print(" ")
        print("Shall it be users or credentials")
        display = input() .lower()
        if display == 'users':
            print(" ")
            print("The Users")
            print('\n')
            for user in display_user():
                print(f"{user.F_name}{user.L_name}{user.P_word}")
        if display == 'credentials':
            print(" ")
            print("The Credentials")
            print('\n')
            for creds in display_creds():   
                print(f"{creds.snapchat},{creds.instagram},{creds.twitter}")
                print(" ")

        else: 
            print('\n')
            print(" ")
            print("CREATE AN ACCOUNT!!")
            print("You have no accounts saved :(")
            print(" ")

    elif short_code == 'gp':
        print(" ")
        print("TO GENERATE YO A NEW PASSWORD PUT IN A NAME")
        print(" ")
        list_of_inputs = [c for c in input()]
        c=input("Enter the password:")
        if(len(c)>=8):
            if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',c))==True):
                print("The password is strong")
            elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',c))==True):
                print("The password is weak")
        else:
            print("You have entered an invalid password.")

        list_of_inputs.reverse()
        print(list_of_inputs)

    elif short_code == 'dc':
        print("WHICH CREDENTIALS WOULD YOU LIKE DELETED??")
        print(" ")
        search_name = input().lower()
        if find_creds(search_name):
            search_creds = find_creds(search_name)
            print(" ")
            search_creds.delete_creds()
            print('\n')
            print(f"Credentials for {creds.display_creds} has been deleted")
            print(" ")
        else:
            print("The searched credentials doesn't exist")
        
    elif short_code == "ex":
        print(" ")
        print("Thank You")
        print("See you next time")
        print(" ")

    else:
        print(" ")
        print("Retry!!")
        print(" ")
        print("Please choose from the option provided")
        print(" ")




        
if __name__ == '__main__':

    main()



        

