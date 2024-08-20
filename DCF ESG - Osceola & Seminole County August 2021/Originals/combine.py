import pandas as pd
import csv
import os

inputs = ["Q4a.csv", "Q6a.csv", "Q6b.csv", "Q6c.csv", "Q6d.csv", "Q6e.csv", "Q14a.csv"]
all_csv = [file_name for file_name in os.listdir(os.getcwd()) if file_name in inputs]

li = []

for filename in all_csv:
    df = pd.read_csv(filename, index_col=None, header=0, parse_dates=True, infer_datetime_format=True)
    li.append(df)

df1 = pd.concat(li, axis=1, ignore_index=True)

numerator = df1.iloc[4,41] + df1.iloc[3,41] + df1.iloc[2,41] + df1.iloc[4,42] + df1.iloc[3,42] + df1.iloc[2,42]
denominator = numerator + df1.iloc[1,41] + df1.iloc[1,42] + df1.iloc[0,41] + df1.iloc[0,42]

bottom = 0 if not df1.iloc[4,1] else df1.iloc[4,1]

acctName = df1.iloc[0,6]
projName = df1.iloc[0,8]
hmisID = str(df1.iloc[0,9])
projType = str(df1.iloc[0,10])
timeliness = str(numerator/(  0 if not denominator else denominator))
name = str(df1.iloc[0,25])
ssn = str(df1.iloc[1,25])
dob = str(df1.iloc[2,25])
race = str(df1.iloc[3,25])
eth = str(df1.iloc[4,25])
gen = str(df1.iloc[5,25])
vet = str(df1.iloc[0,28])
exitDest = str(df1.iloc[0,31])
chronicity = str(df1.iloc[3,39])
disable = str(df1.iloc[4,28])
incomeStart = str(df1.iloc[1,31])
incomeAA = str(df1.iloc[2,31])
incomeExit = str(df1.iloc[3,31])
dv = str(df1.iloc[2,1]/ bottom)
hoh = str(df1.iloc[2,28])


fields = ["Account Name","Project Name","HMIS ID","Project Type (Number)","Timeliness","Name","SSN","DOB","Race","Ethnicity","Gender","Veteran Status","Exit Destination","Chronicity(Prior Living Situation","Disabling Condition","Income at Start","Income at Annual Assessment","Income at Exit","Domestic Violence","Relationship to HoH"]
rows = [[acctName, projName, hmisID, projType, timeliness, name, ssn, dob, race, eth, gen,vet, exitDest, chronicity, disable, incomeStart, incomeAA, incomeExit, dv, hoh]]

with open('Import File.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)

print(df1)
