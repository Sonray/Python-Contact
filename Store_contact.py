

class User_Contact:

    def __init__(self, Account_name, User_name, Account_password):
        self.Account_name = Account_name
        self.User_name  = User_name
        self.Account_password = Account_password


    def Account_credentials(self):
        return '{} {} {}'.format(self.Account_name, self.User_name, self.Account_password)


class User_credentials:

    def __init__(self, Account_name, User_name, Account_password):
        self.Account_name = Account_name
        self.User_name  = User_name
        self.Account_password = Account_password


print('Enter the Account name eg Twitter,Facebook, etc')
Name_of_the_account = input()

print('Enter your username')
Name_of_the_user  = input()

print('Enter the accounts' 'password')
User_password = input()

list_of_Accounts = []
Accounts_Dictionary = {}

user = User_Contact(Name_of_the_account, Name_of_the_user,User_password)

list_of_Accounts.append(user.Account_credentials())

Accounts_Dictionary[Name_of_the_account] = list_of_Accounts

print(Accounts_Dictionary)
print(user.Account_credentials())


