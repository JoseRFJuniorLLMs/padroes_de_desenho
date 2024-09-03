"""
Propósito: Define una familia de algoritmos, encapsula cada uno y los hace intercambiables. Permite al algoritmo variar independientemente de los clientes que lo utilizan.
"""

class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paying {amount} using credit card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paying {amount} using PayPal"

class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        return self._strategy.pay(amount)

# Uso
context = PaymentContext(CreditCardPayment())
print(context.execute_payment(100))  # Imprime: Paying 100 using credit card
context = PaymentContext(PayPalPayment())
print(context.execute_payment(200))  # Imprime: Paying 200 using PayPal

