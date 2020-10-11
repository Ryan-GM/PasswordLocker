from user import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Ryan","Munge","ryanmunge12@gmail.com")

    def test1(self):
        self.assertEqual(self.new_user.F_name,"Ryan")
        self.assertEqual(self.new_user.L_name,"Munge")
        self.assertEqual(self.new_user.E_mail,"ryanmunge12@gmail.com")

    def tearDown(self):
        User.userList = []