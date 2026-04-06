"""
Handles all authentication logic. This includes registering a new user with a name and password,
checking the registry for duplicate accounts, generating a random unique account ID, hashing passwords
with SHA-256 via `hashlib`, and verifying credentials on login.

The registry.csv has the following columns:name,account_id,password_hash
"""

import random as r
import pandas as pd
import os

class Authentacion():

    def __init__(self, client_name: str, password: str):
        
        self.client_name = client_name
        self.password = password
        self.registry_file_name = "registry.csv"
        self.folder_path = "./data"
        self.file_path = os.path.join(self.folder_path, self.registry_file_name)

    def create_database(self):

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

    
    def check_database(self):

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
                
        
    def check_registry(self):

        is_created = self.create_database()
        is_empty = self.check_database()

        while (is_created != False and is_empty != False):

            is_created = self.create_database()
            is_empty = self.check_database()

        else:
            print(f"The Registry have been created and is not empty at: {self.file_path}")
            return True

    #TODO: Add hashing for password and also account name creation and backcheck
    #FIXME: Not done yet
    def add_entitity(self):

        df_registry = pd.read_csv(self.file_path)


        new_client = {'name': self.client_name,
                      'account_name': "",
                      'password':""}

if __name__ == '__main__':

    test = Authentacion("test", "test1")
    test.check_registry()


