class Creds:
    creds_list = []

    def __init__(self, snapchat, instagram, twitter):
        self.instagram = instagram
        self.snapchat = snapchat
        self.twitter = twitter

    def save_creds(self):
        Creds.creds_list.append(self)

    def delete_creds(self):
        Creds.creds_list.remove(self)

    @classmethod
    def display_creds(cls):
        return cls.creds_list
