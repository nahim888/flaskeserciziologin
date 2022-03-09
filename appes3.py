#Realizzare un server web che permetta di conoscere i capoluoghi di regione.
#L'utente inserisce il nome della regione e il programma restituisce il nome del capoluogo di regione.
#Caricare i capoluoghi di regione e le regioni in una opportuna struttura dati.
#Modificare poi l'esercizio precedente per permettere all'utente di inserire un capoluogo e di avere la regione in cui si trova.
#L'utente sceglie se avere la regione o il capoluogo selezionando un radiobutton

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

dict = {"Abruzzo":"L'Aquila", "Basilicata":"Potenza", "Calabria":"Catanzaro", "Campania":"Napoli", "Emilia-Romagna":"Bologna", "Friuli-Venezia Giulia":"Trieste", "Lazio":"Roma", "Liguria":"Genova", "Lombardia":"Milano", "Marche":"Ancona", "Molise":"Campobasso", "Piemonte":"Torino", "Puglia":"Bari", "Sardegna":"Cagliari", "Sicilia":"Palermo", "Toscana":"Firenze", "Trentino-Alto Adige":"Trento", "Umbria":"Perugia", "Valle d'Aosta":"Aosta", "Veneto":"Venezia"}
key_list = list(dict.keys())
values_list = list(dict.values())

def get_key(val):
    for key, value in dict.items():
         if val == value:
             return key

@app.route('/', methods=['GET'])
def index():
    return render_template('home_es3.html')

@app.route('/capreg', methods=['GET'])
def capreg():
    return render_template('capreg.html')

@app.route('/capreg1', methods=['GET'])
def capreg1():
    name = request.args['name']
    if name not in key_list:
        return render_template("errore_es3.html", errore = "Regione non trovata")
    else:
        d = dict[name]
    return render_template('capregf.html', d = d)

@app.route('/regcap', methods=['GET'])
def regcap():
    return render_template('regcap.html')

@app.route('/regcap1', methods=['GET'])
def regcap1():
    name = request.args['name']
    if name not in values_list:
        return render_template("errore_es3.html", errore = "Capoluogo non trovato")
    else:
        d = get_key(name)
    return render_template("regcapf.html", d = d)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)