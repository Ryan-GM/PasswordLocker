class User:
    user_list = []

    def __init__(self, F_name, L_name, E_mail):
        self.F_name = F_name
        self.L_name = L_name
        self.E_mail = E_mail

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        return cls.user_list
