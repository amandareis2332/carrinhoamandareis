class Item:
    id: str
    value: float
    quantity: int

    def __init__(self, id, value, quantity):
        self.id = id
        self.value = value
        self.quantity = quantity

class Carrinho:
    id_user: str
    items: []

    def __init__(self, id_user, items):
        self.id_user = id_user       
        self.items = items 

    def add_item(self, item):
        self.items.append(item)

    def remove(self, id_item):
        for item in self.items:
            if item.id == id_item:
                self.items.remove(item)


carrinho = Carrinho("amanda@gmail.com", [])

item1 = Item("PROD1", 12.2, 1)

carrinho.add_item(item1)


print(vars(carrinho))


