import unittest
from Store_contact import User_credentials, User_Contact

class test_units(unittest.TestCase):

    def setUp(self):
        self.account = 'Twitter'
        self.uses = 'Brother'
        self.password = 'password'

    def test_User_Contact(self):