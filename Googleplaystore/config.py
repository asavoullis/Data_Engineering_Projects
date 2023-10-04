# config.py

import configparser

class Config:
    def __init__(self, config_file_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

    def get_flask_config(self):
        return self.config['Flask']

    def get_data_processing_config(self):
        return self.config['DataProcessing']
