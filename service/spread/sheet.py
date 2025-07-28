import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)
import os
import json
import pandas as pd
import gspread as gs
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials as sac
from gspread import auth
from logs import Logger

class Sheet:
    def __init__(self, id:str):
        self.id = id
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.logger = Logger('Sheet').get_logger()
        
        
        
        try:
            self.logger.info('Se esta cargando el formato')
            with open(os.path.join(self.path, 'format.json')) as f:
                self.format = json.load(f)
            self.logger.info('Se cargo el formato')
        
        except (json.JSONDecodeError, Exception) as e:
            self.logger.error(f'Hubo un error en el formato: {e}')
    
        try:
            self.logger.info('Se estan cargando las credensiales y atenticando')
            self.creds = sac.from_json_keyfile_name(
                filename=os.path.join(self.path, 'token.json'),
                scopes=[
                    'https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive'
                ]
            )
            self.auth = gs.authorize(self.creds)
            self.logger.info('se terminaron de cargar y autenticar')

        except (json.JSONDecodeError, gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error en el token: {e}')
            
    def post(self, data:list, sheet:int, row:int):
        try:
            self.logger.info('Buscando hoja')
            work = self.auth.open_by_key(self.id).get_worksheet(sheet)
            
            if work is None:
                self.logger.error('Hubo un error con los datos')
                return
            else:
                work.insert_rows(data, row)
                work.format('2:2', self.format)
                self.logger.info('Se formatearon y mandaron lo datos')
        
        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error en POST: {e}')
    
    def get(self, sheet:int):
        try:
            self.logger.info('Buscando hoja')
            work = self.auth.open_by_key(self.id).get_worksheet(sheet)
            
            if work is None:
                self.logger.error('Hubo un error con los datos') 
                return
            else:
                self.logger.info('Se obtuvieron los datos')
                return pd.DataFrame(work.get_all_records())

        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')
    
    def gat_array(self, sheet:int):
        try:
            self.logger.info('Buscando hoja')
            work = self.auth.open_by_key(self.id).get_worksheet(sheet)
            
            if work is None:
                self.logger.error('Hubo un error con los datos')
                return
            else:
                self.logger.info('Se obtuvieron los datos')
                return np.array(work.get_all_records())
        
        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')   

    def delete(self, sheet:int, start:int, end:int):
        try:
            self.logger.info('Buscando hoja')
            work = self.auth.open_by_key(self.id).get_worksheet(sheet)
            
            if work is None:
                self.logger.error('Hubo un error con los datos')
                return
            else:
                work.delete_rows(start, end)
                self.logger.info('Se borro')

        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')

    def clear(self, sheet:int):
        self.logger.info('Se limpio la hoja')
        try:
            self.logger.info('Buscando hoja')
            work = self.auth.open_by_key(self.id).get_worksheet(sheet)
            
            if work is None:
                self.logger.error('Hubo un error con los datos')
                return
            else:
                work.clear()
                self.logger.info('Se limpio la hoja ')

        except (gs.exceptions.APIError, Exception) as e:
             self.logger.error(f'Hubo un error: {e}')