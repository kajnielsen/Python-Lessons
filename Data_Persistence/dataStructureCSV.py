import csv



def importCSV():
    list1 = []
    with open('student_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        list1.append(list(csv_reader))
    return list1




print(importCSV())