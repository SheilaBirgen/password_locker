import unittest
from user import User,Credential

class TestUser(unittest.TestCase):
    '''
       A class that inherits the TestCase class from the unittest module.

        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        runs before the test case run
        '''
        self.new_user = User("Bir", "2345")#new user

    def tearDown(self):
        User.user_list = []
        
    #saves a single user
    def test_save_user(self):
        """
            test_save_user test case to test if the user object is saved into
            the user list
            add
        """

        self.new_user.save_user()  
        self.assertEqual(len(User.user_list), 1)
    
    # saves multiple user
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("bir", "12345")  
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
    
    # deletes a user
    def test_delete_user(self):
        """
            test_delete_user to test if we can remove a user from our users list
            """
        self.new_user.save_user()
        test_user = User("bir", "12345")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    # Test to delete User Accounts
    def test_delete_users(self):
        '''
        test_delete_users to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("test", "test")  # new user
        test_user.save_user()
        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)
    
class TestCredentials(unittest.TestCase):
    """
    Class to test the account credentials
    """

    def setUp(self):
        """
        This runs before the tests
        """
        self.new_credential= Credential(
            "bir", "twitter","bir","bir")  
    
    def test_credential_init(self):
        """
        Test case to show that credentials are well initialized.
        """
        self.assertEqual(self.new_credential.username, "bir")
        self.assertEqual(self.new_credential.account, "twitter")
        self.assertEqual(self.new_credential.account_username, "bir")
        self.assertEqual(self.new_credential.account_password, "bir")
    
    def test_save_credential(self):
        """
        Test to check the save feature
        """

        self.new_credential.save_credential()  # saving the new credential

    # Tear down function
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    #save multiple credential
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_credential.save_credential()
        trial_credential = Credential(
            "test", "Facebook", "test", "test")  # new credential
        trial_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

     # Test to delete Credential
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a user from our user list
        '''
        self.new_credential.save_credential()
        test_credential = Credential(
            "test", "twitter", "test", "test")  # new user
        test_credential.save_credential()
        self.new_credential.delete_credential()  # Deleting a user object
        self.assertEqual(len(Credential.credential_list), 1)
        
        
        #Test to see if a crential exist
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credential.save_credential()
        test_credential = Credential(
            "test", "twitter", "test", "test")  # new contact
        test_credential.save_credential()

        credential_exists = Credential.credential_exists("test")

        self.assertTrue(credential_exists)




    

    


if __name__ =='__main__':
    unittest.main()
    

    