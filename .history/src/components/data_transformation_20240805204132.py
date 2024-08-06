
import sys
from dataclasses import dataclass
import os
import pandas as pd

from src.logger import logging
from src.exception import Exception


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        pass

    def get_data_transformer_object(self):
        try:
           
        except Exception as e:
            raise Exception(e, sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train and test data successfully')

            logging.info('Obtaining preprocessing object')
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            


        except Exception as e:
            raise Exception(e, sys)

    