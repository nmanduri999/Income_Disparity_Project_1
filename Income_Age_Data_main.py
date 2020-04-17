import os, csv

# budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
input_file  = "/Users/volfgangsu/Desktop/Income_Age_Data.csv"

with open(input_file,newline="", encoding="utf-8") as Data:

    csvreader = csv.reader(Data, delimiter="/")

    header = next(csvreader)

print(Data)