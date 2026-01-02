#sistema
from aluno import Aluno
import json
import os

class SistemaCadastro:
    """Classe principal do sistema de cadastro"""

    def __init__(self, arquivo_dados='alunos.json'):
        self.alunos = []
        self.arquivo_dados = arquivo_dados
        self.carregar_dados()

    def cadastrar_alunos(self):
        """Cadastra um novo aluno"""
        print("\n" + "="*40)
        print("CADASTRO DE ALUNO")
        print("="*40)

        try:
            nome = input("Nome: ").strip()
            if not nome:
                print("Erro: Nome não pode ser vazio!")
                return
            
            idade = int(input("Idade: "))
            if idade <= 0 or idade > 120:
                print("Erro: idade inválida!")
                return
            
            matricula = input("Matricula: ").strip()
            if not matricula: 
                print("Erro: Matrícula não pode ser vazia")
                return
            
            #Verifica se matricula já existe
            if any(Aluno.matrícula == matricula for aluno in self.alunos):
                print(f"Erro: Matrícula {matricula} já cadastrada")
                return
            
            #Cria e adiciona o aluno 
            novo_aluno = Aluno(nome, idade, matricula)
            self.alunos.append(novo_aluno)
            self.salvar_dados()

            print(f"\n aluno {nome} cadastrado com sucesso!")

        except ValueError:
            print("Erro: Idade deve ser um número inteiro!")

    def listar_alunos(self):
        """Lista todos os alunos cadastrados"""
        print("\n" + "="*50)
        print("LISTA DE ALUNOS CADASTRADOS")
        print("="*50)

        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        
        for i, aluno in enumerate(self.alunos, 1):
            print(f"{i}. {aluno}")
            
        def buscar_por_matricula(self):
            """Busca um aluno pela matrícula"""
            print("\n" "="*40)
            print("BUSCA POR MATRICULA")
            print("="*40)

            matricula = input("Digite a matrícula: ")

            for aluno in self. alunos:
                if aluno.matricula == matricula:
                    print("\n ALUNO ENCONTRADO: ")
                    print(aluno)
                    return
                
            print(f"\n Nenhum aluno encontrado com matrícula {matricula}")

        def calcular_media_idades(self):
            """Calcula a média das idades dos alunos"""
            print("\n" "="*40)
            print("MÉDIA DE IDADES")
            print("="*40)

            if not self.alunos:
                print("Nenhum aluno cadastrado para calcular a média")
                return
            
        total_idades = sum(aluno.idade for aluno in self.alunos)
        media = total_idades / len(self.alunos)

        print(f"Total de alunos: {len(self.alunos)}")
        print(f"Soma das idades: {total_idades}")
        print(f"Média das idades: {media:.2f} anos")

        def salvar_dados(self):
            """Salva os alunos em um arquivo JSON"""
            try:
                dados = [aluno.to_dict() for aluno in self.alunos]
                with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                    json.dump(dados, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print("Erro ao salvar dados: {e}")

            def carregar_dados(self):
                """Carrega os alunos em um arquivo JSON"""
                try:
                    if os.path.exists(self.arquivo_dados):
                        with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                            dados = json.load(f)
                            self.alunos = [Aluno(**aluno) for aluno in dados]
                        print(f"Dados carregados: {len(self.alunos)} aluno(s)")
                except Exception as e:
                    print(f"Erro ao carregar dados: {e} ")
                    self.alunos = []
            
            def exibir_alunos(self):
                """Exibe o menu principal"""
                print("\n" "="*50)
                print("SISTEMA DE CADASTRO DE ALUNOS")
                print("="*50)
                print("1. Cadastra novo aluno")
                print("2. Listar todos os alunos")
                print("3. Buscar aluno por matrícula")
                print("4. Calcular média das idades")
                print("="*50)

            def executar(self):
                """Método principal que excuta o sistema"""
                while True:
                    self.exibir_menu()

                    try:
                        opcao = input("\nDigite sua opção (1-5): " ).strip()

                        if opcao == '1':
                            self.cadastrar_aluno()
                        elif opcao == '2':
                            self.listar_alunos()
                        elif opcao == '3':
                            self.buscar_por_matriculas()
                        elif opcao == '4':
                            self.calcular_media_idades()
                        elif opcao == '5': 
                            print("\n Programa encerrado. Até mais!")
                            break
                        else:
                            print("Opção invalida! Digite um número de 1 a 5.")

                    except KeyboardInterrupt:
                        print("n\n Programa interrompido pelo usuário.")
                        break
                    except Exception as e:
                        print(f"\n Ocorreu um erro: {e}")
