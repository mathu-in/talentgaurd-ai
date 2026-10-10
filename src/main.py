from components.data_ingestion import load_data
from components.data_validation import dataset_validation

def main():
    df = load_data()
    dataset_validation(df)

    print(df.head(), '\n', '*' * 70)

if __name__ == '__main__':
    main()