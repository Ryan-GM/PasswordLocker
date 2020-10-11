class User:
    user_list = []

    def __init__(self, F_name, L_name, P_word):
        self.F_name = F_name
        self.L_name = L_name
        self.P_word = P_word

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        return cls.user_list
