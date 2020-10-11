from user import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Ryan","Munge","ryanmunge12@gmail.com")

    def test_init(self):
        self.assertEqual(self.new_user.F_name,"Ryan")
        self.assertEqual(self.new_user.L_name,"Munge")
        self.assertEqual(self.new_user.E_mail,"ryanmunge12@gmail.com")
    
    def tearDown(self):
        User.user_list = []

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def test_delete_user(self):
        self.new_user.save_user()
        test_data = User("Scott","Ethan","ethanbaraka@gmail.com")
        test_data.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_user(self):
        self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__':
    unittest.main()