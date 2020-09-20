import unittest
from Store_contact import User_credentials, User_Contact

class test_units(unittest.TestCase):

    def setUp(self):
        self.account = 'Twitter'
        self.uses = 'Brother'
        self.password = 'password'

    def test_self(self):
        pass
    
    def test_User_Credentials(self):

        #result_process_2
        user_results = User_credentials.randomer(self)

        expected_results = type(user_results)

        #assert
        self.assertEqual(expected_results, user_results)

if __name__ == "__main__":
    unittest.main()