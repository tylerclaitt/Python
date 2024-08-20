import json



def piecewise(x):
    if x == 0:
        return 1
    elif x == 1:
        return 0.5
    else:
        return 0
        
def divide(x,y):
    return 1-x/y
    
    
name1 = 1
ssn1 = 1
dob1 = 1
race1 = 1
eth1 = 1
gen1 = 1
vet1 = 1
exitDest1 = 1
chron1 = 1
inactive1 = 1
disable1 = 1
start1 = 1
Annual1 = 1
exit1 = 1
hoh1 = 1
time1 = 1
enroll1 = 1
    
# Try to read the configuration file
try:
    with open('settings.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, create it with default values
    config = {
        'esNameWeight' : 'piecewise(name1)',
        'esSSNWeight' : '6',
        'esDOBWeight' : 'piecewise(dob1)',
        'esRaceWeight' : 'piecewise(race1)',
        'esEthWeight' : 'piecewise(eth1)',
        'esGenWeight' : 'piecewise(gen1)',
        'esVetWeight' : 'piecewise(vet1)',
        'esExitDestWeight' : '6',
        'esChronWeight' : '16',
        'esInactiveWeight' : '0',
        'esDisableWeight' : '6',
        'esStartWeight' : '11',
        'esAnnualWeight' : '16',
        'esExitWeight' : '6',
        'esHoHWeight' : 'piecewise(hoh1)',
        'esTimeWeight' : '16',
        'esEnrollWeight' : '16',

        'hpNameWeight' : 'piecewise(name1)',
        'hpSSNWeight' : '6',
        'hpDOBWeight' : 'piecewise(dob1)',
        'hpRaceWeight' : 'piecewise(race1)',
        'hpEthWeight' : 'piecewise(eth1)',
        'hpGenWeight' : 'piecewise(gen1)',
        'hpVetWeight' : 'piecewise(vet1)',
        'hpExitDestWeight' : 'piecewise(exitDest1)',
        'hpChronWeight' : '0',
        'hpInactiveWeight' : '0',
        'hpDisableWeight' : '6',
        'hpStartWeight' : '6',
        'hpAnnualWeight' : '6',
        'hpExitWeight' : '6',
        'hpHoHWeight' : 'piecewise(hoh1)',
        'hpTimeWeight' : '16',
        'hpEnrollWeight' : '0',

        'pshNameWeight' : 'piecewise(name1)',
        'pshSSNWeight' : 'piecewise(ssn1)',
        'pshDOBWeight' : 'piecewise(dob1)',
        'pshRaceWeight' : 'piecewise(race1)',
        'pshEthWeight' : 'piecewise(eth1)',
        'pshGenWeight' : 'piecewise(gen1)',
        'pshVetWeight' : 'piecewise(vet1)',
        'pshExitDestWeight' : 'piecewise(exitDest1)',
        'pshChronWeight' : 'piecewise(chron1)',
        'pshInactiveWeight' : '0',
        'pshDisableWeight' : 'piecewise(disable1)',
        'pshStartWeight' : '6',
        'pshAnnualWeight' : '11',
        'pshExitWeight' : '6',
        'pshHoHWeight' : 'piecewise(hoh1)',
        'pshTimeWeight' : '16',
        'pshEnrollWeight' : '0',

        'rrhNameWeight' : 'piecewise(name1)',
        'rrhSSNWeight' : '6',
        'rrhDOBWeight' : 'piecewise(dob1)',
        'rrhRaceWeight' : 'piecewise(race1)',
        'rrhEthWeight' : 'piecewise(eth1)',
        'rrhGenWeight' : 'piecewise(gen1)',
        'rrhVetWeight' : 'piecewise(vet1)',
        'rrhExitDestWeight' : 'piecewise(exitDest1)',
        'rrhChronWeight' : '6',
        'rrhInactiveWeight' : '0',
        'rrhDisableWeight' : 'piecewise(disable1)',
        'rrhStartWeight' : '11',
        'rrhAnnualWeight' : '11',
        'rrhExitWeight' : '11',
        'rrhHoHWeight' : 'piecewise(hoh1)',
        'rrhTimeWeight' : '16',
        'rrhEnrollWeight' : '0',

        'ssoNameWeight' : 'piecewise(name1)',
        'ssoSSNWeight' : '11',
        'ssoDOBWeight' : 'piecewise(dob1)',
        'ssoRaceWeight' : 'piecewise(race1)',
        'ssoEthWeight' : 'piecewise(eth1)',
        'ssoGenWeight' : 'piecewise(gen1)',
        'ssoVetWeight' : 'piecewise(vet1)',
        'ssoExitDestWeight' : 'piecewise(exitDest1)',
        'ssoChronWeight' : '0',
        'ssoInactiveWeight' : '0',
        'ssoDisableWeight' : '0',
        'ssoStartWeight' : '0',
        'ssoAnnualWeight' : '0',
        'ssoExitWeight' : '0',
        'ssoHoHWeight' : 'piecewise(hoh1)',
        'ssoTimeWeight' : '16',
        'ssoEnrollWeight' : '0',

        'soNameWeight' : 'piecewise(name1)',
        'soSSNWeight' : '11',
        'soDOBWeight' : 'piecewise(dob1)',
        'soRaceWeight' : 'piecewise(race1)',
        'soEthWeight' : 'piecewise(eth1)',
        'soGenWeight' : 'piecewise(gen1)',
        'soVetWeight' : 'piecewise(vet1)',
        'soExitDestWeight' : 'piecewise(exitDest1)',
        'soChronWeight' : '16',
        'soInactiveWeight' : '16',
        'soDisableWeight' : 'piecewise(disable1)',
        'soStartWeight' : '6',
        'soAnnualWeight' : '16',
        'soExitWeight' : 'piecewise(exit1)',
        'soHoHWeight' : 'piecewise(hoh1)',
        'soTimeWeight' : '16',
        'soEnrollWeight' : '0',

        'thNameWeight' : 'piecewise(name1)',
        'thSSNWeight' : '6',
        'thDOBWeight' : 'piecewise(dob1)',
        'thRaceWeight' : 'piecewise(race1)',
        'thEthWeight' : 'piecewise(eth1)',
        'thGenWeight' : 'piecewise(gen1)',
        'thVetWeight' : 'piecewise(vet1)',
        'thExitDestWeight' : '6',
        'thChronWeight' : '11',
        'thInactiveWeight' : '0',
        'thDisableWeight' : '6',
        'thStartWeight' : '16',
        'thAnnualWeight' : '16',
        'thExitWeight' : '16',
        'thHoHWeight' : 'piecewise(hoh1)',
        'thTimeWeight' : '16',
        'thEnrollWeight' : '0',
        
 

        'esNameMult' : '2',
        'esSSNMult' : '2',
        'esDOBMult' : '2',
        'esRaceMult' : '5',
        'esEthMult' : '5',
        'esGenMult' : '2',
        'esVetMult' : '5',
        'esExitDestMult' : '5',
        'esChronMult' : '10',
        'esInactiveMult' : '0',
        'esDisableMult' : '5',
        'esStartMult' : '5',
        'esAnnualMult' : '2',
        'esExitMult' : '5',
        'esHoHMult' : '25',
        'esTimeMult' : '10',
        'esEnrollMult' : '10',

        'hpNameMult' : '2',
        'hpSSNMult' : '5',
        'hpDOBMult' : '5',
        'hpRaceMult' : '2',
        'hpEthMult' : '2',
        'hpGenMult' : '2',
        'hpVetMult' : '2',
        'hpExitDestMult' : '5',
        'hpChronMult' : '0',
        'hpInactiveMult' : '0',
        'hpDisableMult' : '10',
        'hpStartMult' : '10',
        'hpAnnualMult' : '15',
        'hpExitMult' : '5',
        'hpHoHMult' : '25',
        'hpTimeMult' : '10',
        'hpEnrollMult' : '0',

        'pshNameMult' : '2',
        'pshSSNMult' : '5',
        'pshDOBMult' : '5',
        'pshRaceMult' : '2',
        'pshEthMult' : '2',
        'pshGenMult' : '2',
        'pshVetMult' : '2',
        'pshExitDestMult' : '5',
        'pshChronMult' : '10',
        'pshInactiveMult' : '0',
        'pshDisableMult' : '5',
        'pshStartMult' : '5',
        'pshAnnualMult' : '15',
        'pshExitMult' : '5',
        'pshHoHMult' : '25',
        'pshTimeMult' : '10',
        'pshEnrollMult' : '0',

        'rrhNameMult' : '2',
        'rrhSSNMult' : '5',
        'rrhDOBMult' : '5',
        'rrhRaceMult' : '2',
        'rrhEthMult' : '2',
        'rrhGenMult' : '2',
        'rrhVetMult' : '2',
        'rrhExitDestMult' : '5',
        'rrhChronMult' : '10',
        'rrhInactiveMult' : '0',
        'rrhDisableMult' : '5',
        'rrhStartMult' : '5',
        'rrhAnnualMult' : '15',
        'rrhExitMult' : '5',
        'rrhHoHMult' : '25',
        'rrhTimeMult' : '10',
        'rrhEnrollMult' : '0',

        'ssoNameMult' : '5',
        'ssoSSNMult' : '5',
        'ssoDOBMult' : '5',
        'ssoRaceMult' : '5',
        'ssoEthMult' : '5',
        'ssoGenMult' : '5',
        'ssoVetMult' : '15',
        'ssoExitDestMult' : '15',
        'ssoChronMult' : '0',
        'ssoInactiveMult' : '0',
        'ssoDisableMult' : '0',
        'ssoStartMult' : '0',
        'ssoAnnualMult' : '0',
        'ssoExitMult' : '0',
        'ssoHoHMult' : '25',
        'ssoTimeMult' : '15',
        'ssoEnrollMult' : '0',

        'soNameMult' : '2',
        'soSSNMult' : '2',
        'soDOBMult' : '2',
        'soRaceMult' : '2',
        'soEthMult' : '2',
        'soGenMult' : '2',
        'soVetMult' : '7',
        'soExitDestMult' : '15',
        'soChronMult' : '15',
        'soInactiveMult' : '0',
        'soDisableMult' : '5',
        'soStartMult' : '2',
        'soAnnualMult' : '2',
        'soExitMult' : '2',
        'soHoHMult' : '25',
        'soTimeMult' : '15',
        'soEnrollMult' : '0',

        'thNameMult' : '2',
        'thSSNMult' : '5',
        'thDOBMult' : '5',
        'thRaceMult' : '2',
        'thEthMult' : '2',
        'thGenMult' : '2',
        'thVetMult' : '2',
        'thExitDestMult' : '5',
        'thChronMult' : '10',
        'thInactiveMult' : '0',
        'thDisableMult' : '5',
        'thStartMult' : '5',
        'thAnnualMult' : '15',
        'thExitMult' : '5',
        'thHoHMult' : '25',
        'thTimeMult' : '10',
        'thEnrollMult' : '0'

        
    }
    with open('settings.json', 'w') as f:
        json.dump(config, f)

# Get the user settings from the configuration file
if projType == 'Emergency Shelter - ES':
    nameWeight = ES['esNameWeight']
    ssnWeight = ES['esSSNWeight']
    dobWeight = ES['esDOBWeight']
    raceWeight = ES['esRaceWeight']
    ethWeight = ES['esEthWeight']
    genWeight = ES['esGenWeight']
    vetWeight = ES['esVetWeight']
    exitDestWeight = ES['esExitDestWeight']
    chronWeight = ES['esChronWeight']
    inactiveWeight = ES['esInactiveWeight']
    disableWeight = ES['esDisableWeight']
    startWeight = ES['esStartWeight']
    annualWeight = ES['esAnnualWeight']
    exitWeight = ES['esExitWeight']
    hohWeight = ES['esHoHWeight']
    timeWeight = ES['esTimeWeight']
    enrollWeight = ES['esEnrollWeight']

    nameMult = ES['esNameMult']
    ssnMult = ES['esSSNMult']
    dobMult = ES['esDOBMult']
    raceMult = ES['esRaceMult']
    ethMult = ES['esEthMult']
    genMult = ES['esGenMult']
    vetMult = ES['esVetMult']
    exitDestMult = ES['esExitDestMult']
    chronMult = ES['esChronMult']
    inactiveMult = ES['esInactiveMult']
    disableMult = ES['esDisableMult']
    startMult = ES['esStartMult']
    annualMult = ES['esAnnualMult']
    exitMult = ES['esExitMult']
    hoHMult = ES['esHoHMult']
    timeMult = ES['esTimeMult']
    enrollMult = ES['esEnrollMult']

elif projType == 'Homelessness Prevention - HP':
    nameWeight = HP['hpNameWeight']
    ssnWeight = HP['hpSSNWeight']
    dobWeight = HP['hpDOBWeight']
    raceWeight = HP['hpRaceWeight']
    ethWeight = HP['hpEthWeight']
    genWeight = HP['hpGenWeight']
    vetWeight = HP['hpVetWeight']
    exitDestWeight = HP['hpExitDestWeight']
    chronWeight = HP['hpChronWeight']
    inactiveWeight = HP['hpInactiveWeight']
    disableWeight = HP['hpDisableWeight']
    startWeight = HP['hpStartWeight']
    annualWeight = HP['hpAnnualWeight']
    exitWeight = HP['hpExitWeight']
    hoHWeight = HP['hpHoHWeight']
    timeWeight = HP['hpTimeWeight']
    enrollWeight = HP['hpEnrollWeight']

    nameMult = HP['hpNameMult']
    ssnMult = HP['hpSSNMult']
    dobMult = HP['hpDOBMult']
    raceMult = HP['hpRaceMult']
    ethMult = HP['hpEthMult']
    genMult = HP['hpGenMult']
    vetMult = HP['hpVetMult']
    exitDestMult = HP['hpExitDestMult']
    chronMult = HP['hpChronMult']
    inactiveMult = HP['hpInactiveMult']
    disableMult = HP['hpDisableMult']
    startMult = HP['hpStartMult']
    annualMult = HP['hpAnnualMult']
    exitMult = HP['hpExitMult']
    hoHMult = HP['hpHoHMult']
    timeMult = HP['hpTimeMult']
    enrollMult = HP['hpEnrollMult']

elif projType == 'Permenant Supportive Housing - PSH':
    nameWeight = PSH['pshNameWeight']
    ssnWeight = PSH['pshSSNWeight']
    dobWeight = PSH['pshDOBWeight']
    raceWeight = PSH['pshRaceWeight']
    ethWeight = PSH['pshEthWeight']
    genWeight = PSH['pshGenWeight']
    vetWeight = PSH['pshVetWeight']
    exitDestWeight = PSH['pshExitDestWeight']
    chronWeight = PSH['pshChronWeight']
    inactiveWeight = PSH['pshInactiveWeight']
    disableWeight = PSH['pshDisableWeight']
    startWeight = PSH['pshStartWeight']
    annualWeight = PSH['pshAnnualWeight']
    exitWeight = PSH['pshExitWeight']
    hoHWeight = PSH['pshHoHWeight']
    timeWeight = PSH['pshTimeWeight']
    enrollWeight = PSH['pshEnrollWeight']

    nameMult = PSH['pshNameMult']
    ssnMult = PSH['pshSSNMult']
    dobMult = PSH['pshDOBMult']
    raceMult = PSH['pshRaceMult']
    ethMult = PSH['pshEthMult']
    genMult = PSH['pshGenMult']
    vetMult = PSH['pshVetMult']
    exitDestMult = PSH['pshExitDestMult']
    chronMult = PSH['pshChronMult']
    inactiveMult = PSH['pshInactiveMult']
    disableMult = PSH['pshDisableMult']
    startMult = PSH['pshStartMult']
    annualMult = PSH['pshAnnualMult']
    exitMult = PSH['pshExitMult']
    hoHMult = PSH['pshHoHMult']
    timeMult = PSH['pshTimeMult']
    enrollMult = PSH['pshEnrollMult']

elif projType == 'Rapid Re-housing - RRH':
    nameWeight = RRH['rrhNameWeight']
    ssnWeight = RRH['rrhSSNWeight']
    dobWeight = RRH['rrhDOBWeight']
    raceWeight = RRH['rrhRaceWeight']
    ethWeight = RRH['rrhEthWeight']
    genWeight = RRH['rrhGenWeight']
    vetWeight = RRH['rrhVetWeight']
    exitDestWeight = RRH['rrhExitDestWeight']
    chronWeight = RRH['rrhChronWeight']
    inactiveWeight = RRH['rrhInactiveWeight']
    disableWeight = RRH['rrhDisableWeight']
    startWeight = RRH['rrhStartWeight']
    annualWeight = RRH['rrhAnnualWeight']
    exitWeight = RRH['rrhExitWeight']
    hoHWeight = RRH['rrhHoHWeight']
    timeWeight = RRH['rrhTimeWeight']
    enrollWeight = RRH['rrhEnrollWeight']

    nameMult = RRH['rrhNameMult']
    ssnMult = RRH['rrhSSNMult']
    dobMult = RRH['rrhDOBMult']
    raceMult = RRH['rrhRaceMult']
    ethMult = RRH['rrhEthMult']
    genMult = RRH['rrhGenMult']
    vetMult = RRH['rrhVetMult']
    exitDestMult = RRH['rrhExitDestMult']
    chronMult = RRH['rrhChronMult']
    inactiveMult = RRH['rrhInactiveMult']
    disableMult = RRH['rrhDisableMult']
    startMult = RRH['rrhStartMult']
    annualMult = RRH['rrhAnnualMult']
    exitMult = RRH['rrhExitMult']
    hoHMult = RRH['rrhHoHMult']
    timeMult = RRH['rrhTimeMult']
    enrollMult = RRH['rrhEnrollMult']

elif projType == 'Services Only':
    nameWeight = SSO['ssoNameWeight']
    ssnWeight = SSO['ssoSSNWeight']
    dobWeight = SSO['ssoDOBWeight']
    raceWeight = SSO['ssoRaceWeight']
    ethWeight = SSO['ssoEthWeight']
    genWeight = SSO['ssoGenWeight']
    vetWeight = SSO['ssoVetWeight']
    exitDestWeight = SSO['ssoExitDestWeight']
    chronWeight = SSO['ssoChronWeight']
    inactiveWeight = SSO['ssoInactiveWeight']
    disableWeight = SSO['ssoDisableWeight']
    startWeight = SSO['ssoStartWeight']
    annualWeight = SSO['ssoAnnualWeight']
    exitWeight = SSO['ssoExitWeight']
    hoHWeight = SSO['ssoHoHWeight']
    timeWeight = SSO['ssoTimeWeight']
    enrollWeight = SSO['ssoEnrollWeight']

    nameMult = SSO['ssoNameMult']
    ssnMult = SSO['ssoSSNMult']
    dobMult = SSO['ssoDOBMult']
    raceMult = SSO['ssoRaceMult']
    ethMult = SSO['ssoEthMult']
    genMult = SSO['ssoGenMult']
    vetMult = SSO['ssoVetMult']
    exitDestMult = SSO['ssoExitDestMult']
    chronMult = SSO['ssoChronMult']
    inactiveMult = SSO['ssoInactiveMult']
    disableMult = SSO['ssoDisableMult']
    startMult = SSO['ssoStartMult']
    annualMult = SSO['ssoAnnualMult']
    exitMult = SSO['ssoExitMult']
    hoHMult = SSO['ssoHoHMult']
    timeMult = SSO['ssoTimeMult']
    enrollMult = SSO['ssoEnrollMult']

elif projType == 'Street Outreach - SO':
    nameWeight = SO['soNameWeight']
    ssnWeight = SO['soSSNWeight']
    dobWeight = SO['soDOBWeight']
    raceWeight = SO['soRaceWeight']
    ethWeight = SO['soEthWeight']
    genWeight = SO['soGenWeight']
    vetWeight = SO['soVetWeight']
    exitDestWeight = SO['soExitDestWeight']
    chronWeight = SO['soChronWeight']
    inactiveWeight = SO['soInactiveWeight']
    disableWeight = SO['soDisableWeight']
    startWeight = SO['soStartWeight']
    annualWeight = SO['soAnnualWeight']
    exitWeight = SO['soExitWeight']
    hoHWeight = SO['soHoHWeight']
    timeWeight = SO['soTimeWeight']
    enrollWeight = SO['soEnrollWeight']

    nameMult = SO['soNameMult']
    ssnMult = SO['soSSNMult']
    dobMult = SO['soDOBMult']
    raceMult = SO['soRaceMult']
    ethMult = SO['soEthMult']
    genMult = SO['soGenMult']
    vetMult = SO['soVetMult']
    exitDestMult = SO['soExitDestMult']
    chronMult = SO['soChronMult']
    inactiveMult = SO['soInactiveMult']
    disableMult = SO['soDisableMult']
    startMult = SO['soStartMult']
    annualMult = SO['soAnnualMult']
    exitMult = SO['soExitMult']
    hoHMult = SO['soHoHMult']
    timeMult = SO['soTimeMult']
    enrollMult = SO['soEnrollMult']

elif projType == 'Transitional Housing - TH':
    nameWeight = TH['thNameWeight']
    ssnWeight = TH['thSSNWeight']
    dobWeight = TH['thDOBWeight']
    raceWeight = TH['thRaceWeight']
    ethWeight = TH['thEthWeight']
    genWeight = TH['thGenWeight']
    vetWeight = TH['thVetWeight']
    exitDestWeight = TH['thExitDestWeight']
    chronWeight = TH['thChronWeight']
    inactiveWeight = TH['thInactiveWeight']
    disableWeight = TH['thDisableWeight']
    startWeight = TH['thStartWeight']
    annualWeight = TH['thAnnualWeight']
    exitWeight = TH['thExitWeight']
    hoHWeight = TH['thHoHWeight']
    timeWeight = TH['thTimeWeight']
    enrollWeight = TH['thEnrollWeight']

    nameMult = TH['thNameMult']
    ssnMult = TH['thSSNMult']
    dobMult = TH['thDOBMult']
    raceMult = TH['thRaceMult']
    ethMult = TH['thEthMult']
    genMult = TH['thGenMult']
    vetMult = TH['thVetMult']
    exitDestMult = TH['thExitDestMult']
    chronMult = TH['thChronMult']
    inactiveMult = TH['thInactiveMult']
    disableMult = TH['thDisableMult']
    startMult = TH['thStartMult']
    annualMult = TH['thAnnualMult']
    exitMult = TH['thExitMult']
    hoHMult = TH['thHoHMult']
    timeMult = TH['thTimeMult']
    enrollMult = TH['thEnrollMult']




# Update the user settings
theme = input("Enter the theme (light or dark): ")
font_size = input("Enter the font size: ")

# Save the updated user settings back to the configuration file
config = {
    'theme': theme,
    'font_size': font_size
}
with open('settings.json', 'w') as f:
    json.dump(config, f)



if projType == 'Emergency Shelter - ES':
	esNameWeight = piecewise(name1)
	esSSNWeight = divide6(ssn1)
	esDOBWeight = piecewise(dob1)
	esRaceWeight = piecewise(race1)
	esEthWeight = piecewise(eth1)
	esGenWeight = piecewise(gen1)
	esVetWeight = piecewise(vet1)
	esExitDestWeight = divide6(exitDest1)
	esChronWeight = divide16(chron1)
	esInactiveWeight = 0
	esDisableWeight = divide6(disable1)
	esStartWeight = divide11(start1)
	esAnnualWeight = divide16(Annual1)
	esExitWeight = divide6(exit1)
	esHoHWeight = piecewise(hoh1)
	esTimeWeight = divide16(time1)
	esEnrollWeight = divide16(enroll1)

elif projType == 'Homelessness Prevention - HP':
	hpNameWeight = piecewise(name1)
	hpSSNWeight = divide6(ssn1)
	hpDOBWeight = piecewise(dob1)
	hpRaceWeight = piecewise(race1)
	hpEthWeight = piecewise(eth1)
	hpGenWeight = piecewise(gen1)
	hpVetWeight = piecewise(vet1)
	hpExitDestWeight = piecewise(exitDest1)
	hpChronWeight = 0
	hpInactiveWeight = 0
	hpDisableWeight = divide6(disable1)
	hpStartWeight = divide6(start1)
	hpAnnualWeight = divide6(Annual1)
	hpExitWeight = divide6(exit1)
	hpHoHWeight = piecewise(hoh1)
	hpTimeWeight = divide16(time1)
	hpEnrollWeight = 0

elif projType == 'Permenant Supportive Housing - PSH':
	pshNameWeight = piecewise(name1)
	pshSSNWeight = piecewise(ssn1)
	pshDOBWeight = piecewise(dob1)
	pshRaceWeight = piecewise(race1)
	pshEthWeight = piecewise(eth1)
	pshGenWeight = piecewise(gen1)
	pshVetWeight = piecewise(vet1)
	pshExitDestWeight = piecewise(exitDest1)
	pshChronWeight = piecewise(chron1)
	pshInactiveWeight = 0
	pshDisableWeight = piecewise(disable1)
	pshStartWeight = divide6(start1)
	pshAnnualWeight = divide11(Annual1)
	pshExitWeight = divide6(exit1)
	pshHoHWeight = piecewise(hoh1)
	pshTimeWeight = divide16(time1)
	pshEnrollWeight = 0

elif projType == 'Rapid Re-housing - RRH':
	rrhNameWeight = piecewise(name1)
	rrhSSNWeight = divide6(ssn1)
	rrhDOBWeight = piecewise(dob1)
	rrhRaceWeight = piecewise(race1)
	rrhEthWeight = piecewise(eth1)
	rrhGenWeight = piecewise(gen1)
	rrhVetWeight = piecewise(vet1)
	rrhExitDestWeight = piecewise(exitDest1)
	rrhChronWeight = divide6(chron1)
	rrhInactiveWeight = 0
	rrhDisableWeight = piecewise(disable1)
	rrhStartWeight = divide11(start1)
	rrhAnnualWeight = divide11(Annual1)
	rrhExitWeight = divide11(exit1)
	rrhHoHWeight = piecewise(hoh1)
	rrhTimeWeight = divide16(time1)
	rrhEnrollWeight = 0

elif projType == 'Services Only':
	ssoNameWeight = piecewise(name1)
	ssoSSNWeight = divide11(ssn1)
	ssoDOBWeight = piecewise(dob1)
	ssoRaceWeight = piecewise(race1)
	ssoEthWeight = piecewise(eth1)
	ssoGenWeight = piecewise(gen1)
	ssoVetWeight = piecewise(vet1)
	ssoExitDestWeight = piecewise(exitDest1)
	ssoChronWeight = 0
	ssoInactiveWeight = 0
	ssoDisableWeight = 0
	ssoStartWeight = 0
	ssoAnnualWeight = 0
	ssoExitWeight = 0
	ssoHoHWeight = piecewise(hoh1)
	ssoTimeWeight = divide16(time1)
	ssoEnrollWeight = 0

elif projType == 'Street Outreach - SO':
	soNameWeight = piecewise(name1)
	soSSNWeight = divide11(ssn1)
	soDOBWeight = piecewise(dob1)
	soRaceWeight = piecewise(race1)
	soEthWeight = piecewise(eth1)
	soGenWeight = piecewise(gen1)
	soVetWeight = piecewise(vet1)
	soExitDestWeight = piecewise(exitDest1)
	soChronWeight = divide16(chron1)
	soInactiveWeight = divide16(inactive1)
	soDisableWeight = piecewise(disable1)
	soStartWeight = divide6(start1)
	soAnnualWeight = divide16(Annual1)
	soExitWeight = piecewise(exit1)
	soHoHWeight = piecewise(hoh1)
	soTimeWeight = divide16(time1)
	soEnrollWeight = 0

elif projType == 'Transitional Housing - TH':
	thNameWeight = piecewise(name1)
	thSSNWeight = divide6(ssn1)
	thDOBWeight = piecewise(dob1)
	thRaceWeight = piecewise(race1)
	thEthWeight = piecewise(eth1)
	thGenWeight = piecewise(gen1)
	thVetWeight = piecewise(vet1)
	thExitDestWeight = divide6(exitDest1)
	thChronWeight = divide11(chron1)
	thInactiveWeight = 0
	thDisableWeight = divide6(disable1)
	thStartWeight = divide15(start1)
	thAnnualWeight = divide15(Annual1)
	thExitWeight = divide15(exit1)
	thHoHWeight = piecewise(hoh1)
	thTimeWeight = divide15(time1)
	thEnrollWeight = 0




esNameMult = 2
esSSNMult = 2
esDOBMult = 2
esRaceMult = 5
esEthMult = 5
esGenMult = 2
esVetMult = 5
esExitDestMult = 5
esChronMult = 10
esInactiveMult = 0
esDisableMult = 5
esStartMult = 5
esAnnualMult = 2
esExitMult = 5
esHoHMult = 25
esTimeMult = 10
esEnrollMult = 10

hpNameMult = 2
hpSSNMult = 5
hpDOBMult = 5
hpRaceMult = 2
hpEthMult = 2
hpGenMult = 2
hpVetMult = 2
hpExitDestMult = 5
hpChronMult = 0
hpInactiveMult = 0
hpDisableMult = 10
hpStartMult = 10
hpAnnualMult = 15
hpExitMult = 5
hpHoHMult = 25
hpTimeMult = 10
hpEnrollMult = 0

pshNameMult = 2
pshSSNMult = 5
pshDOBMult = 5
pshRaceMult = 2
pshEthMult = 2
pshGenMult = 2
pshVetMult = 2
pshExitDestMult = 5
pshChronMult = 10
pshInactiveMult = 0
pshDisableMult = 5
pshStartMult = 5
pshAnnualMult = 15
pshExitMult = 5
pshHoHMult = 25
pshTimeMult = 10
pshEnrollMult = 0

rrhNameMult = 2
rrhSSNMult = 5
rrhDOBMult = 5
rrhRaceMult = 2
rrhEthMult = 2
rrhGenMult = 2
rrhVetMult = 2
rrhExitDestMult = 5
rrhChronMult = 10
rrhInactiveMult = 0
rrhDisableMult = 5
rrhStartMult = 5
rrhAnnualMult = 15
rrhExitMult = 5
rrhHoHMult = 25
rrhTimeMult = 10
rrhEnrollMult = 0

ssoNameMult = 5
ssoSSNMult = 5
ssoDOBMult = 5
ssoRaceMult = 5
ssoEthMult = 5
ssoGenMult = 5
ssoVetMult = 15
ssoExitDestMult = 15
ssoChronMult = 0
ssoInactiveMult = 0
ssoDisableMult = 0
ssoStartMult = 0
ssoAnnualMult = 0
ssoExitMult = 0
ssoHoHMult = 25
ssoTimeMult = 15
ssoEnrollMult = 0

soNameMult = 2
soSSNMult = 2
soDOBMult = 2
soRaceMult = 2
soEthMult = 2
soGenMult = 2
soVetMult = 7
soExitDestMult = 15
soChronMult = 15
soInactiveMult = 0
soDisableMult = 5
soStartMult = 2
soAnnualMult = 2
soExitMult = 2
soHoHMult = 25
soTimeMult = 15
soEnrollMult = 0

thNameMult = 2
thSSNMult = 5
thDOBMult = 5
thRaceMult = 2
thEthMult = 2
thGenMult = 2
thVetMult = 2
thExitDestMult = 5
thChronMult = 10
thInactiveMult = 0
thDisableMult = 5
thStartMult = 5
thAnnualMult = 15
thExitMult = 5
thHoHMult = 25
thTimeMult = 10
thEnrollMult = 0





























if projType == 'Emergency Shelter - ES':
	NameWeight = piecewise(name1)
	SSNWeight = divide6(ssn1)
	DOBWeight = piecewise(dob1)
	RaceWeight = piecewise(race1)
	EthWeight = piecewise(eth1)
	GenWeight = piecewise(gen1)
	VetWeight = piecewise(vet1)
	ExitDestWeight = divide6(exitDest1)
	ChronWeight = divide15(chron1)
	InactiveWeight = 0
	DisableWeight = divide6(disable1)
	StartWeight = divide11(start1)
	AnnualWeight = divide15(Annual1)
	ExitWeight = divide6(exit1)
	HoHWeight = piecewise(hoh1)
	TimeWeight = divide15(time1)
	EnrollWeight = divide15(enroll1)

elif projType == 'Homelessness Prevention - HP':
	NameWeight = piecewise(name1)
	SSNWeight = divide6(ssn1)
	DOBWeight = piecewise(dob1)
	RaceWeight = piecewise(race1)
	EthWeight = piecewise(eth1)
	GenWeight = piecewise(gen1)
	VetWeight = piecewise(vet1)
	ExitDestWeight = piecewise(exitDest1)
	ChronWeight = 0
	InactiveWeight = 0
	DisableWeight = divide6(disable1)
	StartWeight = divide6(start1)
	AnnualWeight = divide6(Annual1)
	ExitWeight = divide6(exit1)
	HoHWeight = piecewise(hoh1)
	TimeWeight = divide15(time1)
	EnrollWeight = 0

elif projType == 'Permenant Supportive Housing - PSH':
	NameWeight = piecewise(name1)
	SSNWeight = piecewise(ssn1)
	DOBWeight = piecewise(dob1)
	RaceWeight = piecewise(race1)
	EthWeight = piecewise(eth1)
	GenWeight = piecewise(gen1)
	VetWeight = piecewise(vet1)
	ExitDestWeight = piecewise(exitDest1)
	ChronWeight = piecewise(chron1)
	InactiveWeight = 0
	DisableWeight = piecewise(disable1)
	StartWeight = divide6(start1)
	AnnualWeight = divide11(Annual1)
	ExitWeight = divide6(exit1)
	HoHWeight = piecewise(hoh1)
	TimeWeight = divide15(time1)
	EnrollWeight = 0

elif projType == 'Rapid Re-housing - RRH':
	NameWeight = piecewise(name1)
	SSNWeight = divide6(ssn1)
	DOBWeight = piecewise(dob1)
	RaceWeight = piecewise(race1)
	EthWeight = piecewise(eth1)
	GenWeight = piecewise(gen1)
	VetWeight = piecewise(vet1)
	ExitDestWeight = piecewise(exitDest1)
	ChronWeight = divide6(chron1)
	InactiveWeight = 0
	DisableWeight = piecewise(disable1)
	StartWeight = divide11(start1)
	AnnualWeight = divide11(Annual1)
	ExitWeight = divide11(exit1)
	HoHWeight = piecewise(hoh1)
	TimeWeight = divide15(time1)
	EnrollWeight = 0

elif projType == 'Services Only':
	NameWeight = piecewise(name1)
	SSNWeight = divide11(ssn1)
	DOBWeight = piecewise(dob1)
	RaceWeight = piecewise(race1)
	EthWeight = piecewise(eth1)
	GenWeight = piecewise(gen1)
	VetWeight = piecewise(vet1)
	ExitDestWeight = piecewise(exitDest1)
	ChronWeight = 0
	InactiveWeight = 0
	DisableWeight = 0
	StartWeight = 0
	AnnualWeight = 0
	ExitWeight = 0
	HoHWeight = piecewise(hoh1)
	TimeWeight = divide15(time1)
	EnrollWeight = 0

elif projType == 'Street Outreach - SO':
	NameWeight = piecewise(name1)
	SSNWeight = divide11(ssn1)
	DOBWeight = piecewise(dob1)
	RaceWeight = piecewise(race1)
	EthWeight = piecewise(eth1)
	GenWeight = piecewise(gen1)
	VetWeight = piecewise(vet1)
	ExitDestWeight = piecewise(exitDest1)
	ChronWeight = divide15(chron1)
	InactiveWeight = divide15(inactive1)
	DisableWeight = piecewise(disable1)
	StartWeight = divide6(start1)
	AnnualWeight = divide15(Annual1)
	ExitWeight = piecewise(exit1)
	HoHWeight = piecewise(hoh1)
	TimeWeight = divide15(time1)
	EnrollWeight = 0

elif projType == 'Transitional Housing - TH':
	NameWeight = piecewise(name1)
	SSNWeight = divide6(ssn1)
	DOBWeight = piecewise(dob1)
	RaceWeight = piecewise(race1)
	EthWeight = piecewise(eth1)
	GenWeight = piecewise(gen1)
	VetWeight = piecewise(vet1)
	ExitDestWeight = divide6(exitDest1)
	ChronWeight = divide11(chron1)
	InactiveWeight = 0
	DisableWeight = divide6(disable1)
	StartWeight = divide15(start1)
	AnnualWeight = divide15(Annual1)
	ExitWeight = divide15(exit1)
	HoHWeight = piecewise(hoh1)
	TimeWeight = divide15(time1)
	EnrollWeight = 0





esNameMult = 2
esSSNMult = 2
esDOBMult = 2
esRaceMult = 5
esEthMult = 5
esGenMult = 2
esVetMult = 5
esExitDestMult = 5
esChronMult = 10
esInactiveMult = 0
esDisableMult = 5
esStartMult = 5
esAnnualMult = 2
esExitMult = 5
esHoHMult = 25
esTimeMult = 10
esEnrollMult = 10

hpNameMult = 2
hpSSNMult = 5
hpDOBMult = 5
hpRaceMult = 2
hpEthMult = 2
hpGenMult = 2
hpVetMult = 2
hpExitDestMult = 5
hpChronMult = 0
hpInactiveMult = 0
hpDisableMult = 10
hpStartMult = 10
hpAnnualMult = 15
hpExitMult = 5
hpHoHMult = 25
hpTimeMult = 10
hpEnrollMult = 0

pshNameMult = 2
pshSSNMult = 5
pshDOBMult = 5
pshRaceMult = 2
pshEthMult = 2
pshGenMult = 2
pshVetMult = 2
pshExitDestMult = 5
pshChronMult = 10
pshInactiveMult = 0
pshDisableMult = 5
pshStartMult = 5
pshAnnualMult = 15
pshExitMult = 5
pshHoHMult = 25
pshTimeMult = 10
pshEnrollMult = 0

rrhNameMult = 2
rrhSSNMult = 5
rrhDOBMult = 5
rrhRaceMult = 2
rrhEthMult = 2
rrhGenMult = 2
rrhVetMult = 2
rrhExitDestMult = 5
rrhChronMult = 10
rrhInactiveMult = 0
rrhDisableMult = 5
rrhStartMult = 5
rrhAnnualMult = 15
rrhExitMult = 5
rrhHoHMult = 25
rrhTimeMult = 10
rrhEnrollMult = 0

ssoNameMult = 5
ssoSSNMult = 5
ssoDOBMult = 5
ssoRaceMult = 5
ssoEthMult = 5
ssoGenMult = 5
ssoVetMult = 15
ssoExitDestMult = 15
ssoChronMult = 0
ssoInactiveMult = 0
ssoDisableMult = 0
ssoStartMult = 0
ssoAnnualMult = 0
ssoExitMult = 0
ssoHoHMult = 25
ssoTimeMult = 15
ssoEnrollMult = 0

soNameMult = 2
soSSNMult = 2
soDOBMult = 2
soRaceMult = 2
soEthMult = 2
soGenMult = 2
soVetMult = 7
soExitDestMult = 15
soChronMult = 15
soInactiveMult = 0
soDisableMult = 5
soStartMult = 2
soAnnualMult = 2
soExitMult = 2
soHoHMult = 25
soTimeMult = 15
soEnrollMult = 0

thNameMult = 2
thSSNMult = 5
thDOBMult = 5
thRaceMult = 2
thEthMult = 2
thGenMult = 2
thVetMult = 2
thExitDestMult = 5
thChronMult = 10
thInactiveMult = 0
thDisableMult = 5
thStartMult = 5
thAnnualMult = 15
thExitMult = 5
thHoHMult = 25
thTimeMult = 10
thEnrollMult = 0




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


{"ES":{"nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "divide(exitDest1 ,6)", "chronWeight": "divide(chron1 ,16)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,6)", "startWeight": "divide(start1 ,11)", "annualWeight": "divide(Annual1 ,16)", "exitWeight": "divide(exit1 ,6)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,16)","nameMult": "2", "ssnMult": "2", "dobMult": "2", "raceMult": "5", "ethMult": "5", "genMult": "2", "vetMult": "5", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "2", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "10"},"HP":{"nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,0)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,6)", "startWeight": "divide(start1 ,6)", "annualWeight": "divide(Annual1 ,6)", "exitWeight": "divide(exit1 ,6)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)","nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "0", "inactiveMult": "0", "disableMult": "10", "startMult": "10", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"},"PSH":{"nameWeight": "piecewise(name1)", "ssnWeight": "piecewise(ssn1)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "piecewise(chron1)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "piecewise(disable1)", "startWeight": "divide(start1 ,6)", "annualWeight": "divide(Annual1 ,11)", "exitWeight": "divide(exit1 ,6)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)","nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"},"RRH":{"nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,6)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "piecewise(disable1)", "startWeight": "divide(start1 ,11)", "annualWeight": "divide(Annual1 ,11)", "exitWeight": "divide(exit1 ,11)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)","nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"},"SSO":{"nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,11)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,0)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,0)", "startWeight": "divide(start1 ,0)", "annualWeight": "divide(Annual1 ,0)", "exitWeight": "divide(exit1 ,0)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)","nameMult": "5", "ssnMult": "5", "dobMult": "5", "raceMult": "5", "ethMult": "5", "genMult": "5", "vetMult": "15", "exitDestMult": "15", "chronMult": "0", "inactiveMult": "0", "disableMult": "0", "startMult": "0", "annualMult": "0", "exitMult": "0", "hohMult": "25", "timeMult": "15", "enrollMult": "0"},"SO":{"nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,11)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "piecewise(exitDest1)", "chronWeight": "divide(chron1 ,16)", "inactiveWeight": "divide(inactive1 ,16)", "disableWeight": "piecewise(disable1)", "startWeight": "divide(start1 ,6)", "annualWeight": "divide(Annual1 ,16)", "exitWeight": "piecewise(exit1)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)","nameMult": "2", "ssnMult": "2", "dobMult": "2", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "7", "exitDestMult": "15", "chronMult": "15", "inactiveMult": "0", "disableMult": "5", "startMult": "2", "annualMult": "2", "exitMult": "2", "hohMult": "25", "timeMult": "15", "enrollMult": "0"},"TH":{"nameWeight": "piecewise(name1)", "ssnWeight": "divide(ssn1 ,6)", "dobWeight": "piecewise(dob1)", "raceWeight": "piecewise(race1)", "ethWeight": "piecewise(eth1)", "genWeight": "piecewise(gen1)", "vetWeight": "piecewise(vet1)", "exitDestWeight": "divide(exitDest1 ,6)", "chronWeight": "divide(chron1 ,11)", "inactiveWeight": "divide(inactive1 ,0)", "disableWeight": "divide(disable1 ,6)", "startWeight": "divide(start1 ,16)", "annualWeight": "divide(Annual1 ,16)", "exitWeight": "divide(exit1 ,16)", "hohWeight": "piecewise(hoh1)", "timeWeight": "divide(time1 ,16)", "enrollWeight": "divide(enroll1 ,0)","nameMult": "2", "ssnMult": "5", "dobMult": "5", "raceMult": "2", "ethMult": "2", "genMult": "2", "vetMult": "2", "exitDestMult": "5", "chronMult": "10", "inactiveMult": "0", "disableMult": "5", "startMult": "5", "annualMult": "15", "exitMult": "5", "hohMult": "25", "timeMult": "10", "enrollMult": "0"}}

nameWeight
ssnWeight
dobWeight
raceWeight
ethWeight
genWeight
vetWeight
exitDestWeight
chronWeight
inactiveWeight
disableWeight
startWeight
annualWeight
exitWeight
hohWeight
timeWeight
enrollWeight
nameMult
ssnMult
dobMult
raceMult
ethMult
genMult
vetMult
exitDestMult
chronMult
inactiveMult
disableMult
startMult
annualMult
exitMult
hohMult
timeMult
enrollMult


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

nameWeight1 = eval(proj[nameWeight])
ssnWeight1 = eval(proj[ssnWeight]) 
dobWeight1 = eval(proj[dobWeight]) 
raceWeight1 = eval(proj[raceWeight]) 
ethWeight1 = eval(proj[ethWeight]) 
genWeight1 = eval(proj[genWeight]) 
vetWeight1 = eval(proj[vetWeight]) 
exitDestWeight1 = eval(proj[exitDestWeight]) 
chronWeight1 = eval(proj[chronWeight]) 
inactiveWeight1 = eval(proj[inactiveWeight]) 
disableWeight1 = eval(proj[disableWeight]) 
startWeight1 = eval(proj[startWeight]) 
annualWeight1 = eval(proj[annualWeight]) 
exitWeight1 = eval(proj[exitWeight]) 
hohWeight1 = eval(proj[hohWeight]) 
timeWeight1 = eval(proj[timeWeight]) 
enrollWeight1 = eval(proj[enrollWeight]) 
  
nameMult1 = float(proj[nameMult])
ssnMult1 = float(proj[ssnMult])
dobMult1 = float(proj[dobMult])
raceMult1 = float(proj[raceMult])
ethMult1 = float(proj[ethMult])
genMult1 = float(proj[genMult])
vetMult1 = float(proj[vetMult])
exitDestMult1 = float(proj[exitDestMult])
chronMult1 = float(proj[chronMult])
inactiveMult1 = float(proj[inactiveMult])
disableMult1 = float(proj[disableMult])
startMult1 = float(proj[startMult])
annualMult1 = float(proj[annualMult])
exitMult1 = float(proj[exitMult])
hohMult1 = float(proj[hohMult])
timeMult1 = float(proj[timeMult])
enrollMult1 = float(proj[enrollMult])

nameScore = nameWeight1 * nameMult1
ssnScore = ssnWeight1 * ssnMult1
dobScore = dobWeight1 * dobMult1
raceScore = raceWeight1 * raceMult1
ethScore = ethWeight1 * ethMult1
genScore = genWeight1 * genMult1
vetScore = vetWeight1 * vetMult1
exitDestScore = exitDestWeight1 * exitDestMult1
chronScore = chronWeight1 * chronMult1
inactiveScore = inactiveWeight1 * inactiveMult1
disableScore = disableWeight1 * disableMult1
startScore = startWeight1 * startMult1
annualScore = annualWeight1 * annualMult1
exitScore = exitWeight1 * exitMult1
hohScore = hohWeight1 * hohMult1
timeScore = timeWeight1 * timeMult1
enrollScore = enrollWeight1 * enrollMult1


print("Project: " + project)
print("HMIS ID: " + hmis_id)
print("Project Type: " + projType)
print("Start Date: " + start_date)
print("Stop_Date: " + stop_date)


        "ES":
        {
            "nameWeight": True : "piecewise(name1)", "ssnWeight": True : "divide(ssn1 ,6)", "dobWeight": True : "piecewise(dob1)", "raceWeight": True : "piecewise(race1)", "ethWeight": True : "piecewise(eth1)", "genWeight": True : "piecewise(gen1)", "vetWeight": True : "piecewise(vet1)", "exitDestWeight": True : "divide(exitDest1 ,6)", "chronWeight": True : "divide(chron1 ,16)", "inactiveWeight": True : "divide(inactive1 ,0)", "disableWeight": True : "divide(disable1 ,6)", "startWeight": True : "divide(start1 ,11)", "annualWeight": True : "divide(Annual1 ,16)", "exitWeight": True : "divide(exit1 ,6)", "hohWeight": True : "piecewise(hoh1)", "timeWeight": True : "divide(time1 ,16)", "enrollWeight": True : "divide(enroll1 ,16)",
            "nameMult": True : "2", "ssnMult": True : "2", "dobMult": True : "2", "raceMult": True : "5", "ethMult": True : "5", "genMult": True : "2", "vetMult": True : "5", "exitDestMult": True : "5", "chronMult": True : "10", "inactiveMult": True : "0", "disableMult": True : "5", "startMult": True : "5", "annualMult": True : "2", "exitMult": True : "5", "hohMult": True : "25", "timeMult": True : "10", "enrollMult": True : "10"
        },
        "HP":
        {
            "nameWeight": True : "piecewise(name1)", "ssnWeight": True : "divide(ssn1 ,6)", "dobWeight": True : "piecewise(dob1)", "raceWeight": True : "piecewise(race1)", "ethWeight": True : "piecewise(eth1)", "genWeight": True : "piecewise(gen1)", "vetWeight": True : "piecewise(vet1)", "exitDestWeight": True : "piecewise(exitDest1)", "chronWeight": True : "divide(chron1 ,0)", "inactiveWeight": True : "divide(inactive1 ,0)", "disableWeight": True : "divide(disable1 ,6)", "startWeight": True : "divide(start1 ,6)", "annualWeight": True : "divide(Annual1 ,6)", "exitWeight": True : "divide(exit1 ,6)", "hohWeight": True : "piecewise(hoh1)", "timeWeight": True : "divide(time1 ,16)", "enrollWeight": True : "divide(enroll1 ,0)",
            "nameMult": True : "2", "ssnMult": True : "5", "dobMult": True : "5", "raceMult": True : "2", "ethMult": True : "2", "genMult": True : "2", "vetMult": True : "2", "exitDestMult": True : "5", "chronMult": True : "0", "inactiveMult": True : "0", "disableMult": True : "10", "startMult": True : "10", "annualMult": True : "15", "exitMult": True : "5", "hohMult": True : "25", "timeMult": True : "10", "enrollMult": True : "0"
        },
        "PSH":
        {
            "nameWeight": True : "piecewise(name1)", "ssnWeight": True : "piecewise(ssn1)", "dobWeight": True : "piecewise(dob1)", "raceWeight": True : "piecewise(race1)", "ethWeight": True : "piecewise(eth1)", "genWeight": True : "piecewise(gen1)", "vetWeight": True : "piecewise(vet1)", "exitDestWeight": True : "piecewise(exitDest1)", "chronWeight": True : "piecewise(chron1)", "inactiveWeight": True : "divide(inactive1 ,0)", "disableWeight": True : "piecewise(disable1)", "startWeight": True : "divide(start1 ,6)", "annualWeight": True : "divide(Annual1 ,11)", "exitWeight": True : "divide(exit1 ,6)", "hohWeight": True : "piecewise(hoh1)", "timeWeight": True : "divide(time1 ,16)", "enrollWeight": True : "divide(enroll1 ,0)",
            "nameMult": True : "2", "ssnMult": True : "5", "dobMult": True : "5", "raceMult": True : "2", "ethMult": True : "2", "genMult": True : "2", "vetMult": True : "2", "exitDestMult": True : "5", "chronMult": True : "10", "inactiveMult": True : "0", "disableMult": True : "5", "startMult": True : "5", "annualMult": True : "15", "exitMult": True : "5", "hohMult": True : "25", "timeMult": True : "10", "enrollMult": True : "0"
        },
        "RRH":
        {
            "nameWeight": True : "piecewise(name1)", "ssnWeight": True : "divide(ssn1 ,6)", "dobWeight": True : "piecewise(dob1)", "raceWeight": True : "piecewise(race1)", "ethWeight": True : "piecewise(eth1)", "genWeight": True : "piecewise(gen1)", "vetWeight": True : "piecewise(vet1)", "exitDestWeight": True : "piecewise(exitDest1)", "chronWeight": True : "divide(chron1 ,6)", "inactiveWeight": True : "divide(inactive1 ,0)", "disableWeight": True : "piecewise(disable1)", "startWeight": True : "divide(start1 ,11)", "annualWeight": True : "divide(Annual1 ,11)", "exitWeight": True : "divide(exit1 ,11)", "hohWeight": True : "piecewise(hoh1)", "timeWeight": True : "divide(time1 ,16)", "enrollWeight": True : "divide(enroll1 ,0)",
            "nameMult": True : "2", "ssnMult": True : "5", "dobMult": True : "5", "raceMult": True : "2", "ethMult": True : "2", "genMult": True : "2", "vetMult": True : "2", "exitDestMult": True : "5", "chronMult": True : "10", "inactiveMult": True : "0", "disableMult": True : "5", "startMult": True : "5", "annualMult": True : "15", "exitMult": True : "5", "hohMult": True : "25", "timeMult": True : "10", "enrollMult": True : "0"
        },
        "SSO":
        {
            "nameWeight": True : "piecewise(name1)", "ssnWeight": True : "divide(ssn1 ,11)", "dobWeight": True : "piecewise(dob1)", "raceWeight": True : "piecewise(race1)", "ethWeight": True : "piecewise(eth1)", "genWeight": True : "piecewise(gen1)", "vetWeight": True : "piecewise(vet1)", "exitDestWeight": True : "piecewise(exitDest1)", "chronWeight": True : "divide(chron1 ,0)", "inactiveWeight": True : "divide(inactive1 ,0)", "disableWeight": True : "divide(disable1 ,0)", "startWeight": True : "divide(start1 ,0)", "annualWeight": True : "divide(Annual1 ,0)", "exitWeight": True : "divide(exit1 ,0)", "hohWeight": True : "piecewise(hoh1)", "timeWeight": True : "divide(time1 ,16)", "enrollWeight": True : "divide(enroll1 ,0)",
            "nameMult": True : "5", "ssnMult": True : "5", "dobMult": True : "5", "raceMult": True : "5", "ethMult": True : "5", "genMult": True : "5", "vetMult": True : "15", "exitDestMult": True : "15", "chronMult": True : "0", "inactiveMult": True : "0", "disableMult": True : "0", "startMult": True : "0", "annualMult": True : "0", "exitMult": True : "0", "hohMult": True : "25", "timeMult": True : "15", "enrollMult": True : "0"
        },
        "SO":
        {
            "nameWeight": True : "piecewise(name1)", "ssnWeight": True : "divide(ssn1 ,11)", "dobWeight": True : "piecewise(dob1)", "raceWeight": True : "piecewise(race1)", "ethWeight": True : "piecewise(eth1)", "genWeight": True : "piecewise(gen1)", "vetWeight": True : "piecewise(vet1)", "exitDestWeight": True : "piecewise(exitDest1)", "chronWeight": True : "divide(chron1 ,16)", "inactiveWeight": True : "divide(inactive1 ,16)", "disableWeight": True : "piecewise(disable1)", "startWeight": True : "divide(start1 ,6)", "annualWeight": True : "divide(Annual1 ,16)", "exitWeight": True : "piecewise(exit1)", "hohWeight": True : "piecewise(hoh1)", "timeWeight": True : "divide(time1 ,16)", "enrollWeight": True : "divide(enroll1 ,0)",
            "nameMult": True : "2", "ssnMult": True : "2", "dobMult": True : "2", "raceMult": True : "2", "ethMult": True : "2", "genMult": True : "2", "vetMult": True : "7", "exitDestMult": True : "15", "chronMult": True : "15", "inactiveMult": True : "0", "disableMult": True : "5", "startMult": True : "2", "annualMult": True : "2", "exitMult": True : "2", "hohMult": True : "25", "timeMult": True : "15", "enrollMult": True : "0"
        },
        "TH":
        {
            "nameWeight": False : "piecewise(name1)", "ssnWeight": False : "divide(ssn1 ,6)", "dobWeight": False : "piecewise(dob1)", "raceWeight": False : "piecewise(race1)", "ethWeight": False : "piecewise(eth1)", "genWeight": False : "piecewise(gen1)", "vetWeight": False : "piecewise(vet1)", "exitDestWeight": False : "divide(exitDest1 ,6)", "chronWeight": False : "divide(chron1 ,11)", "inactiveWeight": False : "divide(inactive1 ,0)", "disableWeight": False : "divide(disable1 ,6)", "startWeight": False : "divide(start1 ,16)", "annualWeight": False : "divide(Annual1 ,16)", "exitWeight": False : "divide(exit1 ,16)", "hohWeight": False : "piecewise(hoh1)", "timeWeight": False : "divide(time1 ,16)", "enrollWeight": False : "divide(enroll1 ,0)",
            "nameMult": False : "2", "ssnMult": False : "5", "dobMult": False : "5", "raceMult": False : "2", "ethMult": False : "2", "genMult": False : "2", "vetMult": False : "2", "exitDestMult": False : "5", "chronMult": False : "10", "inactiveMult": False : "0", "disableMult": False : "5", "startMult": False : "5", "annualMult": False : "15", "exitMult": False : "5", "hohMult": False : "25", "timeMult": False : "10", "enrollMult": False : "0"
        }


 array = [date,
                    agency,
                    project,
                    hmis_id,
                    projType,
                    start_date,
                    stop_date,
                    nameScore,
                    ssnScore,
                    dobScore,
                    raceScore,
                    ethScore,
                    genScore,
                    vetScore,
                    exitDestScore,
                    chronScore,
                    inactiveScore,
                    disableScore,
                    startScore,
                    annualScore,
                    exitScore,
                    hohScore,
                    timeScore,
                    enrollScore]