class SENAIBANK:
    agencia=0
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.__saldo = 50
        self.lista_extrato = []

    def sacar(self, valor_saque):
        if valor_saque > self.__saldo:
            return False
        return True
    def efetivar_saque(self, valor_saque):
       self.__saldo = self.__saldo - valor_saque
       self.lista_extrato.append(self.__saldo)
       return self.__saldo

    def depositar(self, valor_deposito):
       self.__saldo =  self.__saldo+valor_deposito
       self.lista_extrato.append(self.__saldo)
       return self.__saldo

    def transferir(self, valor_transferido):
        self.__saldo = self.__saldo - valor_transferido
        self.lista_extrato.append(self.__saldo)
        return self.__saldo

    def registrar(self, operacao, valor):
        self.lista_extrato.append(operacao, valor)

    def extrato(self):

        return self.__saldo