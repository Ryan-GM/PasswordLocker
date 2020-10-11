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

    @classmethod
    def find_creds(cls, snapchat, instagram, twitter):
        for credential in cls.creds_list:
            if creds.snapchat == snapchat:
                return credential
            elif creds.instagram == instagram:
                return credential
            elif creds.twitter == twitter:
                return credential


