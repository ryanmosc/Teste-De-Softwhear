class Aluno:
    def __init__(self, nome, idade, turma, nota):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.nota = nota

class Escola:
    def __init__(self):
        self.alunos = []
    
    def cadastrar_aluno(self, nome, idade, turma, nota):
        novo_aluno = Aluno(nome, idade, turma, nota)
        self.alunos.append(novo_aluno)

    def remover_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                self.alunos.remove(aluno)
                print("Aluno removido com sucesso")
                return 
        print("Aluno não encontrado")  
    
    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in self.alunos:
                print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Turma: {aluno.turma}, Nota: {aluno.nota}")

def perguntas_cadastro(escola):
    nome = input("Qual o nome do aluno? ")
    try:
        idade = int(input("Qual a idade? "))
    except ValueError:
        print("Insira somente números inteiros.")
        return  
    
    turma = input("Qual a turma? ")
    try:
        nota = float(input("Qual a nota? "))
    except ValueError:
        print("Insira somente números válidos para a nota.")
        return  
    
    escola.cadastrar_aluno(nome, idade, turma, nota)
    print("Aluno cadastrado com sucesso.")

escola = Escola()

while True:
    print("1- Cadastrar Aluno")
    print("2- Mostrar Lista")
    print("3- Remover Aluno")
    print("4- Sair")
    op = int(input("Qual função deseja selecionar? "))
    
    if op == 1:
        perguntas_cadastro(escola)

    elif op == 2:
        escola.listar_alunos()

    elif op == 3:
        nome = input("Qual o nome do aluno a ser removido? ")
        escola.remover_aluno(nome)

    elif op == 4:
        print("Saindo...")
        break

    else:
        print("Operação inválida. Tente novamente.")