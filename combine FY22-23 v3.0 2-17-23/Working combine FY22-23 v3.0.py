print( "Python Code starting")
import pandas as pd
import os
import csv
import datetime as dt
import tkinter as tk
import settings1 as settings
import re

def setting():
    settings.initialize()

timeNow = dt.datetime.now()
read_excel = pd.read_excel
reader = csv.reader
curdir = os.getcwd()
dir1 = os.listdir(curdir)
paths = os.path.exists
writer = csv.writer
# This function returns a value based on the input parameter x.
# If x is equal to 0, it returns 1. If x is equal to 1, it returns 0.5. Otherwise, it returns 0.
def piecewise(x):
    if x == 0:
        return 1
    elif x == 1:
        return 0.5
    else:
        return 0

# This function divides x by y and returns the result of subtracting that value from 1.
# If y is equal to 0, it returns 0.
def divide(x,y):
    if y==0:
        return 0
    return(1-x/y)

# This function returns a letter grade based on the input parameter score.
# If the score is greater than or equal to 90, it returns "A".
# If the score is greater than or equal to 80, it returns "B".
# If the score is greater than or equal to 70, it returns "C".
# If the score is greater than or equal to 60, it returns "D".
# Otherwise, it returns "F".
def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
## This is the main function
def run():
    
    
    
    
    ## Establishes the date for the dqp name
    date = str(timeNow.month) + str(timeNow.day) + str(timeNow.year)
    # date1 = str(datetime.datetime.now().strftime("%b")) + ' ' + str(datetime.datetime.now().strftime("%y"))

    ## Selects certain files to parse
    refFile = 'reference.csv'
    all_csv = [file_name for file_name in dir1 if(file_name.lower().startswith('dqp_') and file_name.lower().endswith('.xlsx'))]
    other_csv = [file for file in dir1 if(file.lower().startswith('el_') and file.lower().endswith('.xlsx'))]

    ## Add selected files contents to a list
    for filename in all_csv:
        df = read_excel(filename, index_col=None, header=None, parse_dates=True)
        # li.append(df)
        print(filename)
        # df1 = pd.concat(li, axis=1, ignore_index=True)

        ## Calculations for timeliness
        numerator = df.iloc[74,9] + df.iloc[74,12] + df.iloc[75,9] + df.iloc[75,12] + df.iloc[73,9] + df.iloc[73,12]
        denominator = numerator + df.iloc[72,9] + df.iloc[72,12] + df.iloc[71,9] + df.iloc[71,12]
       
       
        

        ## Variable Assignments
        acctName = str(df.iloc[8,3])
        print(acctName)
        x = str(df.iloc[9,3]).split(' - ')
        projName = x[1]
        hmisID = x[0]
        # open file in read mode
        with open(refFile, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                if hmisID == row[3]:
                    projName == row[2]
                    projType = row[4]
                    acctName = row[1]
                    autoExit = row[0]
                    break
        read_obj.close()


        inactive = str(df.iloc[80,15])
        date1 = str(df.iloc[3,0]).split()
        start = date1[0]
        stop = date1[2]
        timeliness = str(int((numerator/(  1 if not denominator else denominator))*100))
        name = str(df.iloc[35,16])
        ssn = str(df.iloc[36,16])
        dob = str(df.iloc[37,16])
        race = str(df.iloc[38,16])
        eth = str(df.iloc[39,16])
        gen = str(df.iloc[40,16])
        vet = str(df.iloc[46,12])
        exitDest = str(df.iloc[55,12])
        chronicity = str(df.iloc[66,20])
        disable = str(df.iloc[50,12])
        incomeStart = str(0 if hmisID == "576" else df.iloc[56,12])
        incomeAA = str(0 if hmisID == "576" else df.iloc[57,12])
        incomeExit = str(0 if hmisID == "576" else (0 if autoExit else df.iloc[58,12]))
        
        if projType.lower().endswith('- hp') or projType.lower().endswith('- hp'):
            disable = 0
            Chronicity = 0
        
        dv = str(0)
        hoh = str(df.iloc[48,12])
        dqp = projName + "_"  + date
        print(incomeStart)
        print(incomeAA)
        print(incomeExit)
        print(hoh)

       
        if "Aspire Health Partners" in projName:
            dqp = "Aspire" + projName[22:] + "_"  + date
        elif "Grand Avenue Economic Community Development" in projName:
            dqp = "Grand Avenue" + projName[43:] + "_"  + date
        elif "Coalition for the Homeless" in projName:
            dqp = "Coalition" + projName[26:] + "_"  + date
        elif "The Christian Sharing Center" in projName:
            dqp = "Christian Sharing Center" + projName[28:] + "_"  + date
        elif "Christian Service Center" in projName:
            dqp = "CSC" + projName[28:] + "_"  + date
        elif "Community Assisted" in projName:
            dqp = "CASL" + projName[28:] + "_"  + date


            
        fields = ["DQP","Agency","Project","HMIS ID","Project Type","Start Date","Stop Date","Timeliness","Name","SSN","DOB","Race","Ethnicity","Gender","Veteran Status","Exit Destination","Chronicity(Prior Living Situation","Disabling Condition","Income at Start","Income at Annual Assessment","Income at Exit","Relationship to HoH","Inactive Records","Enrollment Length"]
        rows = [[dqp, acctName, projName, hmisID, projType, start, stop, timeliness, name, ssn, dob, race, eth, gen, vet, exitDest, chronicity, disable, incomeStart, incomeAA, incomeExit, hoh, inactive, str(0)]]
        fileThere = False
        fileThere = paths(curdir + '\Import File.csv')
                    

        ## Write contents to "Import file"
        with open('Import File.csv', 'a+', newline='') as f:
            write = writer(f)
            if not fileThere:
                write.writerow(fields)
                write.writerows(rows)
            else:
                write.writerows(rows)
        f.close()




       
    for files in other_csv:
        df1 = pd.read_excel(files, index_col=None, header=None, parse_dates=True)
        print(files)
        projName1 = str(df1.iloc[5,3])
        count = 0
        total = 0
        
        # open file in read mode
        with open(refFile, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row1 in csv_reader:
                # row variable is a list that represents a row in csv
                if projName1 == row1[2]:
                    hmisID1 = row1[3]
                    projType1 = row1[4]
                    acctName1 = row1[1]
                    break
        read_obj.close()            
        if projType1 == 'Emergency Shelter - ES':# or projType1 == 'Street Outreach - SO':
            for index1 in range(len(df1)):
                if str(df1.iloc[index1,0]).isnumeric():
                    total += 1
                    if df1.iloc[index1,20] > 180:
                        count += 1
        
        enrollmentLen = str(int((count/(  1 if not total else total))*100))
        
        f = open('Import File.csv', 'r', newline='')
        df2 = reader(f)
        fileThere2 = False
        fileThere2 = paths(curdir + '\Complete Import File.csv')
        fields = ["DQP","Agency","Project","HMIS ID","Project Type","Start Date","Stop Date","Timeliness","Name","SSN","DOB","Race","Ethnicity","Gender","Veteran Status","Exit Destination","Chronicity(Prior Living Situation","Disabling Condition","Income at Start","Income at Annual Assessment","Income at Exit","Relationship to HoH","Inactive Records","Enrollment Length"]
        
        j =  open('Complete Import File.csv', 'a+', newline='')
        df3 = writer(j)
        if not fileThere2:
            df3.writerow(fields)
        for row2 in df2:
            if row2[3] == hmisID1:
                row2[23] = enrollmentLen
                df3.writerow(row2)
        f.close()
        j.close()
        df4 = pd.read_csv("Import File.csv")
        print(df4) 
        

    if other_csv != []:    
        comfile = open('Complete Import File.csv', 'r+', newline='')
        comfile2 = open('Complete Import File.csv', 'a+', newline='')
        bigfile = open('Import File.csv', 'r', newline='')
        
        # pass the file object to reader() to get the reader object
        csv_reader2 = pd.read_csv('Complete Import File.csv', index_col=None, header=None, parse_dates=True)
        csv_writer3 = writer(comfile2)
        csv_reader = reader(bigfile)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            flag = False
            # row variable is a list that represents a row in csv
            for index1 in range(len(csv_reader2)):
                print('Row == ' + row[3])
                print('Row2 == ' + csv_reader2.iloc[index1,3])
                if row[3] == csv_reader2.iloc[index1,3]:
                    print('I broke' +  row[3])
                    flag = True
            if flag == False:        
                csv_writer3.writerow(row)
        bigfile.close()
        comfile.close()   
        comfile2.close()       

        
    print("\n\n\n Process Complete! \n.............................................................................................................................................\nThe import file is ready!")

def scoreCard(filename = "Complete Import File.csv"):
    fields = ["DQP","Agency","Project","HMIS ID","Project Type","Start Date","Stop Date","Timeliness","Name","SSN","DOB","Race","Ethnicity","Gender","Veteran Status","Exit Destination","Chronicity(Prior Living Situation","Disabling Condition","Income at Start","Income at Annual Assessment","Income at Exit","Relationship to HoH","Inactive Records","Enrollment Length"]
    p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'
    try:
        # open file in read mode
        with open(filename, 'r+', newline='') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                if row != fields:
                    dqp = row[0]
                    agency = row[1]
                    project = row[2]
                    hmis_id = int(re.findall(p, row[3])[0])
                    projType = row[4]
                    start_date = row[5]
                    stop_date = row[6]
                    time1 = float(re.findall(p, row[7])[0])
                    name1 = float(re.findall(p, row[8])[0])
                    ssn1 = float(re.findall(p, row[9])[0])
                    dob1 = float(re.findall(p, row[10])[0])
                    race1 = float(re.findall(p, row[11])[0])
                    eth1 = float(re.findall(p, row[12])[0])
                    gen1 = float(re.findall(p, row[13])[0])
                    vet1 = float(re.findall(p, row[14])[0])
                    exitDest1 = float(re.findall(p, row[15])[0])
                    chron1 = float(re.findall(p, row[16])[0])
                    disable1 = float(re.findall(p, row[17])[0])
                    start1 = float(re.findall(p, row[18])[0])
                    Annual1 = float(re.findall(p, row[19])[0])
                    exit1 = float(re.findall(p, row[20])[0])
                    hoh1 = float(re.findall(p, row[21])[0])
                    inactive1 = float(re.findall(p, row[22])[0])
                    enroll1 = float(re.findall(p, row[23])[0])

                    tabs_textboxes = settings.load_settings()

                    

                    ES = tabs_textboxes["ES"]
                    HP = tabs_textboxes["HP"]
                    PSH = tabs_textboxes["PSH"]
                    RRH = tabs_textboxes["RRH"]
                    SSO = tabs_textboxes["SSO"]
                    SO = tabs_textboxes["SO"]
                    TH = tabs_textboxes["TH"]

                    if projType == 'Emergency Shelter - ES':
                        proj = ES
                    elif projType == 'Homelessness Prevention - HP':
                        proj = HP
                    elif projType == 'Permenant Supportive Housing - PSH':
                        proj = PSH
                    elif projType == 'Rapid Re-housing - RRH':
                        proj = RRH
                    elif projType == 'Services Only':
                        proj = SSO
                    elif projType == 'Street Outreach - SO':
                        proj = SO
                    elif projType == 'Transitional Housing - TH':
                        proj = TH


                    nameWeight = eval(proj["nameWeight"])
                    ssnWeight = eval(proj["ssnWeight"]) 
                    dobWeight = eval(proj["dobWeight"]) 
                    raceWeight = eval(proj["raceWeight"]) 
                    ethWeight = eval(proj["ethWeight"]) 
                    genWeight = eval(proj["genWeight"]) 
                    vetWeight = eval(proj["vetWeight"]) 
                    exitDestWeight = eval(proj["exitDestWeight"]) 
                    chronWeight = eval(proj["chronWeight"]) 
                    inactiveWeight = eval(proj["inactiveWeight"]) 
                    disableWeight = eval(proj["disableWeight"]) 
                    startWeight = eval(proj["startWeight"]) 
                    annualWeight = eval(proj["annualWeight"]) 
                    exitWeight = eval(proj["exitWeight"]) 
                    hohWeight = eval(proj["hohWeight"]) 
                    timeWeight = eval(proj["timeWeight"]) 
                    enrollWeight = eval(proj["enrollWeight"]) 
                      
                    nameMult = float(proj["nameMult"])
                    ssnMult = float(proj["ssnMult"])
                    dobMult = float(proj["dobMult"])
                    raceMult = float(proj["raceMult"])
                    ethMult = float(proj["ethMult"])
                    genMult = float(proj["genMult"])
                    vetMult = float(proj["vetMult"])
                    exitDestMult = float(proj["exitDestMult"])
                    chronMult = float(proj["chronMult"])
                    inactiveMult = float(proj["inactiveMult"])
                    disableMult = float(proj["disableMult"])
                    startMult = float(proj["startMult"])
                    annualMult = float(proj["annualMult"])
                    exitMult = float(proj["exitMult"])
                    hohMult = float(proj["hohMult"])
                    timeMult = float(proj["timeMult"])
                    enrollMult = float(proj["enrollMult"])

                    nameScore = nameWeight * nameMult
                    ssnScore = ssnWeight * ssnMult
                    dobScore = dobWeight * dobMult
                    raceScore = raceWeight * raceMult
                    ethScore = ethWeight * ethMult
                    genScore = genWeight * genMult
                    vetScore = vetWeight * vetMult
                    exitDestScore = exitDestWeight * exitDestMult
                    chronScore = chronWeight * chronMult
                    inactiveScore = inactiveWeight * inactiveMult
                    disableScore = disableWeight * disableMult
                    startScore = startWeight * startMult
                    annualScore = annualWeight * annualMult
                    exitScore = exitWeight * exitMult
                    hohScore = hohWeight * hohMult
                    timeScore = timeWeight * timeMult
                    enrollScore = enrollWeight * enrollMult

                    totalScore = round(nameScore + ssnScore + dobScore + raceScore + ethScore + genScore + vetScore + exitDestScore + chronScore + inactiveScore + disableScore + startScore + annualScore + exitScore + hohScore + timeScore + enrollScore, 2)

                    grade = letter(totalScore)
                    print("Agency: " + agency)
                    print("Project: " + project)
                    print("HMIS ID: " + str(hmis_id))
                    print("Project Type: " + projType)
                    print("Start Date: " + start_date)
                    print("Stop_Date: " + stop_date)
                    print('\n')
                    print(str(timeScore)+'%')
                    print(str(enrollScore)+'%\n')
                    print(str(nameScore)+'%')
                    print(str(ssnScore)+'%')
                    print(str(dobScore)+'%')
                    print(str(raceScore)+'%')
                    print(str(ethScore)+'%')
                    print(str(genScore)+'%')
                    print(str(vetScore)+'%')
                    print(str(exitDestScore)+'%')
                    print(str(chronScore)+'%')
                    print(str(inactiveScore)+'%\n')
                    print(str(disableScore)+'%')
                    print(str(startScore)+'%')
                    print(str(annualScore)+'%')
                    print(str(exitScore)+'%')
                    print(str(hohScore)+'%\n')
                    print(grade,'(' + str(totalScore) +'%)\n\n')

                    
        read_obj.close()
    except FileNotFoundError:
        print("\n\n*********************************************************************\n       The file named 'Complete Import File.csv' was not found \n    in the current directory please locate the file and try again \n*********************************************************************\n")



    

    
    
                
## Create window
# This is a python platform named Tkinter that allows window creation
win = tk.Tk()

## Make a canvas on the window
# The canvas allows you to add elements like text, graphics, widgets, frames etc
canvas1 = tk.Canvas(win, width = 300, height = 300)
canvas1.pack()

## Create elements for canvas
label = tk.Label(win, text = ' Place this file in the same location as the xlsx files for your APR(s) then click Combine. Make sure your file names start with dqp_. Make sure to have the Reference file in the same directory with the file name "reference.csv".', wraplength=290, justify="center")
button1 = tk.Button(win, text='Combine',command=run, fg='black')
button2 = tk.Button(win, text='Settings',command=setting, fg='black')
button3 = tk.Button(win, text='ScoreCard',command=scoreCard, fg='black')
## Add elements to canvas
canvas1.create_window(150, 170, window=button1)
canvas1.create_window(150, 80, window=label)
canvas1.create_window(150, 200, window=button2)
canvas1.create_window(150, 230, window=button3)
canvas1.update()

## Changes the wrap size according to the canvas size
def resize(e):
    w = e.width
    h = e.height
    #canvas1.config(height = h-5, width = w-5)
    label.config(width = w-1, wraplength=int(w-10))
    
## <Configure> The widget changed size (or location, on some platforms). The new size is provided in the width and height attributes of the event object passed to the callback.    
canvas1.bind('<Configure>',resize)
## this stops the program from closing until it gets the close command
win.mainloop()


## Project Types
## Emergency Shelter - ES - 1
## Transitional Housing - TH - 2
## Permenant Supportive Housing - PSH - 3
## Street Outreach - SO - 4
## Supportive Services Only - SSO - 6
## Other - OT - 7
## Permenant Housing - PH-H/PH - 9
## Permenant Housing - PH-S - 10
## Homelessness Prevention - HP - 12
## Rapid Re-housing - RRH - 55
## Coordinated Entry System - CES - 14

##auto-py-to-exe





 ## Breakdown for project types
        # if projType == "1":
            # projType = "Emergency Shelter - ES"
        # elif projType == "2":
            # projType = "Transitional Housing - TH"
        # elif projType == "3":
            # projType = "Permenant Supportive Housing - PSH"
        # elif projType == "4":
            # projType = "Street Outreach - SO"
        # elif projType == "6":
            # projType = "Supportive Services Only - SSO"
        # elif projType == "7":
            # projType = "Other - OT"
        # elif projType == "9":
            # projType = "Permenant Housing - PH-H/PH"
        # elif projType == "10":
            # projType = "Permenant Housing - PH-S"
        # elif projType == "12":
            # projType = "Homelessness Prevention - HP"
        # elif projType == "55":
            # projType = "Rapid Re-housing - RRH"
        # elif projType == "14":
            # projType = "Coordinated Entry System - CES"

        # print('income exit: ' + incomeExit)
        # print('hmisID: ' + hmisID)

        # print(curdir+ '\Import File.csv')
        # print(paths(curdir + '\Import File.csv'))
        #with open('Import File' + str(num) + '.csv', 'w') as f:
        # Remove all other CSV Files
        # for csv1 in listdir(curdir):
            # if csv1.endswith('.csv'):
                # if "Import File" not in csv1:
                    # os.remove(csv1)
