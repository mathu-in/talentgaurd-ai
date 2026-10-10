import pandas as pd
from pathlib import Path

def load_data():
    project_root = Path(__file__).resolve().parents[2]
    csv_path = project_root / "Data" / "Raw" / "EmployeeAttrition.csv"
    data = pd.read_csv(csv_path)

    # data = pd.read_csv('../../Data/Raw/EmployeeAttrition.csv')
    return data

if __name__ == '__main__':
    data2 = load_data()
    #---------------------------
    print(data2.head(),'\n','*'*70)
    print(data2.info(),'\n','*'*70)
    print(data2.shape,'\n','*'*70)
    print(data2.columns,'\n','*'*70)