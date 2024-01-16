import pickle
import sys
import os
import numpy as np
import pandas as pd
sys.path.append("C:/Users/nehagour/ml_project")
from src.exception import CustomException
from src.logger import logging
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)