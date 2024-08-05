import tkinter as tk
import tkinter.ttk as ttk
import json

# Define the filename for the JSON file and initialize settings and variables
filename = "settings1.json"
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
tabs_textboxes = {}

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


def default_settings():
    settings = {
        "ES":
        {
            "nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "divide(exitDest1 ,6)", "chronWeight": "divide(chron1 ,16)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,6)", "startWeight": "divide(start1 ,11)", "annualWeight": "divide(Annual1 ,16)", "exitWeight": "divide(exit1 ,6)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,16)",
            "nameMult": "2", "ssnMult": "2", "dobMult": "2", "raceMult": "5", "ethMult": "5", "genMult": "2", "vetMult": "5", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "2", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "10"
        },
        "HP":
        {
            "nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,0)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,6)", "startWeight": "divide(start1 ,6)", "annualWeight": "divide(Annual1 ,6)", "exitWeight": "divide(exit1 ,6)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)",
            "nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "0", "inactiveMult": "0", "disableMult": "10", "startMult": "10", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"
        },
        "PSH":
        {
            "nameWeight": "piecewise(name1)", "ssnWeight": "piecewise(ssn1)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "piecewise(chron1)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "piecewise(disable1)", "startWeight": "divide(start1 ,6)", "annualWeight": "divide(Annual1 ,11)", "exitWeight": "divide(exit1 ,6)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)",
            "nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"
        },
        "RRH":
        {
            "nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,6)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "piecewise(disable1)", "startWeight": "divide(start1 ,11)", "annualWeight": "divide(Annual1 ,11)", "exitWeight": "divide(exit1 ,11)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)",
            "nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"
        },
        "SSO":
        {
            "nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,11)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,0)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,0)", "startWeight": "divide(start1 ,0)", "annualWeight": "divide(Annual1 ,0)", "exitWeight": "divide(exit1 ,0)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)",
            "nameMult": "5", "ssnMult": "5", "dobMult": "5", "raceMult": "5", "ethMult": "5", "genMult": "5", "vetMult": "15", "exitDestMult": "15", "chronMult": "0", "inactiveMult": "0", "disableMult": "0", "startMult": "0", "annualMult": "0", "exitMult": "0", "hohMult": "25", "timeMult": "15", "enrollMult": "0"
        },
        "SO":
        {
            "nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,11)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,16)", "inactiveWeight": "divide(inactive1 ,16)", "disableWeight": "piecewise(disable1)", "startWeight": "divide(start1 ,6)", "annualWeight": "divide(Annual1 ,16)", "exitWeight": "piecewise(exit1)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)",
            "nameMult": "2", "ssnMult": "2", "dobMult": "2", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "7", "exitDestMult": "15", "chronMult": "15", "inactiveMult": "0", "disableMult": "5", "startMult": "2", "annualMult": "2", "exitMult": "2", "hohMult": "25", "timeMult": "15", "enrollMult": "0"
        },
        "TH":
        {
            "nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "divide(exitDest1 ,6)", "chronWeight": "divide(chron1 ,11)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,6)", "startWeight": "divide(start1 ,16)", "annualWeight": "divide(Annual1 ,16)", "exitWeight": "divide(exit1 ,16)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)",
            "nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"
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

# This function takes in a dictionary of settings and saves it to a file using JSON
def save_settings(settings):
    with open(filename, "w") as f:
        json.dump(settings, f)

# This function adds a text box to a tkinter window with a label and default value
def add_textbox(root, row, col, text, default_value):
    label = tk.Label(root, text=text)
    label.grid(row=row, column=col, sticky="W", pady=1)

    textbox = tk.Entry(root)
    textbox.insert(0, default_value)
    textbox.grid(row=row, column=col + 1, pady=1)

    return textbox

# This function sets the value of a text box to a given value
def set_input(value, text):
        text.delete(0, "end")
        text.insert(0, value)

# This function updates the settings based on the current values in the text boxes
# and saves them to a file using the save_settings function
def update_but():
    settings = {}
    for tab, textboxes in tabs_textboxes.items():
        tab_settings = {}
        for textbox in textboxes:
            tab_settings[textbox["text"]] = textbox["widget"].get()
        settings[tab] = tab_settings
    save_settings(settings)
    print('Settings Updated')

# This function sets the values of the text boxes to the default values
# and saves the default settings to a file using the save_settings function
def default_but():
    settings = default_settings()
    for tab, textboxes in tabs_textboxes.items():
        for textbox in textboxes:
            box = textbox["widget"]
            default_value = settings[tab][textbox["text"]]
            set_input(default_value,box)
    save_settings(settings)
    print('Default settings Loaded')

def new_tab(notebook, tab_type, tab = 'default', default_values = '', tabs_textbox = {}):
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


def initialize():
    settings = load_settings()

    root = tk.Tk()
    root.title("Settings")

    notebook = ttk.Notebook(root)

    
    for tab, default_values in settings.items():
        new_tab(notebook, "box", tab, default_values, tabs_textboxes)
        
    new_tab(notebook, "area", "Instructions")
    notebook.pack(fill="both", expand=True)


    update_button = tk.Button(root, text="Update", command=update_but)
    update_button.pack(side="right", padx=10, pady=10)

    default_button = tk.Button(root, text="Load Defaults", command=default_but)
    default_button.pack(side="right", pady=10)

    

    root.mainloop()
