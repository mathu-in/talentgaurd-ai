import pandas as pd
from components.data_ingestion import load_data

def dataset_validation(dataset: pd.DataFrame):

    print('\n'+'*'*100)
    print("Dataset Overview".center(60))
    print('\n' + '*' * 100)
    print(f'Shape: {dataset.shape}')
    print('\n' + '*' * 100)
    print(f'\nColumns: {dataset.columns.tolist()}')
    print('\n' + '*' * 100)
    print(f'\nNulls: {dataset.isnull().sum()}')
    print('\n' + '*' * 100)
    print(f'\nDuplicates: {dataset.duplicated().sum()}')

def main():
    dataset = load_data()
    dataset_validation(dataset)

if __name__ == '__main__':
    main()