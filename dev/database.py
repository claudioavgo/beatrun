import random

used_pins=[]
quest_and_response = {}

def questions(create_questions_false_and_true=False, add_questions=False, remove_questions=False, send_questions=False, database=None):
    if create_questions_false_and_true:
        while True:
            #Exemplo das perguntas sendo adicionadas(SÓ SUBSTITUIR)
            #------------------------------------------------------------------
            #Adicionando a primeira pergunta:

            question = input(f'Digite a pergunta:') #Exemplo: prof ira enviar a pergunta
            first_response = input(f'Digite a primeira resposta: ') #Exemplo: prof ira enviar a 1° resposta
            false_and_true = input(f'Essa é uma resposta true ou false: ') #Exemplo : prof ira dizer se é falso ou verdadeiro
            response1 = [first_response, false_and_true]

            #Adicionando a segunda pergunta:

            second_response = input(f'Digite a segunda resposta: ') #Exemplo: prof ira enviar a 2° resposta
            false_and_true = input(f'Essa é uma resposta true ou false: ') #Exemplo : prof ira dizer se é falso ou verdadeiro
            response2 = [second_response, false_and_true]
            quest_and_response[question] = [response1, response2]
            quest_and_response['teste'] = [['teste1', 'True'], ['teste2', 'True']]
            #------------------------------------------------------------------

            if send_questions:
                with open(f'./dev/games/{database}-game.csv', 'a') as file:
                    file.write(f'\n{quest_and_response}')
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

game_pin = database(new_game=True)
questions(create_questions_false_and_true=True,send_questions=True, database=game_pin)
    