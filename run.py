from user import User
from credential import Creds
import re

def create_credential(snapchat, instagram, twitter):
    new_creds = Creds(snapchat, instagram, twitter)
    return new_creds

def save_credential(credential):
    credential.save_creds()

def display_creds():
    return Creds.display_creds()

def create_account(F_name, L_name, P_word):
    new_user = User(F_name, L_name, P_word)
    return new_user

def save_account(user):
    user.save_user()

def display_user():
    return User.display_user()

def main():
    print("Welcome to password locker where to generate new passwords!!")
    print(" ")
    print("On getting started use the below short codes")
    print(" ")
    print("""Your Guides
    ca - Create new_account
    cc - Create new_credential
    dec - Display existing credentials
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
        print("Your snapchat??")
        snapchat = input()
        print("Your password??")
        P_word = input()
        print(" ")
        print("Your twitter??")
        twitter = input()
        print("Your password??")
        P_word = input()
        print(" ")
        print("Your instagram??")
        instagram = input()
        print("Your password??")
        P_word = input()
        print(" ")
        save_credential(create_credential(snapchat,twitter,instagram))
        print('\n')
        print(f"New Credentials {Creds} {P_word} has been created :)")
        print('\n')

    elif short_code == 'dec':
        if display_user():
            print(" ")
            print("The accounts")
            print('\n')
            for user in display_user():
                print(f"{user.F_name}{user.L_name}{user.P_word}")
            
            for credential in display_creds():
                print(f"{snapchat}{user.P_word},{instagram}{user.P_word},{twitter}{user.P_word}")
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

    


        
if __name__ == '__main__':
    main()



        

