import csv


# Macの場合は以下の通り
with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
# Windowsの場合は改行コードが \r\n となってcsv読み込みの際に2行改行されてしまう
# Windowsの場合は以下のようにする
# with open('test.csv','w',newline='') as csv_file: