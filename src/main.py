from pandas.core.interchange import column

from components.data_ingestion import load_data
from components.data_validation import dataset_validation
from components.eda import general_eda
from components.data_visualization import create_visual
from components.feature_selection import feature_selection
from components.data_transformation import classify_features
from components.train_test_split import split_data
from components.preprocessing import preprocess_data
from components.preprocessing import encode_target
from components.model_factory import get_model


def main():
    df = load_data()
    dataset_validation(df)
    # general_eda(df)
    # create_visual(df)
    X, y = feature_selection(df)
    n , c, t = classify_features(df)
    # print("Numerical features:", n)
    # print("Categorical features:", c)
    # print("Target feature:", t)
    # print(f"num_features: {n}, cat_features: {c}, target_features: {t}")
    # print("num_features:", n)
    # print("cat_features:", c)
    # print("target_features:", t)
    # print("X-Shape: ", X.shape)
    # print("Y-Shape: ", y.shape)

    print("before train test split")
    X_train, X_test, y_train, y_test = split_data(X,y)
    print("before preprocessing")
    X_train_preprocessed , X_test_preprocessed , pre_process_nc_data = preprocess_data(X_train,X_test,n,c)
    y_train_preprocessed , y_test_preprocessed = encode_target(y_train,y_test)

    # print("Column names after preprocessing:")
    # print(pre_process_nc_data.get_feature_names_out())

    print(get_model())

    # print("Preprocessing done")
    # print("*"*50)
    # print("X_train after preprocessing:")
    # print(X_train_preprocessed[:5])
    # print("*"*30)
    # print("X_test after preprocessing:")
    # print(X_test_preprocessed[:5])
    # print("*"*30)
    # print("y_train after preprocessing:")
    # print(y_train_preprocessed[:5])
    # print("*"*30)
    # print("y_test after preprocessing:")
    # print(y_test_preprocessed[:5])
    # print("*"*30)

    # print("After preprocessing")
    # print("Shape after preprocessing")
    # print("X_train shape:", X_train_preprocessed.shape)
    # print("X_test shape:", X_test_preprocessed.shape)
    # print("y_train shape:", y_train_preprocessed.shape)
    # print("y_test shape:", y_test_preprocessed.shape)





    # print(df.head(), '\n', '*' * 70)

    # print(X_train)
    # print(y_train)
    # print(X_test)
    # print(y_test)

if __name__ == '__main__':
    main()