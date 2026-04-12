"""
`storage.py`
A helper module responsible for all CSV read and write operations. Keeps file I/O logic in one place
so the other modules stay clean. Manages both the shared `registry.csv` and the individual
per-account CSV files stored under `data/accounts/`.
"""

import os
import pandas as pd
      
class Storage():
    
    def __init__(self, client_name: str, password: str):
        
        self.client_name = client_name
        self.password = password
        self.registry_file_name = "registry.csv"
        self.folder_path = "./data"
        self.registry_file_path = os.path.join(self.folder_path, self.registry_file_name)   
    
    def create_database(self) -> bool:
        """Create the Registry database if it does not exsist. If it exists returns True with a message.

        Returns:
            bool: If the registry exists or if it has been created
        """
        is_created = False

        if os.path.exists(self.registry_file_path):
            print(f"The file: {self.registry_file_name} exists at: {self.registry_file_path}")
            
            return is_created # If already exists than False
        else:
            with open(self.registry_file_path, "x") as registry:
                print(f"The file: {self.registry_file_name} do not exists.\n Initializing the Registry database at: {self.registry_file_path}")
                print(f"The file: {self.registry_file_name} has been created at: {self.registry_file_path}.")
                is_created = True # If did not exist than True
                return is_created
            
    def check_database(self) -> bool:
        """Check if the Registry is completaly empty. If it is empty populates it with the columns stated in the README.md

        Returns:
            bool: Returns True if it either empyt and has been added columns or it is not empty and has columns
        """
        is_empty = False

        try:
            df_registry = pd.read_csv(self.registry_file_path)
            if df_registry.empty:
                print(f"The registry file exist and is empty.\n")
                return is_empty # If columns already exists than False
            else:
                print(f"The registry file exist and is not empty.\n")
                return is_empty # If columns already exists than False

        except:
            
            column_names = ['name', 'account_id', 'password_hash']
            df = pd.DataFrame(columns=column_names)
            print(f"The registry file exist but has no structure.\n Initializing database columns at: {self.registry_file_path}")

            df.to_csv(self.registry_file_path)

            print(f"The Registry database columns has been initalized in: {self.registry_file_path}")
            is_empty = True
            return is_empty # If columns have been created than True
                
        
    def check_registry(self) -> bool:
        """Main function for the registry backcheck and column creation.

        Returns:
            bool: If it has been created or it it already there and has columns
        """
        is_created = self.create_database()
        is_empty = self.check_database()

        while (is_created != False and is_empty != False):

            is_created = self.create_database()
            is_empty = self.check_database()

        else:
            print(f"The Registry have been created and is not empty at: {self.registry_file_path}")
            return True
        
    def account_file_path_creation(self, account_id: str) -> str:
        """Return the full file path of the Account database

        Args:
            account_id (str): Account Id as a string

        Returns:
            str: File path to the account database of the user.
        """
        
        account_folder_path = "./data/accounts"
        account_id_file = f"{account_id}.csv"
        account_file_path = self.registry_file_path = os.path.join(account_folder_path, account_id_file)
        
        return account_file_path
