""" 
`account.py`
Contains the core banking operations. This covers depositing and withdrawing funds (positive and negative
balance updates), changing the account holder's name, and displaying the full transaction history
as a formatted Pandas DataFrame. 

Each transaction is appended as a new row with a recalculated running balance.
"""
from auth import Authentacion
import pandas as pd
from datetime import datetime

class Account(Authentacion):
    
    def __init__(self, client_name: str, password: str):
        super().__init__(client_name, password)
        
    def update_balance(self, account_id: str, date: datetime, description: str, amount: int) -> bool:
        
        balance_updated = False
        
        account_file = self.account_file_path_creation(account_id= account_id)
        df_account = pd.read_csv(account_file)
        
        updated_balance = df_account['amount'].sum() + amount
        
        new_row = {
            'date': date,
            'description': description,
            'amount': amount,
            'balance': updated_balance
        }
        
        df_account.loc[len(df_account)] = new_row
                
        df_account.to_csv(account_file)
        balance_updated = True
        
        return balance_updated
    
    def withdraw_balance(self):
        pass
    
    def change_client_name(self):
        pass
    
    def display_transaction_history(self, account_id: str) -> pd.DataFrame:
        """Returns the wole transaction history

        Args:
            account_id (str): Account id for which Transaction history to return

        Returns:
            pd.DataFrame: Dataframe of the transactins
        """
        account_file = self.account_file_path_creation(account_id= account_id)
        df_account = pd.read_csv(account_file)
        
        return df_account
    
    def yearly_line(self):
        pass