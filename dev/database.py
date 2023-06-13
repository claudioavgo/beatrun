import random
import json

used_pins=[]

def database(acc_att=False, acc_get=False, att_game=False,data="undefined",check_game=False, started=False, get_questions=False, create_question=False, question='undefined', acc_check=False, email='undefined', senha='undefined', get_game=False, new_game=False, add_players=False, game_pin='000', remove_players=False):
    if new_game:
        while True:
            rnd=random.randint(10000, 99999)
            if not rnd in used_pins:
                used_pins.append(rnd)
                with open(f'./dev/games.json', 'r') as arquivox:
                    save = arquivox.readline()
                    arquivox.close()
                with open(f'./dev/games.json', 'w') as arquivo:
                    save=json.loads(save)
                    save["games"].append(str(rnd))
                    arquivo.write(str(save).replace("'", '"'))
                with open(f'./dev/games/{rnd}-game.json', 'a') as file:
                    base={"game.id":rnd,"started":0,"players":{},"perguntas":{}}
                    base["perguntas"].update(data)
                    file.write(str(base).replace("'", '"'))
                    return rnd
                break
        return rnd
    elif get_game:
        with open(f'./dev/games/{game_pin}-game.json', 'r') as file:
            primeira_linha=file.readline()
            data=json.loads(primeira_linha)
            return(data)
    elif acc_check:
        with open(f'./dev/users_prof.json', 'r') as file:
            dados = json.loads(file.readline())
            
            for i in dados["users"]:
                if email == dados["users"][i]["email"] and  senha == dados["users"][i]["senha"]:
                    return True
            return False
    elif create_question:
        with open(f'./dev/games/{rnd}-game.json', 'a') as file:
            file.write('')
    elif started:
        with open(f'./dev/games/{game_pin}-game.json', 'r') as file:
            data=json.loads(file.readline())
            if data["started"] == 0:
                return False
            else:
                return True
    elif check_game:
        with open("./dev/games.json", 'r') as file:
            data = json.loads(file.readline())
            if game_pin in data["games"]:
                return True
            else:
                return False
    elif att_game:
        with open(f'./dev/games/{game_pin}-game.json', 'w') as file:
            file.write(str(data).replace("'", '"'))
    elif acc_get:
        with open(f'./dev/users_prof.json', 'r') as file:
            dados = json.loads(file.readline())
        
        for i in dados["users"]:
            if dados["users"][i]["email"] == email:
                return dados, i
        return False
    elif acc_att:
        with open(f'./dev/users_prof.json', 'w') as file:
            file.write(str(data).replace("'", '"'))