import csv
import random

writeData = []
average = 16.33
keep  = random.sample(range(1,54807), 500)
n = random.randint(1990,2013)
count = 0
total = 0
avg = 0.0

with open('dataforrandom.csv', 'r') as f:
    data = csv.reader(f)
    for i, line in enumerate(data):
        if i == 0: continue
        if int(line[12]) == 2013: #change the number of the year based on what random number generator generates
            writeData.append(line)
            total += int(line[21])
            count += 1


avg = float(total)/float(count)
print avg

with open('2013.csv', 'w') as g:
    writer = csv.writer(g)
    writer.writerow(["Loan ID", "BorrCity", "BorrState", "BorrZip", "CDC_City",
    "CDC_State", "CDC_Zip", "ThirdPartyLender_City", "ThirdPartyLender_State",
    "ThirdPartyDollars", "GrossApproval", "ApprovalDate", "ApprovalFiscalYear",
    "DeliveryMethod", "InitialInterestRate", "Missing Rate?", "TermInMonths", "NaicsCode",
    "ProjectCounty", "ProjectState", "BusinessType", "LoanStatus", "ChargeOffDate", "GrossChargeOffAmount", "BorrRegion",
    "NaicsTrimmed", "Cont_ApprovalDate", "TotalLoanAmount", "LossRatio", "LoanAge", "BorrSameCDC", "ProjectSameBorr"])
    for wd in writeData:
        writer.writerow(wd);
