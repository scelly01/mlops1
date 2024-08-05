from src.logger import logging
from src.exception import CustomException

import os
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str =  os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data ingestion initiated')
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)

