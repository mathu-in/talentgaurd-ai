from data_ingestion import load_data

def main():
    df = load_data()

    print(df.head(), '\n', '*' * 70)
    print(df.shape, '\n', '*' * 70)


if __name__ == '__main__':
    main()