class User:
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username

user_1 = User("001", "Todd")

print(user_1.id, user_1.username)
