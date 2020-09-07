import random
import string

class User_Contact:

    def __init__(self, Account_name, User_name, Account_password):
        self.Account_name = Account_name
        self.User_name  = User_name
        self.Account_password = Account_password


    def Account_credentials(self):
        return '{} {} {}'.format(self.Account_name, self.User_name, self.Account_password)


class User_credentials():

    def __init__(self):
        pass
        
    def randomer(self):
        mix = random.randint(99999, 99999999)
        return mix

cred = User_credentials()

print('Enter the Account name eg Twitter,Facebook, etc')
Name_of_the_account = input()

print('Enter your username')
Name_of_the_user  = input()

print('Enter the accounts' 'password or leave blank to let your password be generated for you' )
the_password = input()

length = len(the_password)
if length >=1:
    User_password = the_password
else:
    User_password = cred.randomer()

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

length = len(update_password)
if length >=1:
    User_password_1 = update_password
else:
    User_password_1 = cred.randomer()


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

