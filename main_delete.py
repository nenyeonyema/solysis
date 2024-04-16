#!/usr/bin/python3
""" Test delete feature
"""
from models.database.file_storage import FileStorage
from models.user import User

fs = FileStorage()

# All States
all_users = fs.all(User)
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

# Create a new user
new_user = User()
new_user.name = "Slonjoh"
fs.new(new_user)
fs.save()
print("New User: {}".format(new_user))

# All States
all_users = fs.all(User)
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

# Create another User
another_user = User()
another_user.name = "Nenye"
fs.new(another_user)
fs.save()
print("Another User: {}".format(another_user))

# All Users
all_users = fs.all(User)
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])        

# Delete the new State
fs.delete(new_user)

# All Users
all_users = fs.all(User)
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])
