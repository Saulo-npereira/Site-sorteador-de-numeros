from flask import Flask, render_template, redirect, request, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        numero = request.form['numeroForm']
        if numero == '':
            return render_template('home.html', numero='digite algum número')
        numero = int(numero)
        numero_sorteado = random.randint(0, numero)
        return render_template('home.html', numero=numero_sorteado)
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True)

    