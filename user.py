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