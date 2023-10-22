import pandas as pd 
from sklearn.preprocessing import OneHotEncoder
def bin_to_num(data):
    """Splits the column containing multiple values in a string into multiple columns each containing a single value which is float
       Returns:
       A dataframe
    """
    def bin_to_num(data):
        binnedInc = []
        for i in data["binnedInc"]:
        # remove the parentheses and brackets
            i = i.strip("()[]") 
            print(i)
        # split the string into a list after splitting by comma
            i = i.split(",")
            print(i)
        # convert the list to a tuple
            i = tuple(i) 
            print(i)
        # convert individual elements to float
            i = tuple(map(float, i)) 
            print(i)
        # convert the tuple to a list
            i = list(i) 
            print(i)
        # append the list to the binnedinc list
            binnedInc.append(i)
        data["binnedInc"] = binnedInc

    # make a new column lower and upper bound
        data["lower_bound"] = [i[0] for i in data["binnedInc"]]  # lower bound
        data["upper_bound"] = [i[1] for i in data["binnedInc"]]  # upper bound
    # and also median point
        data["median"] = (data["lower_bound"] + data["upper_bound"]) / 2
    # drop the binnedinc column
        data.drop("binnedInc", axis=1, inplace=True)
    return data


def cat_to_col(data):
    """
    Splits the column containing multiple values into multiple columns each containing a single value
    Returns:A DataFrame
    """
    #Feature splitting and reconstruction
    data["county"]=[i.split(',')[0] for i in  data['Geography']]
    data["state"]=[i.split(',')[1] for i in  data['Geography']]
    data.drop('Geography',axis=1,inplace=True)
    return data

def one_hot_encoding(x):
    """
    Returns the data frame after one hot encoding
    """
    #Selecting categorical columns .Categorical columns are those columns which are of type object
    categorical_columns=x.select_dtypes(include=["object"]).columns
    #Instantiating one hot encoder
    one_hot_encoder=OneHotEncoder(sparse=False,handle_unknown="ignore")
    one_hot_encoded=one_hot_encoder.fit_transform(x[categorical_columns])
    #Convert one hot encoded array to a dataframe
    one_hot_encoded=pd.DataFrame(one_hot_encoded,columns=one_hot_encoder.get_feature_names_out(categorical_columns))
    #Drop the categorical_columns
    x=x.drop(categorical_columns,axis=1)
    #Concat the one hot encoded columns
    x=pd.concat([x,one_hot_encoded],axis=1)
    return x

