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
        '''
        test for the user_credentials randomer function
        '''
        #result_process_2
        user_results = User_credentials.randomer(self)
        returned_result = int
        expected_results = type(user_results)

        #assert
        self.assertEqual(expected_results, returned_result)

if __name__ == "__main__":
    unittest.main()