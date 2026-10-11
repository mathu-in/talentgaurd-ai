from components.data_ingestion import load_data
from components.data_validation import dataset_validation
from components.eda import general_eda

def main():
    df = load_data()
    dataset_validation(df)
    general_eda(df)

    print(df.head(), '\n', '*' * 70)

if __name__ == '__main__':
    main()