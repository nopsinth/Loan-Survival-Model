import csv

sp = {}
writeData = []
spdata = []
time = []
dummy = 0

with open('SP500Year.csv', 'r') as f:
    data = csv.reader(f)
    for i, line in enumerate(data):
        if i == 0: continue
        sp[i]= line[2]

with open('test_outsample2.csv', 'r') as g:
    dataTwo = csv.reader(g)
    for i, line in enumerate(dataTwo):
        if i == 0: continue
        d = line[11]
        time = int(d.split('/')[2])-1990 #match time with data in dictionary
        dummy = time + int(line[32]) + 1 #match year
        writeData.append(line + [sp[dummy]])

with open('test_outsample3.csv', 'w') as h:
    writer = csv.writer(h)
    writer.writerow(["Loan ID", "BorrCity", "BorrState", "BorrZip", "CDC_City",
    "CDC_State", "CDC_Zip", "ThirdPartyLender_City", "ThirdPartyLender_State",
    "ThirdPartyDollars", "GrossApproval", "ApprovalDate", "ApprovalFiscalYear",
    "DeliveryMethod", "InitialInterestRate", "Missing Rate?", "TermInMonths", "NaicsCode",
    "ProjectCounty", "ProjectState", "BusinessType", "LoanStatus", "ChargeOffDate", "GrossChargeOffAmount", "BorrRegion",
    "NaicsTrimmed", "Cont_ApprovalDate", "TotalLoanAmount", "LossRatio", "LoanAge", "BorrSameCDC", "ProjectSameBorr", "Start", "Stop", "Unemployment Rate",
    "Log S&P 500 Return"])
    for wd in writeData:
        writer.writerow(wd)
