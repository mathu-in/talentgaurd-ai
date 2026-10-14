from components.data_ingestion import load_data
from components.data_validation import dataset_validation
from components.eda import general_eda
from components.data_visualization import create_visual
from components.feature_selection import feature_selection
from components.data_transformation import classify_features

def main():
    df = load_data()
    dataset_validation(df)
    # general_eda(df)
    # create_visual(df)
    X, y = feature_selection(df)
    n , c, t = classify_features(df)

    # print(f"num_features: {n}, cat_features: {c}, target_features: {t}")
    # print("num_features:", n)
    # print("cat_features:", c)
    # print("target_features:", t)
    # print("X-Shape: ", X.shape)
    # print("Y-Shape: ", y.shape)


    # print(df.head(), '\n', '*' * 70)

if __name__ == '__main__':
    main()