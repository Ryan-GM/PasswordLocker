import unittest
from credential import Creds

class TestCreds(unittest.TestCase):
    def setUp(self):
        self.new_creds = Creds("rg-munge", "ryan.dfw", "rm-githanji", "ryanmunge12@gmail.com")

    def test_init(self):
        self.assertEqual(self.new_creds.snapchat,"rg-munge")
        self.assertEqual(self.new_creds.twitter,"rm-githanji")
        self.assertEqual(self.new_creds.instagram,"ryan.dfw")
        self.assertEqual(self.new_creds.E_mail,"ryanmunge12@gmail.com")

    def test_save_info(self):
        self.new_creds.save_creds()
        