import sys
import pandas as pd
from src.exception import CustomException
from src.utilis import load_object


class PredictPipeline:
    def __init__(self,
        gender: str, 
        parental_level_of_education: str,
        race_ethnicity: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

         # Initialize instance variables
        self.gender = gender
        self.parental_level_of_education = parental_level_of_education
        self.race_ethnicity = race_ethnicity
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dcit = {
                "gender":[self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]}
            
            return pd.DataFrame(custom_data_input_dcit)

             

        except Exception as e:
            raise CustomException(e,sys)


    