from datetime import date


#CLASSE ENDERECO
class Endereco:
    def _init_(self, logradouro="",numero="", endereco_Comercial=False):
        #Inicializar os nossos atributos com valores padrao
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial


#CLASSE PESSOA
class Pessoa:
    def _init_(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento: float):
        return rendimento


#CLASSE PESSOA FISICA
class PessoaFisica(Pessoa):
    #Inicializar os atributos que foram herdados e proprios atributos da classe
    def _init_(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:
            #Se nenhum endereco for fornecido, cria um objeto Endereco padrao
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()
        

        super()._init_(nome, rendimento, endereco)
        #Chama o construtor da superclasse Pessoa para inicializar os atributos herdados

        #Atributos da propria classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def calcular_imposto(self, rendimento: float) -> float:
       #Sem imposto para rendimentos ate R$1500
        if rendimento <= 1500:
            return 0
        
        #2% de imposto para rendimentos entre 1500 e 3500
        elif 1500 < rendimento <= 3500:
            return (rendimento /100)* 2
        #3.5% de imposto para rendimentos entre 3500 e 6000
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        #5% de imposto para rendimentos acima de 6000
        else:
            return (rendimento / 100) * 5

#CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
    def _init_(self, nome='', rendimento=0.0, endereco=None, cnpj=''):
        if endereco is None:
            endereco = Endereco()

        super()._init_(nome, rendimento, endereco) # Chama o construtor da superclasse pessoa para inicializar os atributos herdados

        # Atributos da propria classe
        self.cnpj = cnpj

    def calcular_imposto(self, rendimento: float) -> float:
        # Sem importo para rendimentos até 1500
        if rendimento <= 8100:
            return 0
        elif rendimento > 8100 or rendimento <= 15000:
            # 2% sobre o rendimento
            # return (rendimento / 100) * 2
            return rendimento * 0.02
        elif rendimento > 15000 or rendimento <= 25000:
            # 3.5% sobre o rendimento
            return (rendimento / 100) * 3.5
        else:
            # 5% sobre o rendimento
            return (rendimento / 100) * 5 
    pass