import pandas as pd
import csv as csv
import os
import zipfile
import datetime
import tkinter as tk

## This is the main function
def run():
    ## Establishes the date for the dqp name
    date = str(datetime.datetime.now().month) + str(datetime.datetime.now().day) + str(datetime.datetime.now().year)
    ##date1 = str(datetime.datetime.now().strftime("%b")) + ' ' + str(datetime.datetime.now().strftime("%y"))


    ## Main loop that iterates through all unzipped files
    for zip_file in os.listdir(os.getcwd()):
        if zip_file.endswith('.zip'):
            with zipfile.ZipFile(zip_file , 'r') as zip_ref:
                zip_ref.extractall(os.getcwd())

            ## Selects certain files to parse
            inputs = ["Q4a.csv", "Q6a.csv", "Q6b.csv", "Q6c.csv", "Q6d.csv", "Q6e.csv", "Q14a.csv"]
            all_csv = [file_name for file_name in os.listdir(os.getcwd()) if file_name in inputs]

            li = []
            
            ## Add selected files contents to a list
            for filename in all_csv:
                df = pd.read_csv(filename, index_col=None, header=0, parse_dates=True, infer_datetime_format=True)
                li.append(df)

            df1 = pd.concat(li, axis=1, ignore_index=True)

            ## Calculations for timeliness
            numerator = df1.iloc[4,41] + df1.iloc[3,41] + df1.iloc[2,41] + df1.iloc[4,42] + df1.iloc[3,42] + df1.iloc[2,42]
            denominator = numerator + df1.iloc[1,41] + df1.iloc[1,42] + df1.iloc[0,41] + df1.iloc[0,42]

            bottom = 1 if not df1.iloc[4,1] else df1.iloc[4,1]

            ## Variable Assignments
            acctName = df1.iloc[0,6]
            projName = df1.iloc[0,8]
            hmisID = str(int(df1.iloc[0,9]))
            projType = str(int(df1.iloc[0,10]))
            start = str(df1.iloc[0,18])
            stop = str(df1.iloc[0,19])
            timeliness = str(int((numerator/(  1 if not denominator else denominator))*100))
            name = str(df1.iloc[0,25] * 100)
            ssn = str(df1.iloc[1,25] * 100)
            dob = str(df1.iloc[2,25] * 100)
            race = str(df1.iloc[3,25] * 100)
            eth = str(df1.iloc[4,25] * 100)
            gen = str(df1.iloc[5,25] * 100)
            vet = str(df1.iloc[0,28] * 100)
            exitDest = str(df1.iloc[0,31] * 100)
            chronicity = str(df1.iloc[3,39] * 100)
            disable = str(df1.iloc[4,28] * 100)
            incomeStart = str(df1.iloc[1,31] * 100)
            incomeAA = str(df1.iloc[2,31] * 100)
            incomeExit = str(df1.iloc[3,31] * 100)
            dv = str(int((df1.iloc[3,1]/ bottom)*100))
            hoh = str(df1.iloc[2,28] * 100)
            dqp = projName + "_"  + date

            

            
            ## Breakdpwn for project types
            if projType == "1":
                projType = "Emergency Shelter - ES"
            elif projType == "2":
                projType = "Transitional Housing - TH"
            elif projType == "3":
                projType = "Permenant Supportive Housing - PSH"
            elif projType == "4":
                projType = "Street Outreach - SO"
            elif projType == "6":
                projType = "Supportive Services Only - SSO"
            elif projType == "7":
                projType = "Other - OT"
            elif projType == "10":
                projType = "Permenant Housing - PH-S"
            elif projType == "12":
                projType = "Homelessness Prevention - HP"
            elif projType == "13":
                projType = "Rapid Re-housing - RRH"
            elif projType == "14":
                projType = "Coordinated Entry System - CES"

            if "Aspire Health Partners" in projName:
                dqp = "Aspire" + projName[22:] + "_"  + date
            elif "Grand Avenue Economic Community Development" in projName:
                dqp = "Grand Avenue" + projName[43:] + "_"  + date
                    
            print(os.getcwd()+ '\Import File.csv')
            print(os.path.exists(os.getcwd() + '\Import File.csv'))
                
            fields = ["DQP","Agency","Project","HMIS ID","Project Type","Start Date","Stop Date","Timeliness","Name","SSN","DOB","Race","Ethnicity","Gender","Veteran Status","Exit Destination","Chronicity(Prior Living Situation","Disabling Condition","Income at Start","Income at Annual Assessment","Income at Exit","Domestic Violence","Relationship to HoH"]
            rows = [[dqp, acctName, projName, hmisID, projType, start, stop, timeliness, name, ssn, dob, race, eth, gen, vet, exitDest, chronicity, disable, incomeStart, incomeAA, incomeExit, dv, hoh]]
            fileThere = False
            fileThere = os.path.exists(os.getcwd() + '\Import File.csv')
                        
                ##with open('Import File' + str(num) + '.csv', 'w') as f:
            ## Write contents to "Import file"
            with open('Import File.csv', 'a+', newline='') as f:
                write = csv.writer(f)
                if not fileThere:
                    write.writerow(fields)
                    write.writerows(rows)
                else:
                    write.writerows(rows)
       
                
    # Remove all other CSV Files
    for csv1 in os.listdir(os.getcwd()):
        if csv1.endswith('.csv'):
            if "Import File" not in csv1:
                os.remove(csv1)
    print("\n\n\n Process Complete! \n.............................................................................................................................................\nThe import file is ready!")

                
## Create window
win = tk.Tk()

## Make a canvas on the window
canvas1 = tk.Canvas(win, width = 300, height = 300)
canvas1.pack()

## Create elements for canvas
label = tk.Label(win, text = ' Place this file in the same location as the zip files for your APR(s) then click Combine', wraplength=290, justify="center")
button1 = tk.Button(win, text='Combine',command=run, fg='black')

## Add elements to canvas
canvas1.create_window(150, 150, window=button1)
canvas1.create_window(150, 100, window=label)
canvas1.update()

## Changes the wrap size according to the canvas size
def resize(e):
    w = e.width
    h = e.height
    #canvas1.config(height = h-5, width = w-5)
    label.config(width = w-1, wraplength=int(w-10))
    
canvas1.bind('<Configure>',resize)
win.mainloop()

## Poject Types
## Emergency Shelter - ES - 1
## Transitional Housing - TH - 2
## Permenant Supportive Housing - PSH - 3
## Street Outreach - SO - 4
## Supportive Services Only - SSO - 6
## Other - OT - 7
## Permenant Housing - PH-S - 10
## Homelessness Prevention - HP - 12
## Rapid Re-housing - RRH - 13
## Coordinated Entry System - CES - 14
