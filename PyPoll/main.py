import os
import csv

intVC = 0
varCanNme = []
varCanVote = []
intCanCnt = 0

ed_csv = os.path.join("../PyPoll", "election_data.csv")

with open(ed_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # skip the headers

    for row in csvreader:
        intVC += 1

        if row[2] not in varCanNme:
            varCanNme.append(row[2])
            varCanVote.append(1)
            intCanCnt += 1
        else:
            intIndex = varCanNme.index(row[2])
            varCanVote[intIndex] = varCanVote[intIndex] + 1

varResult = list(zip(varCanNme,varCanVote))
strWinner = varCanNme[0]

print("Election Results")
print("-------------------------")
print (f"Total Votes:       {intVC}")
print("-------------------------")
print (f"Canidates with votes: ")

for (varCanNme, varCanVote) in varResult:
    print(f'{varCanNme}: {"{0:.3f}%".format(varCanVote/intVC*100)}:  ({varCanVote})')
print("-------------------------")
print(f'Winner: {strWinner}')
print("-------------------------")

f = open('Output.txt','w')
f.write("Election Results\n")
f.write("-------------------------\n")
f.write(f"Total Votes:       {intVC}\n")
f.write("-------------------------\n")
f.write(f"Canidates with votes: \n")

for (varCanNme, varCanVote) in varResult:
    f.write(f'{varCanNme}: {"{0:.3f}%".format(varCanVote/intVC*100)}:  ({varCanVote})\n')
f.write("-------------------------\n")
f.write(f'Winner: {strWinner}\n')
f.write("-------------------------\n")
f.close()