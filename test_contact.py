import unittest
from Store_contact import User_credentials, User_Contact

class test_units(unittest.TestCase):

    def setUp(self):
        self.account = 'Twitter'
        self.uses = 'Brother'
        self.password = 'password'

    def test_self(self):
        pass
    
    def test_User_Credentials_returned_type(self):
        '''
        test for the user_credentials randomer function
        '''
        #result_process_2
        user_results = User_credentials.randomer(self)
        returned_result = int
        expected_results = type(user_results)

        '''
        Aserting of the results fom the result varialbles
        '''
        #assert
        self.assertEqual(expected_results, returned_result)

    def test_User_Contact_returned_type(self):
        '''
        test for the user_credentials class
        '''
        #result_process_2
        user_results = User_Contact.Account_credentials(self)
        returned_result = str
        expected_results = type(user_results)

        '''
        Aserting of the results fom the result varialbles
        '''
        #assert


if __name__ == "__main__":
    unittest.main()