import random

MAX_FOME = 10
MAX_TEDIO = 10
MAX_SAUDE = 10

trabalhos = ["Lenhador", "Mecanico", "Professor", "Jardineiro", "Olheiro", "Fogueteiro"]

class PetF:
    def __init__(self, nome):
        self.nome = nome
        self.dia = 1
        self.fome = 5
        self.tedio = 5
        self.saude = 10
        self.empregado = False 
        self.emprego = "Nenhum"
        self.dinheiro = 0
        self.tempoSalario = 7

    def mostrarStatus(self):
        print(f"Dia: {self.dia}")
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome:.2f}")
        print(f"Tédio: {self.tedio:.2f}")
        print(f"Saúde: {self.saude:.2f}")
        print(f"Dinheiro: {self.dinheiro:.2f}R$")
        
    def alimentar(self):
        print(f"\nVocê alimentou {self.nome}!")
        self.fome -= 3
        if self.fome < 0: self.fome = 0
        if self.fome > MAX_FOME: self.fome = MAX_FOME

    def brincar(self):
        if(self.fome > 7):
            print(f"{self.nome} está com muita fome e não pode brincar agora")
        else:
            print(f"\nVocê brincou com {self.nome}!")
            self.tedio -= 4
            self.fome += 2
            if self.tedio < 0: self.tedio = 0
            if self.fome > MAX_FOME: self.fome = MAX_FOME

    def descansar(self):
        print(f"\n{self.nome} está descansando...")
        self.saude += 2
        self.fome += 1
        if self.saude > MAX_SAUDE: self.saude = MAX_SAUDE
        if self.fome > MAX_FOME: self.fome = MAX_FOME
    
    def escolherEmprego(self):
        if(self.empregado == True):
            print("Você já está empregado!")
        else:
            empregoEscolhido = random.choice(trabalhos)
            print(f"Você agora está trabalhando como {empregoEscolhido}!")
            print(f"Seu primeiro salário será depositado em 7 Dias")
            self.emprego = empregoEscolhido
            self.empregado = True

    def passarTempo(self):
        self.fome += 0.2
        self.tedio += 0.2
        if self.fome > 7: self.saude -= 1 
        if self.fome > MAX_FOME: self.fome = MAX_FOME
        if self.tedio > MAX_TEDIO: self.tedio = MAX_TEDIO
        self.dia += 1

        if(self.empregado):
            self.tempoSalario -= 1
            if(self.tempoSalario <= 0):
                salario = random.randint(100, 1500)
                print(f"Salário depositado: {salario}R$")
                self.tempoSalario = 7
                self.dinheiro += salario

        if self.saude <= 0:
            print(f"\nInfelizmente, {self.nome} ficou muito fraco e MORREU.")
            exit()
