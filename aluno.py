#aluno.py
class Aluno:
    """Classe que representa um aluno"""

    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula 

    def __str__(self):
        """Retorna uma representação em string do aluno"""
        return f"matricula: {self.matricula} | Nome: {self.nome} | {self.idade}"
    
    def to_dict(self):
        """Converte o aluno para o dicionario(útil para salvar em JSON)"""
        return {
            'nome': self.nome
            'idade': self.idade
            'matricula': self.matricula
        }
