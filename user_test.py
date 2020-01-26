import unittest
from user import User

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
    
    #test if the user exists
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("test", "test")  # new contact
        test_user.save_user()

        user_exists = User.user_exists("test")

        self.assertTrue(user_exists)

    

    


if __name__ =='__main__':
    unittest.main()
    

    