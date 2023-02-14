class CuentaBancaria:

    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f"Se depositaron {monto} pesos. El nuevo saldo es de {self.balance} pesos.")

    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
            print(f"Se retiraron {monto} pesos. El nuevo saldo es de {self.balance} pesos.")
        else:
            print("No se puede retirar la cantidad solicitada. Fondos insuficientes.")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se aplicó una cuota de manejo del 2%, equivalente a {cuota_manejo} pesos. El nuevo saldo es de {self.balance} pesos.")

    def mostrar_detalles(self):
        print(
            f"Detalles de la cuenta bancaria\nNúmero de cuenta: {self.numero_cuenta}\nPropietarios: {self.propietarios}\nSaldo: {self.balance} pesos")