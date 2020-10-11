import unittest
from credential import Creds

class TestCreds(unittest.TestCase):
    def setUp(self):
        self.new_creds = Creds("rg-munge", "ryan.dfw", "rm-githanji")

    def test_init(self):
        self.assertEqual(self.new_creds.snapchat,"rg-munge")
        self.assertEqual(self.new_creds.twitter,"rm-githanji")
        self.assertEqual(self.new_creds.instagram,"ryan.dfw")

    def test_save_info(self):
        self.new_creds.save_creds()
        self.assertEqual(len(Creds.creds_list),1)
        

    def tearDown(self):
        Creds.creds_list = []

    def test_delete_creds(self):
        self.new_creds.save_creds()
        test_creds = Creds("ethansolo", "s-ethan", "scottethan")
        test_creds.save_creds()
        test_creds.delete_creds()
        self.assertEqual(len(Creds.creds_list),1)

    def test_display_creds(self):
        self.assertEqual(Creds.display_creds(),Creds.creds_list)

if __name__ == '__main__':
    unittest.main()

    

