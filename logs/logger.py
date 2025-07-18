import os
import logging as log

class Logger:
    def __init__(self, name:str = 'App', level=log.DEBUG):
        archive = 'Web.log'
        self.logger = log.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            formatter = log.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            console = log.StreamHandler()
            console.setLevel(level)
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            
            if archive:
                ruta_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), archive) 
                file = log.FileHandler(ruta_log, encoding='utf-8')
                file.setLevel(level)
                file.setFormatter(formatter)
                self.logger.addHandler(file)
    
    def get_logger(self):
        return self.logger