import pandas as pd
from sklearn.model_selection import train_test_split as tts
def find_constant_columns(dataframe):
    """
    This function takes data frame as input and returns the list of unique columns i.e the columns with 1 value
    Parameter:
    The dataframe has to be analyzed
    Returns:
    the list of columns which contain unique values
    """
    list=[]
    for column in dataframe.columns:
        #Gets the unique values in the column
        unique_value=dataframe[column].unique()
        if len(unique_value)==1:
            list.append(column) 
    return list

def delete_constant_columns(dataframe,columns_to_delete):
    """
    Returns the data frame after deleting the columns with one value
    """
    dataframe.drop(columns_to_delete,axis=1)
    return dataframe

def find_columns_with_few_values(dataframe,threshold):
    """
    Returns a list of columns with unique values less than threshold
    """
    list=[]
    for column in dataframe.columns:
        unique_value=dataframe[column].unique()
        if len(unique_value)<threshold: 
            list.append(column)
    return list 

def find_duplicate_rows(dataframe):
    """Returns the duplicate rows"""
    duplicate_rows=dataframe[dataframe.duplicated()]
    return duplicate_rows

def delete_duplicate_rows(dataframe):
    """This function takes dataframe as input and returns the dataframe without duplicate rows"""
    #Drop the duplicate rows by keeping the first
    dataframe=dataframe.drop_duplicates(keep="first")
    return dataframe

def drop_and_fill(dataframe):
    #Get the colums with more than 50% null values
    cols_to_drop=dataframe.columns[dataframe.isnull().mean()>0.5]
    #Drop the columns
    dataframe=dataframe.drop(cols_to_drop,axis=1)
    dataframe=dataframe.fillna(dataframe.mean())
    return dataframe 
def split_data(dataframe, target_column):
    """
    This function takes in a dataframe and a target column as input and splits the dataframe into a feature dataframe and a target dataframe.

    Parameters:
    dataframe (pandas.DataFrame): The dataframe to be analyzed
    target_column (str): The name of the target column

    Returns:
    pandas.DataFrame: The dataframe containing the features
    pandas.DataFrame: The dataframe containing the target column
    """
    # Split the dataframe into a feature dataframe and a target dataframe
    X = dataframe.drop(target_column, axis=1)
    y = dataframe[target_column]
    X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=0)
    return (X_train, X_test, y_train, y_test)
