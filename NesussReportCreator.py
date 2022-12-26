import pandas as pd
import openpyxl

path1 = str(input('Please enter the anem of the Nessus generated report along with FUll Path: '))
data1 = open(path1)
path = str(input('Please enter the destination filename with full path: '))
data = pd.read_csv(data1)

sheetNames = ['Critical Observations', 'High Observations', 'Medium Observations', 'Low Observations']
Risk = ['Critical',  'High', 'Medium', 'Low']
def goku(sheetNames):
    data2 = data[data['Risk'] == Risk]
    df = pd.DataFrame(data2, columns=['Risk', 'Name', 'Host', 'Port', 'CVE', 'Description', 'Synopsis', 'Solution'] )
    df.columns = ['Risk', 'Name', 'Host', 'Port', 'CVE', 'Description', 'Impact', 'Remediation']
    df = df.groupby(["Name", "Risk"]).agg(set)
    with pd.ExcelWriter(path, engine="openpyxl", mode='a', if_sheet_exists=('overlay')) as writer:
        writer.book = openpyxl.load_workbook(path)
        df.to_excel(writer, sheet_name=sheetNames, index=True)
    print(df)
i = 0
for Risk in Risk:
    goku(sheetNames[i])
    i = i+1
