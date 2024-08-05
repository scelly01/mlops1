from src.logger import logging
from src.exception import CustomException

import os
import sys
from dataclasses import dataclass
import pandas as pd


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
            df = pd.read_csv('notebooks/data/student.csv')
            logging.info('Read the dataset into a df')

            os.makedirs()


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == '__main__':
    diobj = DataIngestion()
    train_data, test_data = diobj.initiate_data_ingestion()