from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import FichaPersonagemModel

app = Flask(__name__)

# Conexão com Banco de Dados
user = 'mpxnnhum'
password = 'X_Q7OkzkpL_fIafb5mGD3QGH1Ut_VIMD'
host = 'tuffi.db.elephantsql.com'
database = 'mpxnnhum'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

personagem = FichaPersonagemModel


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/read')
def readAll():
    registros = personagem.FichaPersonagem.readAll()
    closeConn = db.session.close_all()
    return render_template('readAll.html', registros=registros, closeConn = closeConn)


@app.route('/read/<idRegistro>')
def readSingle(idRegistro):
    registro = personagem.FichaPersonagem.readSingle(idRegistro)
    closeConn = db.session.close_all()
    return render_template('fichaCompleta.html', registro=registro, closeConn = closeConn)


# CREATE
@app.route('/create', methods=('GET', 'POST'))
def create():
    idAtribuido = None
    if request.method == 'POST':
        form = request.form
        registro = personagem.FichaPersonagem(
            form['nome'], form['classe'], form['imagem'], form['forca'],
            form['destreza'], form['constituicao'], form['sabedoria'],
            form['inteligencia'], form['bio'])
        registro.save()
        idAtribuido = registro.id
    closeConn = db.session.close_all()
    return render_template('create.html', idAtribuido=idAtribuido, closeConn = closeConn)


# UPDATE
@app.route('/update/<registroId>', methods=('GET', 'POST'))
def update(registroId):
    sucesso = None
    registro = personagem.FichaPersonagem.readSingle(registroId)
    if request.method == 'POST':
        form = request.form
        newData = personagem.FichaPersonagem(form['nome'], form['classe'],
                                             form['imagem'], form['forca'],
                                             form['destreza'],
                                             form['constituicao'],
                                             form['sabedoria'],
                                             form['inteligencia'], form['bio'])
        registro.update(newData)
        sucesso = True
    return render_template('update.html', registro=registro, sucesso=sucesso)


# DELETE
@app.route('/delete/<registroId>')
def delete(registroId):
    registro = personagem.FichaPersonagem.readSingle(registroId)
    return render_template('delete.html', registro = registro)

@app.route('/delete/<registroId>/confirmed')
def deleteConfirmed(registroId):
    sucesso = None
    registro = personagem.FichaPersonagem.readSingle(registroId)
    if registro:
        registro.delete()
        sucesso = True
    return render_template('delete.html', registro = registro, registroId = registroId, sucesso = sucesso)

if __name__ == '__main__':
    app.run(debug=True)