# CLass 
# Naming convention Pascal casing
class User:
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name
        self.followers =0
        self.following = 0
    def follow(self,user):
        user.followers+=1
        self.following+=1

user_1 = User(25,"Manish")
user=User(26,"Pavitra")

print(user.followers)
print(user_1.following)
user_1.follow(user)
print(user.followers)
print(user_1.following)

print(user_1.followers)
print(user.following)