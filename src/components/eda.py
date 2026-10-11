import pandas as pd

def general_eda(df: pd.DataFrame):
    print('\n'+'='*60)
    print("Exploratory Data Analysis".center(60))
    print('='*60)


    print(f'\nDataset shape: {df.shape}')
    print('\nTarget Variable Distribution')
    print(df['Attrition'].value_counts())
    print('\nNumerical Variable Distribution')
    print(df.describe())

    print('\nDepartment Variable Distribution')
    print(df['Department'].value_counts())

    print(pd.crosstab(df['Attrition'], df['OverTime']))


def main():
    from components.data_ingestion import load_data
    df = load_data()
    general_eda(df)

if __name__ == '__main__':
    main()