import sys
import os
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)