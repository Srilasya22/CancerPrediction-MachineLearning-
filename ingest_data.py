import pandas as pd
class IngestData:
    def __init__(self)->None:
        """
          Constructor
        """
        self.data_path=None
    def get_data(self,data_path:str)->pd.DataFrame:
        '''
        This function takes a path of csv file and converts into a dataframe 
        Returns a dataframe
        '''
        self.data_path=data_path
        df=pd.read_csv(self.data_path, encoding='unicode_escape')
        return df
    