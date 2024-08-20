import pandas as pd
import csv
import os
#pd.set_option('max_columns', None)
#pd.set_option('max_rows', None)
#pd.options.display.max_seq_items = None


inputs = ["DQP_CatholicCharities_1059_RRH_June2022.xlsx"]
refFile = 'reference.csv'
all_csv = [file_name for file_name in os.listdir(os.getcwd()) if file_name in inputs]

li = []

for filename in all_csv:
    df = pd.read_excel(filename, index_col=None, header=None, parse_dates=True)
    li.append(df)
    

    df1 = pd.concat(li, axis=1, ignore_index=True)
    
print(df1)
one = df.iloc[70,9]
two = df.iloc[70,12]
three = df.iloc[71,9]
four = df.iloc[71,12]
five = df.iloc[72,9]
six = df.iloc[72,12]

print('One' + str(one))
print('Two' + str(two))
print('Three' + str(three))
print('Four' + str(four))
print('Five' + str(five))
print('Six' + str(six))

numerator = one + two + three + four + five + six
denominator = numerator + df.iloc[73,9] + df.iloc[73,12] + df.iloc[74,9] + df.iloc[74,12]
print('numerator ' + str(numerator ))
print('denominator ' + str(denominator ))


date1 = str(df.iloc[3,0]).split()
start = date1[0]
end = date1[2]
acctName = str(df.iloc[8,3])
projName = str(df.iloc[9,3])


# open file in read mode
with open(refFile, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        if projName == row[2]:
            hmisID = row[3]
            projType = row[4]
            break

timeliness = str(int((numerator/(  1 if not denominator else denominator))*100))
name = str(df.iloc[34,12])
ssn = str(df.iloc[35,12])
dob = str(df.iloc[36,12])
race = str(df.iloc[37,12])
eth = str(df.iloc[38,12])
gen = str(df.iloc[39,12])
vet = str(df.iloc[45,12])
exitDest = str(df.iloc[54,12])
chronicity = str(df.iloc[65,19])
disable = str(df.iloc[49,12])
incomeStart = str(df.iloc[55,12])
incomeAA = str(df.iloc[56,12])
incomeExit = str(df.iloc[57,12])
dv = str(0)
hoh = str(df.iloc[47,12])
print('acctName ' + acctName )
print('projName ' + projName )
print('timeliness ' + timeliness )
print('Name ' + name )
print('SSN ' + ssn )
print('DOB ' + dob )
print('Race ' + race )
print('Ethnicity ' + eth )
print('Gender ' + gen )
print('vet ' + vet )
print('exitDest ' + exitDest )
print('chronicity ' + chronicity )
print('disable ' + disable )
print('incomeStart ' + incomeStart )
print('incomeAA ' + incomeAA )
print('incomeExit ' + incomeExit )
print('HoH ' + hoh )

fields = ["Account Name","Project Name","HMIS ID","Project Type (Number)","Timeliness","Name","SSN","DOB","Race","Ethnicity","Gender","Veteran Status","Exit Destination","Chronicity(Prior Living Situation","Disabling Condition","Income at Start","Income at Annual Assessment","Income at Exit","Domestic Violence","Relationship to HoH"]
rows = [[acctName, projName, hmisID, projType, timeliness, name, ssn, dob, race, eth, gen,vet, exitDest, chronicity, disable, incomeStart, incomeAA, incomeExit, dv, hoh]]

with open('Import File.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)

print(df1)
