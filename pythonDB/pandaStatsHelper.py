################################
## Tool to analyze data sets. ## 
################################

import pandas as pd

def main(file):
    'tool to analyze data sets'
    # assign dataset
    df = pd.read_csv(file)
    columns = list(df.columns)
    # shape
    print("\n\n\n***************SHAPE***************")
    print(f"{df.shape[0]} Rows")
    print(f"{df.shape[1]} Columns")
    # data types
    print("\n\n\n***************DATA TYPES***************")
    print(df.info())
    # columns
    print("\n\n\n***************COLUMNS***************")
    print("List of columns: ",columns,"\n")
    for i,j in enumerate(columns,start=1):
        print(f"\t\tColumn#{i} --> {j} \n\n")
    # describe
    print("***************DESCRIBE***************")
    print(df.describe().to_string())
    # head
    print("\n\n\n***************HEAD***************")
    print(df.head(30).to_string())
    # tail
    print("\n\n\n***************TAIL***************")
    print(df.tail(30).to_string(),'\n\n\n')
    return df



if '__name__'=='__main__':
    main(input("Enter filepath for dataset: ")) 
