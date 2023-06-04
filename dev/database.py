import random

used_pins=[]

def database(new_game=False, add_players=False, game_pin='000', remove_players=False):
    if new_game:
        while True:
            rnd=random.randint(10000, 99999)
            if not rnd in used_pins:
                used_pins.append(rnd)
                with open(f'./dev/games/{rnd}-game.csv', 'a') as file:
                    file.write('')
                break
        return rnd


def pontos(resposta = False, tempo=0, segundos=0):
    if resposta == True:
        pts = round((1 - ((segundos/tempo)/2))*1000)
    else:
        pts = 0
    return pts
