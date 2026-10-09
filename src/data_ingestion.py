import pandas as pd

def load_data():
    data = pd.read_csv('../Data/Raw/EmployeeAttrition.csv')
    return data

if __name__ == '__main__':
    data2 = load_data()
    #---------------------------
    print(data.head(),'\n','*'*70)
    print(data.info(),'\n','*'*70)
    print(data.shape,'\n','*'*70)
    print(data.columns,'\n','*'*70)