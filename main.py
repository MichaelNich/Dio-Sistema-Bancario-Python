import time


def checar_valor(valor, valor2):
    try:
        valor = float(valor)
        if valor <= 0:
            print("Insira um valor maior do que 0")
        else:
            valor2 = False
    except ValueError:
        print("Valor de deposito precisa ser numérico.")


class Conta:
    def __init__(self):
        self.saldo = 0
        self.LIM_SAQUES = 3
        self.num_saques = 0
        self.LIMITE_VALOR_SAQUES = 500
        self.extrato = f"""#########---EXTRATO BANCÁRIO---#########
        Saldo inicial: R${self.saldo}
        """

    def depositar(self):
        self.valor_deposito = None
        self.check_deposito = (
            True  # checa se valor é um número e se o valor é maior do que 0
        )

        while self.check_deposito:
            self.valor_deposito = input("Insira a quantia desejada para depositar: ")

            # Try except para checar se o valor é numérico
            try:
                self.valor_deposito = float(self.valor_deposito)
                if (
                    self.valor_deposito <= 0
                ):  # checa se valor do deposito é maior do que 0
                    print("Insira um valor maior do que 0")
                else:
                    self.check_deposito = False
            except ValueError:
                print("Valor de deposito precisa ser numérico.")

        self.saldo += self.valor_deposito
        self.extrato += f"Valor depositado: R${self.valor_deposito:.2f}\n"
        print(f"Valor depositado: R${self.valor_deposito:.2f}")

    def sacar(self):
        if self.num_saques == self.LIMITE_VALOR_SAQUES:
            print(
                "Quantidade máxima diária de saques alcançada. não é possível mais sacar hoje."
            )
            return
        elif self.saldo == 0:
            print("Você não possui nenhum saldo disponível para saque!")
            return
        else:
            self.check_saque = True

        while self.check_saque:
            self.valor_saque = input("Insira a quantia desejada para sacar: ")

            try:
                self.valor_saque = float(self.valor_saque)
                if self.valor_saque <= 0:  # checa se valor do deposito é maior do que 0
                    print("Insira um valor maior do que 0")
                elif self.valor_saque > self.saldo:
                    print(
                        f"Valor insuficiente para saque. você possui atualmente: R${self.saldo:.2f}"
                    )
                else:
                    self.check_saque = False
            except ValueError:
                print("Valor de saque precisa ser numérico.")
        print(
            "Saque no valor de R$", f"{self.valor_saque:.2f}", " realizado com sucesso!"
        )
        self.extrato += f"Valor sacado: R${self.valor_saque:.2f}\n"
        self.saldo -= self.valor_saque
        self.num_saques += 1

    def visualizar_extrato(self):
        print(self.extrato)
        print("Saldo atual: ", f"{self.saldo:.2f}")
        print("#########------#########")


def main():
    menu = """
    [d] = depositar
    [s] = sacar
    [e] = extrato
    [t] = sair
    Insira a letra correspondente a operação desejada: """
    pessoa = Conta()

    escolha = None
    while escolha != "t":
        escolha = input(menu)

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
