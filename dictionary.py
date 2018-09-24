#Importations

import random
import time
import sys

#Weapon Defining for "On Foot" situations

assault_Rifle = "Assault Rifle"
battle_Rifle = "Battle Rifle"
sMG = "SMG"
lMG = "LMG"
rocket_Launcher = "Rocket Launcher"
hydra = "Hydra"
moonbeam = "Moonbeam"

foot_weapons = {
    'assault rifle': assault_Rifle,
    'battle rifle': battle_Rifle,
    'smg': sMG,
    'lmg': lMG,
    'rocket launcher': rocket_Launcher,
    'hydra': hydra,
    'moonbeam': moonbeam,
}
weapons_list = foot_weapons.keys()

#Equipment Defining

sprint = "Sprint"
armor_lockup = "Armor Lockup"
drop_shield = "Drop Shield"
evade = "Evade"
active_camo = "Active Camoflage"
hologram = "Hologram"
jetpack = "Jetpack"

equipment = {
    'sprint': sprint,
    'armor lockup': armor_lockup,
    'drop shield': drop_shield,
    'evade': evade,
    'active camo': active_camo,
    'hologram': hologram,
    'jetpack': jetpack,
}
equipment_list = equipment.keys()

#Main Loadout Functions

choice_weapons = print(random.choice(weapons_list))

choice_equipment = print(random.choice(equipment_list))

#User Implimentations

gamertag = input("Welcome to Halo Loadout Creator! Type in your gamertag or name: ")
print("Hello %s!" % gamertag)
time.sleep(1)
print("Gathering Things...")
time.sleep(2)

#User Go/Quit Conditional

choice = input("Type 'L' to generate a loadout. Type 'N' to quit program: ")
print("WEAPON: %s    EQUIPMENT: %s" % choice_weapons % choice_equipment)
