#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.discount = discount
        self.total = 0
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        items_to_add = quantity
        while items_to_add > 0:
            self.items.append(item)
            items_to_add -= 1

        self.total += price * quantity
        new_item = {"item": item, "price": price, "quantity": quantity}
        self.previous_transactions.append(new_item)

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${self.total}.\n")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self.previous_transactions) > 0:
            self.total = 0
            for transaction in self.previous_transactions:
                self.total += transaction["price"] * transaction["quantity"]

            last_transaction = self.previous_transactions[-1]

            self.items.remove(last_transaction["item"])
            self.total -= last_transaction["price"] * last_transaction["quantity"]
            self.previous_transactions.remove(last_transaction)
        else:
            print("You have no previous transactions")


# james_transactions = CashRegister()
# james_transactions.add_item("Orange", 30, 3)
# james_transactions.add_item("Milk", 65, 2)
# james_transactions.add_item("Rice", 349, 1)
# print(james_transactions._previous_transactions)
# print(james_transactions._items)
# print(james_transactions.discount)
# print(james_transactions.total)
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
