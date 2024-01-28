################ Funções ################

def iniciar():
    tarefa = input("Ok senhor, me fale a tarefa que o senhor deseja realizar >>> ")
    descricao = input("Descrição da tarefa >>> ")
    grau_necessidade = input("Qual grau de necessidade (Alto, Médio, Baixo): ")
    armazenamento.append({"tarefa": tarefa, "descricao": descricao, "grau_necessidade": grau_necessidade})
    print("Tarefa colocada  !!!!!!")

def excluir():
    tarefa = input("Ok senhor, me fale a tarefa que o senhor deseja excluir >>> ")
    encontrada = False
    for tarefa in armazenamento:
        if tarefa['tarefa'] == tarefa:
            armazenamento.remove(tarefa)
            print("Tarefa excluída!!!!")
            encontrada = True
            break
    if not encontrada:
        print("Tarefa não encontrada!!!!")

def ver_tarefas():
    if armazenamento:
        print("Tarefas:")
        for i, tarefa in enumerate(armazenamento, 1):
            print(f"{i}. Tarefa: {tarefa['tarefa']}")
            print(f"     Descrição: {tarefa['descricao']}")
            print(f"     Grau de Necessidade: {tarefa['grau_necessidade']}")
    else:
        print("Não há tarefas disponíveis.")

################ Listas ################

armazenamento = []

################ Menu ################

print('''
    1. Iniciar uma tarefa
    2. Excluir uma tarefa
    3. Ver tarefas
    4. Sair
''')

escolhas = input("Escolha uma das opcoes: ")

################ Escolhas ################

if escolhas == '1':
    iniciar()

elif escolhas == '2':
    excluir()

elif escolhas == '3':
    ver_tarefas()

elif escolhas == '4':
    print("Finalizando sistema, obrigado por usar...")

else:
    print("ERROR0101010110100")


