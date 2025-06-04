class User():
    def __init__(self, username, ide):
        self.ide = ide
        self.username = username
        self.followers = 0
        self.following = 0
        print(f'This users username is {username} and his or her id is {ide}')
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('Veer', '0000001')
user_2 = User('Nischay', '0000002')
user_3 = User('Rishi', '0000003')
user_4 = User('Riva', '0000004')
user_5 = User('Jacob', '0000005')
user_6 = User('Riaan', '0000006')
user_7 = User('Everett', '0000007')
user_8 = User('Andrew', '0000008')

user_2.follow(user_1)