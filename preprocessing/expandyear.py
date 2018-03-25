import csv
import math

duplicate = []
writeData = []
newline = []

with open('test_outsample.csv', 'r') as f:
    data = csv.reader(f)
    for i, line in enumerate(data):
        if i == 0: continue
        d = line[22] #Check ChargeOffDate
        if len(d) == 2: #not charged off
            duplicate.append(int(math.ceil(int(line[16])/12.0))) # add number of years to duplicate
        else:
            approvalDate = line [11] # approval date
            numMonth = (int(d.split('/')[2]) - int(approvalDate.split('/')[2]))*12 + (int(d.split('/')[0]) - int(approvalDate.split('/')[0]))
            numYear = int(math.ceil(numMonth/12.0))
            duplicate.append(numYear) # add number of year to duplicate

print len(duplicate)

with open('test_outsample.csv', 'r') as h:
    data = csv.reader(h)
    for i, line in enumerate(data):
        if i == 0: continue
        d = line[22] #Check ChargeOffDate
        count = 0
        while count < duplicate[i-1]:
                newline = line + [count,count+1] #add time stamp
                count += 1
                if len(d) != 2 and count != duplicate[i-1]: #check chargeoff
                    newline[21] = 0
                writeData.append(newline) #in new file

with open('test_outsample1.csv', 'w') as g:
    writer = csv.writer(g)
    writer.writerow(["Loan ID", "BorrCity", "BorrState", "BorrZip", "CDC_City",
    "CDC_State", "CDC_Zip", "ThirdPartyLender_City", "ThirdPartyLender_State",
    "ThirdPartyDollars", "GrossApproval", "ApprovalDate", "ApprovalFiscalYear",
    "DeliveryMethod", "InitialInterestRate", "Missing Rate?", "TermInMonths", "NaicsCode",
    "ProjectCounty", "ProjectState", "BusinessType", "LoanStatus", "ChargeOffDate", "GrossChargeOffAmount", "BorrRegion",
    "NaicsTrimmed", "Cont_ApprovalDate", "TotalLoanAmount", "LossRatio", "LoanAge", "BorrSameCDC", "ProjectSameBorr", "Start", "Stop"])

    for wd in writeData:
        writer.writerow(wd);
