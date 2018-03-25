import csv

writeData = []
totalValue = 0
numEntry = 0

with open('loan_data_modified.csv', 'r') as f:
    data = csv.reader(f)
    for i, line in enumerate(data):
        if i == 0: continue
        d = line[14]
        if len(d) == 2:
            writeData.append([0, 1])
        else:
            totalValue += float(d)
            numEntry += 1
            writeData.append([float(d), 0])

averageValue = float(totalValue)/numEntry

for d in writeData:
    if d[1] == 1:
        d[0] = averageValue

with open('new_SBA_load_data.csv', 'w') as g:
    writer = csv.writer(g)
    writer.writerow(["initial interest rate", "missing data"])
    for wd in writeData:
        writer.writerow(wd);
