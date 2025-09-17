class User():
    def __init__(self, id:int, name:str, level_access:str = 'user') -> None:
        self.id = id
        self.__name = name 
        self.__level_access = level_access
    
    
    def get_name(self):
        return self.__name    
     
    def _get_level_access(self):
        return self.__level_access
    
     
    def _set_level_access(self, level):
        self.__level_access = level


class Admin(User):
    def __init__(self, id: int, name: str, level_access: str = 'user', is_admin: bool =True) -> None:
        super().__init__(id, name, level_access)
        self.is_admin = is_admin

    def _add_user(self, users: list, user):
        users.append(user)

    def __remove_user(self, users: list, user):
        if user not in users:
            raise ValueError("User not in the list")
        users.remove(user)

    def delete_user (self, users: list, user):
        if not self.is_admin:
            raise PermissionError("Invalid level access")
        self.__remove_user(users, user)
                        


Petr = User(1, "Петр", "user")

Ivan = User(2, "Иван", 'user')

Olga_Ivanovna = Admin (3, "ОльгаИваннна", 'admin')

Kirill = User(4, "Кирилл", "junior")

collectiv = [Petr, Ivan, Olga_Ivanovna]

 

print([sotrudnik.get_name() for sotrudnik in collectiv])

# print(Petr.get_name())

print(Petr._get_level_access())

Petr._set_level_access('junior')

print(Petr._get_level_access())

Olga_Ivanovna._add_user(collectiv, Kirill)

Olga_Ivanovna.delete_user(collectiv, Ivan)

print([sotrudnik.get_name() for sotrudnik in collectiv])

print(Kirill._User__name)