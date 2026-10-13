from components.data_ingestion import load_data
from components.data_validation import dataset_validation
from components.eda import general_eda
from components.data_visualization import create_visual

def main():
    df = load_data()
    dataset_validation(df)
    general_eda(df)
    create_visual(df)

    print(df.head(), '\n', '*' * 70)

if __name__ == '__main__':
    main()