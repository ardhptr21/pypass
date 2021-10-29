from database.User import User
from database.Account import Account
from system import prompt

user = User("database.db")
account = Account("database.db")
user.connect()
account.connect()


if user.isEmpty():
    prompt.guest(user)
else:
    prompt.auth(user, account)


user.close()
