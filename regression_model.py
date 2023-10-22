import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import statsmodels.api as sm
from data_processing import split_data
from sklearn.metrics import mean_absolute_error, r2_score

def correlation_among_numeric_features(df,cols):
    """Finds the correlation features between among different columns"""
    numeric_col=df[cols]
    corr=numeric_col.corr() #It generates correlation matrix
    corr_features=set()
    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i,j])>0.8:
                colname=corr.columns[i]#Adding the name of column from correlation matrix
                corr_features.add(colname)
    print(corr_features)

def lr_model(x_train,y_train):
    """
    Fitting the model
    Returns the model after fitting
    """
    x_train_with_intercept=sm.add_constant(x_train)
    lr=sm.OLS(y_train,x_train_with_intercept).fit()
    return lr

def identify_significant_vars(lr, p_value_threshold=0.05):
    # print(lr.pvalues)
    # print(lr.rsquared)
    # # print the adjusted r-squared value for the model
    # print(lr.rsquared_adj)
    # identify the significant variables
    significant_vars = [var for var in lr.pvalues.keys() if lr.pvalues[var] < p_value_threshold]
    return significant_vars


if __name__=='__main__':
    capped_data=pd.read_csv('capped_data.csv')
    print(capped_data.shape)
    corr_features=correlation_among_numeric_features(capped_data,capped_data.columns)
    high_corr_columns=['MedianAgeMale', 'PctBlack', 'PctPublicCoverageAlone', 'PctEmpPrivCoverage', 'PctPrivateCoverage', 'MedianAgeFemale', 'povertyPercent', 'PctPublicCoverage', 'PctMarriedHouseholds', 'popEst2015', 'state_ District of Columbia', 'PctPrivateCoverageAlone']
    cols=[col for col in capped_data.columns if col not in high_corr_columns] #Remove the features which are correlated
    x_train,x_test,y_train,y_test=split_data(capped_data[cols],"TARGET_deathRate")
    lr=lr_model(x_train,y_train)
    # print(lr.summary())
    significant_vars = identify_significant_vars(lr)#Identify significant variables
    print(len(significant_vars))
    significant_vars.remove("const")
    lr = lr_model(x_train[significant_vars], y_train)
    summary = lr.summary()
    print(summary)
    # y_pred = lr.predict(sm.add_constant(x_test[significant_vars]))
    # mae = mean_absolute_error(y_test, y_pred)
    # r_squared = r2_score(y_test, y_pred)
    # print(f"Mean Absolute Error (MAE): {mae:.2f}")
    # print(f"R-squared (R²): {r_squared:.2f}")