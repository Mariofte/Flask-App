import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)
import os
import json
import pandas as pd
import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac
from logs import Logger

class Sheet:
    def __init__(self, id:str):
        self.id = id
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.logger = Logger('Sheet').get_logger()
        
        try:
            with open(os.path.join(self.path, 'format.json')) as f:
                self.format = json.load(f)
        
        except (json.JSONDecodeError, Exception) as e:
            self.logger.error(f'Hubo un error en el formato: {e}')
    
        try:
            self.creds = sac.from_json_keyfile_name(
                filename=os.path.join(self.path, 'token.json'),
                scopes=[
                    'https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive'
                ]
            )
            self.auth = gs.authorize(self.creds)

        except (json.JSONDecodeError, gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error en el token: {e}')

    def work(self, sheet:int):
        self.logger.info('Buscando hoja')
        try:
            return self.auth.open_by_key(self.id).get_worksheet(sheet)
        
        except (gs.exceptions.APIError, gs.exceptions.SpreadsheetNotFound, Exception) as e:
             self.logger.error(f'Hubo un error en la hoja: {e}')
             return None
    
    def post(self, data:list, sheet:int, row:int):
        try:
            work = self.work(sheet)
            work.insert_rows(data, row)
            work.format("1:1000", self.format)
            self.logger.info('Se formatearon y mandaron lo datos')
        
        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')
    
    def get(self, sheet:int):
        self.logger.info('Se obtuvieron los datos')
        try:
            return pd.DataFrame(self.work(sheet).get_all_records())
        
        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')

    def delete(self, sheet:int, start:int, end:int):
        self.logger.info('Se borro la fila de datos')
        try:
            self.work(sheet).delete_rows(start, end)

        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')

    def clear(self, sheet:int):
        self.logger.info('Se limpio la hoja')
        try:
            self.work(sheet).clear()

        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')