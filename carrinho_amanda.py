
class Item:
    id_product: str
    value : float
    quantity: int

    def __init__(self, id_product, value, quantity):
        self.id_product = id_product
        self.value = value
        self.quantity = quantity

class Cart:
    id_user: str
    items: []
    def __init__(self, id_user, items):
        self.id_user = id_user
        self.items = items

    def add_item (self, item): #adicionar
        self.items.append(item)

    def get_all_items (self): #buscar lista
        return self.items

    def remove_item(self, id_product): #remover
        self.id_product.pop(item)

    def get_item(self, id_item): #consultar
        self.cart.pop
        


 
        
        
carrinhoitem.append


class Carrinho:
