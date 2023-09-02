import time
import random


class Conta:
    def __init__(self):
        self.cpf = input("Digite seu CPF: ")
        self.conta = None
        self.nome = input("Digite seu nome: ")
        self.idade = input("Digite sua idade: ")
        self.saldo = 0
        self.LIM_SAQUES = 3
        self.num_saques = 0
        self.SAQUE_VALOR_MAX = 500
        self.extrato = f"""#########---EXTRATO BANCÁRIO---#########
        Saldo inicial: R${self.saldo}
        """

    def depositar(self):
        while True:
            valor_deposito = input("Insira a quantia desejada para depositar: ")
            try:
                valor_deposito = float(valor_deposito)
                if valor_deposito <= 0:
                    print("Insira um valor maior do que 0")
                else:
                    self.saldo += valor_deposito
                    self.extrato += f"Valor depositado: R${valor_deposito:.2f}\n"
                    print(f"Valor depositado: R${valor_deposito:.2f}")
                    break
            except ValueError:
                print("Valor de deposito precisa ser numérico.")

    def sacar(self):
        if self.num_saques == self.LIM_SAQUES:
            print(
                "Quantidade máxima diária de saques alcançada. não é possível mais sacar hoje."
            )
            return
        elif self.saldo == 0:
            print("Você não possui nenhum saldo disponível para saque!")
            return

        while True:
            valor_saque = input("Insira a quantia desejada para sacar: ")
            try:
                valor_saque = float(valor_saque)
                if valor_saque <= 0:
                    print("Insira um valor maior do que 0")
                elif valor_saque > self.SAQUE_VALOR_MAX:
                    print(
                        f"Valor máximo para saque é R${self.SAQUE_VALOR_MAX:.2f}! Você possui atualmente: R${self.saldo:.2f}"
                    )
                elif valor_saque > self.saldo:
                    print(
                        f"Valor insuficiente para saque. Você possui atualmente: R${self.saldo:.2f}"
                    )
                else:
                    self.saldo -= valor_saque
                    self.extrato += f"Valor sacado: R${valor_saque:.2f}\n"
                    self.num_saques += 1
                    print(
                        f"Saque no valor de R${valor_saque:.2f} realizado com sucesso!"
                    )
                    break
            except ValueError:
                print("Valor de saque precisa ser numérico.")

    def visualizar_extrato(self):
        print(self.extrato)
        print("Saldo atual: ", f"{self.saldo:.2f}")
        print("#########------#########")


class Banco:
    def __init__(self):
        self.id = 0
        self.contas = {}

    def mostrar_menu(self):
        menu = """
        [d] = depositar
        [s] = sacar
        [e] = extrato
        [t] = sair
        
        Insira a letra correspondente a operação desejada: """
        return menu

    def criar_conta(self, usuario):
        agencia = str(
            random.randint(0, 10000)
        )  # Gera um número entre 0 e 10000 e transform em string
        agencia = (
            (5 - len(agencia)) * "0"
        ) + agencia  # Adiciona 0 no ínicio da string para o tamanho ser sempre 5
        conta = str(random.randint(0, 1000000))
        conta = ((7 - len(agencia)) * "0") + conta

        self.contas[usuario.cpf] = {"agencia": agencia, "conta": conta, "saldo": 0}
        usuario.agencia = agencia
        usuario.conta = conta

        print(f"agencia: {usuario.agencia}\nconta: {usuario.conta}\nCPF: {usuario.cpf}")

    def listar_contas(self):
        print(self.contas)


def main():
    banco = Banco()
    pessoa = Conta()

    cpf = input("Digite seu CPF para acessar sua conta ou criar uma: ")

    if not pessoa.conta:
        print("Você não possui uma conta")
        banco.criar_conta(pessoa)
    else:
        agencia = input("Digite o número da sua agência: ")
        conta = input("Digite o número da sua conta: ")

    escolha = None
    while escolha != "t":
        escolha = input(banco.mostrar_menu())
        if escolha == "d":
            pessoa.depositar()
        elif escolha == "s":
            pessoa.sacar()
        elif escolha == "e":
            pessoa.visualizar_extrato()
        elif escolha == "t":
            print("Encerrando!")
        else:
            print("Comando: ", escolha, " não existe. repita o procedimento novamente.")
            time.sleep(3)  # Espera um tempo para o usuário ler a mensagem


if __name__ == "__main__":
    main()
