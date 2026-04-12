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
        """Inherits the functions from Authentication class

        Args:
            client_name (str): Name of the client
            password (str): Password to back check information
        """
        super().__init__(client_name, password)
        
    def update_balance(self, account_id: str, description: str, amount: int) -> bool:
        """Function for handling money update tasks. 

        Args:
            account_id (str): Id of the account 
            description (str): Description for the action
            amount (int): Amount that is being updated

        Returns:
            bool: Returns true if the balance has been updated
        """
        
        balance_updated = False
        
        account_file = self.account_file_path_creation(account_id= account_id)
        df_account = pd.read_csv(account_file)
        
        updated_balance = df_account['amount'].sum() + amount
        
        new_row = {
            'date': datetime.now(),
            'description': description,
            'amount': amount,
            'balance': updated_balance
        }
        
        df_account.loc[len(df_account)] = new_row
                
        df_account.to_csv(account_file)
        balance_updated = True
        
        return balance_updated
    
    def withdraw_balance(self, account_id: str, description: str, amount: int) -> bool:
        """Function for handling money withdrawel tasks. 

        Args:
            account_id (str): Id of the account 
            description (str): Description for the action
            amount (int): Amount that is being updated

        Returns:
            bool: Returns true if the balance has been updated
        """
        
        balance_updated = False
        
        account_file = self.account_file_path_creation(account_id= account_id)
        df_account = pd.read_csv(account_file)
        
        updated_balance = df_account['amount'].sum() + amount
        
        new_row = {
            'date': datetime.now(),
            'description': description,
            'amount': amount,
            'balance': updated_balance
        }
        
        df_account.loc[len(df_account)] = new_row
                
        df_account.to_csv(account_file)
        balance_updated = True
        
        return balance_updated
    
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
        
        print(df_account)
        return df_account
    
    def yearly_line(self):
        pass
    
    
# if __name__ == '__main__':
    
    # test = Account("test2", "test2")
    # test.update_balance(
    #     account_id="cca75f9d-a609-45e3-a474-a527f345f4f0",
    #     description="test update for test2 user - numb1",
    #     amount= 120
    # )
    
    # test.update_balance(
    #     account_id="cca75f9d-a609-45e3-a474-a527f345f4f0",
    #     description="test update for test2 user - numb2",
    #     amount= 120
    # )
        
    # test.withdraw_balance(
    #     account_id="cca75f9d-a609-45e3-a474-a527f345f4f0",
    #     description="test update for test2 user - numb5",
    #     amount= -250
    # )
    
    # test.display_transaction_history(account_id="cca75f9d-a609-45e3-a474-a527f345f4f0")
