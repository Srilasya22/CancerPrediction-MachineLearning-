from ingest_data import IngestData
from data_processing import find_constant_columns,find_columns_with_few_values,find_duplicate_rows,drop_and_fill
from feature_engineering import bin_to_num,one_hot_encoding,cat_to_col
ingestdata1=IngestData()
df=ingestdata1.get_data("cancer_reg.csv")

list=find_constant_columns(df)
print("The columns that contain constant values",list)
columns_with_few_values=find_columns_with_few_values(df,10)
columns_with_duplicate=find_duplicate_rows(df)

#df["binnedInc"][0]
df=bin_to_num(df)
df=cat_to_col(df)
df=one_hot_encoding(df)
df.to_csv('data/cancer_processed.csv')
