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
    # date1 = str(datetime.datetime.now().strftime("%b")) + ' ' + str(datetime.datetime.now().strftime("%y"))

    # ## Removes previous vesrions of the import file if it exists with the same name
    # ## This is the difference between the two versions
    # for csv1 in os.listdir(os.getcwd()):
        # if csv1 == 'Import File.csv':
            # os.remove(csv1)
    # print(os.listdir(os.getcwd()))
    # ## Main loop that iterates through all unzipped files
    # for zip_file in os.listdir(os.getcwd()):
        # if zip_file.endswith('.zip'):
            # with zipfile.ZipFile(zip_file , 'r') as zip_ref:
                # zip_ref.extractall(os.getcwd())

    ## Selects certain files to parse
    #inputs = ["Report.xlsx"]
    refFile = 'reference.csv'
    all_csv = [file_name for file_name in os.listdir(os.getcwd()) if(file_name.lower().startswith('dqp_') and file_name.lower().endswith('.xlsx'))]

    # li = []
    
    ## Add selected files contents to a list
    for filename in all_csv:
        df = pd.read_excel(filename, index_col=None, header=None, parse_dates=True)
        # li.append(df)
        print(filename)
    # df1 = pd.concat(li, axis=1, ignore_index=True)

        ## Calculations for timeliness
        numerator = df.iloc[70,9] + df.iloc[70,12] + df.iloc[71,9] + df.iloc[71,12] + df.iloc[72,9] + df.iloc[72,12]
        denominator = numerator + df.iloc[73,9] + df.iloc[73,12] + df.iloc[74,9] + df.iloc[74,12]

        

        ## Variable Assignments
        acctName = str(df.iloc[8,3])
        x = str(df.iloc[9,3]).split(' - ')
        projName = x[1]
        hmisID = x[0]
        # open file in read mode
        with open(refFile, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                if hmisID == row[3]:
                    projName == row[2]
                    projType = row[4]
                    acctName = row[1]
                    break
                        
        date1 = str(df.iloc[3,0]).split()
        start = date1[0]
        stop = date1[2]
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
        dqp = projName + "_"  + date

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
        if "Aspire Health Partners" in projName:
            dqp = "Aspire" + projName[22:] + "_"  + date
        elif "Grand Avenue Economic Community Development" in projName:
            dqp = "Grand Avenue" + projName[43:] + "_"  + date
        elif "Coalition for the Homeless" in projName:
            dqp = "Coalition" + projName[26:] + "_"  + date
        elif "The Christian Sharing Center" in projName:
            dqp = "Christian Sharing Center" + projName[28:] + "_"  + date

        print(os.getcwd()+ '\Import File.csv')
        print(os.path.exists(os.getcwd() + '\Import File.csv'))
            
        fields = ["DQP","Agency","Project","HMIS ID","Project Type","Start Date","Stop Date","Timeliness","Name","SSN","DOB","Race","Ethnicity","Gender","Veteran Status","Exit Destination","Chronicity(Prior Living Situation","Disabling Condition","Income at Start","Income at Annual Assessment","Income at Exit","Domestic Violence","Relationship to HoH"]
        rows = [[dqp, acctName, projName, hmisID, projType, start, stop, timeliness, name, ssn, dob, race, eth, gen, vet, exitDest, chronicity, disable, incomeStart, incomeAA, incomeExit, dv, hoh]]
        fileThere = False
        fileThere = os.path.exists(os.getcwd() + '\Import File.csv')
                    
            #with open('Import File' + str(num) + '.csv', 'w') as f:
        ## Write contents to "Import file"
        with open('Import File.csv', 'a+', newline='') as f:
            write = csv.writer(f)
            if not fileThere:
                write.writerow(fields)
                write.writerows(rows)
            else:
                write.writerows(rows)
           
        # Remove all other CSV Files
        # for csv1 in os.listdir(os.getcwd()):
            # if csv1.endswith('.csv'):
                # if "Import File" not in csv1:
                    # os.remove(csv1)
    print("\n\n\n Process Complete! \n.............................................................................................................................................\nThe import file is ready!")

                
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

## Add elements to canvas
canvas1.create_window(150, 170, window=button1)
canvas1.create_window(150, 80, window=label)
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

