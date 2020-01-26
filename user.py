class User:
    '''
    class that genarates new instances for the user
   
    '''
    user_list = []

    def __init__(self,name,user_password):
        self.name = name
        self.user_password = user_password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes saved contact
        """
        User.user_list.remove(self)

class Credential:
    '''
    Class that stores user credential
    '''

    credential_list = []

    def __init__(self, username, account, account_username, account_password):
        """
        Init method for creating new instances of account credentials
        """
        self.username = username
        self.account = account
        self.account_username = account_username
        self.account_password = account_password

    #Save credential function
    def save_credential(self):
        """
        Function for saving credential
        """
        Credential.credential_list.append(self)