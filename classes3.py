class User():
    def __init__(self, id:int, name:str, level_access:str = 'user') -> None:
        self.id = id
        self.__name = name 
        self.__level_access = level_access
    
    @property
    def name(self):
        """прямой доступ к name"""
        return self.__name    
    @property 
    def level_access(self):
        """прямой доступ к level_access"""
        return self.__level_access
    
    #setter
    @level_access.setter 
    def level_access(self, level):
        """устанавливаем уровень level_access"""
        valid_levels = ['user', 'junior', 'middle']
        if level in valid_levels:
            self.__level_access = level
        else:
            raise ValueError(f"Invalid access level. Should be in {valid_levels}")
        
    #deleter
    @level_access.deleter
    def level_access(self):
        """устанавливаем уровень по дефолту"""   
        self.__level_access ='user' 

    def __str__(self) -> str:
        return f"User( {self.id} name {self.name} has level {self.level_access})"    

class Admin(User):
    def __init__(self, id: int, name: str, level_access: str = 'user', is_admin: bool =True) -> None:
        super().__init__(id, name, level_access)
        self.is_admin = is_admin

    def add_user(self, users: list, user):
        """Add user to collection (only admins can do this)"""
        if self.is_admin:
            users.append(user)
        else:
            print("You are not an admin!")    

    def remove_user(self, users: list, user):
        """Remove user from collection (only admins can do this)"""
        if user in users and self.is_admin:
            users.remove(user)
        else:
            print("Access denied or user not found")

     
                        


Petr = User(1, "Петр", "user")

Ivan = User(2, "Иван", 'user')

Olga_Ivanovna = Admin (3, "ОльгаИваннна", 'admin')

Kirill = User(4, "Кирилл", "junior")

collectiv = [Petr, Ivan, Olga_Ivanovna]

 

print([sotrudnik.name for sotrudnik in collectiv])

# print(Petr.get_name())

print(Petr.level_access)

Petr.level_access = 'junior'

print(Petr.level_access)

Olga_Ivanovna.add_user(collectiv, Kirill)

Olga_Ivanovna.remove_user(collectiv, Ivan)

print([sotrudnik.name for sotrudnik in collectiv])

print(Kirill._User__name)