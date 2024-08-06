from src.logger import logging
from src.exception import CustomException
from src.components.model_trainer import ModelTrainer

import os
import sys
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

from src.components.data_transformation import DataTransformation

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

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Ingested the raw df into raw_data_path')

            logging.info('Train Test split initaited')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Ingested train and test data succesfuly')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == '__main__':
    diobj = DataIngestion()
    train_data, test_data = diobj.initiate_data_ingestion()

    dtobj = DataTransformation()
    train_arr, test_arr, _ = dtobj.initiate_data_transformation(train_data,test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))