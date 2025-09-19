import pickle
import json

class Animal():
    def __init__(self, name, age) -> None:
        self.name = name  
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass
    def to_dict(self):
        return {"type":self.__class__.__name__, "name": self.name, "age": self.age}
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

class Bird (Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def make_sound(self):
        print("I'm singing") 


class Mammal (Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.eating = "Хищник"
    def make_sound(self):
        print ("I'm muting")

class Reptile(Animal):

    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.eating = "Хищник"
    def make_sound(self):
        print("I'm looking")

def animal_sounds (animals):
    for animal in animals:
        animal.make_sound()

lion = Mammal("Король Лев", 10)
gekkon = Reptile("Геккончик", 2)
kalibri = Bird("Кеша", 4)
zoopark = [lion, gekkon, kalibri]

animal_sounds(zoopark)


class ZooSotrudnik():
    def __init__(self, name) -> None:
        self.job = 'Зоопарк'
        self.name = name
    
    def to_dict(self):
        return {"type": self.__class__.__name__, "name": self.name, "job": self.job}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])

class Zoo():
    def __init__(self) -> None:
        self.sotrudniki =[]
        self.animals = []

    def hire_sotrudnik(self, new_sotrudnik):
        self.sotrudniki.append(new_sotrudnik)

    def buy_animal(self, new_animal):
        self.animals.append(new_animal)  



    

    def save_zoo(self, filename="zoo.json"):
        data = {
            "animals":[a.to_dict() for a in self.animals],
            "sotrudniki":[s.to_dict() for s in self.sotrudniki]

        } 
        with open (filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
     
    def load_zoo(self, filename="zoo.json"):
        # with open("zoo.pkl", "rb") as f:
        #     loaded_zoo = pickle.load(f)
        with open (filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        type_map_animals = {"Bird": Bird, "Mammal": Mammal, "Reptile": Reptile}
        self.animals = [type_map_animals[a["type"]](a["name"], a["age"]) for a in data["animals"]]   

        type_map_staff = {"ZooKeeper": ZooKeeper, "Veterinarian": Veterinarian}
        self.sotrudniki = [type_map_staff[s["type"]](s["name"]) for s in data["sotrudniki"]] 






class ZooKeeper(ZooSotrudnik):
    def feed_animals(self, animal):
        print(f"add +2 kg meat to {animal.name}")

class Veterinarian(ZooSotrudnik):
     def heal_animals(self, animal):
         print(f"add +5 health to {animal.name}")


NewZoo = Zoo()

Petr = Veterinarian("Петр")

Anna = ZooKeeper("Анна")

collectiv =[]
animals = []
NewZoo.hire_sotrudnik(Anna)


NewZoo.buy_animal(lion)

print([sotrudnik.name for sotrudnik in NewZoo.sotrudniki])

print([animal.name for animal in NewZoo.animals])

for animal in NewZoo.animals:
    Petr.heal_animals(animal)
    print(f"{Petr.name} вылечил {animal.name}")



NewZoo.save_zoo()

LoadedZoo = Zoo()

LoadedZoo.load_zoo()

print ("LoadedZoo")

print([a.name for a in LoadedZoo.animals])

print ([s.name for s in LoadedZoo.sotrudniki])