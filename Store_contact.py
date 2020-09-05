

class User_Contact:

    def __init__(self, Account_name, User_name, Account_password):
        self.Account_name = Account_name
        self.User_name  = User_name
        self.Account_password = Account_password

    def Account_credentials(self):
        return '{} {} {}'.format(self.Account_name, self.User_name, self.Account_password)

Name_of_the_account = input('Enter the Account name eg Twitter,Facebook, etc')
Name_of_the_user  = input('Enter your username')
User_password = input('Enter the accounts' 'password')

user = User_Contact(Name_of_the_account, Name_of_the_user,User_password)

print(user.Account_credentials())


