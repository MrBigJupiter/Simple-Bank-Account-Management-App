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
from storage import Storage 

class Authentacion(Storage):

    def __init__(self, client_name: str, password: str) -> None:
        """Inherits the Storage methods for dealing with backend work

        Args:
            client_name (str): name of the new entitty into the registry
            password (str): password of the new entity added
        """
        super().__init__(client_name, password)
        
        
    def create_account_id(self) -> str :
        """Created an Account Id and returns it as a String.

        Returns:
            str: Newly Created Account Id
        """
        account_id = str(uuid.uuid4())
                
        return account_id
    
    def hash_password(self, before_hash_password: str) -> str:
        """Hashed the given password and returns it.

        Args:
            before_hash_password (str): Given password for the user not hashed as a string.

        Returns:
            str: String of the hashed password
        """
        hashed_password = hashlib.sha256(before_hash_password.encode()).hexdigest()
        return hashed_password
    
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
        
    def check_client_username(self, name: str) -> bool:
        """Check if a new entry is being made with the same client name.

        Args:
            name (str): name of the client

        Returns:
            bool: True if the new entry does not exist
        """
        df_registry = pd.read_csv(self.registry_file_path)
        res = df_registry.isin([name]).any().any()
        
        in_registry = False

        if res:
            print(f"An entry with the username: {name} has already been added to the registry.")
            in_registry = True
            return in_registry
        else:
            print(f"New entry has been added to the registry with the username: {name}")
            return in_registry
        
    def get_account_id(self, client_name: str, password: str) -> str:
        """Return the account id based on the correct password and client combination. Checks if an account exist with this combination in the registry.

        Args:
            client_name (str): Username of the created client.
            password (str): Not hashed password of the user account

        Returns:
            str: Account id of the user account.
        """
        account_id = None # If the acccount is none existent than we return no accoun id
        hashed_password = self.hash_password(password)
        
        in_registry = self.check_client_username(name= client_name)
        if in_registry:
            df_registry = pd.read_csv(self.registry_file_path)
            account_id = df_registry['account_id'][(df_registry['name'] == client_name) & (df_registry['password_hash'] == hashed_password)]
            print(f"There is a Account id with the given username in the registry.")
            return account_id
        else:   
            print(f"There is no account with this client name and password.")         
            return account_id
        
    def add_entitity(self) -> bool:
        """Add new entitty and create a new account .csv. In encapsulates the back checks too.

        Returns:
            bool: If the new Entity has been added to the Registry and the account has been created.
        """
        df_registry = pd.read_csv(self.registry_file_path)
        username_check = self.check_client_username(name=self.client_name)
        
        if username_check:
            return False
        
        else:
            exists = True
            
            while exists:
                account_id = self.create_account_id()
            
                exists =  df_registry.account_id.isin([account_id]).any()
                
            else:
                
                before_hash_password = self.password
                hashed_password = self.hash_password(before_hash_password= before_hash_password)
                
                
                new_client = {'name': self.client_name,
                            'account_id': account_id,
                            'password_hash':hashed_password}
                
                df_registry.loc[len(df_registry)] = new_client
                
                df_registry.to_csv(self.registry_file_path)
                
                df_account = self.create_account_database(account_id = account_id)
                
            return True

# if __name__ == '__main__':
    
#     new_entity = Authentacion("test2", "test2")
#     new_entity.get_account_id("test2", "test2")

