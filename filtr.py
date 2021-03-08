import csv
file = "product_data2.csv"
field = []
row = []
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    field = next(csvreader)
    for a in csvreader:
        if(a[4] not in row):
            row.append(a[4])
            print(a[4])
