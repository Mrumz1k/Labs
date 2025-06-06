class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return f"User(login='{self.login}', password='{self.password}')"

users = [
    User("user1", "pass1"),
    User("user2", "pass2"),
    User("user3", "pass3"),
    User("user4", "pass4"),
    User("user5", "pass5"),
]

def find_user(users_list, login, password):
    for user in users_list:
        if user.login == login and user.password == password:
            return user
    return None

login_to_find = "user3"
password_to_find = "pass3"
found_user = find_user(users, login_to_find, password_to_find)

if found_user:
    print("Пользователь найден:", found_user)
else:
    print("Пользователь с такими данными не найден")