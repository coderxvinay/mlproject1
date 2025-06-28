##Reading a data from a specific database is called data ingestion:-All the code regarding data ingestion is done in this py file.
##Convert jupyter notebook file into model coding, CI CD pipeline, so once it goes into production, it should be continously running.
import os 
import sys 
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig
# from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

##When performing data ingestion component, there are some imputs required by this data ingestion component.
##input can be where do we save the training path, test path 

'''Inside a class, to define a class variable you use __init__ but if you try to use this dataclass, 
you will directly be able to define class variable'''
@dataclass
class DataIngestionConfig:  ##Class for creating input(ie path where files will be saced) for data ingestion component, 
    train_data_path: str=os.path.join("artifacts","train.csv") 
    ##giving a path where train_data(output for data ingestion) will be saved ie (artifacts folder with file name train_data)
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")


##if you are only defining variable then use can use dataclass, but if you have other functions inside class go ahead with init constructior
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  ##ingestion_config will consist of three values mentioned in class above
#As soon as this get executed when i call DataIngestionConfig class, the three paths will get saved inside this class variable(ingestion_config)
##ie inside the variable ingestion_config we will have 3 sub variables or sub objects.

    def initiate_data_ingestion(self):  ##reads data stored in a database
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            ##create the folder arttifacts wrt train data path, test data path 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #getting the directory name wrt specific path....
            ##exist_ok = True, if it's already there we will keep it and don't have to dlt it to create new

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)  ##saving raw data to the path

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)  ##saving train data to the path, after train test split

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            ''' DataIngestion class returns path of train data and test data'''
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj= DataIngestion
    obj.initiate_data_ingestion()

# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.initiate_data_ingestion()

#     data_transformation=DataTransformation()
#     train_array, test_array = data_transformation.initiate_data_transformation(train_data,test_data)

#     ModelTrainer = ModelTrainer()
#     print(ModelTrainer.initiate_model_trainer(train_array,test_array))


