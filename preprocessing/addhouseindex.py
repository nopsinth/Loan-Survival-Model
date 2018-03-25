import csv
import math

houseprice = {}
writeData = []
mydata = []
statedict = {'WA': 47, 'DE': 9, 'WI': 48, 'WV': 49, 'HI': 12, 'FL': 10, 'WY': 50,
'NH': 31, 'NJ': 32, 'NM': 33, 'TX': 43, 'LA': 19, 'NC': 28, 'ND': 29,
'NE': 30, 'TN': 42, 'NY': 35, 'PA': 39, 'RI': 40, 'NV': 34, 'VA': 45,
'CO': 6, 'AK': 1, 'AL': 2, 'AR': 3, 'VT': 46, 'IL': 15, 'GA': 11, 'IN': 16,
'IA': 13, 'MA': 20, 'AZ': 4, 'CA': 5, 'ID': 14, 'CT': 7, 'ME': 22, 'MD': 21,
'OK': 37, 'OH': 36, 'UT': 44, 'MO': 25, 'MN': 24, 'MI': 23, 'KS': 17,
'MT': 27, 'MS': 26, 'SC': 41, 'KY': 18, 'OR': 38, 'SD': 41, 'DC': 8, 'GU':24}
state = 0
time = 0
dummy = 0

with open('housingyear.csv', 'r') as f:
    data = csv.reader(f)
    for i, line in enumerate(data):
        if i == 0: continue
        for state in range (0,51):
            if state == 0: continue
            houseprice[i*100 + state] = line[state] #keep data in dictionary dummy:rate ; dummy = 100*time+state

with open('test_outsample3.csv', 'r') as g:
    dataTwo = csv.reader(g)
    for i, line in enumerate(dataTwo):
        if i == 0: continue
        d = line[11]
        time = int(d.split('/')[2])-1990 #match time with data in dictionary
        state = int(statedict[line[19]])
        dummy = int(100*(time + 1 + int(line[32])) + state) #match year
        mydata.append(line + [houseprice[dummy]])

with open('final_test_outsample.csv', 'w') as h:
     writer = csv.writer(h)
     writer.writerow(["Loan ID", "BorrCity", "BorrState", "BorrZip", "CDC_City",
     "CDC_State", "CDC_Zip", "ThirdPartyLender_City", "ThirdPartyLender_State",
     "ThirdPartyDollars", "GrossApproval", "ApprovalDate", "ApprovalFiscalYear",
     "DeliveryMethod", "InitialInterestRate", "Missing Rate?", "TermInMonths", "NaicsCode",
     "ProjectCounty", "ProjectState", "BusinessType", "LoanStatus", "ChargeOffDate", "GrossChargeOffAmount", "BorrRegion",
     "NaicsTrimmed", "Cont_ApprovalDate", "TotalLoanAmount", "LossRatio", "LoanAge", "BorrSameCDC", "ProjectSameBorr", "Start", "Stop", "Unemployment Rate",
     "S&P 500 Return", "Housing Price Index"])
     for wd in mydata:
         writer.writerow(wd);
