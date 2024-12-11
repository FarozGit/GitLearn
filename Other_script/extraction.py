import pandas as pd
from sqlalchemy import create_engine
from config import *

# Create mysql engine
mysql_engine = create_engine(f'mysql+pymysql://{user_name}:{password}@{dsn}/{db}')

def extract_csv_file_dataSRC_Load_STG(filename,tablename):
    df = pd.read_csv(filename)
    df.to_sql(tablename,mysql_engine, if_exists='replace', index=False)
    print(f'\tThe {filename} file is loaded into {tablename} table.')

def extract_supplier_dataSRC_Load_STG(filename):
    df = pd.read_json(filename)
    df.to_sql("staging_supplier",mysql_engine,if_exists='replace',index=False)
    print(f'Completed loading {filename} file into staging table...')

def extract_inventory_dataSRC_Load_STG(filename):
    df = pd.read_xml(filename,xpath=".//item")
    df.to_sql("staging_inventory",mysql_engine,if_exists='replace',index=False)
    print(f'Completed loading {filename} file into staging table...')

# We have to pass the csv files and the staging table names in same order in Config.py file
# read from Config.py file
src_files=list(csv_filenames)
stg_tablenames=list(staging_tablenames)

if __name__== '__main__':
    #Read csv files and load to staging
    print('Started loading csv files...')
    if len(src_files) == len(stg_tablenames):
        if not (src_files and stg_tablenames):
            print('No source files or stage tables provided to load data into staging')
        else:
            for f, t in zip(src_files, stg_tablenames):
                # call the function.
                extract_csv_file_dataSRC_Load_STG(f, t)
            print('Completed loading csv files into staging tables...')
    else:
        print('Error:\nProvided No of Source files and stage tables are not equal in config.py file...\n...Correct it them in config.py file and rerun the job !!!')

    extract_supplier_dataSRC_Load_STG("src_data/supplier_data.json")
    extract_inventory_dataSRC_Load_STG("src_data/inventory_data.xml")