#3rd
##this code used to inspect the csv file and check the values of the kids column
# import csv
# file_path =r"C:\Users\akava\Downloads\archive (1)\images.csv"

# with open(file_path,"r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(repr(row["kids"]))
#         break

import csv
file_path =r"C:\Users\akava\Downloads\archive (1)\images.csv"

label_count ={}

with open(file_path,"r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        
        label =row["label"]
        kids =row["kids"]

        if kids =="False":
            if label in label_count:
                label_count[label] +=1
            else:
                label_count[label] =1
print(label_count)