import os
from flask import Flask, render_template, redirect, url_for, request
from logs import Logger
from service import Sheet

class Web(Flask):
    def __init__(self, name, static_folder: str | None = None, template_folder: str | None = None):
        super().__init__(name, static_folder=static_folder, template_folder=template_folder)
        
        self.logger = Logger('Web').get_logger()
        self.logger.info('Server iniziado')
        self.path =  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs', 'Web.log'))
        
        self.api = Sheet('1-w-sizFV2i0BTeEd-PzQ9oQojd3A2Y_pvm2XJ4e35z8')
                
        self.add_url_rule('/', endpoint='index', view_func=self.index)
        self.add_url_rule('/App/match', endpoint='match', view_func=self.match, methods=['GET','POST'])
        self.add_url_rule('/App/pits', endpoint='pits', view_func=self.pits, methods=['GET','POST'])
        self.add_url_rule('/view', endpoint='view', view_func=self.logs, methods=['GET'])

    def index(self):
        self.logger.info('Se entro a index')    
        try:
            return render_template('index.html')
        except Exception as e:
            self.logger.error(f'Hubo un error: {e}')
    
    def match(self):
        self.logger.info('Se entro a match')
        try:
            if request.method == 'POST':
                DATA = request.form.getlist('data[]')
                self.api.post([DATA], 0, 2)
                return redirect(url_for('match'))
            return render_template('match.html')
        except Exception as e:
            self.logger.error(f'Hubo un error: {e}')
    
    def pits(self):
        self.logger.info('Se entro a pits')
        try:
            if request.method == 'POST':
                DATA = request.form.getlist('data[]')
                self.api.post([DATA], 1, 2)
                return redirect(url_for('pits'))
            return render_template('pits.html')
        except Exception as e:
            self.logger.error(f'Hubo un error: {e}')
            
    def logs(self):
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as f:
                data = ''.join(f.readlines())
            return render_template('view.html', data=data)
        else:
            self.logger.error('No existe el archivo')