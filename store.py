class Store():
    def __init__ (self, name, address):
        self.name = name  
        self.address = address
        self.items ={}

    def __str__(self):
        stroka = f"{self.name}  {self.address} {self.items}" 
        return stroka  
    

    def add_goods(self, item_name:str, item_price:int):
        self.items[item_name] = item_price

    def delete_goods(self, item_name):
        self.items.pop(item_name, None)

    def get_price(self, item_name) ->float|None:
        price = self.items.get(item_name)
        return price            
    
    def update_price(self, item_name, new_price):
        self.items[item_name] = new_price
          

Fabrika = Store("Фабрика Качества", "ул 40 лет Победы 21")
Fabrika.add_goods("Копченая колбаса", 999)

Magnit = Store("Магнит", "ул 40 лет Победы 14")
Magnit.add_goods("Батон", 65)

KB = Store("Красное и Белое", "ул 40 лет Победы 18")
KB.add_goods("Шампанское", 300)
KB.update_price("Шампанское", 450)

print(KB.get_price("Шампанское"))

KB.delete_goods("Шампанское")