from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#Quando Fdiferenciamos Maiusculas o sqlalchemy adota uma sintaxe separando as palavras com _ exemplo FichaPersonagem passa a ser em tempo de execução ficha_personagem
class FichaPersonagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    classe = db.Column(db.String(255), nullable=False)
    imagem = db.Column(db.String(255), nullable=False)
    forca = db.Column(db.Integer, nullable=False)
    destreza = db.Column(db.Integer, nullable=False)
    constituicao = db.Column(db.Integer, nullable=False)
    sabedoria = db.Column(db.Integer, nullable=False)
    inteligencia = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.Text, nullable=False)

    def __init__(self, nome, classe, imagem, forca, destreza, constituicao,
                 sabedoria, inteligencia, bio):
        self.nome = nome
        self.classe = classe
        self.imagem = imagem
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.sabedoria = sabedoria
        self.inteligencia = inteligencia
        self.bio = bio

    @staticmethod
    def readAll():
        # Select * from filmes order by id desc
        return FichaPersonagem.query.order_by(FichaPersonagem.nome.asc()).all()

    @staticmethod
    def readSingle(idRegistro):
        # Select * from filmes order by id desc
        return FichaPersonagem.query.get(idRegistro)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, newData):
        self.nome = newData.nome
        self.classe = newData.classe
        self.imagem = newData.imagem
        self.forca = newData.forca
        self.destreza = newData.destreza
        self.constituicao = newData.constituicao
        self.sabedoria = newData.sabedoria
        self.inteligencia = newData.inteligencia
        self.bio = newData.bio
        self.save()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
