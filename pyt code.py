import json 
import csv  

f = open('D:/android_flut/product.json',"r") 
data = json.load(f)
fields = ["productId","productName","productCost","productBrand","productCategory","productColor","productMaterial","productImage","productAvailability","productLaunchDate","productSummary"]
filename = "product_data2.csv"
with open(filename, 'w',newline="") as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows
    for i in data:
        csvwriter.writerow(i.values())
