#!/usr/bin/env python3

import sys
import re
import os
import argparse

# Exercise Sheet 6

# 1. Bank account

class BankAccount:
    def __init__(self, pin):
        self.pin = pin
        self.balance = 0
        
    def deposit(self, pin, amount):
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        
        self.balance += amount
        return print(self.balance)
    
    def withdraw(self, pin, amount):
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        if self.balance < amount:
            raise ArithmeticError("Insufficient funds")
        
        self.balance -= amount
        return print(amount)
    
    def get_balance(self, pin):
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        
        return print(self.balance)
    
    def change_pin(self, oldpin, newpin):
        if oldpin != self.pin:
            raise ValueError("Incorrect pin")
        
        self.pin = newpin

testAccount = BankAccount("pin")
testAccount.change_pin("pin", "newpin")
testAccount.get_balance("wrongpin")
testAccount.deposit("newpin", 100)
testAccount.get_balance("newpin")
testAccount.withdraw("newpin", 75)
testAccount.get_balance("newpin")
testAccount.withdraw("newpin", 75)
testAccount.get_balance("newpin")

# 2 Special accounts

datetime.datetime("2020-01-01", "%Y-%m-%d")
test = (datetime.now() - datetime.strptime("2019-01-01", "%Y-%m-%d"))
test.days

from datetime import datetime

class SavingsAccount:
    def __init__(self, pin, account_opened):
        self.pin = pin
        self.balance = 0

        self.account_opened = datetime.strptime(account_opened, "%Y-%m-%d")
        self.yearly_interest_rate = 0.05
        self.balance += (self.balance * self.yearly_interest_rate) * ((datetime.now() - self.account_opened).days / 365.25)
        
    def deposit(self, pin, amount):
        if pin != self.pin:
            raise ValueError("Incorrect pin")

        self.balance += amount
        return print(self.balance)
    
    def withdraw(self, pin, amount):
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        if self.balance < amount:
            raise ArithmeticError("Insufficient funds")
        
        self.balance -= amount
        return print(amount)
    
    def get_balance(self, pin):
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        
        return print(self.balance)
    
    def change_pin(self, oldpin, newpin):
        if oldpin != self.pin:
            raise ValueError("Incorrect pin")
        
        self.pin = newpin

class FeeSavingsAccount:
    def __init__(self, pin, account_opened):
        self.pin = pin
        self.balance = 0
        
        self.account_opened = datetime.strptime(account_opened, "%Y-%m-%d")
        self.yearly_interest_rate = 0.05
        self.balance += (self.balance * self.yearly_interest_rate) * ((datetime.now() - self.account_opened).days / 365.25)
        
        self.fee = 0.01

    def deposit(self, pin, amount):
        if pin != self.pin:
            raise ValueError("Incorrect pin")

        self.balance += amount
        return print(self.balance)
    
    def withdraw(self, pin, amount):
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        if self.balance - self.balance * self.fee < amount:
            raise ArithmeticError("Insufficient funds")
        
        self.balance -= self.balance * self.fee
        self.balance -= amount
        return print(amount)
    
    def get_balance(self, pin):
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        
        return print(self.balance)
    
    def change_pin(self, oldpin, newpin):
        if oldpin != self.pin:
            raise ValueError("Incorrect pin")
        
        self.pin = newpin

class ClipList(list):
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def append(self, item):
        item = self.min if item < self.min else self.max if item > self.max else item
        super(ClipList, self).append(item)

    def extend(self, item):
        item = [self.min if x < self.min else self.max if x > self.max else x for x in item]
        super(ClipList, self).extend(item)

    def __setitem__(self, index, item):
        item = self.min if item < self.min else self.max if item > self.max else item
        super(ClipList, self).__setitem__(index, item)

test_list = ClipList(5, 10)
test_list.append(4)
test_list.append(11)
test_list.extend([1, 2, 3, 12, 13, 14])
test_list.__setitem__(0, 100)
test_list