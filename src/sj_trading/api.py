# src/sj_trading/api.py
import shioaji as sj
import os
from dotenv import load_dotenv

load_dotenv()
class loginAPI:
    def __init__(self, simuMode=False):

        self.api = sj.Shioaji(simuMode)
        self.accounts = None
        if simuMode == True:
            print('simuMode')
    def login(self):
        try:

            # self.api = sj.Shioaji(simulation=False)
            self.api.login(
                api_key=os.environ["API_KEY"],
                secret_key=os.environ["SECRET_KEY"],
                fetch_contract=True
            )
            self.accounts = self.api.list_accounts()
            # api.activate_ca(
            #     ca_path=os.environ["CA_CERT_PATH"],
            #     ca_passwd=os.environ["CA_PASSWORD"],
            # )

            print("Successfully Logged in")
            # print(self.accounts)
            return self.api
        except Exception as e:
            print(f"Login Failed: {e}")
            raise
    
    def activateCA(self):
        try:
            self.api.activate_ca(
                    ca_path=os.environ["CA_CERT_PATH"],
                    ca_passwd=os.environ["CA_PASSWORD"],
                )
            print("Successfully Activate")
        except Exception as e:
            print(f"Activate Failed: {e}")
            raise

sj = loginAPI()
sj.login()

    