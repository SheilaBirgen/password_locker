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

    @classmethod
    def user_exists(cls, name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.name == name:
                return True

        return False