import unittest
from Store_contact import User_credentials, User_Contact

class test_units(unittest.TestCase):

    def setUp(self):
        '''
        this is a declaration function that makes the variables global
        '''

        #declaration_process
        self.account = 'Twitter'
        self.users = 'Brother'
        self.password = 'password'

    def test_self(self):
        '''
        self test in case our tests fail we will know this works and sort for errors
        '''
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
        Aserting of the results fom the result variables
        '''
        #assert
        self.assertEqual(expected_results, returned_result)

    def test_User_Contact_returned_type(self):
        '''
        test for the user_credentials class
        '''
        #result_process_2
        user_results = User_Contact(self.account, self.users,self.password).Account_credentials()
        returned_result = str
        expected_results = type(user_results)

        '''
        Aserting of the results fom the result variables
        '''
        #assert
        self.assertEqual(expected_results, returned_result)


if __name__ == "__main__":
    unittest.main()