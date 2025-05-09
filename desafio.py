lista = []
while True:
    menu = int(input("""\nBem-vindo(a) a sua lista. 
Listar as tarefas: (1) | Inserir uma tarefa:(2) | Deletar uma tarefa:(3) | Sair (4) """))
    if menu == 1:
        print(lista)
    elif menu == 2:
        dado = input("\nDigite a nova tarefa: ")
        lista.append(dado)
    elif menu == 3:
        print("Tarefa deletada!")
        lista.pop()
    elif menu == 4:
        print("Menu encerrado!")
        break
    else:
        print("Erro!")
        break