cart = []
id_user = input("insira o id do usuario")
id_produto = input("insira o id do produto")
price_produto = float(input("insira o preco do produto"))
quantity_produto = int(input("insira a quantidade do produto"))

item = [id_produto, id_user,price_produto,quantity_produto]

def add_item_cart():
    cart.append(item)
    print("sucesso") 

def get_all_itens_cart():
    return cart

def get_item_carrinho(id_produto):
    new_list = [item for item in cart if item[0] == id_produto]
    return new_list[0]

    