import os; os.system('cls')
import random
import json
import time

used_pins=[]
quest_and_response = {}

def login(login=False, create_login_prof=False, student=False, existent_account=False, type='000', database=None):
    if login:    
        if create_login_prof:
            file = open('./dev/games/users_prof.csv', 'a+')
            typee = 'prof'
            login = input('Digite seu nome de login: ')
            try:
                while True:
                    senha = input('Digite sua senha: ')
                    senha_conf = input('Confirme sua senha: ')
                    if senha != senha_conf:
                        print('Senha incorreta, tente novamente...')
                        time.sleep(1)
                    else:
                        file.writelines(f'{typee},{login},{senha}')
                        break
            except ValueError:
                print('Valor incorreto!!')
            return typee
        
        if existent_account:
            try:
                typee = 'prof'
                while True:
                    login = input('Digite seu login: ')
                    senha = input('Digite sua senha: ')
                    file = open('./dev/games/users_prof.csv', 'r+')
                    db = file.readlines()
                    lista = []
                    for i in db:
                        lista.append(i.strip().split('\n'))
                    del lista[0]
                    print(lista)
                    if login and senha in lista:
                        print(f'Bem vindo {login}')
                        time.sleep(1)
                        break
                    print(lista)
            except ValueError:
                print('Digite um valor valido!')
            return typee
        
        if student:
            pin = int(input('Digite o pin da partida: '))

def questions(create_questions_false_or_true=False, create_question_four=False, create_question_three=False, questions={}, add_questions=False, remove_questions=False, read_questions=False, send_questions=False, database=None, game_pin=None):
    if read_questions:
        while True:
            try:
                with open(f'./dev/games/{database}-game.csv', 'r+') as arquivo:
                    conteudo = arquivo.read().strip()
                    _, perguntas = conteudo.split('\n', 1)
                    dicionario = json.loads(perguntas)
                    
                    os.system('cls')
                    print(f'Perguntas:')
                    for i, (c, v) in enumerate(dicionario.items()):
                        print(f' [{i}] [{c}] = {v}')
                    print()
                    chaves = list(dicionario.keys())
                    if len(chaves) == 0:
                        print('Não foi adicionada nenhuma pergunta...')
                        time.sleep(1)
                        os.system('cls')
                        break
                    
                    deletar = input('Digite o numero da questão que quer remover ou sair: ')
                    if deletar == 'sair':
                        print('Saindo...')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        deletar = int(deletar)

                        if deletar < 0 or deletar >= len(chaves):
                            print('Índice inválido...')
                            time.sleep(1)
                            os.system('cls')
                            break
                        else:
                            chave_remover = chaves[deletar]
                            dicionario.pop(chave_remover)
                            quest_and_response.pop(chave_remover)
                            arquivo.seek(0)
                            arquivo.write(f'{database}\n{json.dumps(dicionario)}')
                            arquivo.truncate()
                            print('Removendo pergunta...')
                            time.sleep(1)
                            os.system('cls')
                            break
            except ValueError:
                print('Não foi adicionada nenhuma pergunta!!!')
                time.sleep(1)
                os.system('cls')
                break
            
    if add_questions:
        os.system('cls')
        while True:
            if create_questions_false_or_true:
                responses = []
                question = input(f'Digite a pergunta:') #Exemplo: prof ira enviar a pergunta
                #Exemplo das perguntas sendo adicionadas(SÓ SUBSTITUIR)
                #------------------------------------------------------------------
                #Adicionando a primeira pergunta:
                for i in range(1, 3):
                    os.system('cls')
                    response = input(f'Digite a {i}° resposta: ') #Exemplo: prof ira enviar a 1° e 2° resposta
                    false_or_true = input(f'Essa é uma resposta true ou false: ') #Exemplo : prof ira dizer se é falso ou verdadeiro
                    responses.append([response, false_or_true])
                quest_and_response[question] = responses
                #------------------------------------------------------------------
                break
            if create_question_four:
                responses = []
                question = input(f'Digite a pergunta:')
                for i in range(1, 5):
                    os.system('cls')
                    response = input(f'Digite a {i}° resposta: ')
                    false_or_true = input('Essa é uma pergunta false ou true?')
                    responses.append([response, false_or_true])
                quest_and_response[question] = responses
                break

            if create_question_three:
                responses = []
                question = input(f'Digite a pergunta:')
                for i in range(1, 4):
                    os.system('cls')
                    response = input(f'Digite a {i}° resposta: ')
                    false_or_true = input('Essa é uma pergunta false ou true?')
                    responses.append([response, false_or_true])
                quest_and_response[question] = responses
                break

            if send_questions:
                with open(f'./dev/games/{database}-game.csv', 'w+') as file:
                    dict_string = json.dumps(quest_and_response)
                    file.write(f'{database}\n{dict_string}')
                break
        return quest_and_response

def database(new_game=False, add_players=False, game_pin='000', remove_players=False):
    if new_game:
        while True:
            rnd=random.randint(10000, 99999)
            if not rnd in used_pins:
                used_pins.append(rnd)
                with open(f'./dev/games/{rnd}-game.csv', 'a') as file:
                    file.write(f'{rnd}')
                break
        return rnd

try:
    indent = int(input('[0] - Aluno [1] - Professor :'))
    if indent == 0:
        login(login=True, student=True)
    elif indent == 1:
        escolha = int(input('Criar conta [0] ou usar existente? [1] '))
        if escolha == 0:
            type = login(login=True, create_login_prof=True)
        elif escolha == 1:
            type = login(login=True, existent_account=True)
    if type == 'prof':
        escolha = input('Deseja criar a partida? ')
        if escolha == 'sim':
            game_pin = database(new_game=True)
            while True:
                escolha = input(f'Perguntas: [0] - Adicionar [1] - Consultar ou sair? PIN= [{game_pin}]')
                if escolha == 'sair':
                    break
                elif escolha == '1':
                    questions(read_questions=True, database=game_pin, game_pin=game_pin)
                elif escolha == '0':
                    os.system('cls')
                    pergunt = int(input('Quantas perguntas você quer adicionar? '))
                    os.system('cls')
                    for i in range(1, pergunt+1):
                        print('[1] - Duas Alternativas [2] - Três Alternativas [3] - Quatro Alternativas')
                        pergunta = input(f'Qual sera o tipo da sua {i}° pergunta?')

                        if pergunta == '1':
                            questions(add_questions=True, create_questions_false_or_true=True, database=game_pin)
                        elif pergunta == '2':
                            questions(add_questions=True, create_question_three=True, database=game_pin)
                        elif pergunta == '3':
                            questions(add_questions=True, create_question_four=True, database=game_pin)
                    questions(add_questions=True, send_questions=True, database=game_pin)
except ValueError:
    print('Digite 0 ou 1')


    