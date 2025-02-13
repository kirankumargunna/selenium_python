import openpyxl

filepath="D:\selenium_python\Python Concepts\Advanced\Data driven testing framework\data\ddt_data.xlsx"
sheetname="Sheet1"

def read_excel(filepath,sheetname):
    workbook=openpyxl.load_workbook(filepath)
    sheet=workbook[sheetname]

    data=[]

    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)

    return data


print(read_excel(filepath,sheetname))