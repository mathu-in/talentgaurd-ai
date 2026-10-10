from data_ingestion import load_data
from data_validation import dataset_validation

def main():
    df = load_data()
    dataset_validation(df)

if __name__ == '__main__':
    main()