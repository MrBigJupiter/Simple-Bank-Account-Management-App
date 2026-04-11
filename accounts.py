""" 
`account.py`
Contains the core banking operations. This covers depositing and withdrawing funds (positive and negative
balance updates), changing the account holder's name, and displaying the full transaction history
as a formatted Pandas DataFrame. 

Each transaction is appended as a new row with a recalculated running balance.
"""
from auth import Authentacion

class Account(Authentacion):
    
    def __init__(self, client_name: str, password: str):
        super().__init__(client_name, password)
    
    def update_balance(self, account_id: str):
        pass
    
    def withdraw_balance(self):
        pass
    
    def change_client_name(self):
        pass
    
    def display_transaction_history(self):
        pass
    
    def yearly_line(self):
        pass