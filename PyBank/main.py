import os
import csv

bd_csv = os.path.join("../PyBank", "budget_data.csv")
intMonth = 0
intNetAmt = 0
fltAvgChg = 0.0
strGrtIncDt = "test"
intGrtIncAmt = 0
strGrtDcDt = "Test"
intGrtDcAmt = 0
intFirstAmt = 0
intFinalAmt = 0
intPrevAmt = 0
intNextAmt = 0

with open(bd_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # skip the headers

    for row in csvreader:
        intMonth += 1
        intNetAmt += int(row[1])
        if intFirstAmt == 0:
            intFirstAmt = int(row[1])
            intChgAmt = int(row[1])
        else:
            intPrevAmt = intNextAmt
            intNextAmt = int(row[1])
            intChgAmt = intNextAmt - intPrevAmt


        if intChgAmt > intGrtIncAmt:
            intGrtIncAmt = intChgAmt
            strGrtIncDt = row[0]
        elif intChgAmt < intGrtDcAmt:
            intGrtDcAmt = intChgAmt
            strGrtDcDt = row[0]

intFinalAmt = intNextAmt
fltAvgChg = round((intFinalAmt-intFirstAmt)/(intMonth-1),2)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:                       {intMonth}")
print(f"Total:                              {intNetAmt}")
print(f"Average  Change:                    ${fltAvgChg}")
print(f"Greatest Increase in Profits:       {strGrtIncDt}   (${intGrtIncAmt})")
print(f"Greatest Decrease in Profits:       {strGrtDcDt}   (${intGrtDcAmt})")

# import sys
# f = open("test.out", 'w')
# sys.stdout = f
# print "test"
# f.close()
f = open('Output.txt','w')
f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write(f"Total Months:                       {intMonth}\n")
f.write(f"Total:                              {intNetAmt}\n")
f.write(f"Average  Change:                    ${fltAvgChg}\n")
f.write(f"Greatest Increase in Profits:       {strGrtIncDt}   (${intGrtIncAmt})\n")
f.write(f"Greatest Decrease in Profits:       {strGrtDcDt}   (${intGrtDcAmt})\n")
f.close()