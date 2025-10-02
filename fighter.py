 
from abc import ABC, abstractmethod 

# type_weapon = {'Боец':'slashing', 'Магик':'magic', 'Лучник':'ranged'}

class Fighter:
    def __init__(self,name:str ='Фигер', type_fighter:str ='Боец'):
        self.name = name
        self.type_fighter = type_fighter

    # def has_weapon(self, weapon):

    # def change_weapon(self, weapon):
    #     if weapon.type_fighter == self.type_fighter:
    #         self.weapon = weapon     
    #     else:
    #         print(f"{weapon.name} выпадает из рук и больно бьет {self.name} по ноге. Ты не {weapon.type_fighter} и не можешь использовать меня!")

class WeaponHandler:
    def change_weapon(self, weapon, fighter) -> bool:
        if weapon.type_fighter == fighter.type_fighter:
            return True     
        else:
            print(f"{weapon.name} выпадает из рук и больно бьет {fighter.name} по ноге. Ты не {weapon.type_fighter} и не можешь использовать меня!")    
            return False
        
class ArmedFighter(Fighter):
    def __init__(self,name:str ='Фигер', type_fighter:str ='Боец'):
        super().__init__(name, type_fighter)
        self.weapon = None

    def get_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        
        if self.weapon != None:
            print(f"{self.name} берет в руки {self.weapon.name}")
            self.weapon.attack()
        else:
            print(f"{self.name} не имеет оружия и не наносит урон")

class Monster:
    def __init__(self, name:str ='Монстр'):
        self.name= name


class Weapon(ABC):
    def __init__(self, name, type_fighter):
        self.name = name
        self.type_fighter = type_fighter
        

    @abstractmethod
    def attack(self):
        pass


class MagicWeapon(Weapon):
    def __init__(self, name:str = 'Магический оружие', type_fighter:str = 'Магик'):
        super().__init__(name, type_fighter)

    def magik_attack(self):
        print(f"{self.name} выстреливает в небесный мир!")

    def attack(self):
        print(f"{self.name} расходует ману и не атакует мгновенно")
        self.magik_attack()
    

class Bow(Weapon):

    def __init__(self, name:str = 'Лук', type_fighter:str = 'Лучник'):
        super().__init__(name, type_fighter)
    def attack(self):
        print(f"{self.name} в умелых руках бъет без промаха!")   
    # def check_fighter(self, type_fighter):
    #     if type_weapon[self.kind_weapon] == type_fighter:
    #         return True
    #     else:
    #         return False

class   Sword(Weapon):

    def __init__(self, name:str = 'Кладенец', type_fighter:str = 'Боец'):
        super().__init__(name, type_fighter)
    def attack(self):
        print(f"{self.name} рубит голову!")  



#       бой

bow = Bow('Лук тисовый')
sword = Sword('Кладенец')
staff = MagicWeapon('Стафф')

# Alexander = ArmedFighter('Александер')  
# Alexander.change_weapon(bow)  
# Alexander.attack()

monster = Monster('Минотавр')

Saruman = ArmedFighter('Саруман','Магик')

handler= WeaponHandler() 

if handler.change_weapon(bow, Saruman):
    Saruman.get_weapon(bow)
    Saruman.attack()


if handler.change_weapon(sword, Saruman):
    Saruman.get_weapon(sword)
    Saruman.attack()



print(f"{monster.name} злорадно скалится и бьет {Saruman.name} по почкам! ")


if handler.change_weapon(staff, Saruman):
    Saruman.get_weapon(staff)  
    Saruman.attack()
 

print(f"{monster.name} погибает((")