
import pandas as pd
import pytest
'''
def get_difference(source,target,file_path):
    diff=pd.concat([source,target]).drop_duplicates(keep=False)
    if not diff.empty:
        diff.to_csv(file_path,index=False)
    return diff

#Test case (test method)
def test_source_Target_data():
    source=pd.read_csv('Source_Employees.csv')
    target=pd.read_csv('Target_Employee.csv')
    file_path='C:/Users/mfaro/Myproject/pythonProject/differences.csv'

    difference=get_difference(source,target,file_path)
    if not difference.empty:
        print("Difference between actual and expected data are saved in 'differences.csv'")
    assert source.equals(target), "Source data and target data doesn't match"

'''
def check_data(df_source, df_target, file_path):
    difference = pd.concat([df_source, df_target]).drop_duplicates(keep=False)
    if not difference.empty:
            difference.to_csv(file_path, index=False)
    return difference

@pytest.fixture()
def source_csv_file():
    return 'Source_Employees.csv'

@pytest.fixture()
def target_csv_file():
    return 'Target_Employee.csv'

def test_source_target_data(source_csv_file,target_csv_file):
    df_source=pd.read_csv(source_csv_file)
    df_target=pd.read_csv(target_csv_file)
    file_path='C:/Users/mfaro/Myproject/pythonProject/differences.csv'

    difference_result=check_data(df_source,df_target,file_path)
    if not difference_result.empty:
        print(f"There are difference in source ana target and saved in to 'data/differences.csv'")
    assert df_source.equals(df_target),"source dataaaa and target doesn't match"


