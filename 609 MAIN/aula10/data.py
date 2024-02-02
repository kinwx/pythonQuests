class User:
    def __init__(self, email: str, password: str = "") -> None:
        self.email = email
        self.password = password

class Data:
    def __init__(self) -> None:
        self.dataBase = [
            User(email="joao@email.com"),
            User(email="maria@email.com"),
            User(email="jose@email.com"),
            User(email="ana@email.com"),
            User(email="pedro@email.com"),
            User(email="abel@email.com"),
            User(email="patricia@email.com"),
            User(email="amanda@email.com"),
        ]
    
    def add(self, user: User):
        self.dataBase.append(user)

mainData = Data()
