import csv
file = "product_data2.csv"
field = []
row = []

with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    field = next(csvreader)
    for g in csvreader:
        row.append(g)
    print('Industrial')
    print()
    for k in range(0,100):
        if(row[k][4] == 'Industrial'):
            print(row[k])
            print()
    print('Garden')
    print()
    for k in range(0,100):
        if(row[k][4] == 'Garden'):
            print(row[k])
            print()
    print('Movies')
    for k in range(0,100):
        if(row[k][4] == 'Movies'): 
            print(row[k])
            print()
    print('Movies')
    for k in range(0,100):
        if(row[k][4] == 'Electronics'): 
            print(row[k])
            print()
    print('Movies')
    for k in range(0,100):
        if(row[k][4] == 'Clothing'): 
            print(row[k])
            print()
    print('Outdoors')
    for k in range(0,100):
        if(row[k][4] == 'Outdoors'): 
            print(row[k])
            print()
    print('Books')
    for k in range(0,100):
        if(row[k][4] == 'Books'): 
            print(row[k])
            print()
    print('Automotive')
    for k in range(0,100):
        if(row[k][4] == 'Automotive'): 
            print(row[k])
            print()
    print('Baby')
    for k in range(0,100):
        if(row[k][4] == 'Baby'): 
            print(row[k])
            print()
    print('Computers')
    for k in range(0,100):
        if(row[k][4] == 'Computers'): 
            print(row[k])
            print()
    print('Health')
    for k in range(0,100):
        if(row[k][4] == 'Health'): 
            print(row[k])
            print()
    print('Grocery')
    for k in range(0,100):
        if(row[k][4] == 'Grocery'): 
            print(row[k])
            print()
    print('Beauty')
    for k in range(0,100):
        if(row[k][4] == 'Beauty'): 
            print(row[k])
            print()
    print('Toys')
    for k in range(0,100):
        if(row[k][4] == 'Toys'): 
            print(row[k])
            print()
    print('Sports')
    for k in range(0,100):
        if(row[k][4] == 'Sports'): 
            print(row[k])
            print()
    print('Games')
    for k in range(0,100):
        if(row[k][4] == 'Games'): 
            print(row[k])
            print()
    print('Music')
    for k in range(0,100):
        if(row[k][4] == 'Music'): 
            print(row[k])
            print()
    print('Jewelery')
    for k in range(0,100):
        if(row[k][4] == 'Jewelery'): 
            print(row[k])
            print()
    print('Shoes')
    for k in range(0,100):
        if(row[k][4] == 'Shoes'): 
            print(row[k])
            print()
    print('Tools')
    for k in range(0,100):
        if(row[k][4] == 'Tools'): 
            print(row[k])
            print()
    print('Kids')
    for k in range(0,100):
        if(row[k][4] == 'Kids'): 
            print(row[k])
            print()
    print('Home')
    for k in range(0,100):
        if(row[k][4] == 'Home'): 
            print(row[k])
            print()
   
