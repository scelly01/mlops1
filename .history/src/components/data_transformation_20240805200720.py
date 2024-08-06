
import sys
from dataclasses import dataclass
import os

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
            pass
        except Exception as e:
            raise Exception(e, sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        try:
            pass
        except Exception as e:
            raise Exception(e, sys)

    