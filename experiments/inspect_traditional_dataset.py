##2nd
import json
file_path =r"C:\Users\akava\Downloads\indo-fashion\train_data.json"

class_counts ={}

with open(file_path,"r") as file:
    for line in file:
        if line.strip():
            data =json.loads(line)

            label =data["class_label"]

            if label in class_counts:
                class_counts[label] +=1
            else:
                class_counts[label] =1
print(class_counts)