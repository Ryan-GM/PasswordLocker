class Creds:
    creds_list = []

    def __init__(self,snapchat, instagram, twitter, E_mail):
        self.instagram = instagram
        self.snapchat = snapchat
        self.twitter = twitter
        self.E_mail = E_mail

    def save_creds(self):
        Creds.creds_list.append(self)

    def delete_creds(self):
        Creds.creds_list.remove(self)

    @classmethod
    def display_info(cls):
        return cls.info_list
