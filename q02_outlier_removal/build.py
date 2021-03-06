# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
def outlier_removal(dataset):
    for col in dataset.columns:
        upper = dataset[col].quantile(q=0.975)
        dataset = dataset.loc[(dataset[col] < upper)]
        return dataset
