
import sys
from dataclasses import dataclass
import os
import pandas as pd
import numpy as np

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
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train and test data successfully')

            logging.info('Obtaining preprocessing object')
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
 
            logging.info("Applying preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr = preprocessing_obj.fit_traansform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object")

            # save_object (file_path = obj = )

            return ( train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file )

        except Exception as e:
            raise Exception(e, sys)

    