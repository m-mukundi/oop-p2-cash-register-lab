#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self._items = []
        self._discount = discount
        self._total = 0
        self._previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        self._items.append(item)
        self._total += price * quantity
        new_item = {"item": item, "price": price, "quantity": quantity}
        self._previous_transactions.append(new_item)

    def apply_discount(self):
        if self._discount > 0:
            self._total = self._total * (100 - self._discount) / 100
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self._previous_transactions) > 0:
            self._total = 0
            for transaction in self._previous_transactions:
                self._total += transaction["price"] * transaction["quantity"]

            last_transaction = self._previous_transactions[-1]

            self._items.remove(last_transaction["item"])
            self._total -= last_transaction["price"] * last_transaction["quantity"]
            self._previous_transactions.remove(last_transaction)
        else:
            print("You have no previous transactions")


# james_transactions = CashRegister()
# james_transactions.add_item("Orange", 30, 3)
# james_transactions.add_item("Milk", 65, 2)
# james_transactions.add_item("Rice", 349, 1)
# print(james_transactions._previous_transactions)
# print(james_transactions._items)
# print(james_transactions.discount)
# print(james_transactions._total)
# james_transactions.discount = 25
# print(james_transactions.discount)
# print(james_transactions._total)
# james_transactions.apply_discount()
# print(james_transactions.discount)
# print(james_transactions._total)
# james_transactions.void_last_transaction()
# print(james_transactions._previous_transactions)
# print(james_transactions._items)
# print(james_transactions.discount)
# print(james_transactions._total)
