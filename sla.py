from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rf_fitness_secret_key'

@app.route('/', methods=['GET', 'POST'])
def etapa1():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        session['email'] = request.form['email']
        session['telefone'] = request.form['telefone']
        return redirect(url_for('etapa2'))
    return render_template('index.html')

@app.route('/etapa2', methods=['GET', 'POST'])
def etapa2():
    if request.method == 'POST':
        session['peso'] = request.form['peso']
        session['altura'] = request.form['altura']
        session['objetivo'] = request.form['objetivo']
        return redirect(url_for('obrigado'))
    return render_template('etapa2.html')

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')

if __name__ == '__main__':
    app.run(debug=True)
