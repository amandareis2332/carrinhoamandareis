carrinho = []
acao = ""
while acao != "S":    
    print("Aperte A para adicionar")
    print("Aperte L para listar os produtos")
    print("Aperte C para consultar item")
    print("Aperte R para remover")
    print("Aperte S para sair")
    acao = input("Qual opção você deseja?")
    acao= acao.upper()
    if acao == "A":
        print("Adicionou")
        id_produto = input("informe o id do produto")
        valor_produto = input("informe o valor do produto")
        quantidade_produto = input("Qual a quantidade?")
        item = [id_produto, valor_produto, quantidade_produto]
        carrinho.append(item)
    else:
        if acao == "L":
            print("Listou")
            for elemento in carrinho:
                print("id do produto", elemento[0])                
                print("valor do produto", elemento[1])
                print("quantidade do produto", elemento[2])
                # listar todos items do seu carrinho
        else:
            if acao == "C":
                print("Consultou")
                id_produto = input("Qual o id do produto?")
                for elemento in carrinho:
                    if id_produto == elemento[0]:
                        print("id do produto", elemento[0])                
                        print("valor do produto", elemento[1])
                        print("quantidade do produto", elemento[2])
              # consultar um item do seu carrinho pelo id do produto
            else:
                if acao == "R":
                    print("Removeu")
                    for index, elemento in enumerate(carrinho):
                        if id_produto == elemento[0]:
                            carrinho.pop(index) 