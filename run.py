from user import User
from credential import Creds

def create_credential(snapchat, instagram, twitter, E_mail):
    new_creds = Creds(snapchat, instagram, twitter, E_mail)
    return new_creds

def create_account(F_name, L_name, E_mail):
    new_user = User(F_name, L_name, E_mail)
    return new_user