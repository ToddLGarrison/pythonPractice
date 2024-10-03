class User:
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1

user_1 = User("001", "Todd")
user_2 = User("002", "Becky")

print(user_1.id, user_1.username, user_1.followers)

user_1.follow(user_2)
print(user_1.followings)
print(user_1.followers)
print(user_2.followings)
print(user_2.followers)
