"""
Handles all authentication logic. This includes registering a new user with a name and password,
checking the registry for duplicate accounts, generating a random unique account ID, hashing passwords
with SHA-256 via `hashlib`, and verifying credentials on login.

The registry.csv has the following columns:name,account_id,password_hash
"""

import uuid
import pandas as pd
import os
import hashlib

class Authentacion():

    def __init__(self, client_name: str, password: str):
        
        self.client_name = client_name
        self.password = password
        self.registry_file_name = "registry.csv"
        self.folder_path = "./data"
        self.file_path = os.path.join(self.folder_path, self.registry_file_name)

    def create_database(self) -> bool:
        """Create the Registry database if it does not exsist. If it exists returns True with a message.

        Returns:
            bool: If the registry exists or if it has been created
        """
        is_created = False

        if os.path.exists(self.file_path):
            print(f"The file: {self.registry_file_name} exists at: {self.file_path}")
            
            return is_created # If already exists than False
        else:
            with open(self.file_path, "x") as registry:
                print(f"The file: {self.registry_file_name} do not exists.\n Initializing the Registry database at: {self.file_path}")
                print(f"The file: {self.registry_file_name} has been created at: {self.file_path}.")
                is_created = True # If did not exist than True
                return is_created

    
    def check_database(self) -> bool:
        """Check if the Registry is completaly empty. If it is empty populates it with the columns stated in the README.md

        Returns:
            bool: Returns True if it either empyt and has been added columns or it is not empty and has columns
        """
        is_empty = False

        try:
            df_registry = pd.read_csv(self.file_path)
            if df_registry.empty:
                print(f"The registry file exist and is empty.\n")
                return is_empty # If columns already exists than False
            else:
                print(f"The registry file exist and is not empty.\n")
                return is_empty # If columns already exists than False

        except:
            
            column_names = ['name', 'account_id', 'password_hash']
            df = pd.DataFrame(columns=column_names)
            print(f"The registry file exist but has no structure.\n Initializing database columns at: {self.file_path}")

            df.to_csv(self.file_path)

            print(f"The Registry database columns has been initalized in: {self.file_path}")
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
            print(f"The Registry have been created and is not empty at: {self.file_path}")
            return True
        
    def create_account_id(self) -> str :
        """Created an Account Id and returns it as a String.

        Returns:
            str: Newly Created Account Id
        """
        account_id = str(uuid.uuid4())
                
        return account_id
    
    def create_account_database(self, account_id : str) -> bool:
        """Create the Account of the new Registry entry (new client).

        Args:
            account_id (str): Created account Id for the New Registry entry.

        Returns:
            bool: Account with the Account ID has been created at the ./data/accounts
        """
        account_file_path = "./data/accounts"
        file_name = account_id + ".csv"
        create_account = os.path.join(account_file_path, file_name)
        
        account_columns = ['date', 'description', 'amount', 'balance']
        
        df_new_account = pd.DataFrame(columns=account_columns)
        
        df_new_account.to_csv(create_account)
        
        print(f"Account with Id: {account_id} has been created at: {create_account}")
        
        return True
        
    def add_entitity(self) -> bool:
        """Add new entitty and create a new account .csv. In encapsulates the back checks too.

        Returns:
            bool: If the new Entity has been added to the Registry and the account has been created.
        """
        df_registry = pd.read_csv(self.file_path)
        
        exists = True
        
        while exists:
            account_id = self.create_account_id()
        
            exists =  df_registry.account_id.isin([account_id]).any()
            
        else:
            
            before_hash_password = self.password
            hashed_password = hashlib.sha256(before_hash_password.encode()).hexdigest()
            
            
            new_client = {'name': self.client_name,
                        'account_id': account_id,
                        'password_hash':hashed_password}
            
            df_registry.loc[len(df_registry)] = new_client
            
            df_registry.to_csv(self.file_path)
            
            df_account = self.create_account_database(account_id = account_id)
            
        return True

#if __name__ == '__main__':

 #   new_entity = Authentacion("test", "test1")
 #   new_entity.check_registry()
 #   new_entity.add_entitity()

