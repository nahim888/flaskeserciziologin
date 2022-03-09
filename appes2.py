from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

utenti = []

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET'])
def login():
    username = request.args['username']
    password = request.args['password']
    for user in utenti:
        sex = user['sex']
        name = user['name']
        if user['sex'] == 'M':
            sex1 = 'o'
        if user['sex'] == 'F':
            sex1 = 'a'
        if user['sex'] == 'A':
            sex1 = '*'
        if user["username"] == request.args["username"]:
            if user["password"] == request.args['password']:
                return render_template('welcome2.html', letter=sex1 ,sex=sex, name=name, username=username,password=password)
    return render_template('error.html', err='utente non registrato')

@app.route('/data1', methods=['GET'])
def data():
    name = request.args['name']
    username = request.args['username']
    password = request.args['password']
    confirm = request.args['confirmpassword']
    sex = request.args['sex']
    if password == confirm:
        if sex:
            if username:
                if password:
                    if confirm:
                        if name:
                            utenti.append({"name": name, "username": username, "password": password, "confirm": confirm, "sex": sex})
                            print(utenti)
                            #return redirect(url_for("/login"))
                            return render_template('login.html', utenti=utenti)
    return render_template('error.html', nome = username, err='errore generico')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)
