# Import packages
import numpy as np
import pandas as pd

# Load data
df = pd.read_parquet('data_exjobb_070425.parquet')

# Split into targets and data, and remove undesired features.
dataframe = df.copy()
Targets = pd.DataFrame(dataframe['LogAdjSalePrice202006'])
to_drop = ['TransactionId', 'BaseAreaName', 'DesoArea', 'geometry', 'DistAnyCity', 'DistAnyWater', 'SalePrice', 'LogAdjSalePrice202006', 'LogSalePrice',
            'AdjSalePrice202006']
dataframe = dataframe.drop(to_drop, axis=1)


# Define prepare_data function
def prepare_data(dataframe_original):
    """Takes a dataframe and finds the columns with values that are non-numerical and assigns each unique non-numerical value a numerical value."""
    dataframe = dataframe_original.copy()
    cols = np.shape(dataframe)[1]

    for col in range(cols):
        c = type(dataframe.iloc[0, col]) # Value of the first element in column i row 1

        if c != np.float64 and c != np.int64:
            a = dataframe.iloc[:, col].unique()   # Gives the unique values of a given column
            number_of_unique_values = np.shape(a)[0]
            b = np.linspace(1, number_of_unique_values, number_of_unique_values) / number_of_unique_values

            changed_data = pd.DataFrame(dataframe[f'{dataframe.axes[1][col]}'].copy())

            for j in range(number_of_unique_values):
                if a[j] == None:
                    changed_data = changed_data.replace('None', b[j])
                else:
                    changed_data = changed_data.replace(a[j], b[j], regex=False)
                    
            dataframe[f'{dataframe.axes[1][col]}'] = changed_data
            

    return dataframe.fillna(0) # Returns the changed data with NaN values changed to zero.

# Export
prepared_data = prepare_data(df)
prepared_data.to_parquet('ready_data.parquet')
Targets.to_parquet('ready_targets.parquet')