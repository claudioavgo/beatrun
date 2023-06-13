from flask import Flask, render_template, url_for, redirect, request, make_response
import jinja2
import dev.database as db
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/login-professor', methods=['GET', 'POST'])
def login_professor():
    if request.method == 'GET':
        return render_template('login-professor.html')
    if request.method == "POST":
        if db.database(acc_check=True, email=request.form.get("email", False), senha=request.form.get("senha", False)):
            resp = make_response(redirect(url_for('create_game')))
            resp.set_cookie('email',f'{request.form.get("email", False)}')
            resp.set_cookie('senha', f'{request.form.get("senha", False)}')
            return resp
        else:
            return render_template('login-professor.html')
    
@app.route('/create-game', methods=['GET', 'POST'])
def create_game():
    if request.method == 'GET':
        return render_template('create-game.html')
    
@app.route('/login-aluno', methods=['GET', 'POST'])
def login_aluno():
    if request.method == 'GET':
        pin = request.cookies.get('pin')
        user= request.cookies.get('nick')
        if pin:
            return redirect(url_for('aluno_aguardando'))

        return render_template('login-aluno.html')
    elif request.method == "POST":
        if db.database(check_game=True, game_pin=f'{request.form.get("pin", False)}'):
            resp = make_response(redirect(url_for('aluno_aguardando')))
            resp.set_cookie('pin',f'{request.form.get("pin", False)}')
            resp.set_cookie('nick', f'{request.form.get("nick", False)}')
            return resp
        else:
            return render_template('login-aluno.html')

def asyncx(pin):
    while True:
        if db.database(game_pin=pin, started=True):
            break

        time.sleep(2)
        
@app.route('/aluno-aguardando', methods=['GET', 'POST'])
def aluno_aguardando():
    if request.method == 'GET':
        pin = request.cookies.get('pin')
        asyncx(pin)
        return redirect(url_for('game'))
    
@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        pin = request.cookies.get('pin')
        user= request.cookies.get('nick')

        if not user:
            return redirect(url_for('login_aluno'))

        data = db.database(get_game=True, game_pin=pin)

        if not user in data["players"]:
            data["players"].update({f"{user}": {"pergunta": 0, "pontos": 0}})
            db.database(att_game=True, data=data, game_pin=pin)

        pergunta=list(data["perguntas"])[int(data["players"][user]["pergunta"])]
        resposta=data["perguntas"][pergunta]["respostas"]

        return render_template('game.html', pergunta=pergunta, resposta=resposta)
    else:
        pin = request.cookies.get('pin')
        user= request.cookies.get('nick')

        data = db.database(get_game=True, game_pin=pin)

        if not len(data["perguntas"]) <= int(data["players"][user]["pergunta"])+1:
            pergunta=list(data["perguntas"])[int(data["players"][user]["pergunta"])]
            if request.args.get('letra') == data["perguntas"][pergunta]["certa"]:
                data["players"][user]["pontos"]+=200
            data["players"][user]["pergunta"]+=1
            db.database(att_game=True, data=data, game_pin=pin)
            return redirect(url_for('game'))
        else:
            resp = make_response(render_template('game-final.html', pontuacao=data["players"][user]["pontos"]))
            resp.delete_cookie('pin')
            return resp

@app.route('/registro-professor', methods=['GET', 'POST'])
def registro_professor():
    if request.method == 'GET':
        return render_template('registro-professor.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        email = request.cookies.get('email')
        data, nome=db.database(acc_get=True, email=email)
        questoes=data["users"][nome]["questoes"]
        questoes_tratadas=[]
        for questao in questoes:
            if len(questao) > 43:
                questoes_tratadas.append(questao[:43])
            else:
                questoes_tratadas.append(questao)

        return render_template('dashboard.html', questoes=questoes_tratadas)
    else:
        email = request.cookies.get('email')
        data, nome=db.database(acc_get=True, email=email)
        if request.args.get('botao') == "adicionar":
            return redirect(url_for('dashboard_create'))
        
@app.route('/dashboard-create', methods=['GET', 'POST'])
def dashboard_create():
    if request.method == 'GET':
        return render_template('dashboard-create.html')
    else:
        email = request.cookies.get('email')
        data, nome=db.database(acc_get=True, email=email)

        nova_pergunta=request.form.get("pergunta", False)
        nova_pergunta_letra_a=request.form.get("a", False)
        nova_pergunta_letra_b=request.form.get("b", False)
        nova_pergunta_letra_c=request.form.get("c", False)
        nova_pergunta_letra_d=request.form.get("d", False)
        nova_pergunta_correta=request.form.get("correta", False)

        data["users"][nome]["questoes"].update({nova_pergunta: {"respostas": [nova_pergunta_letra_a, nova_pergunta_letra_b, nova_pergunta_letra_c, nova_pergunta_letra_d], "certa":request.form.get(nova_pergunta_correta, False)}})

        db.database(acc_att=True, data=data)

        return redirect(url_for("dashboard"))

@app.route('/dashboard-share', methods=['GET', 'POST'])
def dashboard_share():
    if request.method == 'GET':
        email = request.cookies.get('email')
        data, nome=db.database(acc_get=True, email=email)

        rnd=db.database(new_game=True, data=data["users"][nome]["questoes"])
        resp = make_response(render_template('dashboard-share.html', pin=rnd))
        resp.set_cookie('pin',f'{rnd}')

        return resp
    else:
        pin = request.cookies.get('pin')
        print(request.args.get('botao'))
        if request.args.get('botao') == "comecar":
            data = db.database(get_game=True, game_pin=pin)
            data["started"]=1
            db.database(att_game=True, game_pin=pin, data=data)
        return render_template('dashboard-share-view.html', pin=pin)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)