import tkinter as tk
import tkinter.ttk as ttk
import json

filename = "settings.json"
settings = {}
name1 = 0
ssn1 = 0
dob1 = 0
race1 = 0
eth1 = 0
gen1 = 0
vet1 = 0
exitDest1 = 0
chron1 = 0
inactive1 = 0
disable1 = 0
start1 = 0
Annual1 = 0
exit1 = 0
hoh1 = 0
time1 = 0
enroll1 = 0
projType="Emergency Shelter - ES"

def piecewise(x):
    if x == 0:
        return 1
    elif x == 1:
         return 0.5
    else:
        return 0
        
def divide(x,y):
    if y==0:
        return 0
    return(1-x/y)

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

def default_settings():
    settings = {
            "ES":
            {	
                "esNameWeight": "piecewise(name1)", "esSSNWeight": "divide(ssn1 ,6)", "esDOBWeight": "piecewise(dob1)", "esRaceWeight": "piecewise(race1)", "esEthWeight": "piecewise(eth1)", "esGenWeight": "piecewise(gen1)", "esVetWeight": "piecewise(vet1)", "esExitDestWeight": "divide(exitDest1 ,6)", "esChronWeight": "divide(chron1 ,16)", "esInactiveWeight": "divide(inactive1 ,0)",  "esDisableWeight": "divide(disable1 ,6)", "esStartWeight": "divide(start1 ,11)", "esAnnualWeight": "divide(Annual1 ,16)", "esExitWeight": "divide(exit1 ,6)", "esHoHWeight": "piecewise(hoh1)", "esTimeWeight": "divide(time1 ,16)", "esEnrollWeight": "divide(enroll1 ,16)",
                "esNameMult": "2", "esSSNMult": "2", "esDOBMult": "2", "esRaceMult": "5", "esEthMult": "5", "esGenMult": "2", "esVetMult": "5", "esExitDestMult": "5", "esChronMult": "10", "esInactiveMult": "0",  "esDisableMult": "5", "esStartMult": "5", "esAnnualMult": "2", "esExitMult": "5", "esHoHMult": "25", "esTimeMult": "10", "esEnrollMult": "10"
            },
            "HP":
            {   
                "hpNameWeight": "piecewise(name1)", "hpSSNWeight": "divide(ssn1 ,6)", "hpDOBWeight": "piecewise(dob1)", "hpRaceWeight": "piecewise(race1)", "hpEthWeight": "piecewise(eth1)", "hpGenWeight": "piecewise(gen1)", "hpVetWeight": "piecewise(vet1)", "hpExitDestWeight": "piecewise(exitDest1)",  "hpChronWeight": "divide(chron1 ,0)", "hpInactiveWeight": "divide(inactive1 ,0)", "hpDisableWeight": "divide(disable1 ,6)", "hpStartWeight": "divide(start1 ,6)", "hpAnnualWeight": "divide(Annual1 ,6)", "hpExitWeight": "divide(exit1 ,6)", "hpHoHWeight": "piecewise(hoh1)", "hpTimeWeight": "divide(time1 ,16)","hpEnrollWeight": "divide(enroll1 ,0)",
                "hpNameMult": "2", "hpSSNMult": "5","hpDOBMult": "5", "hpRaceMult": "2", "hpEthMult": "2", "hpGenMult": "2", "hpVetMult": "2", "hpExitDestMult": "5", "hpChronMult": "0", "hpInactiveMult": "0",  "hpDisableMult": "10", "hpStartMult": "10", "hpAnnualMult": "15", "hpExitMult": "5", "hpHoHMult": "25", "hpTimeMult": "10", "hpEnrollMult": "0"
            },
            "PSH":
            {
                "pshNameWeight": "piecewise(name1)", "pshSSNWeight": "piecewise(ssn1)", "pshDOBWeight": "piecewise(dob1)", "pshRaceWeight": "piecewise(race1)", "pshEthWeight": "piecewise(eth1)", "pshGenWeight": "piecewise(gen1)", "pshVetWeight": "piecewise(vet1)", "pshExitDestWeight": "piecewise(exitDest1)", "pshChronWeight": "piecewise(chron1)", "pshInactiveWeight": "divide(inactive1 ,0)", "pshDisableWeight": "piecewise(disable1)", "pshStartWeight": "divide(start1 ,6)", "pshAnnualWeight": "divide(Annual1 ,11)", "pshExitWeight": "divide(exit1 ,6)", "pshHoHWeight": "piecewise(hoh1)", "pshTimeWeight": "divide(time1 ,16)", "pshEnrollWeight": "divide(enroll1 ,0)",
                "pshNameMult": "2", "pshSSNMult": "5", "pshDOBMult": "5", "pshRaceMult": "2", "pshEthMult": "2", "pshGenMult": "2", "pshVetMult": "2", "pshExitDestMult": "5", "pshChronMult": "10", "pshInactiveMult": "0", "pshDisableMult": "5", "pshStartMult": "5", "pshAnnualMult": "15", "pshExitMult": "5", "pshHoHMult": "25", "pshTimeMult": "10", "pshEnrollMult": "0"
            },
            "RRH":
            {
                "rrhNameWeight": "piecewise(name1)", "rrhSSNWeight": "divide(ssn1 ,6)", "rrhDOBWeight": "piecewise(dob1)", "rrhRaceWeight": "piecewise(race1)", "rrhEthWeight": "piecewise(eth1)", "rrhGenWeight": "piecewise(gen1)", "rrhVetWeight": "piecewise(vet1)", "rrhExitDestWeight": "piecewise(exitDest1)", "rrhChronWeight": "divide(chron1 ,6)", "rrhInactiveWeight": "divide(inactive1 ,0)", "rrhDisableWeight": "piecewise(disable1)", "rrhStartWeight": "divide(start1 ,11)", "rrhAnnualWeight": "divide(Annual1 ,11)", "rrhExitWeight": "divide(exit1 ,11)", "rrhHoHWeight": "piecewise(hoh1)", "rrhTimeWeight": "divide(time1 ,16)", "rrhEnrollWeight": "divide(enroll1 ,0)",
                "rrhNameMult": "2", "rrhSSNMult": "5", "rrhDOBMult": "5", "rrhRaceMult": "2", "rrhEthMult": "2", "rrhGenMult": "2", "rrhVetMult": "2", "rrhExitDestMult": "5", "rrhChronMult": "10", "rrhInactiveMult": "0", "rrhDisableMult": "5", "rrhStartMult": "5", "rrhAnnualMult": "15", "rrhExitMult": "5", "rrhHoHMult": "25", "rrhTimeMult": "10", "rrhEnrollMult": "0"
            },
            "SSO":
            {
                "ssoNameWeight": "piecewise(name1)", "ssoSSNWeight": "divide(ssn1 ,11)", "ssoDOBWeight": "piecewise(dob1)", "ssoRaceWeight": "piecewise(race1)", "ssoEthWeight": "piecewise(eth1)", "ssoGenWeight": "piecewise(gen1)", "ssoVetWeight": "piecewise(vet1)", "ssoExitDestWeight": "piecewise(exitDest1)", "ssoChronWeight": "divide(chron1 ,0)", "ssoInactiveWeight": "divide(inactive1 ,0)", "ssoDisableWeight": "divide(disable1 ,0)", "ssoStartWeight": "divide(start1 ,0)", "ssoAnnualWeight": "divide(Annual1 ,0)", "ssoExitWeight": "divide(exit1 ,0)", "ssoHoHWeight": "piecewise(hoh1)", "ssoTimeWeight": "divide(time1 ,16)", "ssoEnrollWeight": "divide(enroll1 ,0)",
                "ssoNameMult": "5", "ssoSSNMult": "5", "ssoDOBMult": "5", "ssoRaceMult": "5", "ssoEthMult": "5", "ssoGenMult": "5", "ssoVetMult": "15", "ssoExitDestMult": "15", "ssoChronMult": "0", "ssoInactiveMult": "0", "ssoDisableMult": "0", "ssoStartMult": "0", "ssoAnnualMult": "0", "ssoExitMult": "0", "ssoHoHMult": "25", "ssoTimeMult": "15", "ssoEnrollMult": "0"
            },
            "SO":
            {
                "soNameWeight": "piecewise(name1)", "soSSNWeight": "divide(ssn1 ,11)", "soDOBWeight": "piecewise(dob1)", "soRaceWeight": "piecewise(race1)", "soEthWeight": "piecewise(eth1)", "soGenWeight": "piecewise(gen1)", "soVetWeight": "piecewise(vet1)", "soExitDestWeight": "piecewise(exitDest1)", "soChronWeight": "divide(chron1 ,16)", "soInactiveWeight": "divide(inactive1 ,16)", "soDisableWeight": "piecewise(disable1)", "soStartWeight": "divide(start1 ,6)", "soAnnualWeight": "divide(Annual1 ,16)", "soExitWeight": "piecewise(exit1)", "soHoHWeight": "piecewise(hoh1)", "soTimeWeight": "divide(time1 ,16)", "soEnrollWeight": "divide(enroll1 ,0)",
                "soNameMult": "2", "soSSNMult": "2", "soDOBMult": "2", "soRaceMult": "2", "soEthMult": "2", "soGenMult": "2", "soVetMult": "7", "soExitDestMult": "15", "soChronMult": "15", "soInactiveMult": "0", "soDisableMult": "5", "soStartMult": "2", "soAnnualMult": "2", "soExitMult": "2", "soHoHMult": "25", "soTimeMult": "15", "soEnrollMult": "0"
            },
            "TH":
            {
                "thNameWeight": "piecewise(name1)", "thSSNWeight": "divide(ssn1 ,6)", "thDOBWeight": "piecewise(dob1)", "thRaceWeight": "piecewise(race1)", "thEthWeight": "piecewise(eth1)", "thGenWeight": "piecewise(gen1)", "thVetWeight": "piecewise(vet1)", "thExitDestWeight": "divide(exitDest1 ,6)", "thChronWeight": "divide(chron1 ,11)", "thInactiveWeight": "divide(inactive1 ,0)", "thDisableWeight": "divide(disable1 ,6)", "thStartWeight": "divide(start1 ,16)", "thAnnualWeight": "divide(Annual1 ,16)", "thExitWeight": "divide(exit1 ,16)", "thHoHWeight": "piecewise(hoh1)", "thTimeWeight": "divide(time1 ,16)", "thEnrollWeight": "divide(enroll1 ,0)",
                "thNameMult": "2", "thSSNMult": "5", "thDOBMult": "5", "thRaceMult": "2", "thEthMult": "2", "thGenMult": "2", "thVetMult": "2", "thExitDestMult": "5", "thChronMult": "10", "thInactiveMult": "0", "thDisableMult": "5", "thStartMult": "5", "thAnnualMult": "15", "thExitMult": "5", "thHoHMult": "25", "thTimeMult": "10", "thEnrollMult": "0"
            }
        }
    return settings

# Function to load user settings from JSON file
def load_settings():
    # Load the saved settings from a JSON file
    try:
        with open(filename, "r") as f:
            settings = json.load(f)
    except FileNotFoundError:
        # Use default settings if the file does not exist
        settings = default_settings()
    return settings

def save_settings(settings):
    with open(filename, "w") as f:
        json.dump(settings, f)

def add_textbox(root, row, col, text, default_value):
    label = tk.Label(root, text=text)
    label.grid(row=row, column=col, sticky="W", pady=1)

    textbox = tk.Entry(root)
    textbox.insert(0, default_value)
    textbox.grid(row=row, column=col + 1, pady=1)

    return textbox

def set_input(value, text):
        text.delete(0, "end")
        text.insert(0, value)

def update_button():
    settings = {}
    for tab, textboxes in tabs_textboxes.items():
        tab_settings = {}
        for textbox in textboxes:
            tab_settings[textbox["text"]] = textbox["widget"].get()
        settings[tab] = tab_settings
    save_settings(settings)
    print('Settings Updated')


        
def default_button():
    settings = default_settings()
    for tab, textboxes in tabs_textboxes.items():
        for textbox in textboxes:
            box = textbox["widget"]
            default_value = settings[tab][textbox["text"]]
            set_input(default_value,box)
    save_settings(settings)
    print('Default settings Loaded')

def new_tab(notebook, tab_type, tab = 'default', default_value = '', tabs_textbox = {}):
    tab_frame = ttk.Frame(notebook)
    notebook.add(tab_frame, text= tab)

    scrollbar = ttk.Scrollbar(tab_frame)
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(tab_frame, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", expand=True)

    scrollbar.config(command=canvas.yview)

    frame = ttk.Frame(canvas)
    frame.pack()

    if tab_type == "area":
        instructions = tk.Text(frame, width=50, height=20)
        instructions.pack()
        instructions.insert(tk.END, "Instructions on how to use the program...")
    elif tab_type == "box":
        textboxes = []
        num_settings = len(default_values)
        num_cols = 9
        num_rows = 17
        for i, (text, default_value) in enumerate(default_values.items()):
            row = i % num_rows
            col = (i // num_rows) * num_cols
            textbox = add_textbox(frame, row, col, text, default_value)
            textboxes.append({"text": text, "widget": textbox})

        tabs_textbox[tab] = textboxes

settings = load_settings()

root = tk.Tk()
root.title("Settings")

notebook = ttk.Notebook(root)

tabs_textboxes = {}
for tab, default_values in settings.items():
    new_tab(notebook, "box", tab, default_values, tabs_textboxes)
    
new_tab(notebook, "area", "Instructions")
notebook.pack(fill="both", expand=True)


update_button = tk.Button(root, text="Update", command=update_button)
update_button.pack(side="right", padx=10, pady=10)

default_button = tk.Button(root, text="Load Defaults", command=default_button)
default_button.pack(side="right", pady=10)

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


nameWeight = eval(proj[0]['widget'].get())
ssnWeight = eval(proj[1]['widget'].get()) 
dobWeight = eval(proj[2]['widget'].get()) 
raceWeight = eval(proj[3]['widget'].get()) 
ethWeight = eval(proj[4]['widget'].get()) 
genWeight = eval(proj[5]['widget'].get()) 
vetWeight = eval(proj[6]['widget'].get()) 
exitDestWeight = eval(proj[7]['widget'].get()) 
chronWeight = eval(proj[8]['widget'].get()) 
inactiveWeight = eval(proj[9]['widget'].get()) 
disableWeight = eval(proj[10]['widget'].get()) 
startWeight = eval(proj[11]['widget'].get()) 
annualWeight = eval(proj[12]['widget'].get()) 
exitWeight = eval(proj[13]['widget'].get()) 
hohWeight = eval(proj[14]['widget'].get()) 
timeWeight = eval(proj[15]['widget'].get()) 
enrollWeight = eval(proj[16]['widget'].get()) 
  
nameMult = float(proj[17]['widget'].get())
ssnMult = float(proj[18]['widget'].get())
dobMult = float(proj[19]['widget'].get())
raceMult = float(proj[20]['widget'].get())
ethMult = float(proj[21]['widget'].get())
genMult = float(proj[22]['widget'].get())
vetMult = float(proj[23]['widget'].get())
exitDestMult = float(proj[24]['widget'].get())
chronMult = float(proj[25]['widget'].get())
inactiveMult = float(proj[26]['widget'].get())
disableMult = float(proj[27]['widget'].get())
startMult = float(proj[28]['widget'].get())
annualMult = float(proj[29]['widget'].get())
exitMult = float(proj[30]['widget'].get())
hohMult = float(proj[31]['widget'].get())
timeMult = float(proj[32]['widget'].get())
enrollMult = float(proj[33]['widget'].get())

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
print(grade,'(' + str(totalScore) +'%)')

root.mainloop()
