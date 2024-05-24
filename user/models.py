
class UserEntity:

    def __init__(self, username, 
                 id = None, 
                 name = None, 
                 email = None, 
                 password = None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f'{self.username}: {self.password}'