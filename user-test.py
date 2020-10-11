from user import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Ryan","Munge","ryanmunge12@gmail.com")

    