import random
import string

class User_Contact:

    def __init__(self, Account_name, User_name, Account_password):
        self.Account_name = Account_name
        self.User_name  = User_name
        self.Account_password = Account_password


    def Account_credentials(self):
        return '{} {} {}'.format(self.Account_name, self.User_name, self.Account_password)


class User_credentials(object):

    def __init__(self, user_data = ''):
        self.user_data = user_data
        
    def __lengther(self):
        lengths = len(self.user_data)
        if lengths > 1:
            return self.user_data

    def __randomer(self):
        mix = random.randint(99999, 99999999)
        return mix

    def valid(self):
        length = self.__lengther()

        if length == True:
            return length
        else:
            the_random = self.__randomer()
            return the_random

print('Enter the Account name eg Twitter,Facebook, etc')
Name_of_the_account = input()

print('Enter your username')
Name_of_the_user  = input()

print('Enter the accounts' 'password or leave blank to let your password be generated for you' )
the_password = input()
the_pass_auth = User_credentials(the_password)
User_password = the_pass_auth.valid()

list_of_Accounts = []
Accounts_Dictionary = {}

user = User_Contact(Name_of_the_account, Name_of_the_user,User_password)

list_of_Accounts.append(user.Account_credentials())

Accounts_Dictionary[Name_of_the_account] = list_of_Accounts

print(Accounts_Dictionary)
print(user.Account_credentials())

#reset an account

print('Chande account details')
print('change Account username name')
update_username = input()

print('Change User Password')
update_password = input()
the_pass_auth_1 = User_credentials(update_password)
User_password_1 = the_pass_auth.valid()

Account_string = str(Accounts_Dictionary[Name_of_the_account])
Split_xter = Account_string.split()
Split_xter[1] = update_username
Split_xter[2] = User_password_1


print(Account_string)
print(Split_xter)

#delete the Account
print('Delete Account')

Accounts_Dictionary.pop(str(Name_of_the_account))

print(Accounts_Dictionary)

